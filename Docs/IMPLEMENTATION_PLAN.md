# 🏆 ZeroDay — SuRaksha 2.0 Winning Strategy & Implementation Plan

> **Team:** ZeroDay | **Hackathon:** SuRaksha Cyber Hackathon 2.0 by Canara Bank
> **Prototype Phase:** June 1–30, 2026 | **Grand Finale:** July 20, 2026 (Bengaluru)
> **Prize Target:** 🥇 ₹5,00,000

---

## 1. Critical Strategic Analysis

### 1.1 Understanding the Judges

The evaluation is split **equally** across 4 criteria (25 marks each). This means we can't just build cool tech — we must score high on ALL four:

| # | Criteria | What Judges Want | Our Strategy |
|---|----------|-----------------|--------------|
| 1 | **Problem Understanding** (25) | Deep insight into the *real* pain point | Show we understand Canara Bank's actual underwriting bottleneck — manual document verification taking 3-5 days per loan |
| 2 | **Originality / Innovation** (25) | Novel approach, not just another ML classifier | Multi-layered forensic pipeline + Agentic explainability + real-time streaming |
| 3 | **Technical Implementation** (25) | Clean code, solid architecture, working prototype | Microservice architecture, Docker, test coverage, live demo |
| 4 | **Real-World Applicability** (25) | Practical, scalable, deployable at Canara Bank | Integration path with CBS, RBI FREE-AI compliance, data localization |

### 1.2 Theme Selection — Critical Decision

| Factor | Theme 1: Real-Time Anomaly Detection | Theme 2: Agentic Regulatory Compliance |
|--------|--------------------------------------|---------------------------------------|
| **Demo Impact** | 🟢 Highly visual (heatmaps, overlays) | 🟡 Text-heavy dashboards |
| **Technical Depth** | 🟢 CV + NLP + Forensics + ML | 🟡 Mostly LLM orchestration + RAG |
| **Originality** | 🟢 Multi-layer forensic pipeline is novel | 🔴 Many existing RegTech solutions |
| **Business Impact** | 🟢 Directly saves ₹Cr in fraud losses | 🟡 Indirect cost savings |
| **Feasibility (30 days)** | 🟢 Well-scoped, achievable | 🟡 Regulatory data sourcing is hard |
| **Canara Bank Relevance** | 🟢 Core underwriting pain point | 🟡 Important but operational |

> [!IMPORTANT]
> **PICK: Theme 1 — Real-Time Anomaly Detection**
>
> Higher demo impact, deeper technical surface, direct revenue protection for Canara Bank. The visual nature of document forensics gives us a massive presentation advantage at the finale.

### 1.3 Competitive Intel

Last year's winner (Team Finavat) built **RiverAuth** — behavioral analytics with Half-Space Trees. To beat that:

- ✅ Build a **multi-modal forensic intelligence platform** with explainable AI
- ✅ Show **real-time streaming** capability (not batch processing)
- ✅ Demonstrate **RBI FREE-AI compliance** (explainability, audit trails, human-in-the-loop)
- ✅ Present a clear **Canara Bank integration pathway**

---

## 2. Product Vision — "Forensica"

### 2.1 One-Liner
> **Forensica** — An intelligent, real-time document forensic engine that detects tampering, forgery, and anomalies across land records, legal documents, and financial statements during Canara Bank's underwriting process.

### 2.2 Problem Statement

**The Pain:**
- Canara Bank processes ~2.5 lakh loan applications/month across branches
- Each application involves 5-15 critical documents
- Manual verification takes 3-5 working days per application
- Document fraud costs Indian banks ₹800+ Cr annually

**Our Solution:**
- Real-time analysis (< 3 seconds per document)
- 5-layer forensic pipeline — forensic-grade detection
- Explainable results — visual heatmaps + natural language reasoning (RBI compliant)
- Agentic workflow — automated routing of flagged documents
- Zero PII leakage — on-premise capable, data stays in India

### 2.3 Key Differentiators

| What Others Will Build | What We Build |
|----------------------|---------------|
| Single CNN model | 5-layer forensic pipeline with decision fusion |
| Binary output (real/fake) | Confidence score + tampering heatmap + NL explanation |
| Batch upload interface | Real-time streaming API + live dashboard |
| Generic document checker | Banking-specific (land records, financial statements) |
| Black-box model | XAI-compliant with full audit trail |
| Cloud-only | Hybrid deployment (cloud + on-premise ready) |

---

## 3. System Architecture

### 3.1 High-Level Flow

```
Document Upload → Ingestion Service → 5-Layer Forensic Engine → Decision Fusion → Explainability → Dashboard
                                                                                                      ↓
                                                                                            Agentic Workflow
                                                                                        (auto-route flagged docs)
```

### 3.2 The 5-Layer Forensic Engine (Core Innovation)

| Layer | Name | What It Does | Tech |
|-------|------|-------------|------|
| **L1** | Metadata Forensics | EXIF analysis, creation tool detection, timestamp consistency | Python + Pillow |
| **L2** | Error Level Analysis (ELA) | JPEG compression artifact detection, re-save profiling | OpenCV + custom |
| **L3** | Pixel-Level Deep Analysis | CNN forgery classification, noise residual mapping, copy-move detection | PyTorch + EfficientNet-B3 |
| **L4** | Structural & Semantic Analysis | OCR + NLP for content extraction, cross-field validation, font analysis | Tesseract + EasyOCR + NLP |
| **L5** | Cross-Document Intelligence | Multi-document cross-reference, historical pattern matching, ensemble scoring | Custom + LLM |

Each layer produces an independent confidence score → **Decision Fusion Engine** combines them with learned weights → Final verdict with explainable reasoning.

### 3.3 Tech Stack

| Layer | Technology | Why |
|-------|-----------|-----|
| **Frontend** | Next.js 14 + TypeScript | SSR, React ecosystem |
| **UI** | Shadcn/ui + Framer Motion | Premium look, animations |
| **Backend API** | FastAPI (Python) | Async, ML-friendly |
| **ML/CV** | PyTorch + EfficientNet-B3 | SOTA accuracy, fast inference |
| **Image Forensics** | OpenCV + Pillow + custom ELA | Industry standard |
| **OCR** | Tesseract + EasyOCR | Hindi + English support |
| **NLP/LLM** | Google Gemini API | Explainability generation |
| **Database** | PostgreSQL | Audit trails, structured data |
| **Cache** | Redis | Real-time caching |
| **Task Queue** | Celery + Redis | Background processing |
| **Containers** | Docker + Docker Compose | One-command deployment |

---

## 4. Sprint Plan (June 1–30, 2026)

### Sprint 0: Foundation (May 25–31) — Pre-prototype prep

- [ ] Set up monorepo structure (frontend + backend + ml)
- [ ] Docker Compose for full stack
- [ ] Collect training datasets (CASIA 2.0, document forgery datasets)
- [ ] Prototype ELA implementation
- [ ] Design UI wireframes
- [ ] PostgreSQL schema + API skeleton

### Sprint 1: Core Engine (June 1–8)

**Goal:** Working forensic pipeline (Layers 1-3)

| Days | Task | Area |
|------|------|------|
| 1-2 | Metadata forensics + Document ingestion service | Backend |
| 3-4 | ELA engine + Frontend upload interface | ML + Frontend |
| 5-6 | CNN model training (EfficientNet-B3, transfer learning) | ML |
| 5-6 | API endpoints: upload, analyze, get-results | Backend |
| 7-8 | Noise residual analysis + Integration testing | ML + All |

**Deliverable:** Upload a document → get 3-layer forensic analysis

### Sprint 2: Intelligence Layer (June 9–16)

**Goal:** Layers 4-5 + Decision Fusion

| Days | Task | Area |
|------|------|------|
| 9-10 | OCR pipeline (Hindi + English) + Results dashboard | Backend + Frontend |
| 11-12 | Cross-field NLP validation + Font consistency analyzer | ML/NLP |
| 13-14 | Cross-document intelligence + Decision fusion engine | Backend + ML |
| 15-16 | LLM-powered explainability + Audit trail system | Backend |

**Deliverable:** Full 5-layer analysis with fused score + explanation

### Sprint 3: Dashboard & Polish (June 17–24)

**Goal:** Production-quality UI + Agentic workflow

| Days | Task | Area |
|------|------|------|
| 17-18 | Analytics dashboard + Agentic auto-routing | Frontend + Backend |
| 19-20 | Side-by-side document comparison + Review interface | Frontend |
| 21-22 | Real-time WebSocket notifications + Batch processing | Full Stack |
| 23-24 | Performance optimization + Mobile responsive | ML + Frontend |

**Deliverable:** Complete, polished platform

### Sprint 4: Hardening & Demo (June 25–30)

**Goal:** Battle-tested, demo-ready product

| Days | Task | Area |
|------|------|------|
| 25-26 | End-to-end testing + Security hardening | All |
| 27-28 | Demo script + Sample forged documents | All |
| 29-30 | Documentation + Video demo recording | All |

**Deliverable:** Demo-ready, documented, deployable product

---

## 5. Scoring Maximization Strategy

### Problem Understanding (25 marks)
- Open with Canara Bank's **specific** underwriting pain
- Quote real numbers (processing time, fraud losses)
- Show regulatory awareness (RBI FREE-AI, DPDP Act)
- Demonstrate knowledge of Indian land record formats

### Originality / Innovation (25 marks)
- 5-layer pipeline depth (no competitor will match)
- Cross-document intelligence (unique capability)
- Explainable AI with visual heatmaps + NL reasoning
- Agentic workflow with intelligent routing

### Technical Implementation (25 marks)
- Microservice architecture (not a Jupyter notebook)
- Docker containerized — `docker compose up` to deploy
- FastAPI auto-generated Swagger docs
- Test coverage + clean Git history

### Real-World Applicability (25 marks)
- CBS integration pathway for Canara Bank
- Data localization compliance (no data leaving India)
- Hindi + English OCR support
- Cost analysis: automated vs manual verification

---

## 6. Repository Structure

```
ZeroDay/
├── Docs/                          # All documentation
│   ├── Detail.md                  # Hackathon details
│   ├── IMPLEMENTATION_PLAN.md     # This file
│   ├── ARCHITECTURE.md            # Architecture doc
│   ├── PROGRESS_LOG.md            # Daily progress
│   └── DEMO_SCRIPT.md            # Finale presentation
├── frontend/                      # Next.js 14 app
│   ├── src/app/                   # App router pages
│   ├── src/components/            # UI components
│   └── Dockerfile
├── backend/                       # FastAPI app
│   ├── app/api/                   # Route handlers
│   ├── app/services/forensics/    # 5-layer engine
│   │   ├── metadata.py            # Layer 1
│   │   ├── ela.py                 # Layer 2
│   │   ├── pixel.py               # Layer 3
│   │   ├── semantic.py            # Layer 4
│   │   └── crossdoc.py            # Layer 5
│   ├── app/services/fusion/       # Decision fusion
│   ├── app/services/explainability/
│   └── Dockerfile
├── ml/                            # ML training & models
├── docker-compose.yml
└── README.md
```

---

## 7. Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| CNN accuracy too low | Use pre-trained EfficientNet + fine-tune; ELA alone gives solid results |
| No internet at finale | Bundle local Llama model OR pre-cache explanations for demo docs |
| Demo document doesn't trigger | Prepare 5+ known-forged docs; test extensively |
| GPU unavailable for training | Use Google Colab Pro / Kaggle notebooks |
| Architecture too complex | Fallback "lite" version with just Layers 1-3 working E2E |

---

## 8. Demo Strategy (July 20 Finale)

### Flow (8-10 minutes)

1. **Hook (1 min):** Show two documents, challenge judges to spot the fake
2. **Problem (2 min):** Canara Bank's underwriting fraud challenge with real numbers
3. **Live Demo (4 min):**
   - Upload authentic doc → ✅ Clean analysis
   - Upload tampered doc → 🚨 5 layers light up with heatmap + explanation
   - Show agentic routing to reviewer queue
4. **Architecture (1.5 min):** Quick technical walkthrough
5. **Business Case (1 min):** ROI for Canara Bank
6. **Q&A**

### Killer Moments
- **Side-by-side heatmap** — visually stunning
- **Real-time processing** — results appear live
- **Hindi OCR** — shows Indian banking context awareness
- **"One-click deploy"** — `docker compose up`

---

## 9. Immediate Next Steps (This Week)

1. [ ] Team alignment — share plan, assign roles (Frontend / Backend / ML)
2. [ ] Dataset collection — CASIA 2.0, Indian document samples
3. [ ] Environment setup — Python, Node.js, Docker, PostgreSQL
4. [ ] Prototype ELA — quick Python script to validate approach
5. [ ] UI mockup design

> [!CAUTION]
> **5 Critical Success Factors:**
> 1. Demo MUST work flawlessly — rehearse 10+ times
> 2. Every team member must understand the full system
> 3. Frame everything as "for Canara Bank" — not generic
> 4. Mention RBI FREE-AI compliance early — huge differentiator
> 5. Show edge case awareness (blurry scans, old docs, regional formats)
