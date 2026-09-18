#!/usr/bin/env python3
"""IG login verification for travel-influencer restore queue (re-dispatch 2026-09-17).
READ-ONLY: profile + posts only. Extracts FACTS only (no raw verbatim dumps).
Stops immediately on genuine 429/rate-limit (exit 42). Budget guard: max 55 calls.
Usage: python3 staging/ig_verify2.py handle1 handle2 ...
Output: staging/ig_verify_2026-09-17/<handle>.evidence.json
"""
import json, subprocess, sys, os, time, datetime

ACCT = "17841401257941416"
OUTDIR = os.path.expanduser("~/workspace/travel-influencer-pilot/staging/ig_verify_2026-09-17")
CALL_BUDGET = 55
calls = 0
os.makedirs(OUTDIR, exist_ok=True)

def cli(*args):
    global calls
    calls += 1
    if calls > CALL_BUDGET:
        print("BUDGET_EXCEEDED", flush=True)
        sys.exit(43)
    p = subprocess.run(["instagram-cli"] + list(args), capture_output=True, text=True, timeout=120)
    return p.stdout, p.stderr, p.returncode

def is_rate_limited(text):
    t = (text or "").lower()
    return ("429" in t and ("rate" in t or "limit" in t or "too many" in t)) or \
           ("rate limit" in t) or ("ratelimit" in t)

def get_json(args):
    out, err, rc = cli(*args)
    if is_rate_limited(out) or is_rate_limited(err):
        print("RATE_LIMIT_STOP", flush=True)
        sys.exit(42)
    try:
        return json.loads(out)
    except Exception:
        return {"_parse_error": (out or err)[:300]}

def summarize_profile(d):
    profs = d.get("profiles") or []
    if not profs:
        return {"error": d.get("error") or d.get("_parse_error") or "no profile returned"}
    p = profs[0]
    return {
        "username": p.get("username"),
        "name": p.get("name"),
        "follower_count": p.get("follower_count"),
        "following_count": p.get("following_count"),
        "post_count": p.get("post_count"),
        "is_private": p.get("is_private"),
        "is_verified": p.get("is_verified"),
        "account_type": p.get("account_type"),
        "bio_gist": (p.get("bio") or "")[:220],
        "website": p.get("website"),
        "observed_utc": (d.get("retrieved_at") or {}).get("utc"),
    }

def summarize_posts(d):
    items = d.get("posts") or d.get("media") or d.get("items") or []
    out = []
    for m in items[:5]:
        created = m.get("created_at") or m.get("taken_at") or m.get("timestamp")
        date = None
        try:
            date = datetime.datetime.fromtimestamp(int(created), tz=datetime.timezone.utc).strftime("%Y-%m-%d")
        except Exception:
            date = str(created)[:10] if created else None
        out.append({
            "url": m.get("url") or (m.get("shortcode") and f"https://www.instagram.com/p/{m.get('shortcode')}/"),
            "date": date,
            "comment_count": m.get("comments") if m.get("comments") is not None else m.get("comment_count"),
            "like_count": m.get("likes") if m.get("likes") is not None else m.get("like_count"),
            "location_tag": m.get("tagged_location_name") or m.get("location"),
            "caption_gist": (m.get("post_caption") or m.get("caption") or "")[:110],
            "media_type": m.get("media_type"),
        })
    return out

done = 0
for h in sys.argv[1:]:
    uname = h.lstrip('@')
    evpath = os.path.join(OUTDIR, uname + ".evidence.json")
    if os.path.exists(evpath):
        print("SKIP (exists)", uname, flush=True)
        continue
    print("VERIFY", uname, flush=True)
    prof = get_json(["profile", "--account-id", ACCT, "--username", uname])
    ev = {"profile": summarize_profile(prof)}
    time.sleep(4)
    posts = get_json(["posts", "--account-id", ACCT, "--username", uname, "--limit", "5"])
    ev["posts"] = summarize_posts(posts)
    ev["posts_raw_error"] = posts.get("error") or posts.get("_parse_error")
    with open(evpath, "w") as f:
        json.dump(ev, f, indent=1)
    print("DONE", uname, "followers=", ev["profile"].get("follower_count"),
          "posts=", len(ev["posts"]), "calls=", calls, flush=True)
    done += 1
    time.sleep(4)
print("COMPLETED", done, "calls=", calls, flush=True)
