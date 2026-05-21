# 🧑‍💻 Aaryan — Phase 1 Task Sheet (Technical Research + Feasibility)

> **Role:** Technical Researcher, Data Handling, Feasibility Author
> **Deadline:** All tasks complete by **May 23**

---

## 🎯 Core Responsibilities

You own: **technical validation**, **ML/dataset research**, **feasibility proof**, and **existing solution analysis**. Your job is to make sure everything we claim in the submission is technically REAL and BUILDABLE.

---

## Task 1: Document Forgery Detection — Technical Deep Dive
**⏰ Deadline: May 12**

### Research each forensic technique we'll use:

#### 1a: Error Level Analysis (ELA)
- [x] How ELA works (JPEG re-compression artifacts)
- [x] What types of tampering it catches (copy-paste, text edits, signature insertion)
- [x] What it CANNOT catch (limitations — important for credibility)
- [x] Find 2-3 research papers on ELA effectiveness
- [x] Find open-source implementations (Python/OpenCV)

#### 1b: Metadata Forensics
- [x] EXIF data analysis — what fields reveal editing?
- [x] Tool detection (Photoshop, GIMP, GenAI fingerprints)
- [x] Timestamp consistency checking
- [x] What Python libraries exist? (Pillow, ExifTool, python-exif)

#### 1c: CNN-based Forgery Detection
- [x] Which architectures work best? (EfficientNet-B3, ResNet, MobileNet)
- [x] Transfer learning approaches — what's pre-trained on forgery detection?
- [x] What accuracy numbers are realistic? (don't overclaim)
- [x] Inference time on CPU vs GPU — can we do <3 seconds?
- [x] Find 3-5 key research papers (2023-2026)

#### 1d: Noise Residual Analysis
- [x] How noise patterns detect splicing
- [x] Computational cost — feasible in real-time?
- [x] Open-source implementations available?

#### 1e: Font Consistency Analysis
- [x] How to detect font changes within a document
- [x] Tools/libraries for font analysis
- [x] How effective is this for Indian documents (multiple scripts)?

### Output: `Phase1/research/forensic_techniques.md`
- For each technique: How it works | Accuracy | Limitations | Libraries | Papers (COMPLETED ✅)

---

## Task 2: Dataset Research & Collection
**⏰ Deadline: May 13**

### Find and catalog ALL usable datasets:

| Dataset | Type | Size | Access | Status |
|---------|------|------|--------|--------|
| CASIA 2.0 | Image forgery (splicing, copy-move) | 12,614 images | Public | [x] Found download link |
| Columbia Uncompressed | Splicing detection | 933 images | Public | [x] Found download link |
| COVERAGE | Copy-move forgery | 100 pairs | Public | [x] Found download link |
| CoMoFoD | Copy-move forgery | 260 sets | Public | [x] Found download link |
| IMD2020 | Image manipulation | 2,010 images | Public | [x] Found download link |
| Indian document samples | Land records, financial docs | ? | Need to find | [x] Researched sources |

### Additional dataset work:
- [x] Can we find/create Indian-specific document datasets? (Found Mendeley and BHSig260-Hindi datasets)
- [x] Are there any Kaggle datasets for document fraud? (Identified and linked)
- [x] Search: "document forgery detection dataset", "image manipulation dataset"
- [x] For each dataset: note format, size, labels, download URL, license
- [x] Identify which datasets are best for our fine-tuning needs

### Output: `Phase1/research/datasets.md` — Complete catalog with download links (COMPLETED ✅)

---

## Task 3: Existing Solutions Analysis
**⏰ Deadline: May 14**

### Analyze these competitors/existing tools:

| Solution | What to Find |
|----------|-------------|
| **HyperVerge** (Indian) | What docs they verify, techniques used, pricing, limitations |
| **Digio** (Indian) | Features, target market, what they miss |
| **SignDesk** (Indian) | Document verification capabilities |
| **Attestiv** (US) | AI-based document authentication approach |
| **Jumio** (US) | Document verification + identity |
| **Onfido** (UK) | Document fraud detection techniques |
| **FotoForensics** | Free ELA tool — test with sample docs |

### For each competitor document:
- [x] What forensic techniques do they use?
- [x] What document types do they support?
- [x] Do they support Indian documents specifically?
- [x] What's their accuracy claim?
- [x] What are their limitations?
- [x] How is DocShield AI different/better?

### Output: `Phase1/research/competitor_analysis.md` (COMPLETED ✅)

---

## Task 4: Tech Stack Validation
**⏰ Deadline: May 15**

### Validate every technology we plan to use:

| Technology | Validate |
|-----------|----------|
| **FastAPI** | Can it handle file uploads + async ML inference? Benchmark examples? |
| **EfficientNet-B3** | Inference time on CPU? Model size? PyTorch Hub availability? |
| **Tesseract OCR** | Hindi accuracy? How good on scanned documents? |
| **EasyOCR** | Hindi + English support? Better than Tesseract for handwritten? |
| **OpenCV** | ELA implementation feasibility? |
| **Celery + Redis** | Task queue for background processing — setup complexity? |
| **Docker** | Full stack compose with GPU passthrough possible? |
| **Google Gemini API** | Free tier limits? Can it generate explanations for doc analysis? |

### For each technology:
- [x] Confirm it's free / open-source / has free tier
- [x] Check latest stable version
- [x] Find a "hello world" example for our use case
- [x] Note any gotchas or compatibility issues
- [x] Estimate setup time

### Output: `Phase1/research/tech_validation.md` (COMPLETED ✅)

---

## Task 5: Feasibility Section Writing
**⏰ Deadline: May 16**

### Write the Feasibility section for the idea submission using your research:

#### Structure:
```
1. PROVEN TECHNOLOGIES
   "Every component uses battle-tested open-source tools: [list]"

2. AVAILABLE DATA
   "Training data is available through [CASIA 2.0, etc.] 
   totaling [X] images across [Y] forgery types"

3. REALISTIC TIMELINE
   "Week 1: Core forensic engine (Layers 1-3)
    Week 2: Intelligence layers + decision fusion
    Week 3: Dashboard + agentic workflow
    Week 4: Testing + demo preparation"

4. TEAM CAPABILITIES
   "Our team has experience in [Python, ML, web dev] 
   with prior projects in [mention relevant experience]"

5. INCREMENTAL DELIVERY
   "Each layer is independently functional — even with 
   only Layers 1-3, the system provides value"
```

### Key credibility boosters:
- [x] Mention specific model accuracy from papers (e.g., "EfficientNet-B3 achieves 97.2% on CASIA 2.0")
- [x] Mention inference time benchmarks
- [x] Mention dataset sizes
- [x] Show fallback plan: "Even if Layer 5 isn't complete, Layers 1-4 deliver a working product"

### Output: `Phase1/drafts/feasibility_section.md` (COMPLETED ✅)

---

## Task 6: RBI FREE-AI Framework Research
**⏰ Deadline: May 13**

### Deep dive into RBI's FREE-AI (August 2025):
- [x] Find the original RBI circular/document (Published Aug 13, 2025)
- [x] List all 7 Sutras (principles)
- [x] For EACH Sutra, write how DocShield AI complies:

| Sutra | Principle | How DocShield Complies |
|-------|-----------|----------------------|
| 1 | Trust is the Foundation | 5-layer pipeline + Decision Fusion avoids single model failure |
| 2 | People First | Human-in-the-Loop workflow with agentic routing |
| 3 | Innovation over Restraint | Accelerates TAT from days to <3s safely |
| 4 | Fairness and Equity | Ignores user demographics, focuses only on file/pixel properties |
| 5 | Accountability | Full PostgreSQL immutable audit trail of execution hashes |
| 6 | Understandable by Design | Generates heatmaps and Gemini natural language explanations |
| 7 | Safety & Resilience | Microservice containerization in Docker for secure hybrid/on-prem |

- [x] This is a MASSIVE differentiator — no student team will do this research
- [x] Share findings with Sonali (she needs it for compliance section) and Aditya (innovation section)

### Output: `Phase1/research/rbi_free_ai.md` (COMPLETED ✅)

---

## 📅 Timeline

| Date | Deliverable | Status |
|------|------------|--------|
| May 9-12 | `forensic_techniques.md` | ✅ Done |
| May 12-13 | `datasets.md` + `rbi_free_ai.md` | ✅ Done |
| May 13-14 | `competitor_analysis.md` | ✅ Done |
| May 14-15 | `tech_validation.md` | ✅ Done |
| May 15-16 | `feasibility_section.md` | ✅ Done |
| May 17-20 | Revisions based on Aditya's feedback | ✅ Done |

---

## 📚 Resources

| Topic | Where to Look | Priority |
|-------|--------------|----------|
| ELA research papers | Google Scholar, IEEE Xplore | 🔴 Critical |
| CASIA 2.0 dataset | Kaggle, original paper site | 🔴 Critical |
| EfficientNet benchmarks | PyTorch Hub, papers with code | 🔴 Critical |
| RBI FREE-AI circular | rbi.org.in | 🔴 Critical |
| Competitor products | Company websites, G2 reviews | 🟡 High |
| Tesseract Hindi OCR | tesseract-ocr GitHub, docs | 🟡 High |
| FotoForensics.com | Test ELA with sample images | 🟡 High |

---

## 📝 Deliverables Checklist

| # | Deliverable | Deadline | Status |
|---|------------|----------|--------|
| 1 | `Phase1/research/forensic_techniques.md` | May 12 | ✅ Done |
| 2 | `Phase1/research/datasets.md` | May 13 | ✅ Done |
| 3 | `Phase1/research/rbi_free_ai.md` | May 13 | ✅ Done |
| 4 | `Phase1/research/competitor_analysis.md` | May 14 | ✅ Done |
| 5 | `Phase1/research/tech_validation.md` | May 15 | ✅ Done |
| 6 | `Phase1/drafts/feasibility_section.md` | May 16 | ✅ Done |

> [!IMPORTANT]
> **Test don't guess.** For any accuracy claim or feasibility claim, find a paper, benchmark, or existing implementation that backs it up. If you write "94% accuracy", you MUST have a source. Judges will challenge vague technical claims.
