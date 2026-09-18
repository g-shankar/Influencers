#!/usr/bin/env python3
"""TikTok public-page verification fetcher.
Fetches a TikTok profile or video page with a browser UA and extracts the
embedded __UNIVERSAL_DATA_FOR_REHYDRATION__ / SIGI_STATE JSON.
Writes JSON to stdout: {ok, handle, author stats, video stats, recent_videos}.
No login, no browser — public data only.
"""
import json, re, sys, html, datetime
import urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36")

def fetch(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept-Language": "en-US,en;q=0.9",
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")

def extract_state(html_text):
    m = re.search(
        r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__" type="application/json">(.*?)</script>',
        html_text, re.S)
    if not m:
        return None
    return json.loads(html.unescape(m.group(1)))

def video_create_time(vid):
    try:
        return int(vid) >> 32
    except Exception:
        return None

def profile(url):
    out = {"ok": False, "fetch_date": datetime.date.today().isoformat()}
    try:
        h = fetch(url)
    except Exception as e:
        out["error"] = f"fetch: {e}"
        return out
    st = extract_state(h)
    if not st:
        out["error"] = "no embedded state (bot-block or not found)"
        return out
    try:
        scope = st["__DEFAULT_SCOPE__"]
        if "webapp.user-detail" in scope:
            ud = scope["webapp.user-detail"]["userInfo"]
            user = ud.get("user", {}); stats = ud.get("stats", {})
            out.update({"ok": True, "kind": "profile",
                        "handle": user.get("uniqueId"),
                        "nickname": user.get("nickname"),
                        "signature": user.get("signature"),
                        "verified": user.get("verified"),
                        "followerCount": stats.get("followerCount"),
                        "followingCount": stats.get("followingCount"),
                        "heartCount": stats.get("heartCount"),
                        "videoCount": stats.get("videoCount")})
            vids = ud.get("user", {})
        elif "webapp.video-detail" in scope:
            vd = scope["webapp.video-detail"]["itemInfo"]["itemStruct"]
            author = vd.get("author", {}); stats = vd.get("stats", {})
            ctime = video_create_time(str(vd.get("id")))
            out.update({"ok": True, "kind": "video",
                        "video_id": str(vd.get("id")),
                        "desc": vd.get("desc"),
                        "createTime": ctime,
                        "createDate": datetime.datetime.utcfromtimestamp(ctime).isoformat() if ctime else None,
                        "playCount": stats.get("playCount"),
                        "diggCount": stats.get("diggCount"),
                        "commentCount": stats.get("commentCount"),
                        "shareCount": stats.get("shareCount"),
                        "author_handle": author.get("uniqueId"),
                        "author_nickname": author.get("nickname"),
                        "author_signature": author.get("signature"),
                        "author_followerCount": author.get("followerCount"),
                        "author_videoCount": author.get("videoCount"),
                        "music_title": (vd.get("music") or {}).get("title")})
        else:
            out["error"] = f"unknown scope keys: {list(scope)[:5]}"
    except Exception as e:
        out["error"] = f"parse: {e}"
    return out

def video_list(url, n=10):
    """Attempt to pull recent video ids/stats from a profile page."""
    out = {"ok": False, "fetch_date": datetime.date.today().isoformat()}
    try:
        h = fetch(url)
    except Exception as e:
        out["error"] = f"fetch: {e}"
        return out
    st = extract_state(h)
    if not st:
        out["error"] = "no embedded state"
        return out
    try:
        scope = st["__DEFAULT_SCOPE__"]
        ud = scope["webapp.user-detail"]["userInfo"]
        items = ud.get("itemList", []) or []
        vids = []
        for v in items[:n]:
            ctime = video_create_time(str(v.get("id")))
            vids.append({
                "id": str(v.get("id")),
                "desc": (v.get("desc") or "")[:160],
                "createDate": datetime.datetime.utcfromtimestamp(ctime).strftime("%Y-%m-%d") if ctime else None,
                "playCount": (v.get("stats") or {}).get("playCount"),
                "diggCount": (v.get("stats") or {}).get("diggCount"),
                "commentCount": (v.get("stats") or {}).get("commentCount"),
            })
        out.update({"ok": True, "videos": vids,
                    "followerCount": ud.get("stats", {}).get("followerCount"),
                    "nickname": ud.get("user", {}).get("nickname")})
    except Exception as e:
        out["error"] = f"parse: {e}"
    return out

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "profile"
    url = sys.argv[2]
    if mode == "videos":
        print(json.dumps(video_list(url), indent=1))
    else:
        print(json.dumps(profile(url), indent=1))
