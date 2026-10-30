# Server-Side GTM Cost Optimizer & Noise Event Pruner

> Model server-side GTM event filtering and Cloud Run settings. Actual cost effects depend on traffic, configuration, and pricing; no savings percentage is promised.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: TEMPLATE_FRAMEWORK](https://img.shields.io/badge/Format-TEMPLATE--FRAMEWORK-green.svg)](#)
[![Tier: 1](https://img.shields.io/badge/Tier-1-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**PRO** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Create an open-source server-side GTM cost optimization toolkit: 1) Architecture guide detailing client-side event filtering triggers (blocking scroll, timer, and visibility events from sending sGTM requests), 2) Ready-to-import Web GTM transformation rules, 3) Python cloud billing cost estimator (`estimate_sgtm_cost.py`), 4) Step-by-step GCP Cloud Run auto-scaling and concurrency tuning instructions.

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `architecture/filtering-blueprint.md`
- `configs/cloud-run-budget-alerts.json`
- `docs/cloud-run-tuning.md`
- `examples/cost-reduction-case-study.md`
- `examples/cost_reduction_case_study.md`
- `gtm-templates/noise-filter-trigger.json`
- `LICENSE`
- `README.md`
- `scripts/estimate_sgtm_cost.py`
- `scripts/filter_noise_events.py`
- `templates/sgtm-cost-reduction-rules.md`
- `tests/test_cost_optimizer.py`


---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

### Run CLI Script
```bash
python scripts/estimate_sgtm_cost.py --help
```

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "reporting",
  "repository": "server-side-gtm-cost-optimizer",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **Cloud Run Concurrency Limits:** Configures container min/max instances to handle flash sales without incurring idle runtime billing during low-traffic night hours.
- **High-Volume Noise Event Pruning:** Discards non-essential interaction events (e.g. scroll_depth, element_visibility) before firing billable downstream endpoints.
- **First-Party Cookie Lifetime:** Extends cookie expiration using server-side Set-Cookie headers while remaining compliant with regional privacy guidelines.

---

## 📚 Primary Documentation & Verifiable References

- [Google Tag Platform: Server-Side Tagging Overview](https://developers.google.com/tag-platform/tag-manager/server-side) - Core architecture for managing cloud container clients and tags.
- [Google Cloud Run Pricing & Scalability Guidelines](https://cloud.google.com/run/pricing) - Cost optimization strategies for container CPU allocation and memory limits.
- [Cloudflare Workers Server-Side GTM Integration Guide](https://developers.cloudflare.com/) - Edge routing for routing tracking requests through first-party domains.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
