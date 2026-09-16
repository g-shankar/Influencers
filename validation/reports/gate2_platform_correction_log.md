# Gate 2 — Platform-Label Correction Log (2026-09-16)

## What happened
The initial Gate 2 rerun reported only 3 quarantined handles instead of the expected 8.
Investigation showed **five quarantine.json records had the wrong platform label**, so
they were excluded from the platform-split reconciliation logic that expected them on
the other side.

## Corrections applied (quarantine.json platform labels)
| Handle | Was | Corrected to |
|---|---|---|
| @nastasiawong | TikTok | Instagram |
| @nomadicmovement | TikTok | Instagram |
| @oceanwanderer | TikTok | Instagram |
| @rachid_dahnoun | TikTok | Instagram |
| @sidewalkerdaily | Instagram | TikTok |

## Result after correction
- `GATE 2 [PASS]` — 100 influencer rows, 50 Instagram / 50 TikTok, **8 quarantined**,
  0 errors, 0 warnings.
- Quarantined handles (zero itinerary attribution allowed):
  1. @africansafari
  2. @limsawkward
  3. @marklharriosn
  4. @nastasiawong
  5. @nomadicmovement
  6. @oceanwanderer
  7. @rachid_dahnoun
  8. @sidewalkerdaily
- Gate 4 (DB reconciliation) will re-verify zero itineraries are attributed to these handles.
