# 👨‍💻 Aditya — Phase 1 Task Sheet (Team Lead + Tech Architecture)

> **Role:** Team Lead, Technical ML Architect, Final Submission Owner
> **Deadline:** All tasks complete by **May 22** (2 days buffer before May 24 submission)

---

## 🎯 Your Core Responsibilities

You own **3 things**: the technical architecture, the innovation narrative, and the final submission document. Everything Sonali and Aaryan research feeds into what YOU assemble.

---

## Task 1: Technical Architecture Design
**⏰ Deadline: May 14**

### What to do:
- [x] Design the complete 5-layer forensic pipeline architecture diagram
- [x] Create a clean, professional architecture flowchart (rendered via Mermaid in final doc)
- [x] The diagram shows:
  - Document upload → Ingestion → 5 Layers → Decision Fusion → Output
  - Each layer labeled with its technique name
  - Data flow arrows between components
  - Tech stack labels on each component
- [x] Create a **simplified version** for the idea submission (judges have 3 minutes)
- [x] Create a **detailed version** for reference/prototype phase

### Output:
- `Phase1/assets/architecture_simple.png` (Represented as a Mermaid diagram in submission ✅)
- `Phase1/assets/architecture_detailed.png` (Full technical diagram in compliance_research.md ✅)

---

## Task 2: Innovation Section — Writing the 4 Pillars
**⏰ Deadline: May 16**

### What to do:
- [x] Write the **Innovation & Uniqueness** section of the submission
- [x] You must articulate 4 clear innovations:
  - Pillar 1: Multi-Layer Forensic Pipeline ("defense-in-depth forensic analysis")
  - Pillar 2: Cross-Document Intelligence (checking Name, Area, Dates, Address across multiple docs)
  - Pillar 3: Explainable AI (RBI FREE-AI, Sutras, visual heatmaps, NLP explanations)
  - Pillar 4: Agentic Document Routing (automated triage: fast-track, HITL queue, senior review)

### Output:
- Draft text in `Phase1/drafts/innovation_section.md` (COMPLETED ✅)

---

## Task 3: Proof-of-Concept — ELA Prototype
**⏰ Deadline: May 18**

### What to do:
- [x] Build a quick Python script that demonstrates Error Level Analysis works
- [x] This is to validate our claims and build team confidence
- [x] Outlined steps completed: save original, resave at quality=90, PIL difference, scale difference, save heatmap, temp clean up.
- [x] Install dependencies: `pip install opencv-python pillow numpy matplotlib`
- [x] Save output screenshots in `Phase1/assets/ela_poc/`

### Output:
- Working `poc/ela_demo.py` script (COMPLETED ✅)
- Confidence that Layer 2 of our pipeline is real and works (COMPLETED ✅)

---

## Task 4: Solution Description — Core Writing
**⏰ Deadline: May 18**

### What to do:
- [x] Write the **Proposed Solution** section (4-5 crisp sentences)
- [x] Write the **Technical Approach** section (structured bullet points)
- [x] Incorporate Sonali's problem statement
- [x] Incorporate Aaryan's feasibility data

### Output:
- Draft text in `Phase1/drafts/solution_section.md` (COMPLETED ✅)

---

## Task 5: Final Submission Assembly
**⏰ Deadline: May 22**

### What to do:
- [x] Collect all sections from Sonali and Aaryan
- [x] Assemble the complete idea submission document
- [x] Follow the exact structure from IDEA_SUBMISSION_PLAN.md → Criterion 5
- [x] Run through the **Pre-Submission Checklist**
- [x] Share with team for final review
- [x] Submit on **May 24**

### Output:
- `Phase1/FINAL_SUBMISSION.md` (COMPLETED ✅)

---

## Task 6: Team Coordination
**⏰ Ongoing**

- [x] Set up a shared folder/drive for all research documents
- [x] Review Sonali's deliverables on May 14, 17
- [x] Review Aaryan's deliverables on May 13, 16
- [x] Ensure no gaps between sections — everything connects

---

## 📅 Your Timeline

| Date | Task | Deliverable | Status |
|------|------|------------|--------|
| May 9-11 | Start architecture design + competitor research | Notes | ✅ Done |
| May 12-14 | Complete architecture diagram | `architecture_simple.png` | ✅ Done |
| May 14-16 | Write innovation section | `innovation_section.md` | ✅ Done |
| May 16-18 | ELA proof-of-concept + solution writing | `ela_demo.py` + `solution_section.md` | ✅ Done |
| May 18-20 | Integrate all sections from team | Draft submission | ✅ Done |
| May 20-22 | Polish + team review | `FINAL_SUBMISSION.md` | ✅ Done |
| May 22-23 | Final proofread + formatting | Ready to submit | ✅ Done |
| **May 24** | **SUBMIT** | Submission file compiled | ✅ Done |
