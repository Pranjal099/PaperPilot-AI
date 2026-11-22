# PaperPilot AI — Milestone 2 Submission Document

**Course:** SCSE4041 — Prompt Engineering  
**Milestone:** Milestone 2 (12 Marks)  
**Submission Deadline:** 22 November 2026  
**Problem ID:** C15 — Research Paper Summariser for Students  
**Team Name:** Token Titans  
**Team ID:** PE-B49-56  
**Batch:** B49–B64  
**Team Leader:** Aayushi Nagar (Enrollment No: `[ENROLLMENT_NO_LEADER]`)  
**Team Member:** Pranjal (Enrollment No: `[ENROLLMENT_NO_MEMBER]`)  

---

## SECTION 1: Project & Team Details
- **Project Title:** PaperPilot AI: Research Paper Summarizer Using Prompt Engineering
- **Team Name:** Token Titans
- **Team ID:** PE-B49-56
- **Problem ID:** C15 — Research Paper Summariser for Students
- **Batch:** B49–B64
- **Course:** SCSE4041 — Prompt Engineering
- **Team Members:**
  1. Aayushi Nagar (Team Leader) — `[ENROLLMENT_NO_LEADER]`
  2. Pranjal (Team Member) — `[ENROLLMENT_NO_MEMBER]`
- **Project Type:** App with code (Python Streamlit web application)

---

## SECTION 2: Problem Statement & Objectives
Undergraduate engineering students frequently struggle to digest academic literature due to dense mathematical prose, unstandardized paper structures, and complex terminology. When students attempt to use generic zero-shot AI chatbots, models frequently fabricate nonexistent quantitative benchmarks, invent missing limitations, or output superficial prose.

**Objectives:**
1. Develop an intuitive, modern web application (Streamlit) accepting PDF uploads (up to 15MB) and pasted text.
2. Implement robust digital PDF extraction using PyMuPDF (`pymupdf`) with scanned image detection.
3. Engineer a strictly sequenced 3-stage prompt chaining architecture separating factual extraction, pedagogical synthesis, and source verification.
4. Enforce strict anti-hallucination guardrails (*"If missing, state: 'Not specified in the provided text'"*).
5. Build an adversarial source verification audit module providing claim-by-claim evaluation, verbatim quotes, and Grounding Confidence Scores.
6. Deliver a 27-test automated unit test suite and a 14-case comprehensive test matrix.

---

## SECTION 3: Proposed Solution & Architecture
PaperPilot AI implements an auditable 3-tier architecture:
1. **Presentation Layer (Streamlit):** Web UI featuring PDF uploader, quick-load sample benchmarks, 11-section student summary view, Claims Verification Table with badges (`[SUPPORTED]`, `[PARTIALLY SUPPORTED]`, `[UNSUPPORTED]`), and a Developer Trace Inspector.
2. **Ingestion & Validation Layer:** Enforces input length boundaries (100 to 150,000 characters, >25 words), checks binary magic headers (`%PDF-`), and detects non-selectable scanned PDFs using PyMuPDF.
3. **Reasoning & Prompt Chain Layer:**
   - **Stage 1 (Extraction):** Strictly extracts 12 factual dimensions.
   - **Stage 2 (Student Summary):** Synthesizes extracted facts into 11 student-friendly sections, an *"Explain Like I'm a Beginner"* (ELI5) analogy, and a jargon buster.
   - **Stage 3 (Source Verification):** Cross-examines summary claims against the source text to detect hallucinations and discrepancies.

---

## SECTION 4: Tools & Model Used
- **AI Inference Engine:** Google Gemini API (`gemini-2.5-flash` / `gemini-1.5-flash`) via official `google-genai` SDK.
- **Web Application Framework:** Python Streamlit (v1.67.0+).
- **PDF Extraction:** PyMuPDF (`pymupdf` v2.1+).
- **Environment & Configuration:** Python-dotenv.
- **Testing & Quality Assurance:** Pytest (v9.2+) with 27 automated unit tests; Pandas (v3.1+) for verification data structures.
- **PDF Compilation:** ReportLab (v5.1+).

---

## SECTION 5: Prompt Design & Final Workflow
The final workflow implements **exactly THREE distinct logical prompts**:
- **Prompt 1 (`prompts/prompt_1_extraction.txt`):** Research Information Extraction. Extracts 12 factual fields. Guardrail: *"If missing, state: 'Not specified in the provided text.' Do NOT extrapolate or invent numbers."*
- **Prompt 2 (`prompts/prompt_2_summary.txt`):** Student-Friendly Structured Summary. Synthesizes 11 sections, an ELI5 sticky-note analogy, and a jargon buster.
- **Prompt 3 (`prompts/prompt_3_verification.txt`):** Source-Based Verification Audit. Audits summary claims against original text, outputting a Claims Table, verbatim quotes, Grounding Score %, and truth disclaimer.

---

## SECTION 6: Prompt Iteration Log (4 Recorded Versions)
- **Version 1 (Baseline):** Zero-shot unconstrained prompt (*"Summarize this paper in simple plain language"*). Omitted quantitative metrics (10,000x, 3x) and limitations; generated unstructured prose. `[REPLACED]`
- **Version 2 (Structured):** Added 6 academic sections. Hallucinated plausible limitations on incomplete papers; jargon remained too dense. `[REPLACED]`
- **Version 3 (Role Refined):** Introduced mentor persona, negative constraints (*"Not specified in text"*), ELI5 analogy, and glossary. Cognitive overload in single prompt led to subtle metric drift; lacked verifiable audit trail. `[REPLACED]`
- **Version 4 (Chained Workflow):** Decoupled 3-stage chain (Extraction -> Synthesis -> Audit). Achieved 100% grounding on benchmarks, verbatim evidence quotes, and active detection of missing sections and unsupported claims. `[RETAINED IN PRODUCTION]`

---

## SECTION 7: Team Contributions (Proposed Split)
- **Aayushi Nagar (Team Leader, Enrollment: `[ENROLLMENT_NO_LEADER]`):** Project coordination, scope alignment on Problem C15, UX audit of Streamlit interface, demo reel script preparation, and final submission coordination. Proposed Split: **50%**.
- **Pranjal (Team Member, Enrollment: `[ENROLLMENT_NO_MEMBER]`):** 3-stage prompt pipeline design, application development, PyMuPDF extractor, 27-test automated pytest suite, 14-case test matrix, and technical documentation. Proposed Split: **50%**.

---

## SECTION 8: Comprehensive Test Table (14 Completed Test Cases)
14 completed test cases documented in `docs/test_cases.md` and `docs/test_cases.csv` spanning:
- TC-01: Pasted Text (Normal) — PASS
- TC-02: Digital PDF Upload (Normal) — PASS
- TC-03: Missing Limitations (Edge Case) — PASS
- TC-04: Numerical Findings (Edge Case) — PASS
- TC-05: Very Short Text (<100 chars) — PASS
- TC-06: Long Text (>150,000 chars) — PASS
- TC-07: Empty Input (Invalid) — PASS
- TC-08: Corrupted PDF Header (Invalid) — PASS
- TC-09: Scanned Image-Only PDF (Edge Case) — PASS
- TC-10: Repetitive Gibberish (Invalid) — PASS
- TC-11: Ambiguous Tradeoffs (Edge Case) — PASS
- TC-12: Unsupported Claim Detection (Adversarial) — PASS
- TC-13: Multi-Benchmark Literature (Normal) — PASS
- TC-14: Offline Fallback Mode (System) — PASS

---

## SECTION 9: Prototype Modules & Working Status
**Prototype Status: All Modules Working**
1. PDF Text Extraction & Scanned Document Detection Module (`src/pdf_processing.py`)
2. Input Validation & Content Guardrail Module (`src/validation.py`)
3. Stage 1: Research Information Extraction Module (`src/ai_service.py`)
4. Stage 2: Student-Friendly Structured Summary Generation Module (`src/ai_service.py`)
5. Stage 3: Source-Based Verification Audit Module (`src/ai_service.py`, `src/verification.py`)
6. Developer Execution Trace & Prompt Inspector Module (`app.py`)
7. Summary Export & Download Module (`app.py`)

---

## SECTION 10: Results & Observations
- **Software Quality:** 27 automated unit tests passed in 0.91s with 100% pass rate.
- **Factual Fidelity:** Complete elimination of invented limitations on incomplete texts.
- **Verification Accuracy:** Corroborated 5/5 claims on the LoRA benchmark paper (100.0% Grounding Score) and accurately flagged an injected unsupported claim with a student warning.

---

## SECTION 11: Limitations & Future Work
- **Limitations:** Scanned image-only PDFs require OCR preprocessing; LLM-based verification is an automated screening aid, not formal mathematical proof.
- **Future Work:** Client-side Tesseract OCR integration, multimodal diagram/table parsing, and multi-document comparative synthesis.

---

## SECTION 12: References
1. Hu, E. J., et al. (2021). *LoRA: Low-Rank Adaptation of Large Language Models*. arXiv:2106.09685.
2. Lewis, P., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS 2020.
