# 📁 Dataset Research & Collection Catalog

This document catalogs open-source and research datasets available for training, fine-tuning, and evaluating the **DocShield AI** forensic layers. It includes image tampering datasets, Indian-specific document resources, and signature datasets.

---

## 📊 Core Forgery Detection Datasets

| Dataset | Type / Tampering Vectors | Size & Details | License / Terms | Download / Reference Link |
| :--- | :--- | :--- | :--- | :--- |
| **CASIA v2.0** | Splicing, Copy-Move, Blur, De-noising. High-resolution uncompressed & compressed. | 12,614 images (7,491 authentic, 5,123 tampered). | Academic/Research | [Kaggle - CASIA 2.0](https://www.kaggle.com/datasets/sophatvathana/casia-dataset) |
| **Columbia Uncompressed** | Image Splicing (coarse boundary cuts, edge properties). | 1,845 image blocks (933 authentic, 912 spliced) + 363 full uncompressed images. | Research Use Only (Credit required) | [Columbia DVMM Lab](https://www.ee.columbia.edu/ln/dvmm/downloads/AuthSplicedDataSet/AuthSplicedDataSet.htm) |
| **COVERAGE** | Copy-Move forgery with specific focus on similarity-based masking (difficult edge cases). | 100 pairs (100 original, 100 tampered). | Non-Commercial Research (Cite Wen et al.) | [GitHub - COVERAGE](https://github.com/BihanWen/COVERAGE) |
| **CoMoFoD** | Copy-Move forgery with translation, rotation, scaling, and post-processing (noise, compression). | 10,400 images (260 original, rest are variations under 25 different attack parameters). | Academic / Research | [VCL FER - CoMoFoD](http://www.vcl.fer.hr/comofod/) |
| **IMD2020** | Large-scale real-life manipulations (inpainting, splicing, local enhancement, JPEG compression). | 2,010 real-world manipulated images with masks + 70,000+ synthetic matches. | CC BY 4.0 / Apache 2.0 | [GitHub - IMD2020 / UTIA](https://github.com/adior/IMD2020) |

---

## 🇮🇳 Indian-Specific & Document-Specific Datasets

Because general forgery datasets focus on natural scenes (animals, buildings), we supplement training with document-specific and Indian-context datasets:

### 1. Forged Handwritten Document Database (Mendeley Data)
- **Use Case:** Specifically checks for text editing, insertion, blur, and splicing on document papers.
- **Details:** 500 document images (50 original and 450 forged) collected from academic circles in Karnataka, India. Includes 10 different forgery classes (copy-paste, line insertion, noise addition).
- **Format:** High-resolution JPEG.
- **License:** CC BY 4.0.
- **Link:** [Mendeley Data - Forged Handwritten Document Database](https://data.mendeley.com/datasets/j3p5m3b22k/1)

### 2. BHSig260-Hindi Signature Dataset
- **Use Case:** Verification of handwritten signatures on loan applications, checks, and deeds.
- **Details:** Signature samples from 160 individuals. Contains 24 genuine and 30 skilled forgeries per person in Hindi script.
- **Format:** Grayscale PNGs, bounding-boxed signatures.
- **License:** Research use only.
- **Link:** [Kaggle - BHSig260 Signature Dataset](https://www.kaggle.com/datasets/srinivas1/bhsig260-signature-dataset)

### 3. Synthetic Aadhaar and PAN Card Datasets (Kaggle / Local Generator)
- **Use Case:** Fine-tuning OCR alignment and layout tampering detection.
- **Details:** Generates templates of Aadhaar, PAN, and Voter IDs using synthetic names, survey numbers, and addresses. Forgeries are introduced programmatically (shifting digits, mismatched text baselines).
- **Link:** [Kaggle - Aadhaar Tampering Detection Baseline](https://www.kaggle.com/datasets/...)

---

## 🎯 Dataset Selection & Fine-Tuning Strategy

### Phase 1: Deep Learning Backbone (Layer 3 - CNN)
*   **Pre-training:** **IMD2020** and **CASIA 2.0** will be used to pre-train our **EfficientNet-B3** backbone. This teaches the model to identify basic splicing boundaries and compression inconsistencies.
*   **Fine-tuning:** We will overlay the **Forged Handwritten Document Database** and synthetic Indian land/identity documents. This optimizes the CNN to identify boundaries between printed templates and edited text fonts.

### Phase 2: Signature Validation (Layer 4 - Semantic)
*   We will train a Siamese network on **BHSig260-Hindi** to compare the applicant's signature on the loan application with their signature on Aadhaar/PAN cards. The model will calculate a similarity vector; a similarity score below 0.7 will trigger a manual review.

### Phase 3: Land Record Mock Generation
*   Since public land record datasets (e.g., Karnataka RTC / Khata, Maharashtra 7/12) are restricted, we will create 150 synthetic land record documents representing 3 states (Karnataka, Maharashtra, Punjab). We will apply 3 typical attack profiles:
    1.  **Acreage Tampering:** Altering numeric land area (e.g., `1.2 acres` to `7.2 acres`).
    2.  **Survey Number Splicing:** Altering the survey block numbers to match a high-value adjacent plot.
    3.  **Owner Name Modification:** Replacing the rightful owner's name using text-matching fonts.
