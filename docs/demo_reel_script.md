# PaperPilot AI — 120-Second Demonstration Reel Script

**Project Title:** PaperPilot AI: Research Paper Summarizer Using Prompt Engineering  
**Team Name:** Token Titans (`PE-B49-56`)  
**Problem ID:** C15 — Research Paper Summariser for Students  
**Course:** SCSE4041 — Prompt Engineering | **Milestone 2**  
**Target Duration:** Exactly 120 Seconds (Allowed window: 90 to 150 seconds)  
**Status:** **[READY FOR RECORDING — NOT YET RECORDED]**  

---

## Production & Recording Notes for Presenter
- **Screen Setup:** Full screen browser displaying `http://localhost:8501` at 100% zoom.
- **Audio:** Clear microphone audio, speaking at a measured, enthusiastic, professional academic pace.
- **Mouse Movement:** Smooth, deliberate cursor movements highlighting UI cards, badges, and tabs.
- **Video Resolution:** 1080p (1920x1080) at 30 fps or 60 fps.

---

## Detailed Video Timeline & Script

```
====================================================================================================
TIMELINE (0:00 - 0:10) | PART 1: INTRODUCTION & PROBLEM STATEMENT
====================================================================================================
Visual on Screen:
- Open on the PaperPilot AI Streamlit hero header.
- Cursor hovers smoothly over the title "PaperPilot AI 🎓" and badges: "Milestone 2", "3-Stage Prompt Chaining", "Source Verification".
- Brief camera shot of the sidebar showing Team Token Titans (PE-B49-56), Aayushi Nagar & Pranjal.

Voiceover (Speaker):
"Hello evaluators! We are Team Token Titans, presenting PaperPilot AI—an intelligent research paper summarizer engineered specifically for undergraduate students tackling complex academic papers."

====================================================================================================
TIMELINE (0:10 - 0:25) | PART 2: PAPER INPUT & PDF PROCESSING MODULE
====================================================================================================
Visual on Screen:
- Switch to "Upload PDF Document" tab or click the quick-load button: "LoRA Paper".
- The UI instantly displays the successful extraction banner:
  "✅ Successfully extracted 6,569 characters (850 words) across 2 page(s)."
- Click "Preview Extracted Raw Text" to show clean digital extraction using PyMuPDF.

Voiceover (Speaker):
"Traditional summaries often overwhelm students or hallucinate nonexistent claims. PaperPilot AI accepts either pasted paper text or digital PDFs. Behind the scenes, PyMuPDF extracts clean text, detects scanned images, and strictly validates input length."

====================================================================================================
TIMELINE (0:25 - 0:55) | PART 3: SUMMARIZATION & PROMPT STAGES 1 & 2
====================================================================================================
Visual on Screen:
- Click the primary action button: "🚀 Run PaperPilot AI".
- The animated progress bar steps through:
  * Stage 1: Extracting research objective, methods, metrics & limitations...
  * Stage 2: Synthesizing plain-English explanations & beginner analogies...
  * Stage 3: Cross-examining summary claims against source text...
- Click on the "📖 Student-Friendly Summary" tab.
- Scroll down to showcase:
  * Section 6: Key Findings & Quantitative Results (10,000x parameter reduction, 3x GPU savings).
  * Section 7: Honest Limitations.
  * Section 10: "Explain Like I'm a Beginner" (the intuitive encyclopedia sticky-note analogy).
  * Section 11: Technical Glossary (Jargon Buster).

Voiceover (Speaker):
"With one click, our multi-step prompt pipeline springs into action. Rather than a generic summary, the student receives eleven clearly labeled sections. Notice the quantitative precision: our Stage 1 prompt strictly extracted exact numbers—like a 10,000-fold parameter reduction—while Stage 2 synthesized an intuitive 'Explain Like I'm a Beginner' sticky-note analogy and a technical jargon buster."

====================================================================================================
TIMELINE (0:55 - 1:15) | PART 4: SOURCE-BASED VERIFICATION AUDIT (STAGE 3)
====================================================================================================
Visual on Screen:
- Click on the "🛡️ Source Verification Audit" tab.
- The screen highlights the top metric cards:
  * Grounding Score: 100.0%
  * Claims Audited: 5
  * Supported: 5 (Green)
  * Unsupported: 0
- Showcase the Claims Verification Table with green `[SUPPORTED]` badges.
- Expand Claim 1 and Claim 2 to reveal verbatim source quotes matched directly against the paper text.
- Highlight the Ground Truth Disclaimer at the bottom.

Voiceover (Speaker):
"Here is where prompt engineering truly protects the student: Stage 3 acts as an adversarial auditor. It extracts each factual claim, searches the original text, and classifies it as Supported, Partially Supported, or Unsupported with verbatim quote evidence. We also provide a Grounding Confidence Score and an explicit truth disclaimer."

====================================================================================================
TIMELINE (1:15 - 1:35) | PART 5: PROMPT CHAINING & ITERATION LOG
====================================================================================================
Visual on Screen:
- Click on the "💻 Prompt Execution Traces" tab.
- Expand Stage 1, Stage 2, and Stage 3 to show the exact rendered prompt templates, execution latency, and token outputs.
- Briefly show the `docs/prompt_iteration_log.md` document on screen, showing the progression from Version 1 baseline to Version 4 chained pipeline.

Voiceover (Speaker):
"In our Developer Trace section, evaluators can inspect every prompt stage executed live. In our iteration log, we documented four genuine versions—evolving from an unconstrained baseline to structured instructions, role refinements, and ultimately our decoupled 3-prompt architecture."

====================================================================================================
TIMELINE (1:35 - 1:50) | PART 6: COMPREHENSIVE TESTING EVIDENCE
====================================================================================================
Visual on Screen:
- Bring up terminal showing `pytest` execution:
  `27 passed in 0.91s`.
- Show the 14-case test matrix in `docs/test_cases.md`, highlighting edge cases:
  * TC-03: Missing limitations detected without hallucination.
  * TC-08: Corrupted PDF rejected.
  * TC-09: Scanned PDF flagged.
  * TC-12: Unsupported claim detection.

Voiceover (Speaker):
"We backed our implementation with rigorous testing: 27 automated unit tests passed at 100%, and a comprehensive 14-case test matrix covering edge cases, corrupted PDFs, missing sections, and adversarial claim detection."

====================================================================================================
TIMELINE (1:50 - 2:00) | PART 7: CONCLUSION & SUMMARY DOWNLOAD
====================================================================================================
Visual on Screen:
- Return to the main summary tab.
- Click the "📥 Download Summary (Markdown)" button to show the downloaded file.
- Pan out to the PaperPilot AI header with team details.

Voiceover (Speaker):
"Students can download their verified summary in Markdown with a single click. PaperPilot AI makes academic research transparent, verifiable, and student-ready. Thank you!"
====================================================================================================
```
