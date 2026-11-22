# PaperPilot AI — Milestone 2 Submission Form Answers
## Team: Token Titans | Team ID: PE-B49-56 | SCSE4041 Prompt Engineering

> **Generated:** 22 November 2026  
> **Status:** Copy-paste ready. Fields marked `[NEEDS YOUR INPUT]` require information only you hold.  
> **Do NOT submit until** you fill all `[NEEDS YOUR INPUT]` fields and obtain the video/prototype links.

---

## ✅ ALL 24 ANSWERS

---

### Q1. Team ID

```
PE-B49-56
```

---

### Q2. Team Name as Given in Milestone 1

```
Token Titans
```

---

### Q3. Project Title / Name

```
PaperPilot AI: Research Paper Summarizer Using Prompt Engineering
```

---

### Q4. Team Leader Name

```
Aayushi Nagar
```

---

### Q5. Team Leader Enrollment No.

```
[NEEDS YOUR INPUT — Enter Aayushi Nagar's enrollment number]
```

---

### Q6. Select Your Group (Batch)

```
B49-64
```
> Select the option **B49-64** in the dropdown.

---

### Q7. Enrollment Numbers of All Team Members (one per line)

```
[NEEDS YOUR INPUT — Aayushi Nagar's enrollment number]
[NEEDS YOUR INPUT — Pranjal's enrollment number]
```
> Enter one enrollment number per line in the form field.

---

### Q8. Project Type (maximum 2 options)

```
App with code
```
> Select **"App with code"** — the project is a fully working Python + Streamlit application with 27 automated pytest tests.

---

### Q9. Main AI Tool and Model Used

```
Google Gemini API — Model: gemini-3.5-flash-lite
```
> **Verified live:** `DEFAULT_MODEL = "gemini-3.5-flash-lite"` confirmed in `src/ai_service.py` and `GEMINI_MODEL=gemini-3.5-flash-lite` in `.env`. Live pipeline ran successfully: Stage 1 (5.05 s), Stage 2 (18.66 s), Stage 3 (5.08 s) — all LIVE, 100% grounding score.

---

### Q10. Number of Prompts in the Final Solution

```
3
```
> Three distinct prompt templates used in the chained pipeline:
> - `prompt_1_extraction.txt` — Stage 1: Research Information Extraction
> - `prompt_2_summary.txt` — Stage 2: Student-Friendly Structured Summary
> - `prompt_3_verification.txt` — Stage 3: Source-Based Verification Audit

---

### Q11. Prototype Link

```
[LINK NOT AVAILABLE — App runs locally at http://localhost:8501 and is not deployed]
```
> **Action required before submitting:** If you want to share a live link, deploy the app to [Streamlit Cloud](https://streamlit.io/cloud) for free and paste the URL here. Otherwise, leave this field blank or write "Local prototype — see GitHub repository and demo video."

---

### Q12. Git Repository or Project Folder Link

```
https://github.com/Pranjal099/PaperPilot-AI
```
> **Verified:** Confirmed as `origin` remote in the local git config. Ensure the repository is set to **Public** before submitting.

---

### Q13. Reel / Video Link

```
[LINK NOT AVAILABLE — Demo video has not been recorded yet]
```
> **Action required before submitting:** Record the ~120-second demo reel following `docs/demo_reel_script.md`, upload to YouTube or Google Drive (unlisted is fine), and paste the link here.

---

### Q14. Video Duration (in seconds)

```
120
```
> Target duration per `docs/demo_reel_script.md`. **Update this value** after recording if the actual duration differs.

---

### Q15. Supporting Document Type

```
Technical Report
```
> Select **"Technical Report"** in the form dropdown.

---

### Q16. Supporting Document (Upload)

```
UPLOAD FILE: TokenTitans_TechnicalReport.pdf
```
> File location on your machine:  
> `/Users/pranjalgautam/Desktop/PaperPilot_AI/TokenTitans_TechnicalReport.pdf`  
> Upload this file directly in the Microsoft Form upload field for Q16.

---

### Q17. Number of Test Inputs / Test Cases Used

```
14
```
> **Verified:** `docs/test_cases.csv` contains 14 rows (TC-01 through TC-14), each with Input, Expected Output, Actual Output, and Status columns. All 14 test cases have status **PASS**.

---

### Q18. Number of Prompt Versions / Iterations

```
4
```
> **Verified:** Four prompt versions exist in `prompts/prompt_versions/`:
> - `v1_baseline.txt` — Initial zero-shot prompt
> - `v2_structured.txt` — Added structured output format
> - `v3_role_refined.txt` — Added expert persona and role
> - `v4_chained_workflow.txt` — Final 3-stage chained pipeline

---

### Q19. Prototype / Implementation Status

```
All modules working
```
> Select **"All modules working"** — 27/27 pytest tests pass and all 9 application modules are fully functional with live Gemini API confirmed.

---

### Q20. Working Modules (describe what works)

```
1. PDF Text Extraction & Scanned Document Detection (PyMuPDF/fitz)
2. Input Validation & Academic Content Guardrail
3. Stage 1: Research Information Extraction (live Gemini API — gemini-3.5-flash-lite)
4. Stage 2: Student-Friendly Structured Summary (live Gemini API — gemini-3.5-flash-lite)
5. Stage 3: Source-Based Verification Audit (live Gemini API — gemini-3.5-flash-lite)
6. Verification Claims Parser & Grounding Scoring Engine
7. Developer Execution Trace & Prompt Inspector (expandable in UI)
8. Summary Export & Download (Markdown and plain text)
9. API Key Local Persistence & Dynamic Model Discovery (.env-based)
```

---

### Q21. Milestone 2 PDF (Upload)

```
UPLOAD FILE: TokenTitans_Milestone2.pdf
```
> File location on your machine:  
> `/Users/pranjalgautam/Desktop/PaperPilot_AI/TokenTitans_Milestone2.pdf`  
> Upload this file directly in the Microsoft Form upload field for Q21.

---

### Q22. Team Member Contributions (one per line: Enrollment — Name — Contribution)

```
[NEEDS YOUR INPUT — Aayushi Nagar's enrollment number] – Aayushi Nagar – Project coordination, UX audit, demo reel script preparation, and submission coordination.
[NEEDS YOUR INPUT — Pranjal's enrollment number] – Pranjal – Prompt engineering and chaining, full-stack application development (Streamlit + Gemini API), automated testing (27 pytest tests), and technical documentation.
```
> Replace both `[NEEDS YOUR INPUT]` placeholders with the actual enrollment numbers before submitting.

---

### Q23. Additional Notes for Evaluator

```
PaperPilot AI implements a 3-stage prompt chaining pipeline built on Google Gemini API (gemini-3.5-flash-lite). Stage 1 extracts structured research metadata (title, objectives, methodology, key findings, limitations). Stage 2 synthesises a student-friendly, section-structured summary from Stage 1 output. Stage 3 performs source-grounded claim verification with a quantitative grounding score. The application includes offline heuristic simulation mode (clearly labelled) for demonstration without an API key. All 27 automated pytest tests pass. Four documented prompt versions show iterative refinement from baseline zero-shot to the final chained workflow. 14 test cases with full Input/Expected/Actual/Status records are included. Source code, prompt templates, test cases, and technical documentation are available in the public GitHub repository.
```

---

### Q24. Declaration / Confirmation

```
Confirmed by both team members (Aayushi Nagar and Pranjal). The work submitted is original, completed as part of SCSE4041 Prompt Engineering Milestone 2, and accurately represents our project PaperPilot AI.
```

---

## 📋 BEFORE SUBMITTING — CHECKLIST

| # | Item | Status |
|---|------|--------|
| 1 | Fill **Q5** — Aayushi Nagar's enrollment number | ⬜ Needs your input |
| 2 | Fill **Q7** — both enrollment numbers (one per line) | ⬜ Needs your input |
| 3 | Fill **Q22** — replace both enrollment placeholders | ⬜ Needs your input |
| 4 | Record ~120-second demo reel per `docs/demo_reel_script.md` | ⬜ Not yet done |
| 5 | Upload demo video to YouTube/Drive and paste URL in **Q13** | ⬜ Needs video link |
| 6 | Update **Q14** video duration if actual recording differs from 120 s | ⬜ After recording |
| 7 | Upload `TokenTitans_TechnicalReport.pdf` for **Q16** | ⬜ Upload file |
| 8 | Upload `TokenTitans_Milestone2.pdf` for **Q21** | ⬜ Upload file |
| 9 | Optionally deploy to Streamlit Cloud and paste URL in **Q11** | ⬜ Optional |
| 10 | Verify GitHub repo `https://github.com/Pranjal099/PaperPilot-AI` is **Public** | ⬜ Verify |
| 11 | Confirm submission with Aayushi Nagar (Q24) | ⬜ Confirm |

---

*Document generated by Antigravity AI based on verified project files. All factual claims cross-checked against `src/ai_service.py`, `.env`, `docs/test_cases.csv`, `prompts/prompt_versions/`, and live Gemini API test results.*
