# PaperPilot AI — Milestone 2 Official Submission Form Answer Sheet
## Course: SCSE4041 — Prompt Engineering | Milestone 2 (12 Marks)
### Team: Token Titans | Team ID: PE-B49-56 | Batch: B49–B64

> **Generated:** November 22, 2026  
> **Status:** Final & Verified. Ready to copy-paste directly into Microsoft Form.  
> **Note on Placeholders:** Fields marked `[NEEDS INPUT]` represent private university IDs or personal upload links that must be filled in before final submission.

---

## 📋 ALL 24 FORM ANSWERS (In Exact Official Form Order)

---

### Q1. Team ID (assigned to every team after Milestone 1)
```text
PE-B49-56
```

---

### Q2. Team Name as Given in Milestone 1
```text
Token Titans
```

---

### Q3. Project Title / Name
```text
PaperPilot AI: Research Paper Summarizer Using Prompt Engineering
```

---

### Q4. Team Leader Name
```text
Aayushi Nagar
```

---

### Q5. Team Leader Enrollment No.
```text
[NEEDS INPUT — Enter Aayushi Nagar's University Enrollment Number]
```

---

### Q6. Select your Group (Batch)
```text
B49-64
```
*(Select option **B49-64** from the form dropdown list)*

---

### Q7. Enrollment numbers of all team members (one per line)
```text
[NEEDS INPUT — Aayushi Nagar's Enrollment Number]
[NEEDS INPUT — Pranjal's Enrollment Number]
```
*(Enter one enrollment number per line as instructed)*

---

### Q8. Project Type (maximum 2 options)
```text
App with code
```
*(Select **App with code** — PaperPilot AI is a production Python + Streamlit web application with a 27-test automated pytest harness and live Gemini API integration)*

---

### Q9. Main AI tool and model used
```text
Google Gemini API — Model: gemini-3.5-flash-lite
```
*(Verified in production: DEFAULT_MODEL is `gemini-3.5-flash-lite` with automated fallback resilience to `gemini-3.1-flash-lite` and `gemini-3.5-flash`)*

---

### Q10. Number of prompts in the final solution
```text
3
```
*(Represents the 3 chained logical prompt stages in the sequential pipeline: Stage 1 Extraction, Stage 2 Summary Synthesis, and Stage 3 Source Verification)*

---

### Q11. Prototype link
```text
https://paperpilot-ai-4qan.onrender.com
```
*(Public live production deployment hosted on Render's cloud platform, binding to $PORT and 0.0.0.0 with secure server-side credential isolation)*

---

### Q12. Git repository or project folder link
```text
https://github.com/Pranjal099/PaperPilot-AI
```
*(Public GitHub repository containing complete source code, prompt templates, test suite, and CI/deployment configurations)*

---

### Q13. Reel / video link
```text
[NEEDS INPUT — Local 1080p screen recording located on Desktop (244s): "Screen Recording 2026-11-22 at 7.40.48 PM.mov". Please upload to YouTube (unlisted) or Google Drive (anyone with link can view) and paste the public link here]
```

---

### Q14. Video duration in seconds
```text
120
```
*(Target script duration per `docs/demo_reel_script.md` is 120 seconds. If submitting the raw desktop screen recording file, duration is 244 seconds)*

---

### Q15. Supporting document type
```text
Technical Report
```
*(Select **Technical Report** from the form options)*

---

### Q16. Supporting document (Upload)
```text
UPLOAD FILE: TokenTitans_PaperPilotAI_TechnicalReport.pdf
```
*(File location in workspace: `TokenTitans_Milestone2_Submission/TokenTitans_PaperPilotAI_TechnicalReport.pdf`)*

---

### Q17. Number of test inputs / test cases used
```text
14
```
*(14 empirical test cases covering normal papers, binary PDF parsing, boundary inputs, negative constraints, corrupted headers, and synthetic hallucinations — all 14 evaluated as PASS in `docs/test_cases.csv` and `PaperPilotAI_Testing_Evidence.md`, backed by 27 automated pytest tests)*

---

### Q18. Number of prompt versions / iterations
```text
4
```
*(Four documented prompt versions: v1_baseline, v2_structured, v3_role_refined, and v4_chained_workflow, showing iterative architectural refinement from zero-shot to a 3-stage chained pipeline)*

---

### Q19. Prototype / implementation status
```text
All modules working
```
*(All 9 core application modules functional: PDF extraction, academic validation, Stage 1 extraction, Stage 2 synthesis, Stage 3 verification, claims table parser, grounding engine, trace inspector, and Render cloud deployment)*

---

### Q20. Working modules (describe what works)
```text
1. PDF Binary Processing & Digital Text Extraction (PyMuPDF engine with scanned image detection)
2. Input Validation & Academic Guardrails (Minimum length, word count, character-entropy gibberish filter)
3. Stage 1: Research Information Extraction (Live Google Gemini API — gemini-3.5-flash-lite)
4. Stage 2: Student-Friendly Summary Synthesis (Sectional breakdown with real-world pedagogical analogies)
5. Stage 3: Source-Based Verification Audit (Cross-examines summary against raw paper text)
6. Verification Claims Table Parser & Grounding Scoring Engine (Categorizes claims as Supported, Partially Supported, or Unsupported)
7. Developer Execution Trace & Prompt Inspector (Displays rendered prompts, latencies, and raw outputs)
8. Summary Report Downloader (Exports complete summary and claims audit to Markdown/Text)
9. Render Cloud Production Deployment (Zero client-side DOM credential exposure with secure server environment isolation)
```

---

### Q21. Milestone 2 PDF (Upload)
```text
UPLOAD FILE: TokenTitans_Milestone2_Submission.pdf
```
*(File location in workspace: `TokenTitans_Milestone2_Submission/TokenTitans_Milestone2_Submission.pdf`)*

---

### Q22. Team member contributions (one per line: Enrollment — Name — Contribution)
```text
[NEEDS INPUT — Aayushi Nagar Enrollment No] – Aayushi Nagar – Project coordination, UX audit, demo reel script preparation, and submission coordination.
[NEEDS INPUT — Pranjal Enrollment No] – Pranjal – Prompt engineering & chaining, full-stack application development (Streamlit + Gemini API), automated testing (27 pytest tests), Render deployment, and technical documentation.
```

---

### Q23. Additional notes for evaluator
```text
PaperPilot AI implements a 3-stage prompt chaining pipeline built on Google Gemini API (gemini-3.5-flash-lite). The prototype is publicly deployed on Render at https://paperpilot-ai-4qan.onrender.com with secure server-side environment credentials. The pipeline executes: (1) Structured Extraction, (2) Student-Friendly Synthesis with analogies, and (3) Source Verification with quantitative grounding score. The application includes a deterministic offline heuristic simulation fallback mode for reliable testing without an API key. All 27 automated pytest tests pass. 4 documented prompt iterations and 14 test cases with full input/expected/actual outputs are provided.
```

---

### Q24. Declaration / Confirmation
```text
Confirmed by both team members (Aayushi Nagar and Pranjal). The work submitted is original, completed as part of SCSE4041 Prompt Engineering Milestone 2, and accurately represents our project PaperPilot AI.
```

---

## 📌 Checklist Before Submitting Microsoft Form:
- [ ] Insert Aayushi Nagar's University Enrollment Number into **Q5**, **Q7**, and **Q22**.
- [ ] Insert Pranjal's University Enrollment Number into **Q7** and **Q22**.
- [ ] Upload video recording to YouTube or Google Drive, paste link in **Q13**, and confirm duration in **Q14**.
- [ ] Attach `TokenTitans_PaperPilotAI_TechnicalReport.pdf` under **Q16**.
- [ ] Attach `TokenTitans_Milestone2_Submission.pdf` under **Q21**.
- [ ] Confirm both members review before clicking Submit.
