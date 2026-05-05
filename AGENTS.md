---
title: Advanced Systems & Data Agents Bundle
description: Three specialized agents for creative system design, deep research, and data transformation.
version: 1.0.0
created: 2026-05-05
---

# Advanced Systems & Data Agents Bundle

A collection of three specialized agents designed for complex technical work, informed by Andrej Karpathy's principles on AI-assisted coding and design.

## Agents in This Bundle

### 1. Advanced Systems Architect
**File:** `advanced-systems-architect.agent.md`

Specialized in designing and building creative advanced systems with structured thinking and minimal complexity.

**Best for:**
- System architecture and design decisions
- Distributed systems and data pipelines
- Technology choices and tradeoff analysis
- Scalability and performance design

**Example prompt:** "Design a distributed caching layer for real-time data. What are the tradeoffs?"

---

### 2. Deep Web Researcher
**File:** `deep-web-researcher.agent.md`

Conducts thorough web research, uncovers information from disparate sources, and synthesizes actionable insights.

**Best for:**
- Competitive intelligence and market research
- Finding technical documentation and open-source projects
- Validating facts and discovering emerging trends
- Deep-dive investigations with multiple sources

**Example prompt:** "Research the founding team of [company]. Find their LinkedIn profiles, prior roles, and any public interviews."

---

### 3. Data Enrichment & Structurer
**File:** `data-enrichment-structurer.agent.md`

Transforms raw, unstructured data into clean, enriched, validated datasets with clear schema.

**Best for:**
- Data cleaning and normalization
- Schema design and data pipeline creation
- Data validation and quality assessment
- Enriching datasets with external sources

**Example prompt:** "Clean and normalize this customer data: [CSV]. Remove duplicates, standardize phone numbers, add geocoding."

---

## Shared Foundation: Karpathy Principles

All three agents operate on four core principles:

| Principle | Purpose |
|-----------|---------|
| **Think Before Coding** | Clarify assumptions, surface tradeoffs, and ask for help before executing |
| **Simplicity First** | Minimum viable solution; no speculative features or over-engineering |
| **Surgical Changes** | Touch only what's necessary; preserve existing patterns and style |
| **Goal-Driven Execution** | Define success criteria upfront; loop until verified |

---

## How to Use This Bundle

1. **Choose the right agent** — Select based on your task (architecture, research, or data work)
2. **State your goal clearly** — Provide context, constraints, and success criteria
3. **Expect clarifying questions** — Each agent will surface assumptions before proceeding
4. **Iterate on results** — Agents verify against explicit success criteria

---

## Workflow Examples

### Example 1: Design + Research + Data
*"I want to build a recommendation system"*
1. Use **Advanced Systems Architect** to design the system (model, inference pipeline, serving)
2. Use **Deep Web Researcher** to find benchmarks and emerging techniques
3. Use **Data Enrichment & Structurer** to prepare training and evaluation datasets

### Example 2: Competitive Analysis
*"Analyze a competitor's product offering"*
1. Use **Deep Web Researcher** to gather product info, pricing, features
2. Use **Data Enrichment & Structurer** to normalize findings into a comparison matrix
3. Use **Advanced Systems Architect** to propose counter-strategies

### Example 3: Data Pipeline
*"Build a real-time event processing system"*
1. Use **Data Enrichment & Structurer** to define event schema and validation rules
2. Use **Advanced Systems Architect** to design the pipeline (ingestion, processing, storage)
3. Use **Deep Web Researcher** to validate against industry best practices

---

## Startup Growth Agents

These agents support a three-stage SMB lead and solution workflow:

### 1. Startup Lead Discovery
**File:** `startup-lead-discovery.agent.md`

Find small and medium businesses in a target region with weak digital presence, poor website quality, missing Google profile signals, weak review response, or sparse social activity.

### 2. Startup Data Enrichment
**File:** `startup-data-enrichment.agent.md`

Enrich lead intelligence, analyze top competitor success patterns, and structure recommended digital growth strategies for each business.

### 3. Startup Growth Engineer
**File:** `startup-growth-engineer.agent.md`

Design and build tailored 3-page websites, review/social workflows, and outreach campaigns that convert leads into paying customers.

**Example prompt:** "Discover local cafes with bad websites, enrich the lead list, then build a campaign and 3-page website strategy for spring launch."

---

### 4. Startup Lead System
**File:** `startup-lead-system.agent.md`

Orchestrates discovery, enrichment, and growth engineering for a complete lead system. Use it to find 5 target businesses and generate 5 review-ready outreach drafts.

**Example prompt:** "@startup-lead-system Find 5 businesses in SE Portland, OR with broken or outdated websites and weak local profiles, then produce 5 message drafts to review and send."

---

### 5. Wallstreet Broker Agent
**File:** `wallstreet-broker-agent.agent.md`

Research, scrape, and analyze stock market data to provide high-probability buy/sell signals with detailed reasoning and predictions. Uses web scraping, quantitative analysis, and historical data techniques.

**Example prompt:** "Analyze AAPL stock: scrape recent news, analyze technicals, compare to MSFT and GOOGL, provide buy/sell signal with 80%+ probability and reasoning."

---

## Installation

These agents are already saved in your workspace as `.agent.md` files. VS Code will auto-discover them based on context and file proximity.

To use a specific agent, reference it in your prompt:
```
@advanced-systems-architect Design a real-time analytics platform...
@deep-web-researcher Research the state of vector databases in 2026...
@data-enrichment-structurer Clean this messy transaction log...
```

---

## Notes

- **Principle adherence** — Each agent enforces the Karpathy principles to reduce costly mistakes
- **Caution over speed** — These agents bias toward asking clarifying questions for non-trivial work
- **Source-driven** — Research agent always cites sources; data agent tracks transformations
- **Minimal specs** — All agents push back on overengineering and speculative features

---

## License

MIT - Derived from [Karpathy-inspired principles](https://github.com/forrestchang/andrej-karpathy-skills)
