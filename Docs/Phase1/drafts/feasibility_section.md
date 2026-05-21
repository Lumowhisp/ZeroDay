# 🏗️ Feasibility Analysis Section (Draft for Submission)

This section provides the raw content and credibility indicators for the **Feasibility & Execution** portion of the ZeroDay submission (aligned with Criterion 3 of the Idea Phase).

---

## 1. PROVEN TECHNOLOGIES
Every architectural component of **DocShield AI** is built using mature, battle-tested open-source tools and frameworks. By avoiding proprietary black-box software or experimental architectures, we ensure high reliability and immediate deployability:

*   **API & Processing Engine:** **FastAPI** serves as our asynchronous API gateway, handling file uploads in parallel. It is combined with **Celery** and **Redis** for asynchronous task execution to prevent blocking requests during heavy machine learning processes.
*   **Deep Learning (Computer Vision):** The core image classification models are built on **PyTorch**, leveraging the **EfficientNet-B3** architecture. This network is widely recognized in academic benchmarks for its balance between performance and compute requirements (12M parameters, ~48MB model size).
*   **Text & Semantic Recognition:** OCR tasks are split between **Tesseract OCR** (for structured data extraction and coordinate-based font analysis) and **EasyOCR** (for complex, multi-lingual English/Hindi handwritten texts).
*   **Forensic Math & OpenCV:** Image re-compression, Error Level Analysis (ELA) subtraction, and noise residual filtering are implemented using **OpenCV** headless bindings, delivering spatial operations in milliseconds.
*   **Deployment Architecture:** The entire stack is containerized using **Docker** and orchestrated via **Docker Compose**, enabling a single-command deploy (`docker compose up`) that is cloud-agnostic and ready for on-premise integration within Canara Bank's servers.

---

## 2. AVAILABLE DATA & TRAINING PIPELINE
We have identified and structured a pipeline of **15,000+ public and synthetic images** to train and fine-tune DocShield AI's detection layers:

*   **Foundation Tampering Detection:** We utilize the public **CASIA 2.0** dataset (12,614 images) and the **IMD2020** dataset (72,000+ images including subsets) containing diverse image splicing, copy-move, and post-processed manipulations.
*   **Document-Specific Forgery:** To adapt the models to paperwork, we train on the **Forged Handwritten Document Database** (Mendeley Data), which provides 500 high-resolution document images mapping 10 distinct tampering categories (insertion, blur, splicing).
*   **Indian Script Signature Verification:** We use the **BHSig260-Hindi** dataset (containing skilled forgeries from 160 individuals) to train our signature comparison Siamese network.
*   **Synthetic Indian Documents:** We generate a custom testing set of 150 simulated land documents (7/12 Extracts, Khatas) and bank statements to calibrate the baseline thresholds for our OCR/NLP cross-document checks.

---

## 3. REALISTIC TIMELINE & SPRINT PLAN
Our 30-day prototype timeline (June 1 - June 30, 2026) is structured into focused 1-week sprints with clear, testable deliverables:

*   **Sprint 1 (June 1–8): Core Forensic Engine (Layers 1-3)**
    *   *Goal:* Build the ingestion service, Metadata analysis, ELA difference generator, and fine-tune the EfficientNet-B3 classifier.
    *   *Deliverable:* Working API endpoint that accepts a JPEG/PDF, calculates a tamper probability score, and returns an ELA difference image.
*   **Sprint 2 (June 9–16): Semantic & Intelligence Layers (Layers 4-5)**
    *   *Goal:* Implement English + Hindi OCR, font baseline checking, cross-document text matchers, and integrate the Gemini API for natural language reports.
    *   *Deliverable:* Fusion of all 5 layers into a single ensemble decision score with a structured explanation payload.
*   **Sprint 3 (June 17–24): Underwriter Dashboard & Workflow (UI)**
    *   *Goal:* Build the Next.js frontend, interactive side-by-side document views, red overlay heatmap visualizations, and the agentic routing queue.
    *   *Deliverable:* A premium React interface that displays flagged files and allows underwriters to quickly inspect and verify anomalies.
*   **Sprint 4 (June 25–30): Hardening & Demo Preparation**
    *   *Goal:* Perform end-to-end load testing, security hardening (sanitizing file inputs), compile sample forged test cases, and record the demo video.
    *   *Deliverable:* A battle-tested, demo-ready prototype package deployable in a single command.

---

## 4. INCREMENTAL DELIVERY & RISK MITIGATION (FALLBACK PLAN)
To guarantee a functional prototype at the finale, DocShield AI is designed with an **incremental delivery model**. Each layer operates independently; if one layer experiences technical hurdles, the surrounding layers still deliver substantial value:

*   **Optimal Pipeline (Layers 1-5):** Full metadata, ELA, deep-learning, semantic font checks, cross-document intelligence, and automated natural language explanations.
*   **Fallback Option A (Layers 1-4):** If cross-document indexing (Layer 5) is delayed, individual documents are still fully scanned for structural, graphical, and metadata anomalies.
*   **Fallback Option B (Layers 1-2 + Dashboard):** In the worst-case scenario, the system uses ELA and EXIF parsing alone. Because these techniques do not require heavy model weights, they provide a lightning-fast, zero-overhead tampering detector that immediately flags edits, signature splicing, and editing tool signatures.

---

## 5. RELEVANT TEAM CAPABILITIES
Our team possesses the multi-disciplinary skills required to deliver this architecture:
*   **Backend & Orchestration (Aaryan/Aditya):** Experienced in building async Python REST APIs (FastAPI) and setting up Docker Compose environments.
*   **Machine Learning & CV (Aaryan):** Familiar with PyTorch transfer learning, CNN architectures (ResNet, EfficientNet), and OpenCV image operations.
*   **Frontend UI/UX (Sonali/Aditya):** Experienced in developing responsive React/Next.js dashboards using Tailwind CSS / vanilla CSS.
*   **Domain & Compliance (Sonali):** Clear understanding of Indian banking workflows and compliance requirements (DPDP Act, RBI regulations).
