# PaperPilot AI — Prompt Engineering Iteration Log

**Project Name:** PaperPilot AI: Research Paper Summarizer Using Prompt Engineering  
**Team Name:** Token Titans  
**Team ID:** PE-B49-56  
**Problem ID:** C15 — Research Paper Summariser for Students  
**Batch:** B49–B64 | **Course:** SCSE4041 — Prompt Engineering  
**Team Leader:** Aayushi Nagar | **Team Member:** Pranjal  
**Date of Evaluation:** November 22, 2026  

---

## Executive Summary of Prompt Iterations

The core research objective of PaperPilot AI is to bridge complex academic literature and undergraduate comprehension without introducing hallucinated claims, missing limitations, or unverified quantitative assertions. Over the development lifecycle, the prompt architecture progressed through four distinct evolutionary phases:

1. **Version 1 (Baseline):** A naive, unconstrained single-instruction summarization prompt.
2. **Version 2 (Structured Instructions):** Introduction of explicit academic section headings, format boundaries, and extraction constraints.
3. **Version 3 (Context & Role Refinement):** Establishing the persona of an undergraduate research mentor, introducing anti-hallucination negative constraints, and pedagogical mechanisms (ELI5 analogies, jargon glossaries).
4. **Version 4 (Final 3-Prompt Chained Workflow):** Complete architectural transition from a single monolithic prompt into an auditable, sequential 3-stage prompt pipeline:
   - **Stage 1:** Research Information Extraction (`prompt_1_extraction.txt`)
   - **Stage 2:** Student-Friendly Structured Summary (`prompt_2_summary.txt`)
   - **Stage 3:** Source-Based Verification Audit (`prompt_3_verification.txt`)

Each prompt version was tested against the same standardized baseline input: the landmark natural language processing paper *"LoRA: Low-Rank Adaptation of Large Language Models"* (Hu et al., 2021; 6,569 characters). Below are the full logs of each version.

---

## Prompt Version 1: Baseline (Unconstrained Instruction)

### 1. Version Information
- **Version Identifier:** `v1_baseline`
- **Date of Implementation:** November 14, 2026
- **Architecture:** Single-turn monolithic prompt
- **Prompt File:** `prompts/prompt_versions/v1_baseline.txt`

### 2. Exact Prompt Template
```text
Summarize the following research paper in simple and plain language:

"""
{paper_text}
"""
```

### 3. Rationale & Changes
- **What was implemented:** A minimal zero-shot directive instructing the model to summarize the provided paper text in plain English.
- **Why this was chosen:** Establishes an empirical baseline for standard LLM behavior prior to prompt engineering intervention.
- **Expected Improvement:** Produce a brief, readable overview of the research paper.

### 4. Actual Observations from Execution
- **Output Characteristics:** Generated a generic 3-paragraph summary. While grammatically fluent, the summary merged problem statements, methodology, and results into loose prose.
- **Failure Modes & Omissions:**
  - Omitted explicit mathematical formulation of Low-Rank Adaptation ($W = W_0 + B \times A$).
  - Missed crucial quantitative metrics: omitted the 10,000x parameter reduction and 3x GPU memory savings.
  - Completely omitted the authors' stated limitations (inability to easily batch different tasks with distinct LoRA weights in a single forward pass).
  - Lacked structured navigational headings for student reference.
- **Limitations:** Highly non-deterministic; high risk of hallucinating numbers; no accountability for missing paper elements.
- **Status:** **REPLACED.** Inadequate for structured undergraduate learning and factual verification.

---

## Prompt Version 2: Structured Instructions (Sectional Constraints)

### 1. Version Information
- **Version Identifier:** `v2_structured`
- **Date of Implementation:** November 16, 2026
- **Architecture:** Single-turn structured prompt
- **Prompt File:** `prompts/prompt_versions/v2_structured.txt`

### 2. Exact Prompt Template
```text
Summarize this academic paper for an undergraduate student.

Please include the following sections:
1. Title and Objective
2. Problem Statement
3. Methodology
4. Key Findings and Quantitative Results
5. Limitations
6. Conclusion

Paper:
"""
{paper_text}
"""
```

### 3. Rationale & Changes
- **What was changed:** Added 6 explicit section headings, defined the target audience as undergraduate students, and specifically requested quantitative results and limitations.
- **Why the change was made:** To eliminate unstructured prose blobs and force the model to categorize information into standardized academic dimensions.
- **Expected Improvement:** Uniform output format, explicit capture of quantitative gains, and dedicated focus on paper limitations.

### 4. Actual Observations from Execution
- **Output Characteristics:** Successfully generated the 6 specified sections. Quantitative figures (10,000x parameter reduction, 3x memory reduction) were now captured under Section 4.
- **Failure Modes & Omissions:**
  - When tested on incomplete texts (e.g., papers lacking an explicit limitations section), the prompt encouraged the model to invent plausible limitations (e.g., "The model might struggle on low-resource languages") that were nowhere in the source paper.
  - Explanations of complex linear algebra concepts (rank decomposition, intrinsic dimension) remained too dense for beginner undergraduates.
  - No mechanism existed to verify whether the cited numbers actually came from the text or from the model's pre-trained knowledge base.
- **Limitations:** Susceptible to ungrounded extrapolation when sections are missing in the source text.
- **Status:** **REPLACED.** Improved structure, but failed anti-hallucination and beginner accessibility criteria.

---

## Prompt Version 3: Context & Role Refinement (Audience & Negative Guardrails)

### 1. Version Information
- **Version Identifier:** `v3_role_refined`
- **Date of Implementation:** November 18, 2026
- **Architecture:** Single-turn persona-guided prompt with negative constraints
- **Prompt File:** `prompts/prompt_versions/v3_role_refined.txt`

### 2. Exact Prompt Template
```text
You are an expert academic research assistant helping undergraduate computer science and engineering students understand scholarly publications.

Read the following research paper carefully and generate a structured summary.

Rules:
1. Do not invent or assume information. If a detail (like dataset size or limitation) is missing in the paper text, explicitly state "Not specified in the provided text."
2. Write in accessible language without losing technical precision.
3. Include an "Explain Like I'm a Beginner" analogy and a technical glossary.

Required Sections:
- Paper Overview
- Research Motivation & Problem
- Methodology & Architecture
- Experimental Results & Key Findings
- Explicit Limitations
- Future Work
- Beginner Explanation (Analogy)
- Key Terminology Glossary

Source Paper:
"""
{paper_text}
"""
```

### 3. Rationale & Changes
- **What was changed:**
  - Assigned a dedicated system persona: *"expert academic research assistant"*.
  - Introduced strict negative constraints: *"If a detail is missing, explicitly state 'Not specified in the provided text.'"*
  - Added pedagogical sections: an *"Explain Like I'm a Beginner"* analogy (ELI5) and a *"Key Terminology Glossary"* (Jargon Buster).
- **Why the change was made:** To suppress hallucinated extrapolation when processing incomplete papers, and to actively translate esoteric machine learning jargon into intuitive mental models for students.
- **Expected Improvement:** Complete elimination of invented limitations, clear beginner analogies, and structured terminology definitions.

### 4. Actual Observations from Execution
- **Output Characteristics:** Marked qualitative improvement. The beginner analogy (comparing LoRA to attaching sticky notes inside a textbook instead of reprinting the entire encyclopedia) was immediately intuitive. Incomplete test cases correctly stated *"Not specified in the provided text"* for missing limitations.
- **Failure Modes & Omissions:**
  - **Single-prompt cognitive load bottleneck:** Asking the model to simultaneously extract facts, re-explain them simply, maintain strict fidelity, and format analogies in a single context window resulted in occasional subtle factual drifting. For instance, the prompt occasionally mischaracterized rank $r$ as a percentage rather than an integer dimension.
  - Still lacked an objective, verifiable audit trail. Students had no way of knowing which sentences in the summary were backed by direct paper quotes.
- **Limitations:** A single prompt cannot simultaneously serve as author, teacher, and rigorous auditor without compromise.
- **Status:** **REPLACED.** Led directly to the realization that extraction, pedagogical synthesis, and source verification must be decoupled into separate prompt stages.

---

## Prompt Version 4: Final 3-Prompt Chained Workflow (Extraction, Synthesis & Verification)

### 1. Version Information
- **Version Identifier:** `v4_chained_workflow`
- **Date of Implementation:** November 20–22, 2026
- **Architecture:** Sequential 3-stage prompt chain with adversarial verification audit
- **Active Prompt Files:**
  - `prompts/prompt_1_extraction.txt` (Stage 1: Research Information Extraction)
  - `prompts/prompt_2_summary.txt` (Stage 2: Student-Friendly Structured Summary)
  - `prompts/prompt_3_verification.txt` (Stage 3: Source-Based Verification Audit)

### 2. Stage-by-Stage Architecture and Prompts

#### Stage 1: Research Information Extraction (`prompts/prompt_1_extraction.txt`)
- **Input:** Extracted raw paper text.
- **Output:** 12 structured fields (Problem, Objective, Questions, Methodology, Datasets, Key Findings, Quantitative Metrics, Limitations, Future Work, Conclusion, Evidence Quotes, Ambiguities).
- **Core Guardrail:** Strict grounding constraint: *"If any field is missing or not explicitly discussed in the source text, state exactly: 'Not specified in the provided text.' Do NOT extrapolate, speculate, or invent numbers."*

#### Stage 2: Student-Friendly Structured Summary (`prompts/prompt_2_summary.txt`)
- **Input:** Factual output from Stage 1 + raw source excerpt context.
- **Output:** 11-section comprehensive student guide (Executive Overview, The Big Picture, Objectives, How It Works, Dataset/Setup, Key Findings, Honest Limitations, Future Directions, Takeaway, Beginner Analogy ELI5, Technical Glossary).
- **Core Guardrail:** Strict fidelity to Stage 1 extracted facts; zero new unsupported claims introduced.

#### Stage 3: Source-Based Verification Audit (`prompts/prompt_3_verification.txt`)
- **Input:** Original paper text + Generated Stage 2 summary.
- **Output:**
  - Claims Verification Table with 4 standardized labels: `[SUPPORTED]`, `[PARTIALLY SUPPORTED]`, `[UNSUPPORTED]`, `[NOT VERIFIABLE]`.
  - Verbatim source quotes for each claim.
  - Discrepancy analysis and suggested corrections.
  - Quantitative audit metrics (Supported count, Partially supported count, Unsupported count, Grounding Confidence Score %).
  - Critical student warnings and mandatory truth disclaimer.

### 3. Rationale & Changes
- **Why the change was made:** Decouples factual extraction from creative pedagogical communication. By isolating extraction in Stage 1, synthesis in Stage 2, and adversarial auditing in Stage 3, each prompt specializes in a single cognitive task.
- **Expected Improvement:** Maximum factual grounding, auditable evidence trail, student-friendly clarity, and transparent detection of any hallucination or discrepancy.

### 4. Actual Observations from Execution
- **Tested Input:** `sample_data/sample_paper_1_lora.txt` (LoRA paper).
- **Execution Results:**
  - **Stage 1 Output:** Extracted all 12 fields cleanly, capturing the 10,000x parameter reduction, 3x GPU VRAM savings, and verbatim quotes.
  - **Stage 2 Output:** Generated 11 comprehensive student sections with an ELI5 sticky-note analogy and 3-term technical glossary.
  - **Stage 3 Output:** Audited 5 major claims:
    * Claim 1 (Low-rank matrix injection): `[SUPPORTED]` — corroborated by Section 3.
    * Claim 2 (10,000x parameter reduction): `[SUPPORTED]` — corroborated by Section 5.
    * Claim 3 (3x GPU memory reduction): `[SUPPORTED]` — corroborated by Section 5.
    * Claim 4 (Evaluated on RoBERTa, DeBERTa, GPT-2/3): `[SUPPORTED]` — corroborated by Section 4.
    * Claim 5 (Multi-task batching limitation): `[SUPPORTED]` — corroborated by Section 6.
    * **Grounding Confidence Score:** **100.0%**.
- **Tested Edge Case:** `sample_data/sample_paper_3_incomplete.txt` (Missing limitations).
  - Correctly identified absence of limitations in Stage 1 (`"Not specified in the provided text."`), carried it faithfully through Stage 2, and Stage 3 assigned `[PARTIALLY SUPPORTED]` with a note explaining the missing limitation in the source text.
- **Status:** **RETAINED AS FINAL SYSTEM WORKFLOW.**

---

## Comparison Summary Across Iteration Versions

| Evaluation Dimension | Version 1 (Baseline) | Version 2 (Structured) | Version 3 (Role Refined) | Version 4 (Final Chained Workflow) |
|---|---|---|---|---|
| **Prompt Architecture** | Single zero-shot prompt | Single structured prompt | Single role/constraint prompt | **3-Stage Sequential Pipeline** |
| **Number of Prompts** | 1 | 1 | 1 | **3 (Extraction, Summary, Verification)** |
| **Sectional Organization** | None (unstructured prose) | 6 basic sections | 8 academic sections | **11 comprehensive student sections** |
| **Pedagogical Features** | None | Student-targeted tone | ELI5 analogy & Glossary | **ELI5 analogy, Jargon Buster, Big Picture** |
| **Handling Missing Info** | Hallucinates or omits | Often hallucinates | States "Not specified" | **Enforces strict negative constraint across chain** |
| **Quantitative Precision** | Omitted specific metrics | Partially captured | Captured in results section | **Directly extracted & verified with exact quotes** |
| **Source Grounding Check** | None | None | None | **Automated Claim-by-Claim Adversarial Audit** |
| **Audit Metrics Output** | None | None | None | **Grounding Score %, Claims Table, Warnings** |
| **Developer Transparency** | None | None | None | **Full prompt & output execution trace inspector** |
| **Final Disposition** | Replaced | Replaced | Replaced | **RETAINED IN PRODUCTION** |
