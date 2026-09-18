import urllib.request, re, json, time, datetime
UA={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'}
def get(url):
    req=urllib.request.Request(url,headers=UA)
    try: return urllib.request.urlopen(req,timeout=20).read().decode('utf-8','ignore')
    except Exception as e: return 'ERR:'+str(e)
def blob(h):
    m=re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__" type="application/json">(.*?)</script>',h,re.S)
    return json.loads(m.group(1)) if m else None
def ts(t):
    try: return datetime.datetime.fromtimestamp(int(t),datetime.timezone.utc).strftime('%Y-%m-%d')
    except: return None
def fetch_profile(handle):
    h=get('https://www.tiktok.com/'+handle)
    if h.startswith('ERR:'): return {'error':h}
    d=blob(h)
    if not d: return {'error':'no data'}
    u=d.get('__DEFAULT_SCOPE__',{}).get('webapp.user-detail',{}).get('userInfo',{})
    us,ss=u.get('user',{}),u.get('stats',{})
    recent=[]
    for k,v in d.get('__DEFAULT_SCOPE__',{}).items():
        if isinstance(v,dict) and 'itemList' in v and isinstance(v['itemList'],list):
            recent=v['itemList'][:8]
            break
    rp=[{'id':p.get('id'),'date':ts(p.get('createTime')),'plays':p.get('stats',{}).get('playCount'),'likes':p.get('stats',{}).get('diggCount'),'comments':p.get('stats',{}).get('commentCount'),'shares':p.get('stats',{}).get('shareCount'),'saves':p.get('stats',{}).get('collectCount')} for p in recent]
    return {'handle':us.get('uniqueId'),'nickname':us.get('nickname'),'bio':(us.get('signature') or '')[:400],
            'followers':ss.get('followerCount'),'likes':ss.get('heartCount'),'videos':ss.get('videoCount'),
            'verified':us.get('verified'),'private':us.get('privateAccount'),'recent':rp}
def fetch_media(handle,kind,mid):
    h=get('https://www.tiktok.com/'+handle+'/'+kind+'/'+mid)
    if h.startswith('ERR:'): return {'error':h}
    d=blob(h)
    if not d: return {'error':'no data'}
    v=d.get('__DEFAULT_SCOPE__',{}).get('webapp.video-detail',{}).get('itemInfo',{}).get('itemStruct',{})
    if not v: return {'error':'no itemStruct'}
    return {'media_id':v.get('id'),'desc':(v.get('desc') or '')[:3000],'date':ts(v.get('createTime')),
            'plays':v.get('stats',{}).get('playCount'),'likes':v.get('stats',{}).get('diggCount'),
            'comments':v.get('stats',{}).get('commentCount'),'shares':v.get('stats',{}).get('shareCount'),
            'saves':v.get('stats',{}).get('collectCount')}
targets=[
 ('@solosavvynancy', [('video','7568717242628721931')]),
 ('@xela.travels', [('video','7595658473514224918')]),
 ('@dearandrea_', [('video','7397605555579194631')]),
 ('@jvwanderer', [('video','7602404215570435348')]),
 ('@everydropoftia', [('video','7596642470528617750')]),
 ('@wheretonexttt__', [('video','7448724907761880351')]),
]
out={}
for handle,medias in targets:
    try:
        p=fetch_profile(handle); out[handle]={'profile':p,'media':{}}
        for kind,mid in medias:
            out[handle]['media'][mid]=fetch_media(handle,kind,mid)
    except Exception as e: out[handle]={'fatal':str(e)}
    time.sleep(3)
json.dump(out,open('staging/verify2/verify8_results.json','w'),ensure_ascii=False,indent=1)
print('saved')
