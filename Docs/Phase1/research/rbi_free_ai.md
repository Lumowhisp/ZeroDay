# 🏛️ Regulatory Compliance: RBI FREE-AI Framework Mapping

This document provides a detailed compliance analysis of **DocShield AI** against the Reserve Bank of India’s (RBI) **FREE-AI Framework** (Framework for Responsible and Ethical Enablement of Artificial Intelligence) released on **August 13, 2025**. 

Adherence to this framework is a key business differentiator for DocShield AI, aligning our technical design with the compliance expectations of Canara Bank's risk management and supervisory audits.

---

## 🧭 The 7 Sutras of FREE-AI Compliance

The RBI's FREE-AI framework anchors the deployment of AI in Indian financial institutions around **7 guiding principles (Sutras)**. The table below details how DocShield AI implements these principles at the architecture and workflow levels.

| Sutra | Principle Name | How DocShield AI Complies & Technical Implementation |
| :--- | :--- | :--- |
| **Sutra 1** | **Trust is the Foundation** | We avoid single-point-of-failure algorithms. Instead of relying on a single deep learning model, DocShield AI employs a **5-layer forensic engine** (Metadata, ELA, CNN, Semantic, and Cross-Document). The **Decision Fusion Engine** weights each layer's confidence, ensuring the final verdict is highly reliable and verifiable. |
| **Sutra 2** | **People First** | The platform enforces a **Human-in-the-Loop (HITL)** architecture. DocShield AI is designed as a decision-support system, not a final arbitrator. Borderline cases (anomaly scores between `0.4` and `0.8`) are routed to human underwriters with visual annotations, ensuring human oversight governs credit decisions. |
| **Sutra 3** | **Innovation over Restraint** | By automating 98% of the document verification workload and dropping TAT from days to under 3 seconds, DocShield AI enables Canara Bank to innovate its digital loan offerings securely, preventing fraud losses (₹Cr) without slowing down customer onboarding. |
| **Sutra 4** | **Fairness and Equity** | Forensic analysis is strictly objective. The engine evaluates file metadata, JPEG compression grids, pixel textures, and font baselines. It has no access to customer demographics (gender, caste, religion, income level), ensuring that the document validation process remains completely unbiased and fair. |
| **Sutra 5** | **Accountability** | Every validation run generates an immutable audit record in PostgreSQL. This trail logs the uploaded file hash, the individual confidence scores of all 5 layers, the weights applied by the fusion engine, and the final metadata. This enables complete traceability for regulatory audits by RBI supervisors. |
| **Sutra 6** | **Understandable by Design** | DocShield AI rejects "black box" machine learning. The **Explainability Engine** generates visual heatmaps (tampered areas highlighted in red) and utilizes the **Google Gemini API** to output natural language explanations (e.g., *"The survey number block contains local compression anomalies suggesting splicing, and the font style diverges from the template standard."*). |
| **Sutra 7** | **Safety, Resilience, and Sustainability** | The application is fully containerized using **Docker** and built on a microservice-ready modular architecture. It supports a hybrid deployment model, allowing it to run within Canara Bank's secure, on-premise infrastructure. This guarantees data localization (DPDP Act) and high system availability. |

---

## 🛠️ Deep Dive: Implementing Sutra 6 (Understandable by Design)

In banking, an underwriter cannot reject a loan application simply because "the AI model said so." The rejection must have a clear legal and operational basis.

DocShield AI delivers on **Explainable AI (XAI)** through two integrated layers:

1.  **Visual Tampering Heatmap (Layer 2 & 3):**
    *   The backend outputs a spatial coordinate grid highlighting exactly where pixel inconsistencies or ELA differences occur.
    *   The frontend displays this grid as a semi-transparent red overlay on top of the original scanned document, allowing the human verifier to see the altered digits or signature boundaries.
2.  **Natural Language Reasoning (Layer 4 & 5):**
    *   The engine extracts the OCR text, font discrepancies, EXIF editing logs, and ELA scores, and formats them into a structured JSON payload.
    *   This payload is passed to a localized or secure instance of the Google Gemini API to compile a human-readable justification.
    *   *Example Output:* 
        > **DocShield AI Analysis Report:**
        > *   **Verdict:** Tampered (92% Confidence)
        > *   **EXIF Analysis:** File modified using Canva on 2026-05-20. Original camera capture metadata is missing.
        > *   **Error Level Analysis:** High discrepancy detected surrounding the 'Property Area' field (Row 14, Column 3).
        > *   **Cross-Document Check:** The property area stated in the Sale Deed (8,500 sq ft) does not match the digitized Khata record (5,800 sq ft) for Survey No. 45/A.

---

## 📈 Audit & Governance Framework

To satisfy the **Accountability (Sutra 5)** guidelines of the FREE-AI framework:
*   **Version Control for Models:** Every model deployed in the pipeline is tagged with a unique version identifier in the database.
*   **Data Integrity Check:** Files are hashed using SHA-256 upon ingestion. This hash is logged in the database, ensuring that the documents reviewed during an audit are identical to those processed during the initial loan application.
*   **Regular Calibration:** The Decision Fusion Engine's weights are monitored for drift. If false positive rates exceed 5%, a notification triggers automatic model recalibration.
