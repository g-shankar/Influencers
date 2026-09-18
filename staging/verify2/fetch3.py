import urllib.request, re, json, time
UA={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'}
def get(url):
    req=urllib.request.Request(url,headers=UA)
    try: return urllib.request.urlopen(req,timeout=20).read().decode('utf-8','ignore')
    except Exception as e: return 'ERR:'+str(e)
def blob(h):
    m=re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__" type="application/json">(.*?)</script>',h,re.S)
    return json.loads(m.group(1)) if m else None
def fetch_profile(handle):
    h=get('https://www.tiktok.com/'+handle)
    if h.startswith('ERR:'): return {'error':h}
    d=blob(h)
    if not d: return {'error':'no data'}
    u=d.get('__DEFAULT_SCOPE__',{}).get('webapp.user-detail',{}).get('userInfo',{})
    us,ss=u.get('user',{}),u.get('stats',{})
    return {'handle':us.get('uniqueId'),'nickname':us.get('nickname'),'bio':us.get('signature'),
            'followers':ss.get('followerCount'),'likes':ss.get('heartCount'),'videos':ss.get('videoCount')}
def fetch_video(handle,vid):
    h=get('https://www.tiktok.com/'+handle+'/video/'+vid)
    if h.startswith('ERR:'): return {'error':h}
    d=blob(h)
    if not d: return {'error':'no data'}
    v=d.get('__DEFAULT_SCOPE__',{}).get('webapp.video-detail',{}).get('itemInfo',{}).get('itemStruct',{})
    if not v: return {'error':'no itemStruct'}
    return {'video_id':v.get('id'),'desc':v.get('desc'),'create_time':v.get('createTime'),
            'plays':v.get('stats',{}).get('playCount'),'likes':v.get('stats',{}).get('diggCount'),
            'comments':v.get('stats',{}).get('commentCount'),'shares':v.get('stats',{}).get('shareCount'),
            'saves':v.get('stats',{}).get('collectCount')}
targets=[
 ('@trinitytravel3', ['7507435550786825490']),
 ('@tiamo.vietnam', ['7620432610728135957']),
 ('@haylsa', ['7508514989817269526']),
 ('@eltravel.12', ['7498116754338483478']),
 ('@tanya.travels', ['7622835610705693957']),
 ('@marijasolotraveler', ['7517715681216654872']),
 ('@wonder.odysseys', ['7531358587352173846']),
]
out={}
for handle,vids in targets:
    try:
        p=fetch_profile(handle); out[handle]={'profile':p}
        for vid in vids:
            out[handle]['videos']={vid:fetch_video(handle,vid)}
    except Exception as e: out[handle]={'fatal':str(e)}
    time.sleep(4)
json.dump(out,open('verify3_results.json','w'),ensure_ascii=False,indent=1)
print('saved')
