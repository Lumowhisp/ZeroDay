# 🛠️ Proposed Solution & Technical Approach (Draft for Submission)

This section contains the core technical and solution description text for the DocShield AI idea submission (aligned with Criterion 1 of the Idea Phase).

---

## 💡 Proposed Solution
DocShield AI is an automated document forensic verification engine designed to detect high-resolution digital manipulations, signature forgery, and data inconsistencies in loan files. The platform ingests scanned assets and evaluates them through a five-layer forensic pipeline, converting raw image arrays and text structures into localized anomaly scores. Unlike standard identity verification (IDV) platforms that verify data lookups in isolation, DocShield AI analyzes the integrity of the files themselves and cross-references variables across the application graph to catch complex fraud schemes. The system fully complies with the RBI’s FREE-AI framework, delivering visual heatmaps and natural language justifications to underwriters. Designed specifically for Canara Bank, DocShield AI deploys containerized on-premise to keep customer records secure within the bank's data center while reducing mortgage processing turnaround times from days to seconds.

---

## ⚙️ Technical Approach

*   **Layer 1: Metadata Forensics:** Parses EXIF, XMP, and system headers to detect software signatures (Photoshop, GIMP), creator histories, and timestamp anomalies in uploaded JPEGs and PDFs.
*   **Layer 2: Error Level Analysis (ELA):** Resaves images at a specific compression ratio (90%) and calculates pixel difference maps to expose local edits that possess distinct compression history grids.
*   **Layer 3: Deep Pixel Analysis (CNN):** Employs an EfficientNet-B3 network fine-tuned on CASIA 2.0 and IMD2020 datasets to classify local splicing boundaries and copy-move forgery patterns.
*   **Layer 4: Semantic Validation (OCR & Font Geometrics):** Extracts script lines via Tesseract/EasyOCR and checks character aspect ratios, heights, and baseline offsets to identify digit changes in numbers.
*   **Layer 5: Cross-Document Intelligence:** Formulates a data graph of the application to check logical consistency (names, survey numbers, dates) across all uploaded collateral deeds, income certificates, and KYC cards.
*   **Decision Fusion Engine:** Blends scores from Layers 1-5 using a weighted classifier ensemble to compute an aggregate risk score, preventing single-model failure modes.
*   **Explainability Engine:** Translates the mathematical outputs of the forensic layers into visual red-overlay heatmaps and generates natural language explanations via an LLM.
