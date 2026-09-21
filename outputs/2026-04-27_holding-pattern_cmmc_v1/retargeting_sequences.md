# Retargeting & Lead Magnet Sequences

## Audience Buckets
| Segment Tag | Definition | Primary Channel |
|-------------|------------|-----------------|
| `cohort:cmmc_subs_warm` | Opted-in, opened Email 1 | Email + LinkedIn DM |
| `stage:hp_engaged` | Clicked checklist or consult link | SMS + Paid Custom Audience |
| `stage:hp_idle` | No opens/clicks after 5 days | Paid + Newsletter bump |

## Email Bump (goes to `stage:hp_idle`)
- **Subject:** "Still need that SPRS score sanity check?"
- **Timing:** Day 7
- **Copy:** 2-paragraph reminder + resend checklist link + micro CTA "Reply 'score'".

## SMS Nudge (goes to `stage:hp_engaged`)
- **Trigger:** Calendly not booked within 48h of Email 2 click
- **Copy:**
  > "YaRo Security: Want me to hold a Control Compression slot for you this week? Text back a time window and I’ll lock it." (Link shortened with branded domain.)

## Paid Retargeting
- **Platform:** LinkedIn + Meta custom audiences built from email list export.
- **Creative 1 (Video):** 15-sec clip of dashboard with caption "48-hour SPRS audit for $299".
- **Creative 2 (Static):** Quote card "We saved our Navy option year" + CTA button "Book audit".
- **Offer:** Direct to audit checkout with limited slots.
- **Frequency Cap:** 2 impressions/day/user.

## Lead Magnet Recycling
- If contact does not claim checklist (no click in Email 1), automatically send **Lead Magnet Reminder** 24h later with subject "You unlocked the Prime Readiness Checklist" — include link + snippet of Section 3 (Access & Credential Hygiene) to show value.

## Workflow Diagram
1. **Opt-in → Email 1**
2. If opened → add to `cohort:cmmc_subs_warm`
3. If clicked → add `stage:hp_engaged`, start SMS timer
4. No open by Day 5 → add `stage:hp_idle`, send Email bump + add to paid retargeting audience
5. After selling event invite (Email 3), anyone still `stage:hp_idle` remains in paid loop until they attend event or unsubscribe.
