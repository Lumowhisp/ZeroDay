<div align="center">

<img src="Logo/Red.png" alt="DocShield AI" width="200"/>

# 🛡️ DocShield AI

### *Real-Time Document Forensic Intelligence for Indian Banking*

[![SuRaksha 2.0](https://img.shields.io/badge/SuRaksha_2.0-Canara_Bank-orange?style=for-the-badge)](https://canarabank.com)
[![Theme](https://img.shields.io/badge/Theme_1-Real--Time_Anomaly_Detection-blue?style=for-the-badge)](#-theme-alignment)
[![RBI FREE-AI](https://img.shields.io/badge/RBI_FREE--AI-All_7_Sutras_Compliant-green?style=for-the-badge)](#-rbi-free-ai-compliance-all-7-sutras)
[![Team](https://img.shields.io/badge/Team-ZeroDay-red?style=for-the-badge)](#-team-zeroday)
[![License](https://img.shields.io/github/license/Lumowhisp/ZeroDay?style=for-the-badge&color=purple)](LICENSE)

---

**An intelligent 5-layer forensic engine that detects tampering, forgery, and cross-document inconsistencies across land records, legal documents, and financial statements — in under 3 seconds.**

Built specifically for **Canara Bank's** underwriting pipeline. Compliant with **RBI FREE-AI (Aug 2025)** and **DPDP Act 2023**.

[📄 Idea Submission](Docs/Phase1/FINAL_SUBMISSION.md) · [🏗️ Implementation Plan](Docs/IMPLEMENTATION_PLAN.md) · [📊 Research Repository](#-phase-1-research-repository) · [🧬 How It Works](#-5-layer-forensic-pipeline)

</div>

---

## 📖 Table of Contents

- [🔥 The Problem](#-the-problem)
- [💡 Our Solution](#-our-solution)
- [🧬 5-Layer Forensic Pipeline](#-5-layer-forensic-pipeline)
- [🎯 Theme Alignment](#-theme-alignment)
- [🚀 Innovation Highlights](#-innovation-highlights)
- [🧭 RBI FREE-AI Compliance](#-rbi-free-ai-compliance-all-7-sutras)
- [🔒 Data Privacy Architecture](#-data-privacy--dpdp-act-2023)
- [📈 Impact & Business Case](#-impact--business-case)
- [🏗️ Feasibility & Sprint Plan](#-feasibility--4-week-sprint-plan)
- [🧩 Tech Stack](#-tech-stack)
- [📊 Phase 1 Research Repository](#-phase-1-research-repository)
- [📁 Project Structure](#-project-structure)
- [🎬 Team ZeroDay](#-team-zeroday)
- [📄 License](#-license)

---

## 🔥 The Problem

<table>
<tr>
<td width="60%">

Indian banks lost **₹13,930 Cr to fraud in FY24** (RBI Annual Report), with loan advances accounting for **70%+ of total losses**. At Canara Bank — with **9,849 domestic branches** and ₹10.73 Lakh Cr in global advances — every mortgage and commercial loan requires manual verification of land records, legal documents, and financial statements.

**Current pain points:**
- 📅 Manual verification takes **3–7 working days** per application
- 💸 Costs **~₹1,500 per file** in empanelled legal searches & CA audits
- 🔍 Human reviewers **miss sophisticated digital forgeries** — modified survey numbers, photoshopped salary figures, spliced signatures
- 🤖 Existing tools (HyperVerge, Digio, SignDesk) only do **identity OCR & database lookups** — they verify that a PAN *number* exists, not whether the PAN *card image* was digitally manipulated

</td>
<td width="40%">

```
₹13,930 Cr
  └── Bank fraud losses in FY24

70%+
  └── From loan advance fraud

3–7 days
  └── Manual verification TAT

₹1,500/app
  └── Current verification cost

0 tools
  └── Perform pixel-level forensic
      analysis on Indian banking
      documents today
```

</td>
</tr>
</table>

---

## 💡 Our Solution

**DocShield AI** is a real-time document forensic intelligence engine that **automatically detects tampering, changes, and forgery attempts** across land records, legal documents (Power of Attorney, sale deeds, court orders, affidavits), and financial statements (ITR, bank statements, salary slips).

Unlike single-model approaches (`Image → CNN → Real/Fake`), DocShield AI implements **defense-in-depth forensic analysis** — five independent detection layers, each catching what others miss:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        DOCSHIELD AI PIPELINE                           │
│                                                                        │
│  📄 Upload ──► L1: Metadata ──► L2: ELA ──► L3: CNN ──► L4: OCR/Font │
│                                                              │         │
│                                              L5: Cross-Doc ◄─┘         │
│                                                   │                    │
│                                         Decision Fusion Engine         │
│                                                   │                    │
│                                    ┌──────────────┼──────────────┐     │
│                                    ▼              ▼              ▼     │
│                              🟢 Low Risk    🟡 Medium Risk   🔴 High  │
│                              Fast-track     Human Review     Escalate  │
└─────────────────────────────────────────────────────────────────────────┘
```

**Key capabilities:**
- ⚡ **Real-time analysis** — under 3 seconds per document
- 🔬 **5-layer forensic pipeline** — defense-in-depth, not single-point failure
- 🧠 **Explainable verdicts** — visual heatmaps + natural language reasoning
- 🔗 **Cross-document intelligence** — catches fraud that single-doc analysis misses
- 🤖 **Agentic routing** — auto-triages flagged documents to the right reviewer
- 🇮🇳 **India-first** — Hindi + English OCR, Khata/7-12/Patta support, on-premise deployment

---

## 🧬 5-Layer Forensic Pipeline

| Layer | Technique | What It Catches | Technology |
|:-----:|:----------|:----------------|:-----------|
| **L1** | **Metadata Forensics** | Editing software fingerprints (Photoshop, GIMP, Canva), timestamp anomalies, creator history trails | `Pillow`, `PyExifTool` |
| **L2** | **Error Level Analysis (ELA)** | Locally edited regions with different compression histories — modified numbers, pasted signatures, spliced fields | `OpenCV`, `PIL` |
| **L3** | **Deep Pixel Analysis (CNN)** | Splicing boundaries, copy-move forgery patterns, noise residual inconsistencies. **94%+ accuracy** on CASIA 2.0 & IMD2020 benchmarks | `PyTorch`, `EfficientNet-B3` |
| **L4** | **Semantic & Font Validation** | Manipulated digits (e.g., "3" → "8" in survey numbers), font baseline deviations, character geometry anomalies | `Tesseract`, `EasyOCR` |
| **L5** | **Cross-Document Intelligence** | Name mismatches across Aadhaar/PAN/salary slips, property area contradictions between Sale Deed & Revenue Record, timeline inconsistencies | Custom graph engine |

> **Decision Fusion Engine** aggregates all 5 layer scores via weighted ensemble → **Explainability Engine** generates visual heatmaps + natural language justifications for every verdict.

---

## 🎯 Theme Alignment

> **Theme 1:** *"How can a bank automatically detect tampering, changes, or forgery attempts across land records, legal documents, and financial statements in real time? The goal is to provide intelligent insights to support faster, reliable decision-making during underwriting."*

| Theme Keyword | DocShield AI Coverage |
|:---|:---|
| "automatically detect" | ✅ 5-layer pipeline runs without human intervention |
| "tampering" | ✅ L2 (ELA) + L3 (CNN) catch pixel-level digital edits |
| "changes" | ✅ L4 (semantic/font analysis) detects altered values and dates |
| "forgery attempts" | ✅ L1 (metadata) + L3 (CNN) identify fabricated documents |
| "land records" | ✅ Supports Karnataka Khata, Maharashtra 7/12, Tamil Nadu Patta, Punjab Jamabandi |
| "legal documents" | ✅ Power of Attorney, sale deeds, court orders, affidavits, encumbrance certificates |
| "financial statements" | ✅ Bank statements, ITR, salary slips, balance sheets |
| "in real time" | ✅ Sub-3-second analysis per document |
| "intelligent insights" | ✅ Visual heatmaps + natural language explanations |
| "faster, reliable decision-making" | ✅ Agentic routing: fast-track / human review / escalation |
| "underwriting" | ✅ Designed specifically for Canara Bank's loan underwriting pipeline |

**11/11 keywords directly addressed.**

---

## 🚀 Innovation Highlights

### 1. Defense-in-Depth Pipeline (No Other Team Will Have This)
Most teams will build: `Image → CNN → Real/Fake`. We build a **5-layer ensemble** where each layer catches what others miss. Even if an adversarial image fools one model, the other four catch it.

### 2. Cross-Document Intelligence (Genuinely Novel)
Standard IDV platforms analyze documents in isolation. If a PAN card, Aadhaar, and Sale Deed are individually clean, they pass — even if the data between them contradicts. DocShield AI builds a **unified application graph** that cross-references names, survey numbers, dates, and addresses across all uploaded collateral.

### 3. Explainable AI (RBI FREE-AI Compliant)
Not just "forged" but *"forged because the registration number field shows re-compression artifacts inconsistent with the surrounding template, and the stated property area (8,500 sq ft) exceeds the Khata record (5,800 sq ft)."* Visual heatmaps + natural language reasoning for every verdict.

### 4. Agentic Document Routing (Human-in-the-Loop)
| Risk Score | Action | Destination |
|:-----------|:-------|:------------|
| `< 0.4` | ✅ Auto-verified | Fast-track to CBS approval |
| `0.4 – 0.8` | ⚠️ Flagged with annotations | Underwriter dashboard with heatmaps |
| `> 0.8` | 🚫 Blocked | Senior credit manager / audit queue |

No loan is ever auto-rejected without human oversight — compliant with FREE-AI Sutra 2 (People First).

---

## 🧭 RBI FREE-AI Compliance (All 7 Sutras)

DocShield AI is designed to comply with the **RBI FREE-AI Framework (August 13, 2025)** from day one:

| Sutra | Principle | How We Comply |
|:-----:|:----------|:--------------|
| **1** | Trust is the Foundation | 5-layer ensemble prevents single-point failure. Each layer is independently testable and auditable. |
| **2** | People First | Human-in-the-Loop (HITL) architecture. No loan auto-rejected without human review. |
| **3** | Innovation over Restraint | Automates 80%+ of low-risk verifications, cutting TAT from days to seconds. |
| **4** | Fairness & Equity | Engine evaluates only pixel/file properties — **zero access** to borrower demographics. Structural guarantee of non-discrimination. |
| **5** | Accountability | Immutable audit trail: SHA-256 hashes, per-layer scores, model versions, timestamps in append-only PostgreSQL. |
| **6** | Understandable by Design | Dual-channel XAI: visual heatmaps + natural language explanations in English/Hindi. |
| **7** | Safety & Resilience | Containerized deployment. Graceful degradation — falls back to L1+L2 if ML workers crash. Crypto-shredding for data lifecycle safety. |

> 📄 **Full Sutra-by-Sutra mapping with deep dives:** [compliance_research.md](Docs/Phase1/research/compliance_research.md)

---

## Data Privacy — DPDP Act 2023

DocShield AI implements a **4-Phase Tiered Data Retention Architecture** with **Crypto-Shredding**:

```
Phase 1: Active Processing          ──► AES-256 encrypted, app workers have access
    ↓ (Loan Decision Logged)
Phase 2: Restricted Cold Storage    ──► Re-encrypted with separate HSM key (Key-C),
    ↓                                    application access revoked
Phase 3: Cooling-Off (60–90 days)   ──► Retained for disputes, audits, bias reviews
    ↓ (Window Expires)
Phase 4: Crypto-Shredding           ──► HSM key destroyed → all raw images become
                                         permanently unreadable in milliseconds
    ↓
Permanent Archive: SHA-256 hashes + consent logs + derived fields only
```

**Key design decisions:**
- Separate encryption keys for active vs cold storage (blast radius containment)
- PMLA `regulatory_hold` flag prevents auto-deletion for AML-flagged cases (5-year override)
- SHA-256 hash archival serves as proof-of-existence under Bharatiya Sakshya Adhiniyam 2023

> **Full compliance analysis:** [compliance_research.md](Docs/Phase1/research/compliance_research.md)

---

## Impact & Business Case

### Canara Bank Case Study

| Metric | Current (Manual) | With DocShield AI | Improvement |
|:-------|:-----------------|:------------------|:------------|
| **Verification Time** | 3–7 days | < 3 seconds | **~100,000x faster** |
| **Cost per Application** | ₹1,500 | ₹30 | **98% reduction** |
| **Annual Operational Savings** | — | **₹22.05 Cr/year** | New |
| **Fraud Write-off Prevention** | — | **₹84.6 Cr/year** | New |
| **Detection Accuracy** | ~85% (human) | **94%+** (AI ensemble) | +9% |
| **Consistency** | Varies across 9,849 branches | Standardized | Uniform |

### Social Impact
- **Rural Land Protection:** Verifies land record integrity, preventing fraudulent property mortgaging that disproportionately affects rural communities
- **Financial Inclusion:** Lower verification costs make micro-loans (Mudra, SHG) viable to audit, expanding access for underserved borrowers

> **Full financial model:** [impact_section.md](Docs/Phase1/drafts/impact_section.md) · **Fraud landscape research:** [fraud_landscape.md](Docs/Phase1/research/fraud_landscape.md)

---

## Feasibility & 4-Week Sprint Plan

| Week | Focus | Deliverable |
|:-----|:------|:------------|
| **Week 1** (June 1–8) | Core Forensic Engine (L1–L3) | API that accepts JPEGs/PDFs, parses metadata, generates ELA maps, outputs CNN scores |
| **Week 2** (June 9–16) | Intelligence Layers (L4–L5) + Fusion | OCR integration (English + Hindi), font geometry, cross-doc parsing, LLM explanations |
| **Week 3** (June 17–24) | Dashboard + Agentic Routing | Next.js interface with heatmap viewer, risk queue, and side-by-side doc review |
| **Week 4** (June 25–30) | Hardening + Demo Prep | `docker compose up`, unit tests, forged test cases, presentation materials |

**Graceful Degradation:** If Layer 3 (CNN) or Layer 4 (OCR) workers crash, the system falls back to Layers 1–2 (Metadata + ELA) inline — API stays operational with reduced but functional detection.

> **Full feasibility analysis:** [feasibility_section.md](Docs/Phase1/drafts/feasibility_section.md) · **Tech validation scripts:** [tech_validation.md](Docs/Phase1/research/tech_validation.md)

---

## Tech Stack

| Component | Technology |
|:----------|:-----------|
| **Backend API** | FastAPI · Python 3.11 · Celery · Redis |
| **Frontend** | Next.js 14 · TypeScript · Shadcn/ui · Framer Motion |
| **ML / Computer Vision** | PyTorch · EfficientNet-B3 · OpenCV · Pillow |
| **OCR** | Tesseract 5.x · EasyOCR (Hindi + English + Regional) |
| **LLM (Explainability)** | Google Gemini API (India region) / Llama-3-8B (air-gapped fallback) |
| **Database** | PostgreSQL (WAL + PITR, Row-Level Security) |
| **Deployment** | Docker · Docker Compose · On-premise ready |
| **Security** | AES-256 encryption · TLS 1.3 · HSM/KMS key segregation |

---

## Phase 1 Research Repository

All research produced during the Idea Phase is documented and available for review:

### Research Files

| # | Document | Description | Link |
|:-:|:---------|:------------|:-----|
| 1 | **Forensic Techniques** | ELA, metadata forensics, CNN classifiers, noise residual filters, font analysis — with code examples and paper citations | [forensic_techniques.md](Docs/Phase1/research/forensic_techniques.md) |
| 2 | **Datasets Catalog** | CASIA v2.0, Columbia, COVERAGE, CoMoFoD, IMD2020, and Indian-specific datasets (Mendeley, BHSig260-Hindi) | [datasets.md](Docs/Phase1/research/datasets.md) |
| 3 | **RBI FREE-AI Mapping** | Full 7-Sutra compliance matrix with deep dives on Fairness (Sutra 4) and Resilience (Sutra 7) | [rbi_free_ai.md](Docs/Phase1/research/rbi_free_ai.md) |
| 4 | **Competitor Analysis** | Feature comparison with HyperVerge, Digio, SignDesk, Attestiv, Jumio, Onfido, and FotoForensics | [competitor_analysis.md](Docs/Phase1/research/competitor_analysis.md) |
| 5 | **Tech Validation** | Integration versions, "Hello World" scripts, gotchas, and performance benchmarks for all dependencies | [tech_validation.md](Docs/Phase1/research/tech_validation.md) |
| 6 | **Canara Bank Profile** | FY25 financials: 9,849 branches, ₹10.73L Cr advances, 2.94% Gross NPA, 0.70% Net NPA | [canara_bank_profile.md](Docs/Phase1/research/canara_bank_profile.md) |
| 7 | **Indian Land Records** | Regional terminology (Khata, 7/12, Patta, Jamabandi), DILRMP/ULPIN systems, and common forgery vectors | [land_records_india.md](Docs/Phase1/research/land_records_india.md) |
| 8 | **Fraud Landscape** | Banking fraud metrics (₹13,930 Cr FY24), verification costs, and historical fraud case studies | [fraud_landscape.md](Docs/Phase1/research/fraud_landscape.md) |
| 9 | **Compliance & Privacy** | DPDP Act 2023, PMLA overrides, data localization, tiered retention, crypto-shredding architecture, key segregation | [compliance_research.md](Docs/Phase1/research/compliance_research.md) |

### Draft Sections

| # | Document | Description | Link |
|:-:|:---------|:------------|:-----|
| 1 | **Problem Statement** | Data-backed 4-sentence overview | [problem_statement.md](Docs/Phase1/drafts/problem_statement.md) |
| 2 | **Solution Section** | Proposed solution + technical approach | [solution_section.md](Docs/Phase1/drafts/solution_section.md) |
| 3 | **Innovation Section** | Four pillars of uniqueness | [innovation_section.md](Docs/Phase1/drafts/innovation_section.md) |
| 4 | **Feasibility Section** | 4-week sprint plan + fallback architecture | [feasibility_section.md](Docs/Phase1/drafts/feasibility_section.md) |
| 5 | **Impact Section** | Cost-benefit projections + social impact | [impact_section.md](Docs/Phase1/drafts/impact_section.md) |

### Proof of Concept

| # | File | Description | Link |
|:-:|:-----|:------------|:-----|
| 1 | **ELA Demo Script** | Python script demonstrating Error Level Analysis on sample images | [ela_demo.py](poc/ela_demo.py) |

---

## Project Structure

```
ZeroDay/
├── 📄 README.md                          ← You are here
├── 📄 LICENSE                            # MIT License
│
├── 📂 Docs/
│   ├── Detail.md                         # SuRaksha hackathon details & rules
│   ├── IMPLEMENTATION_PLAN.md            # Full technical architecture blueprint
│   └── Phase1/                           # ── Idea Submission Phase ──
│       ├── FINAL_SUBMISSION.md           # Assembled submission document
│       ├── SUBMISSION_DESCRIPTION.md     # Portal description text
│       ├── IDEA_SUBMISSION_PLAN.md       # Scoring strategy & criteria mapping
│       ├── aditya.md                     # Task sheet — Lead / Architect
│       ├── aaryan.md                     # Task sheet — ML / Tech Research
│       ├── sonali.md                     # Task sheet — Domain / Impact
│       ├── research/                     # 9 research documents (see table above)
│       ├── drafts/                       # 5 section drafts
│       └── assets/                       # Diagrams & POC outputs
│
├── 📂 poc/
│   └── ela_demo.py                       # ELA proof-of-concept script
│
├── 📂 Logo/                              # Project branding assets
│
├── 📂 frontend/                          # Next.js dashboard (Phase 2)
├── 📂 backend/                           # FastAPI service (Phase 2)
└── 📂 ml/                               # PyTorch training pipeline (Phase 2)
```

---

## Hackathon Timeline

| Phase | Date | Status |
|:------|:-----|:------:|
| **Idea Submission** | May 24, 2026 | ✅ Ready |
| **Prototype Development** | June 1–30, 2026 | ⬜ Upcoming |
| **Grand Finale** | July 20, 2026 (Bengaluru) | ⬜ Upcoming |

---

## Team ZeroDay

| Member | Role | Responsibilities |
|:-------|:-----|:-----------------|
| **Aditya** | Team Lead & Tech Architect | FastAPI/Next.js architecture, system integration, submission ownership, key lifecycle management |
| **Aaryan** | ML Developer & Tech Researcher | PyTorch CNN models, OpenCV ELA, Tesseract OCR, dataset pipelines, feasibility validation |
| **Sonali** | Domain Researcher & Impact Analyst | Banking workflow mapping, regulatory compliance (DPDP, FREE-AI, PMLA), financial modeling |

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with 🔥 by Team ZeroDay for SuRaksha Cyber Hackathon 2.0**

*Protecting documents. Preventing fraud. Powering trust.*

[![Canara Bank](https://img.shields.io/badge/Built_for-Canara_Bank-orange?style=flat-square)](https://canarabank.com)
[![RBI](https://img.shields.io/badge/Compliant_with-RBI_FREE--AI-green?style=flat-square)](#-rbi-free-ai-compliance-all-7-sutras)
[![DPDP](https://img.shields.io/badge/Privacy-DPDP_Act_2023-blue?style=flat-square)](#-data-privacy--dpdp-act-2023)

</div>