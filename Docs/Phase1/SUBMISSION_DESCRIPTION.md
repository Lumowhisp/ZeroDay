# Forensica — Submission Description

> **Project Codebase & Research Repository:** [GitHub - Lumowhisp/ZeroDay](https://github.com/Lumowhisp/ZeroDay)

---

## The Problem

Indian banks lost ₹13,930 Cr to fraud in FY24 (RBI Annual Report), with loan advances accounting for over 70% of these losses. At Canara Bank — with 9,849 domestic branches and ₹10.73 Lakh Cr in advances — every mortgage and commercial loan requires manual verification of land records, legal documents (Power of Attorney, sale deeds, affidavits), and financial statements (ITR, bank statements, salary slips). This manual process takes 3–7 working days, costs ~₹1,500 per file, and is vulnerable to sophisticated digital forgeries that human reviewers consistently miss — such as forged survey numbers, photoshopped salary figures, and spliced signatures. For a detailed breakdown, see our [Fraud Landscape Deep Dive](https://github.com/Lumowhisp/ZeroDay/blob/main/Docs/Phase1/research/fraud_landscape.md).

Existing verification tools focus narrowly on identity card OCR and database lookups. They verify that a PAN exists — but cannot detect if the document image itself was digitally manipulated. No commercial solution in India currently performs pixel-level forensic analysis on banking documents. See our [Competitor Analysis & Differentiation](https://github.com/Lumowhisp/ZeroDay/blob/main/Docs/Phase1/research/competitor_analysis.md).

## Our Solution: Forensica

Forensica is a real-time document forensic intelligence engine built specifically for Canara Bank's underwriting pipeline (see [Canara Bank Underwriting Profile](https://github.com/Lumowhisp/ZeroDay/blob/main/Docs/Phase1/research/canara_bank_profile.md)). It automatically detects tampering, changes, and forgery attempts across land records, legal documents, and financial statements using a proprietary **5-layer forensic analysis pipeline**.

Unlike single-model approaches (Image → CNN) that most teams build, Forensica implements **defense-in-depth forensic analysis** — five independent detection layers that catch what others miss. For an in-depth review, refer to our [Forensic Techniques Analysis](https://github.com/Lumowhisp/ZeroDay/blob/main/Docs/Phase1/research/forensic_techniques.md):

*   **Layer 1 — Metadata Forensics:** Parses EXIF/XMP headers to detect editing software signatures (Photoshop, GIMP, Canva), timestamp anomalies, and creator history trails.
*   **Layer 2 — Error Level Analysis (ELA):** Resaves images at a known quality and computes pixel-level difference maps. Tampered regions (modified numbers, signatures) glow brightly because their compression history differs from original content. You can run our prototype script in the [Proof-of-Concept Directory](https://github.com/Lumowhisp/ZeroDay/tree/main/poc) or view the [ELA Demo Script](https://github.com/Lumowhisp/ZeroDay/blob/main/poc/ela_demo.py).
*   **Layer 3 — Deep Pixel Analysis (CNN):** An EfficientNet-B3 neural network fine-tuned on CASIA 2.0 and IMD2020 forgery datasets achieves **94%+ detection accuracy** (benchmarked on peer-reviewed datasets: Dong et al., 2022). It classifies splicing boundaries and copy-move patterns at the pixel level. Learn more in our [Datasets Profile](https://github.com/Lumowhisp/ZeroDay/blob/main/Docs/Phase1/research/datasets.md) and [Technical Validation Log](https://github.com/Lumowhisp/ZeroDay/blob/main/Docs/Phase1/research/tech_validation.md).
*   **Layer 4 — Font & Semantic Validation:** A hybrid OCR engine (Tesseract + EasyOCR for regional scripts) extracts text and analyzes character geometry — aspect ratios, baseline offsets, and line-heights — to catch digit manipulation (e.g., a "3" changed to an "8").
*   **Layer 5 — Cross-Document Intelligence:** Instead of analyzing documents in isolation, Forensica builds a **unified data graph** across the entire loan application — cross-referencing names across Aadhaar, PAN, and salary slips; matching survey numbers between Sale Deeds, Encumbrance Certificates, and Land Revenue Records (Khata/7-12 Extract/Patta); and verifying timeline consistency across employment dates, registration, and tax filings. Fraud where individual documents look clean but contradict each other is caught here. See our [Land Records India Research](https://github.com/Lumowhisp/ZeroDay/blob/main/Docs/Phase1/research/land_records_india.md).

A **Decision Fusion Engine** aggregates all five layer scores into a single weighted risk verdict. An **Explainability Engine** then generates visual tampering heatmaps and natural language justifications — fully aligned with **RBI's FREE-AI Framework (August 2025), Sutra 6: Understandable by Design**.

## Agentic Document Routing (Human-in-the-Loop)

Forensica intelligently routes documents to optimize underwriting:
*   **Low Risk (Score < 0.4):** Auto-verified, fast-tracked for CBS approval.
*   **Medium Risk (0.4–0.8):** Routed to underwriter dashboard with AI-annotated heatmaps for human review.
*   **High Risk (Score > 0.8):** Blocked and escalated to senior credit manager queue.

This creates a scalable Human-in-the-Loop workflow aligned with **FREE-AI Sutra 2 (People First)** — no loan is ever auto-rejected without human oversight.

## RBI FREE-AI Compliance (All 7 Sutras)

Forensica is designed to comply with all 7 Sutras of RBI's FREE-AI framework. You can read our exhaustive mapping in the [RBI FREE-AI Compliance Report](https://github.com/Lumowhisp/ZeroDay/blob/main/Docs/Phase1/research/compliance_research.md):
*   **Sutra 1 (Trust):** 5-layer ensemble prevents single-point failure.
*   **Sutra 2 (People First):** HITL routing ensures human authority at decision points.
*   **Sutra 3 (Innovation):** Automates 80%+ of low-risk verifications, cutting TAT from days to seconds.
*   **Sutra 4 (Fairness):** Evaluates only pixel/file properties — **zero access** to borrower demographics. Architectural guarantee of non-discrimination.
*   **Sutra 5 (Accountability):** Immutable audit trail in PostgreSQL (SHA-256 hashes, model versions, fusion weights, timestamps).
*   **Sutra 6 (Explainability):** Visual heatmaps + natural language justifications in English/Hindi.
*   **Sutra 7 (Safety):** Containerized deployment with graceful degradation (falls back to L1+L2 if ML workers fail).

## Data Privacy (DPDP Act 2023 + PMLA Compliance)

Forensica implements a **4-Phase Tiered Data Retention Architecture**:
1.  **Active Processing:** Documents encrypted with AES-256 during underwriting.
2.  **Cold Storage:** Upon loan decision, files migrate to restricted storage with separate encryption keys (HSM/KMS).
3.  **Cooling-Off (60–90 days):** Retained for disputes, audits, and bias reviews.
4.  **Crypto-Shredding:** HSM key is destroyed — raw images become permanently unreadable.

Post-erasure, only SHA-256 hashes, consent logs, and non-sensitive derived fields are retained for audit compliance (PMLA 5-year requirement).

## Impact & Business Case (Canara Bank Study)

Core business metrics are structured below for high readability:
*   **Verification Time:** Drastically reduced from 3–7 days (manual processing) to **under 3 seconds** per document.
*   **Cost per Application:** Cut from ~₹1,500 (empanelled searches and audits) to just **₹30** per application (a **98% cost reduction**).
*   **Annual Operational Savings:** Projected savings of **₹22.05 Cr/year** for Canara Bank based on ~1,50,000 processed mortgage applications.
*   **Fraud Write-off Prevention:** Projected prevention of **₹84.6 Cr/year** in loan write-offs by flagging digital tampering, directly improving Net NPA ratios.
*   **Detection Accuracy:** Boosted to **94%+** using our multi-layer AI ensemble compared to the ~85% baseline human detection rate.
*   **Operational Consistency:** Standardized evaluation criteria across all 9,849 domestic branches, removing human variance.

For the underlying financial modeling, see our [Operational Impact Analysis](https://github.com/Lumowhisp/ZeroDay/blob/main/Docs/Phase1/drafts/impact_section.md).

## Feasibility & Tech Stack

Built entirely on proven, open-source technologies: **FastAPI** (backend), **Next.js** (dashboard), **PyTorch** (CNN inference), **Redis + Celery** (async queue), **PostgreSQL** (audit DB), **Docker Compose** (single-command deployment).

**4-Week Sprint Plan:**
*   Week 1: Core forensic engine (Layers 1–3) — working MVP
*   Week 2: Intelligence layers (4–5) + Decision Fusion + LLM explanations
*   Week 3: Underwriter dashboard + agentic routing UI
*   Week 4: Containerization, testing, and demo preparation

Every component uses pre-existing libraries and pre-trained weights. No moonshot dependencies. Check our public files in the [ZeroDay Repository](https://github.com/Lumowhisp/ZeroDay) to inspect the structure.

## Team ZeroDay

*   **Aditya** — Team Lead & Tech Architect (FastAPI, ML, system integration)
*   **Aaryan** — FrontEnd Developer & UI/UX Designer
*   **Sonali** — Domain Researcher & Impact Analyst (banking workflows, regulatory compliance, financial modeling)
