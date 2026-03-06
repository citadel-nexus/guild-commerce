# Guild: Commerce

> *"Every transaction is a relationship. Every relationship is an empire."*

The Commerce Guild is the front line of Citadel Nexus revenue — trade contractors,
service businesses, and B2B operators who need automation without complexity.
This guild powers the **ZES (Zero-Entry Services)** product line and the
**TradeBuilder** website platform.

---

## Identity

| | |
|---|---|
| **Sigil** | The Crossed Keys |
| **Vibe** | Hustle. Precision. The handshake that seals the deal. |
| **Color** | Gold `#F0A500` |
| **NATS Prefix** | `citadel.commerce.*` |
| **Port** | `8422` |
| **Parent Guild** | Commerce (root) |

---

## Purpose

Commerce is the engine of the guild economy. Its mandate:

- Deliver **ZES Scout / Operator / Autopilot** tiers to 30+ trade industries
- Power **TradeBuilder** — professional websites for contractors at $129–$299/mo
- Capture leads, qualify them through the Sorting Hat, and route to C.R.E.W. agents
- Track live subscription revenue via Stripe, surface it in the Finance Guild dashboard

---

## Domains of Operation

### ZES (Zero-Entry Services)
| Tier | Price | Capability |
|------|-------|-----------|
| Scout | $15/mo | Basic CRM + scheduling |
| Operator | $20/mo | + AI voice + SEO |
| Autopilot | $30/mo | Full automation + analytics |

### TradeBuilder
| Tier | Price | Capability |
|------|-------|-----------|
| Starter | $129/mo | Landing page + contact forms |
| Growth | $199/mo | + Conversion funnels |
| Premium | $299/mo | + Ops dashboard + custom dev |

### Target Industries
HVAC, Plumbing, Electrical, Roofing, Landscaping, Pest Control, Cleaning,
Painting, Flooring, Concrete, Fencing, Pool Service, Auto Repair, and 16+ more.

---

## Services & Integrations

| Service | Role |
|---------|------|
| **Stripe** | Live subscription billing + webhook events |
| **Cal.com** | Appointment scheduling (Scout+) |
| **ElevenLabs** | AI voice agent (Operator+) |
| **Customer.io** | Lifecycle email journeys |
| **PostHog** | Conversion funnel analytics |
| **Datadog** | API latency + error rate monitors |
| **NATS** | `citadel.commerce.lead.*`, `citadel.commerce.subscription.*` |

---

## NATS Event Subjects

```
citadel.commerce.lead.captured      — New lead from form/webhook
citadel.commerce.lead.qualified     — Dossier enrichment complete
citadel.commerce.subscription.new   — Stripe checkout succeeded
citadel.commerce.subscription.churn — Subscription cancelled
citadel.commerce.voice.call_end     — ElevenLabs call completed
citadel.commerce.booking.scheduled  — Cal.com appointment created
```

---

## Mission System

Commerce missions drive XP and Brotherhood rank progression. Missions reset every sprint (14 days).

| Mission | Description | XP | Unlock |
|---------|-------------|-----|--------|
| First Lead | Capture your first lead via Sorting Hat | 100 | Default |
| Voice Agent Live | Deploy a ZES voice agent for a client | 300 | Scout rank |
| TradeBuilder Launch | Complete a TradeBuilder site delivery | 500 | Operator rank |
| Stripe Wired | Connect a live subscription webhook end-to-end | 150 | Default |
| 10-Lead Streak | Capture 10 qualified leads in 7 days | 250 | Scout rank |
| Churn Defender | Retain a cancellation through the dunning flow | 400 | Operator rank |
| New Vertical | Launch ZES for a new trade industry | 600 | Autopilot rank |

**Daily missions (reset 00:00 UTC):**
- Emit a `citadel.commerce.lead.captured` event — 25 XP
- Log a Stripe subscription renewal — 25 XP

XP accumulates toward Brotherhood rank: Initiate → Brother → Devotion Leader → Council → Royal Family.
Trust Points (TP) are spent per agent invocation and earned through successful outcomes.

---

## Guild Expectations

**Members:**
- Complete at least 1 mission per sprint
- Maintain CAPS composite score ≥ 0.60 to stay Active
- Complete Commerce guild onboarding within 7 days of Sorting Hat placement
- Post weekly activity in `#deal-talk` or `#agent-dev` lobby channels

**Contributors:**
- All PRs must reference an SRS code (e.g., `SRS: COM-ZES-001`) in the description
- Stripe webhook handlers require unit tests before review
- New trade industry configs must include a ZES `.yaml` configuration file
- Code review turnaround: 48 hours

**Guild Lead (Chief Revenue Officer):**
- Weekly revenue summary posted to `#announcements`
- Resolve open PRs within 72 hours
- Create 2 new missions per sprint minimum

---

## Contributing

**Branch naming:**
```
feat/<srs-code>/<short-description>
fix/<srs-code>/<short-description>
docs/<srs-code>/<short-description>
```

**PR checklist:**
- [ ] SRS code referenced (e.g., `SRS: COM-ZES-007`)
- [ ] `npm test` passes
- [ ] New NATS subjects documented in this README
- [ ] `.env.example` updated if new env vars added
- [ ] No hardcoded credentials, IPs, or internal URLs

**Commit format:** `<type>(<srs-code>): <description>`
Example: `feat(COM-ZES-007): add HVAC industry ZES config`

**SAKE compliance:** New automation modules require a `.sake` file stub.
See [guild-sdk](https://github.com/citadel-nexus/guild-sdk) for the format.

---

## Getting Started

```bash
npm install
cp .env.example .env
# Fill in NATS_URL, SUPABASE_SERVICE_ROLE_KEY, STRIPE_SECRET_KEY
npm run dev
```

## Key Files

```
src/index.ts                  — Guild entry point
src/routes/health.ts          — Health check endpoint
src/automation/nats-listener.ts — NATS event router
src/automation/cml-bridge.ts  — CML task queue bridge
```

## Environment Variables

See `.env.example` for the full list. Required at minimum:

```
NATS_URL=nats://<your-nats-host>:4222
SUPABASE_URL=https://<your-project-ref>.supabase.co
SUPABASE_SERVICE_ROLE_KEY=<key>
STRIPE_SECRET_KEY=<key>
GUILD_PORT=8422
```
