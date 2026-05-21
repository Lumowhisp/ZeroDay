<div align="center">

# 🛡️ DocShield AI
### *Real-Time Document Forensic Intelligence for Banking*

[![GitHub License](https://img.shields.io/github/license/Lumowhisp/ZeroDay?style=for-the-badge&color=blue)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/Lumowhisp/ZeroDay?style=for-the-badge&color=gold)](https://github.com/Lumowhisp/ZeroDay/stargazers)
[![Hackathon](https://img.shields.io/badge/SuRaksha_2.0-Canara_Bank-orange?style=for-the-badge)](https://canarabank.com)
[![Team](https://img.shields.io/badge/Team-ZeroDay-red?style=for-the-badge)](https://github.com/Lumowhisp/ZeroDay)

---

An intelligent, real-time document forensic engine that detects **tampering, forgery, and anomalies** across land records, legal documents, and financial statements — built for Canara Bank's underwriting pipeline.

[Implementation Plan](Docs/IMPLEMENTATION_PLAN.md) · [Phase 1 Strategy](Docs/Phase1/IDEA_SUBMISSION_PLAN.md) · [Report Bug](https://github.com/Lumowhisp/ZeroDay/issues)

</div>

---

## 📖 Table of Contents
- [🚀 About](#-about)
- [🔥 The Problem](#-the-problem)
- [💡 Our Solution](#-our-solution)
- [🧬 5-Layer Forensic Engine](#-5-layer-forensic-engine)
- [🧩 Tech Stack](#-tech-stack)
- [📁 Project Structure](#-project-structure)
- [🎬 Team ZeroDay](#-team-zeroday)
- [📄 License](#-license)

---

## 🚀 About

**DocShield AI** is Team ZeroDay's submission for the **SuRaksha Cyber Hackathon 2.0** by Canara Bank. We're building a multi-layered forensic intelligence platform that goes beyond simple image classification to deliver forensic-grade document analysis with explainable AI — fully compliant with RBI's FREE-AI framework.

**Theme:** Real-Time Anomaly Detection — Detecting tampering, changes, and forgery across land records, legal documents, and financial statements in real time.

---

## 🔥 The Problem

- Indian banks lose **₹800+ Cr annually** to document fraud
- Manual document verification takes **3-5 working days** per loan application
- Existing tools rely on basic OCR or single-model classifiers — missing sophisticated forgeries
- No solution analyzes documents **across** a loan application to catch coordinated fraud
- RBI now mandates **explainable AI** (FREE-AI framework, Aug 2025) — black-box models won't fly

---

## 💡 Our Solution

DocShield AI provides:
- ⚡ **Real-time analysis** — < 3 seconds per document
- 🔬 **5-layer forensic pipeline** — defense-in-depth detection
- 🧠 **Explainable verdicts** — visual heatmaps + natural language reasoning
- 🔗 **Cross-document intelligence** — catches fraud that single-doc analysis misses
- 🤖 **Agentic workflow** — auto-routes flagged documents to the right reviewer
- 🇮🇳 **India-first** — Hindi + English OCR, on-premise deployment, data localization

---

## 🧬 5-Layer Forensic Engine

| Layer | Name | What It Detects |
|-------|------|----------------|
| **L1** | Metadata Forensics | Editing tool fingerprints, timestamp inconsistencies, EXIF anomalies |
| **L2** | Error Level Analysis (ELA) | Re-compression artifacts, digitally altered regions |
| **L3** | Pixel-Level Deep Analysis | CNN-based forgery classification, noise residual mapping, copy-move detection |
| **L4** | Structural & Semantic Analysis | OCR content validation, cross-field inconsistencies, font analysis |
| **L5** | Cross-Document Intelligence | Multi-document cross-referencing, historical pattern matching |

Each layer produces an independent confidence score → **Decision Fusion Engine** combines them → Final verdict with explainable reasoning + visual evidence.

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | Next.js 14 · TypeScript · Shadcn/ui · Framer Motion |
| **Backend** | FastAPI · Python · Celery · Redis |
| **ML/CV** | PyTorch · EfficientNet-B3 · OpenCV · Pillow |
| **OCR** | Tesseract · EasyOCR (Hindi + English) |
| **LLM** | Google Gemini API |
| **Database** | PostgreSQL |
| **Deployment** | Docker · Docker Compose |

---

## 📁 Project Structure

```
ZeroDay/
├── Docs/
│   ├── Detail.md                  # Hackathon details
│   ├── IMPLEMENTATION_PLAN.md     # Full implementation plan
│   └── Phase1/                    # Idea submission phase
│       ├── IDEA_SUBMISSION_PLAN.md
│       ├── aditya.md              # Task sheet — Lead/Architect
│       ├── aaryan.md              # Task sheet — Tech Research
│       ├── sonali.md              # Task sheet — Domain/Pitching
│       ├── research/              # All research documents
│       ├── drafts/                # Section drafts
│       └── assets/                # Diagrams & POC outputs
├── frontend/                      # Next.js application (coming)
├── backend/                       # FastAPI application (coming)
├── ml/                            # ML training & models (coming)
├── Logo/
├── docker-compose.yml             # (coming)
├── README.md
└── LICENSE
```

---

## 🎬 Team ZeroDay

| Member | Role |
|--------|------|
| **Aditya** | Team Lead · Technical Architect · ML |
| **Aaryan** | Technical Research · Data Handling · Feasibility |
| **Sonali** | Domain Research · Pitching · Documentation |

---

## 🏆 Hackathon Timeline

| Phase | Date | Status |
|-------|------|--------|
| Idea Submission | May 24, 2026 | 🔄 In Progress |
| Prototype Development | June 1–30, 2026 | ⬜ Upcoming |
| Grand Finale | July 20, 2026 (Bengaluru) | ⬜ Upcoming |

---

## 📄 License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with 🔥 by Team ZeroDay for SuRaksha Cyber Hackathon 2.0**

*Protecting documents. Preventing fraud. Powering trust.*

</div>