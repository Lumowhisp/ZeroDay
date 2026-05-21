# 🏢 Canara Bank Corporate & Underwriting Profile

This document details the corporate structure, financial status, and loan underwriting workflows of **Canara Bank** based on the bank's **Annual Report 2024-25** and recent operational metrics.

---

## 📊 Key Financial & Operational Metrics (FY25)

| Metric | FY 2023-24 | FY 2024-25 | Source |
| :--- | :--- | :--- | :--- |
| **Total Domestic Branches** | 9,604 | **9,849** | Canara Bank Investor Presentation (Q4 FY25) |
| **Global Advances (Loan Book)** | ₹9.32 Lakh Cr | **₹10.73 Lakh Cr** (+11.74% YoY) | Q4 FY25 Financial Results |
| **Gross NPA Ratio** | 4.23% | **2.94%** | Asset Quality Reports (FY25) |
| **Net NPA Ratio** | 1.27% | **0.70%** | Asset Quality Reports (FY25) |
| **Provision Coverage Ratio (PCR)** | 89.10% | **92.70%** | Q4 FY25 Earnings Call Transcripts |
| **Annual Net Profit** | ₹14,554 Cr | **₹17,027 Cr** (+17.0% YoY) | Annual Report 2024-25 |

---

## 💻 Tech Adoption & Digital Initiatives

*   **Current KYC & Onboarding:** Canara Bank utilizes standard API gateways (e.g., DigiLocker integration, basic Aadhaar-based OTP verification, and basic OCR tools like HyperVerge or Digio for PAN extraction) to onboard retail savings accounts.
*   **The Underwriting Bottleneck:** While *onboarding* is semi-digital, *loan underwriting* (advances) is highly manual. The bank's credit departments manually review property papers, valuation certificates, and financial filings.
*   **Annual Report Tech Strategy:** The bank’s **Annual Report 2024-25** specifically outlines a commitment to digital transformation (under the **Utkarsh** operational guidelines), focusing on AI-based credit scoring models, robotic process automation (RPA), and upgrading its core banking solution (CBS) to support real-time digital lending.

---

## 📝 Loan Processing Workflow & Documents Required

### 🏡 Home Loans (Retail Advances)
1.  **Application Ingestion:** KYC documents (PAN, Aadhaar) + income proof (Salary slips, ITR, 6-month bank statements).
2.  **Property Document Scrutiny:**
    *   **Sale Deed / Mother Deed:** Verifying chain of title.
    *   **Encumbrance Certificate (EC):** Form 15/16 spanning 13-30 years to check for existing mortgages.
    *   **Land Revenue Records:** 7/12 Extract (Maharashtra), Khata (Karnataka), or Jamabandi (Punjab/Haryana) to confirm matching survey numbers and ownership.
    *   **Approved Plan / NOC:** Layout approvals from local municipal authorities.
3.  **Manual Scrutiny & Legal Search Report (LSR):** The documents are sent to an empanelled lawyer who manually checks physical or scanned registries.
4.  **Disbursement:** Takes **3 to 7 working days** on average, primarily delayed by manual document verification and title search.

### 🏢 MSME / Business Loans (Wholesale Advances)
1.  **Financial Document Ingestion:** 2-3 years ITR, audited Balance Sheets, Profit & Loss accounts, and GST returns.
2.  **Verification:** Credit analysts manually verify figures across tax filings, bank statement turnovers, and audit reports to detect mismatching revenues.
3.  **Disbursement:** Takes **10 to 15 working days**, depending on the complexity of corporate structures and property collateral evaluations.

---

## ⚠️ Document Fraud News & Vulnerabilities
*   **Collateral Inflation:** Recent banking news highlights cases where fraudsters submitted forged land sale deeds with altered survey numbers to collateralize loans with non-existent or highly inflated land values.
*   **Identity Splicing:** Instances where individuals tampered with scanned land documents, editing the names of landowners or survey areas to obtain agricultural loans from regional rural branches.
*   **Dual Mortgaging:** Generating forged copies of the same Sale Deed with altered registration seals to obtain loans from multiple banks concurrently.
*   *Operational Impact:* Manual checks frequently fail to catch high-resolution digital alterations (such as edited digits in land measurements or photocopied registration stamps).
