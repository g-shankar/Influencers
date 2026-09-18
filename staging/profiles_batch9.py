#!/usr/bin/env python3
"""Fetch TikTok profile fields for a list of handles, spaced 4s apart. Usage: profiles_batch9.py h1 h2 ..."""
import json, re, sys, time, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"}

def profile(handle):
    req = urllib.request.Request(f"https://www.tiktok.com/@{handle}", headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            html = r.read().decode("utf-8", "replace")
    except Exception as e:
        return {"handle": handle, "error": str(e)[:80]}
    out = {"handle": handle}
    for pat, key, n in [(r'"followerCount":(\d+)', "followers", 1),
                        (r'"followingCount":(\d+)', "following", 1),
                        (r'"heartCount":(\d+)', "likes", 1),
                        (r'"videoCount":(\d+)', "videos", 1),
                        (r'"nickname":"([^"]+)"', "nickname", 1),
                        (r'"signature":"([^"]{0,300})', "bio", 1)]:
        m = re.search(pat, html)
        out[key] = m.group(1) if m else None
    return out

results = []
for i, h in enumerate(sys.argv[1:]):
    if i:
        time.sleep(4)
    results.append(profile(h))
print(json.dumps(results, indent=1, ensure_ascii=False))
