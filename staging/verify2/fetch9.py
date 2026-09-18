import sys; sys.path.insert(0,'staging/verify2')
from fetch8 import fetch_profile
import json, time
targets=['@nicolemsunderland','@jetset_anna','@calebthill','@helenemoo','@emilynels8','@pagingmrmorrow','@thisisyules','@talesofnomads','@travelhaggs','@global.and.beyond.travel','@ladytrailmix','@vannypacktravels','@travel.w.amanda']
out={}
for h in targets:
    try: out[h]=fetch_profile(h)
    except Exception as e: out[h]={'fatal':str(e)}
    time.sleep(2)
json.dump(out,open('staging/verify2/verify9_results.json','w'),ensure_ascii=False,indent=1)
print('saved')
