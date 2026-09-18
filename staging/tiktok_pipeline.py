#!/usr/bin/env python3
"""Combined TikTok verification: profile (SIGI_STATE) + urlebird recent videos.
Usage: python3 tiktok_pipeline.py @handle
Outputs JSON verification record. fetch_date = observation date (2026-09-17).
"""
import json, re, html, sys, datetime
import urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36")

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")

def extract_state(html_text):
    m = re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__" type="application/json">(.*?)</script>', html_text, re.S)
    return json.loads(html.unescape(m.group(1))) if m else None

def vid_time(vid):
    try: return int(vid) >> 32
    except Exception: return None

def profile(handle):
    st = extract_state(fetch(f"https://www.tiktok.com/@{handle}"))
    if not st: return {"ok": False, "error": "no state"}
    ud = st["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]
    u, s = ud["user"], ud["stats"]
    return {"ok": True, "handle": u.get("uniqueId"), "nickname": u.get("nickname"),
            "signature": u.get("signature"), "verified": u.get("verified"),
            "followerCount": s.get("followerCount"), "followingCount": s.get("followingCount"),
            "heartCount": s.get("heartCount"), "videoCount": s.get("videoCount")}

def urlebird_recent(handle, n=12):
    h = fetch(f"https://urlebird.com/user/{handle}/")
    vids = []
    for m in re.finditer(r'"uploadDate":"([^"]+)"', h):
        chunk = h[max(0, m.start()-2500):m.start()]
        # video names are followed by a "description"; music/author names are not
        nm = re.findall(r'"name":"((?:[^"\\]|\\.){1,160})","description":"', chunk)
        name = html.unescape(nm[-1]) if nm else ""
        vids.append({"title": name, "date": m.group(1)[:10]})
    stats = []
    for d in re.findall(r'<div class="stats">(.*?)</div>\s*</div>', h, re.S):
        txt = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', d)).strip()
        parts = txt.split(' ')
        # card text is like "1 year ago 1.12M 89.35K 342" = rel_time views likes comments
        stats.append({"rel_time": ' '.join(parts[:3]),
                      "views": parts[3] if len(parts) > 3 else None,
                      "likes": parts[4] if len(parts) > 4 else None,
                      "comments": parts[5] if len(parts) > 5 else None})
    out = []
    for i, v in enumerate(vids[:n]):
        v = dict(v)
        if i < len(stats):
            v.update(stats[i])
        out.append(v)
    return out

def video_stats(video_id, handle):
    st = extract_state(fetch(f"https://www.tiktok.com/@{handle}/video/{video_id}"))
    if not st: return {"ok": False}
    vd = st["__DEFAULT_SCOPE__"]["webapp.video-detail"]["itemInfo"]["itemStruct"]
    s = vd.get("stats", {})
    ct = vid_time(str(vd.get("id")))
    return {"ok": True, "desc": vd.get("desc"),
            "createDate": datetime.datetime.utcfromtimestamp(ct).strftime("%Y-%m-%d") if ct else None,
            "playCount": s.get("playCount"), "diggCount": s.get("diggCount"),
            "commentCount": s.get("commentCount"), "shareCount": s.get("shareCount")}

if __name__ == "__main__":
    handle = sys.argv[1].lstrip("@")
    rec = {"handle": "@" + handle, "fetch_date": "2026-09-17"}
    try:
        rec["profile"] = profile(handle)
    except Exception as e:
        rec["profile"] = {"ok": False, "error": str(e)[:120]}
    try:
        rec["recent_videos"] = urlebird_recent(handle)
    except Exception as e:
        rec["recent_videos"] = {"error": str(e)[:120]}
    print(json.dumps(rec, indent=1, ensure_ascii=False))
