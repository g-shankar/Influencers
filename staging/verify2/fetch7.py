import sys, json, datetime
sys.path.insert(0, 'staging/verify2')
from fetch import new_session, jdump, S
API = 'https://www.tiktok.com/api/post/item_list/'
def posts(sess, sec_uid, n=15):
    return S(sess).get(API, params={'secUid': sec_uid, 'count': str(n), 'cursor': '0'}, timeout=20).json().get('itemList', [])
def check(handle, video_id, items, mins):
    sess = new_session(); prof = sess.get(f'https://www.tiktok.com/@{handle}', timeout=20)
    au = prof['userInfo']['user']
    out = {
      'handle': '@'+handle,
      'name': au.get('nickname'),
      'followers': au.get('followerCount'),
      'likes': au.get('heartCount'),
      'videos': au.get('videoCount'),
      'bio': (au.get('signature') or '')[:300],
      'target_id': video_id,
    }
    for it in posts(sess, au['secUid']):
        if str(it['id']) == video_id:
            out['video'] = {
              'desc': it.get('desc','')[:300],
              'createTime': it.get('createTime'),
              'date': datetime.datetime.fromtimestamp(it.get('createTime',0), datetime.timezone.utc).strftime('%Y-%m-%d'),
              'stats': it.get('stats', {}),
            }
            break
    else:
        out['video'] = None
    out['expected_items'] = items
    out['recent_plays'] = [str(p['id'])[:0] or {k: v for k,v in {'id':p['id'],'createTime':datetime.datetime.fromtimestamp(p.get('createTime',0),datetime.timezone.utc).strftime('%Y-%m-%d'),'plays':p.get('stats',{}).get('playCount')}.items()} for p in posts(sess, au['secUid'], 6)]
    return out
if __name__ == '__main__':
    sess_kw = {}
    results = [
      check('solosavvynancy', '7568717242628721931', ['Wat Arun/Eagle Nest','Yaowarat Chinatown','Wat Paknam','ICON SIAM','Lumphini Park','Central Park rooftop'], None),
      check('xela.travels', '7595658473514224918', ['Siem Reap 4d','Battambang 2d','Kampot 3d','Koh Rong 5d','Phnom Penh 4d'], None),
      check('dearandrea_', '7397605555579194631', ['Meiji Jingu','Takeshita','Shibuya','Nakamise/Sensoji','Tokyo Skytree','Akihabara','teamLab Planets','Tsukiji','Tokyo Tower','Ginza'], None),
    ]
    print(json.dumps(results, indent=1))
