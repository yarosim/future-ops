# CloserForge — Daily Orchestration Loop

## Daily Flow

1. **Pull target niches from Einstein**
2. **Run niche-research** on each target
3. **Score niches** for urgency, budget, simplicity, retention
4. **Build offer** with offer-designer per top niche
5. **Generate outreach** with cold-outreach-generator
6. **Generate discovery pack** (questions, objection map, call prep)
7. **Push leads into LeadFlow / PostOffice**
8. **When reply received** → generate call prep with sales-call-prep
9. **After call** → generate proposal with proposal-writer
10. **On close** → trigger client-onboarding-workflow
11. **Send fulfillment tasks** to OnyxAgency / delivery agents
12. **Log wins and losses** into MEMORY.md

---

## Niche Scoring Model

```
profit_score =
  (urgency * 0.25) +
  (monthly_recurring_pain * 0.20) +
  (ease_of_delivery * 0.15) +
  (ticket_size * 0.15) +
  (short_sales_cycle * 0.10) +
  (low_competition * 0.10) +
  (upsell_potential * 0.05)
```

Each factor scored 1–10. Minimum viable score to pursue: 6.0.

---

## Top Initial Verticals

- Local trades
- Private clinics
- Legal intake
- Med spas
- Home services
- Specialty contractors
- Small manufacturers
- Cybersecurity compliance leads for SMB and GovCon
- Turo-host tools as digital/service products
- Federal contractor cyber readiness packages

---

## Daily Outputs

Every day, CloserForge emits:

1. **Top 3 niches to pursue** (scored)
2. **One offer per niche** (from offer-designer)
3. **10 outbound messages per niche** (from cold-outreach-generator)
4. **One discovery call pack per niche** (from discovery-question-generator)
5. **One proposal skeleton** (from proposal-writer)
6. **One onboarding checklist** (from client-onboarding-workflow)
7. **One "kill / keep / double-down" memo to Alex**

---

## Example Command Brief for Alex

```
Run CloserForge for today.

Target priority:
1. YaRo Security cyber/compliance services
2. local contractor automation offers
3. GovElites business support offers

Tasks:
- find highest-urgency niches
- produce best recurring offer per niche
- generate outreach pack
- generate discovery pack
- generate onboarding workflow
- return only top opportunities with clear revenue potential
```
