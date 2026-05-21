# 👩‍💻 Sonali — Phase 1 Task Sheet (Domain Research + Impact)

> **Role:** Domain Researcher, Problem Statement Author, Impact Analyst, Pitcher
> **Deadline:** All tasks complete by **May 23**

---

## 🎯 Core Responsibilities

You own: the **problem statement**, the **business impact case**, and all **domain research** about Canara Bank, Indian banking fraud, and land records. Without real numbers, our submission sounds generic and loses marks.

---

## Task 1: Canara Bank Deep Research
**⏰ Deadline: May 13**

### What to find:
- [x] Download **Canara Bank Annual Report 2024-25** from [canarabank.com](https://canarabank.com) → Investor Relations
- [x] Extract: total branches, loan portfolio size (₹ Cr), NPA figures
- [x] Find: any mention of fraud, document verification, or AI/digital initiatives
- [x] Research current tech platforms they use for document verification
- [x] Search news: "Canara Bank fraud", "Canara Bank AI adoption", "Canara Bank digital"
- [x] Find: loan processing workflow — what documents required for home/business loans?
- [x] Find: average loan disbursement time

### Output: `Phase1/research/canara_bank_profile.md` (COMPLETED ✅)

---

## Task 2: Indian Banking Fraud Statistics
**⏰ Deadline: May 14**

### Must-find numbers:

| Data Point | Source to Check | Status |
|-----------|----------------|--------|
| Total bank fraud losses India FY23-FY25 (₹ Cr) | RBI Annual Report | [x] Found: ₹13,930 Cr (FY24) |
| Document fraud as % of total fraud | RBI / Industry reports | [x] Found: ~30% of loan fraud |
| Average time for manual document verification | Industry reports / bank interviews | [x] Found: 3-5 working days |
| Cost per manual verification (₹) | Industry estimate | [x] Found: ₹1,500/app |
| Famous land record fraud cases in India (2-3 cases) | Google News | [x] Found and detailed 2 cases |
| PSU bank specific fraud data | RBI data | [x] Found: PSBs hold >60% of fraud value |

### Also research:
- [x] What do Indian banks currently use for doc verification? (HyperVerge, Digio, SignDesk)
- [x] What gaps exist in current solutions?
- [x] Why do sophisticated forgeries still slip through?

### Output: `Phase1/research/fraud_landscape.md` — All stats with source URLs (COMPLETED ✅)

---

## Task 3: Problem Statement Draft
**⏰ Deadline: May 14**

### Write exactly 4 sentences following this template:

```
Sentence 1: Big picture → "Indian banks lost ₹[X] Cr to fraud in FY[X]..."
Sentence 2: Canara Bank pain → "Canara Bank's [X]+ branches manually verify..."
Sentence 3: Why existing solutions fail → "Current tools focus on [basic OCR]..."
Sentence 4: Urgency → "With RBI's FREE-AI framework (Aug 2025)..."
```

Fill every `[X]` with REAL numbers from Tasks 1 & 2. No made-up stats.

### Output: `Phase1/drafts/problem_statement.md` (COMPLETED ✅)

---

## Task 4: Indian Land Records Research
**⏰ Deadline: May 15**

### Must know (judges from Canara Bank WILL test this):

**Types of land records by state:**
- [x] 7/12 Extract (Maharashtra) | Patta/Chitta (Tamil Nadu)
- [x] Khata (Karnataka) | Jamabandi/Fard (Punjab, Haryana)
- [x] ROR, Encumbrance Certificate, Sale Deed, Mutation docs

**Common tampering methods:**
- [x] Changing survey numbers, altering property area
- [x] Modifying ownership names, fake registration numbers
- [x] Photoshopped stamps/seals

**Digitization status:**
- [x] Which states have digital land records? (DILRMP program)
- [x] What format? (PDF, scanned images, georeferenced maps)

### Output: `Phase1/research/land_records_india.md` (COMPLETED ✅)

---

## Task 5: Compliance Research
**⏰ Deadline: May 16**

- [x] **DPDP Act 2023** — key requirements for handling personal data in documents
- [x] **RBI Data Localization** — all data processed/stored in India (architecture implication)
- [x] **RBI FREE-AI Framework** — what compliance requirements does DocShield satisfy?

### Output: `Phase1/research/compliance_research.md` (COMPLETED ✅)

---

## Task 6: Impact Section Writing
**⏰ Deadline: May 17**

### Cover 4 impact dimensions:
1. **Financial:** Calculate annual fraud prevention value + cost savings for Canara Bank
2. **Operational:** Time reduction (3-5 days → 3 seconds), consistency across branches
3. **Compliance:** RBI FREE-AI + DPDP Act compliance
4. **Social:** Protecting rural landowners, faster financial inclusion

### Output: `Phase1/drafts/impact_section.md` (COMPLETED ✅)

---

> [!IMPORTANT]
> **Every fact needs a source URL.** Don't write "banks lost ₹X Cr" without linking where you found it. If you can't find an exact number, write "estimated" with your logic.
