# Technical Report: PaperPilot AI

**Project Name:** PaperPilot AI: Research Paper Summarizer Using Prompt Engineering  
**Team Name:** Token Titans  
**Team ID:** PE-B49-56  
**Problem ID:** C15 — Research Paper Summariser for Students  
**Batch:** B49–B64 | **Course:** SCSE4041 — Prompt Engineering  
**Team Leader:** Aayushi Nagar (`[ENROLLMENT_NO_LEADER]`)  
**Team Member:** Pranjal (`[ENROLLMENT_NO_MEMBER]`)  
**Submission Date:** 22 November 2026  
**Corresponding PDF Deliverable:** `TokenTitans_TechnicalReport.pdf`  

---

## 1. Abstract
Undergraduate engineering and computer science students face severe cognitive barriers when engaging with scholarly research literature. Primary challenges include dense mathematical formalisms, unstandardized paper structures, domain-specific terminology, and the prevalence of unsupported or hallucinated assertions produced by naive, single-prompt large language model (LLM) summarizers. To address these issues under Problem C15, we present **PaperPilot AI**, a student-friendly web application leveraging an auditable, three-stage prompt chaining architecture. Stage 1 executes strict factual information extraction across 12 dimensions with explicit negative constraints ('Not specified in the provided text'). Stage 2 synthesizes extracted findings into an accessible 11-section pedagogical guide featuring an 'Explain Like I'm a Beginner' (ELI5) analogy and technical glossary. Stage 3 conducts an adversarial source verification audit, classifying claims as Supported, Partially Supported, or Unsupported while extracting verbatim corroborating quotes. The system is backed by a 27-test automated pytest suite (100% pass rate) and a 14-case comprehensive test matrix spanning PDFs, incomplete texts, numerical findings, and adversarial claim injections.

## 2. Introduction
Scientific discovery relies on literature synthesis. However, undergraduate novice researchers often spend hours parsing single papers due to unfamiliarity with experimental setups, mathematical conventions, and nuanced ablation studies. When students turn to generic AI chatbots, standard zero-shot prompts exhibit critical failure modes: (1) fabricating nonexistent quantitative benchmarks, (2) inventing missing limitations when authors omit them, and (3) producing superficial prose summaries that omit vital architectural specifications.

## 3. Problem Statement (Problem ID: C15)
Design, implement, and evaluate an intelligent research paper summarizer for students that leverages structured prompt engineering and prompt chaining to extract research objectives, methodologies, quantitative findings, and limitations into verifiable summaries while preventing unsupported claims.

## 4. Existing Problem & Motivation
Standard LLMs suffer from "hallucination under uncertainty": when asked to summarize an academic paper that omits limitations or datasets, models extrapolate plausible-sounding but completely fabricated facts. Furthermore, academic jargon discourages early-stage undergraduate researchers. The motivation behind PaperPilot AI is to combine pedagogical clarity with uncompromising factual grounding.

## 5. Project Objectives
1. Develop an intuitive web interface (Streamlit) supporting both PDF uploads (up to 15MB) and pasted text.
2. Implement robust PDF text extraction with PyMuPDF, including scanned image detection and boundary validation.
3. Engineer a strictly decoupled 3-prompt chained pipeline separating factual extraction, student synthesis, and adversarial verification.
4. Integrate anti-hallucination negative constraints requiring explicit acknowledgment of missing paper sections.
5. Provide full transparency through a Developer Trace Inspector displaying rendered prompts, latencies, and raw outputs.
6. Execute a comprehensive QA test suite covering at least 10 unique inputs (completed: 14 test cases and 27 automated unit tests).

## 6. Proposed Solution
PaperPilot AI replaces black-box one-shot generation with an auditable three-stage prompt pipeline:
- Stage 1 extracts 12 grounded factual dimensions without speculation.
- Stage 2 synthesizes extracted dimensions into 11 student-centric sections, an ELI5 analogy, and a jargon buster.
- Stage 3 audits each major claim against the raw text, extracting verbatim quotes and computing a Grounding Confidence Score.

## 7. System Architecture
The system consists of three architectural tiers:
- **Presentation Layer (Streamlit):** Reactive web interface with file upload, quick-load sample benchmarks, claims verification tables, badges, and developer trace inspectors.
- **Ingestion & Validation Layer:** PyMuPDF digital text extractor, scanned PDF detector, and boundary validator (100–150,000 chars, >25 words).
- **Reasoning & Prompt Chain Layer:** Google Gemini API (`gemini-2.5-flash` / `gemini-1.5-flash`) executing the sequential 3-stage chain with deterministic heuristic fallback.

## 8. Technology Stack
- **Web Interface:** Streamlit (v1.67.0+)
- **LLM Engine:** Google Gemini API via official `google-genai` SDK (v3.6+)
- **PDF Processing:** PyMuPDF (`pymupdf` v2.1+)
- **Environment & Secrets:** python-dotenv (v1.2+)
- **Data & Tables:** Pandas (v3.1+)
- **Automated Testing:** Pytest (v9.2+)
- **PDF Compilation:** ReportLab (v5.1+)

## 9. Application Modules
1. **PDF Text Extraction Module (`src/pdf_processing.py`):** In-memory PyMuPDF stream processing, page counting, and scanned PDF detection.
2. **Input Validation Module (`src/validation.py`):** Character and word length boundary enforcement, magic header checking (`%PDF-`), and low-entropy gibberish rejection.
3. **Stage 1 Extraction Module (`src/ai_service.py`):** Zero-shot factual extraction across 12 structured dimensions.
4. **Stage 2 Student Summary Module (`src/ai_service.py`):** Pedagogical synthesis across 11 sections with ELI5 analogy and jargon glossary.
5. **Stage 3 Source Verification Module (`src/ai_service.py`, `src/verification.py`):** Markdown claims table parser, status classifier, and Grounding Score % calculator.
6. **Developer Execution Trace Module (`app.py`):** Real-time inspection of rendered prompts, execution latencies, and raw model outputs.
7. **Summary Export Module (`app.py`):** Download verified reports in Markdown format.

## 10. Prompt Engineering Approach
The core prompt engineering strategy isolates distinct cognitive tasks:
- **Extraction Specialization:** Prompt 1 has no license to generate analogies or conversational prose; it is strictly an objective data parser.
- **Synthesis Specialization:** Prompt 2 works exclusively from the factual anchors established by Prompt 1, eliminating hallucination risks.
- **Adversarial Verification:** Prompt 3 acts as an independent auditor, searching for discrepancies between Prompt 2 claims and the raw source text.

## 11. Description of the Three Final Prompts
- **Prompt 1 (`prompts/prompt_1_extraction.txt`):** Research Information Extraction. Requires 12 fields (Title, Problem, Objective, Questions, Methodology, Datasets, Findings, Metrics, Limitations, Future Work, Conclusion, Evidence Quotes, Ambiguities). Guardrail: *"If missing, state: Not specified in provided text."*
- **Prompt 2 (`prompts/prompt_2_summary.txt`):** Student-Friendly Structured Summary. Requires 11 sections including Executive Overview, The Big Picture, Objectives, How It Works, Dataset/Setup, Key Findings, Limitations, Future Work, Conclusion, ELI5 Analogy, and Jargon Buster.
- **Prompt 3 (`prompts/prompt_3_verification.txt`):** Source-Based Verification Audit. Adversarially cross-examines 4 to 8 claims against raw source text, assigning `[SUPPORTED]`, `[PARTIALLY SUPPORTED]`, `[UNSUPPORTED]`, or `[NOT VERIFIABLE]`.

## 12. Prompt Iteration Methodology & Evolutionary History
Documented across 4 empirical versions in `docs/prompt_iteration_log.md`:
- **Version 1 (Baseline):** Zero-shot prompt. Missed quantitative gains (10,000x, 3x) and limitations; generated unstructured prose. `[REPLACED]`
- **Version 2 (Structured):** 6 academic sections. Hallucinated plausible limitations on incomplete papers. `[REPLACED]`
- **Version 3 (Role Refined):** Mentor persona, negative constraints, ELI5 analogy, and glossary. Cognitive overload in single prompt led to subtle metric drift; lacked audit. `[REPLACED]`
- **Version 4 (Final Chained Workflow):** Decoupled 3-stage chain. Achieved 100% grounding, verbatim quotes, and active detection of missing sections and unsupported claims. `[RETAINED IN PRODUCTION]`

## 13. Testing Methodology
Quality Assurance combines 27 automated unit tests via Pytest and a 14-case comprehensive test matrix evaluating normal, boundary, invalid, and adversarial inputs.

## 14. Test Table (14 Completed Test Cases)
Documented in `docs/test_cases.md` and `docs/test_cases.csv`:
- TC-01: Pasted Text (LoRA paper) — PASS (100% Grounding)
- TC-02: PDF Upload (sample_paper_1_lora.pdf) — PASS (Clean PyMuPDF extract)
- TC-03: Missing Limitations (FastGraph text) — PASS (Strict negative guardrail)
- TC-04: Numerical Findings (10,000x, 3x memory) — PASS (Zero metric drift)
- TC-05: Very Short Text (<100 chars) — PASS (Validation error displayed)
- TC-06: Long Text (>150,000 chars) — PASS (Boundary error displayed)
- TC-07: Empty Input (whitespace) — PASS (Rejected immediately)
- TC-08: Corrupted PDF Header — PASS (Magic byte check rejected)
- TC-09: Scanned Image PDF — PASS (PyMuPDF flagged scanned file)
- TC-10: Gibberish Input — PASS (Entropy check caught repetitive characters)
- TC-11: Ambiguous Statements — PASS (Nuanced tradeoff preserved)
- TC-12: Unsupported Claim Detection — PASS (Synthetic claim flagged as Unsupported)
- TC-13: Multi-Benchmark Literature (RAG paper) — PASS (Extracted DPR & BART metrics)
- TC-14: Offline Fallback Mode — PASS (Graceful fallback without unhandled exception)

## 15. Actual Results & Observations
- All 27 automated unit tests passed in 0.91 seconds.
- On benchmark literature (LoRA), the system extracted all key metrics (10,000x parameter reduction, 3x memory savings) with zero numerical distortion.
- Stage 3 successfully corroborated 5/5 claims, achieving a 100.0% Grounding Score, while correctly flagging an injected quantum computing claim as `[UNSUPPORTED]`.

## 16. Limitations
- Scanned bitmap PDFs require external OCR preprocessing.
- Extremely large monographs (>150,000 characters) must be segmented by chapter or section.
- LLM-based automated verification is a screening aid, not formal mathematical proof.

## 17. Ethical Considerations
Summaries are designed as undergraduate learning aids, not plagiarism shortcuts. PaperPilot AI embeds truth disclaimers and encourages students to inspect primary literature citations.

## 18. Future Improvements
- Integration with client-side Tesseract OCR for scanned PDF support.
- Multimodal extraction of figures, charts, and mathematical equations.
- Vector retrieval indexing for interactive student Q&A over full book-length dissertations.

## 19. Conclusion
PaperPilot AI successfully demonstrates that multi-step prompt engineering and prompt chaining effectively solve the trade-off between undergraduate accessibility and factual fidelity in academic summarization.

## 20. References
1. Hu, E. J., et al. (2021). *LoRA: Low-Rank Adaptation of Large Language Models*. arXiv:2106.09685.
2. Lewis, P., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS 2020.
3. Vaswani, A., et al. (2017). *Attention Is All You Need*. NeurIPS 2017.

## 21. Team Contribution Table (Milestone 2)
| Team Member | Enrollment No. | Responsibilities & Deliverables | Proposed Split |
|---|---|---|---|
| **Aayushi Nagar** (Team Leader) | `[ENROLLMENT_NO_LEADER]` | Project coordination, scope alignment on Problem C15, UX audit of Streamlit interface, demo reel script preparation, and final submission coordination. | 50% (Proposed) |
| **Pranjal** (Team Member) | `[ENROLLMENT_NO_MEMBER]` | 3-stage prompt pipeline design, application development, PyMuPDF extractor, 27-test automated pytest suite, 14-case test matrix, and report documentation. | 50% (Proposed) |
