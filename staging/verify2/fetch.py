import urllib.request, re, json, time, sys
UA={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'}
def get(url):
    req=urllib.request.Request(url,headers=UA)
    try:
        return urllib.request.urlopen(req,timeout=20).read().decode('utf-8','ignore')
    except Exception as e:
        return 'ERR:'+str(e)
def fetch_profile(handle):
    h=get('https://www.tiktok.com/'+handle)
    if h.startswith('ERR:'): return {'error':h}
    m=re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__" type="application/json">(.*?)</script>',h,re.S)
    if not m: return {'error':'no rehydration'}
    d=json.loads(m.group(1))
    defd=d.get('__DEFAULT_SCOPE__',{}).get('webapp.user-detail',{}).get('userInfo',{})
    u=defd.get('user',{}); s=defd.get('stats',{})
    return {'handle':u.get('uniqueId'),'nickname':u.get('nickname'),'bio':u.get('signature'),
            'followers':s.get('followerCount'),'following':s.get('followingCount'),'likes':s.get('heartCount'),
            'videos':s.get('videoCount'),'private':u.get('privateAccount')}
def fetch_video(handle,vid):
    h=get('https://www.tiktok.com/'+handle+'/video/'+vid)
    if h.startswith('ERR:'): return {'error':h}
    m=re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__" type="application/json">(.*?)</script>',h,re.S)
    if not m: return {'error':'no rehydration'}
    d=json.loads(m.group(1))
    v=d.get('__DEFAULT_SCOPE__',{}).get('webapp.video-detail',{}).get('itemInfo',{}).get('itemStruct',{})
    return {'video_id':v.get('id'),'desc':v.get('desc'),'create_time':v.get('createTime'),
            'plays':v.get('stats',{}).get('playCount'),'likes':v.get('stats',{}).get('diggCount'),
            'comments':v.get('stats',{}).get('commentCount'),'shares':v.get('stats',{}).get('shareCount'),
            'saves':v.get('stats',{}).get('collectCount'),'author':v.get('author',{}).get('uniqueId')}
targets=[
 ('@dearhaley_', ['7511305496599612679']),
 ('@pam', ['7610053903621987662']),
 ('@caseyroman', ['7520118149023218990']),
 ('@marijasolotraveler', ['7517715681216654872']),
 ('@wonder.odysseys', ['7531358587352173846']),
 ('@discover.travel.j', ['7523519669609827602','7607370817160121608']),
 ('@gvan_trip', []),
 ('@tjtravels4', []),
 ('@hannahseuton', []),
]
out={}
for handle,vids in targets:
    p=fetch_profile(handle); out[handle]={'profile':p}
    for vid in vids:
        out[handle]['videos']={vid:fetch_video(handle,vid)}
    time.sleep(4)
json.dump(out,open('verify2_results.json','w'),ensure_ascii=False,indent=1)
print('saved')
