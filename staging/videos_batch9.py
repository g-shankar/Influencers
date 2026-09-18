#!/usr/bin/env python3
"""Fetch recent video IDs+descs+createTimes from TikTok profile pages, spaced 4s apart.
Usage: videos_batch9.py h1 h2 ...  (writes JSON list to stdout)
"""
import json, re, sys, time, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"}

def profile(handle):
    req = urllib.request.Request(f"https://www.tiktok.com/@{handle}", headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            html = r.read().decode("utf-8", "replace")
    except Exception as e:
        return {"handle": handle, "error": str(e)[:80]}
    # find item entries: "id":"<19 digits>","desc":"...","createTime":"..."
    items = []
    seen = set()
    for m in re.finditer(r'"id":"(\d{18,20})","desc":"((?:[^"\\]|\\.){0,220})","createTime":"(\d+)"', html):
        vid, desc, ct = m.group(1), m.group(2), int(m.group(3))
        if vid in seen:
            continue
        seen.add(vid)
        desc = desc.encode("utf-8", "replace").decode("unicode_escape", "replace")
        items.append({"id": vid, "desc": desc[:160], "date": ct})
        if len(items) >= 30:
            break
    out = {"handle": handle, "videos": items}
    for pat, key in [(r'"followerCount":(\d+)', "followers"),
                     (r'"nickname":"([^"]+)"', "nickname"),
                     (r'"signature":"([^"]{0,300})', "bio")]:
        m = re.search(pat, html)
        out[key] = m.group(1) if m else None
    return out

results = []
for i, h in enumerate(sys.argv[1:]):
    if i:
        time.sleep(4)
    results.append(profile(h))
print(json.dumps(results, indent=1, ensure_ascii=False))
