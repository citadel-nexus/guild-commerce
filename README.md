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
