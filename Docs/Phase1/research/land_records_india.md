# 🌾 Indian Land Records: Structure, Tampering, & Digitization

This document provides domain research on Indian land administration records, their regional terminology, common fraud methodologies, and their integration with the **DocShield AI** verification engine.

---

## 🗺️ State-by-State Land Record Terminology

Indian land administration is a state subject, meaning each state maintains distinct structures and names for land records:

| State | Primary Land Document | Purpose |
| :--- | :--- | :--- |
| **Karnataka** | **RTC (Record of Rights, Tenancy, and Crops) / Pahani / Khata** | Details owner name, soil type, crop patterns, and liabilities (mortgages). Khata registers tax assessments. |
| **Maharashtra** | **7/12 Extract (Saat Bara Utara) / 8A Extract** | Primary document proving ownership (7) and tax liability (12) for agricultural and rural land. |
| **Tamil Nadu** | **Patta / Chitta** | **Patta:** Government register proving land ownership. **Chitta:** Details land area, classification (dry/wet land), and tax details. |
| **Punjab & Haryana** | **Jamabandi / Fard** | Record of Rights revised every 5 years detailing shares of ownership and cultivation rights. |
| **Uttar Pradesh** | **Khatauni** | A register of book-of-accounts mapping all land holdings of a family in a village. |

### 📄 Other Critical Legal Documents
*   **Sale Deed:** The primary legal document showing transfer of ownership from buyer to seller. Needs registration at the Sub-Registrar Office (SRO).
*   **Encumbrance Certificate (EC):** Form 15 (lists all registered transactions/mortgages) or Form 16 (no encumbrance recorded) spanning 13 to 30 years.
*   **Mutation Register (Dakhil Kharij):** Shows the update in land records when ownership changes hands due to sale, inheritance, or partition.

---

## 🚨 Common Tampering Modus Operandi

Fraudsters target land records during the loan underwriting process through specific manipulation techniques:

1.  **Survey Number Splicing (Copy-Paste Forgery):**
    *   *Mechanism:* A borrower owns a low-value land parcel (e.g., Survey No. 45/A, dry land). They crop and paste a high-value survey number (e.g., Survey No. 45/B, commercial/highway adjacent) using graphic editors.
    *   *Tamper Vector:* Cut boundaries, mismatched text alignment, and local compression discrepancies in the cropped survey number region.
2.  **Property Area/Acreage Inflation:**
    *   *Mechanism:* Modifying numerical areas in the document (e.g., altering `0.15 hectares` to `8.15 hectares` or `1.5 acres` to `7.5 acres`) to inflate the collateral valuation for securing larger loan limits.
    *   *Tamper Vector:* Font inconsistency (altered digits do not match the size, stroke width, or baseline of the surrounding characters) and visual re-compression artifacts.
3.  **Owner Name Modification:**
    *   *Mechanism:* Replacing the actual owner's name with the borrower's name on a scanned RTC or Fard, allowing them to mortgage land they do not own.
    *   *Tamper Vector:* Mismatched font rendering, kerning anomalies, and local metadata modifications.
4.  **Fabricated Registration Seals & Stamps:**
    *   *Mechanism:* Copying a digital image of a Sub-Registrar seal from a legitimate document and pasting it onto a forged Sale Deed.
    *   *Tamper Vector:* Mismatched rotation angles, inconsistent transparency grids, and ELA glowing edges around the seal boundary.

---

## 🌐 Digitization Status (DILRMP Program)

Under the **Digital India Land Records Modernization Programme (DILRMP)**, land records are undergoing digitization:

*   **Computerization of RoRs:** Over **95%** of villages across India have digitized textual Records of Rights (RoRs).
*   **Cadastral Map Digitization (Bhu-Naksha):** Spatial maps are being digitized and linked to textual records. States like Karnataka (Bhoomi), Maharashtra (Mahabhulekh), and Uttar Pradesh (Bhulekh) provide online portals to verify records.
*   **ULPIN (Unique Land Parcel Identification Number):** Also known as **Bhu-Aadhaar**, a 14-digit alphanumeric identification number for every land parcel based on longitude/latitude coordinates.
*   **Scanned Images vs. Digitally Signed PDFs:**
    *   *Scanned TIFFs/JPEGs:* Older records are stored as low-resolution scanned raster images, which are highly vulnerable to digital manipulation.
    *   *Digitally Signed PDFs:* Modern registries issue digitally signed PDF land documents containing QR codes. Fraudsters attempt to tamper with the text inside these PDFs while presenting them as authentic.

---

## 🛡️ DocShield AI Mitigation Engine

DocShield AI addresses these vulnerabilities directly:
*   **Cross-Reference Validation:** Layer 5 compares the uploaded scanned deed's details against digitized government API endpoints (e.g., Bhoomi API) to ensure the owner, area, and survey number exist and match.
*   **Font Geometry Checking:** Layer 4 analyzes script-specific line heights and character alignment in regional Indian scripts (like Devnagari or Kannada) to spot altered numbers.
*   **Visual Alteration Spotting:** Layer 2 & 3 identify spliced borders and compression differences around registration seals and survey tables.
