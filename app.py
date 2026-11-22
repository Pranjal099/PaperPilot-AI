"""
PaperPilot AI - Research Paper Summarizer Using Prompt Engineering
Team: Token Titans (Team ID: PE-B49-56)
Batch: B49–B64 | Course: SCSE4041 Prompt Engineering
Team Leader: Aayushi Nagar | Team Member: Pranjal
"""

import os
import streamlit as st
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv

from src.validation import validate_pasted_text, validate_pdf_upload
from src.pdf_processing import extract_text_from_pdf_bytes
from src.ai_service import AIService
from src.verification import parse_verification_output, format_status_badge

# Load environment
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="PaperPilot AI | Research Paper Summarizer",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Styling (Academic Theme)
st.markdown(
    """
    <style>
    /* Main container styling */
    .main {
        background-color: #F8FAFC;
    }
    .stApp {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    /* Header card */
    .hero-card {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        color: #FFFFFF;
        padding: 2.2rem 2.4rem;
        border-radius: 14px;
        margin-bottom: 1.8rem;
        border-left: 6px solid #4F46E5;
        box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    }
    .hero-title {
        font-size: 2.3rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        margin: 0;
        color: #F8FAFC;
    }
    .hero-subtitle {
        font-size: 1.1rem;
        font-weight: 400;
        color: #94A3B8;
        margin-top: 0.5rem;
        margin-bottom: 0.8rem;
    }
    .badge-pill {
        display: inline-block;
        background-color: #312E81;
        color: #C7D2FE;
        font-size: 0.8rem;
        font-weight: 600;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        margin-right: 0.5rem;
        border: 1px solid #4338CA;
    }
    /* Section cards */
    .metric-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 1.2rem;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1E293B;
    }
    .metric-label {
        font-size: 0.85rem;
        color: #64748B;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 0.05em;
    }
    /* Trace code block */
    .trace-box {
        background-color: #0F172A;
        color: #E2E8F0;
        padding: 1rem;
        border-radius: 8px;
        font-family: monospace;
        font-size: 0.85rem;
        max-height: 380px;
        overflow-y: auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def load_sample_file(filename: str) -> str:
    """Helper to load sample text from sample_data/"""
    sample_path = Path(__file__).resolve().parent / "sample_data" / filename
    if sample_path.exists():
        return sample_path.read_text(encoding="utf-8")
    return ""


# Initialize session state variables
if "summary_result" not in st.session_state:
    st.session_state.summary_result = None
if "input_text" not in st.session_state:
    st.session_state.input_text = ""
if "source_metadata" not in st.session_state:
    st.session_state.source_metadata = {}


# Sidebar Controls & Information
with st.sidebar:
    st.image("https://img.icons8.com/isometric/100/graduation-cap.png", width=64)
    st.title("PaperPilot AI")
    st.caption("Prompt-Engineered Academic Paper Summarizer")

    st.markdown("---")
    st.markdown("### 👥 Team Details")
    st.markdown("**Team:** Token Titans (`PE-B49-56`)")
    st.markdown("**Batch:** B49–B64")
    st.markdown("**Course:** SCSE4041 — Prompt Engineering")
    st.markdown("**Team Leader:** Aayushi Nagar")
    st.markdown("**Team Member:** Pranjal")
    st.markdown("**Problem ID:** C15 — Research Paper Summariser for Students")

    st.markdown("---")
    st.markdown("### ⚙️ API Configuration")
    env_api_key = os.getenv("GEMINI_API_KEY", "")
    user_api_key = st.text_input(
        "Google Gemini API Key",
        value=env_api_key,
        type="password",
        help="Optional. Enter your Gemini API key from Google AI Studio. If left empty, the application runs in verified Offline Simulation Mode for demonstration and testing.",
    )

    selected_model = st.selectbox(
        "Gemini Model",
        options=["gemini-1.5-flash", "gemini-2.0-flash", "gemini-1.5-pro"],
        index=0,
        help="Select Google Gemini model for live inference. gemini-1.5-flash is fast, reliable, and recommended.",
    )

    if user_api_key:
        st.success("🟢 Gemini API Key Active (Live Inferences)")
    else:
        st.info("ℹ️ Offline Heuristic Mode Active (No Key Set)")

    st.markdown("---")
    st.markdown("### 📚 Load Sample Papers")
    st.caption("Click to load pre-verified benchmark academic papers:")

    col_s1, col_s2 = st.columns(2)
    with col_s1:
        if st.button("📄 LoRA Paper", use_container_width=True):
            st.session_state.input_text = load_sample_file("sample_paper_1_lora.txt")
            st.session_state.source_metadata = {"source": "Sample: LoRA (Hu et al., 2021)", "chars": len(st.session_state.input_text)}
            st.rerun()

    with col_s2:
        if st.button("📄 RAG Paper", use_container_width=True):
            st.session_state.input_text = load_sample_file("sample_paper_2_rag.txt")
            st.session_state.source_metadata = {"source": "Sample: RAG (Lewis et al., 2020)", "chars": len(st.session_state.input_text)}
            st.rerun()

    if st.button("⚠️ Incomplete Paper (Edge Case Test)", use_container_width=True):
        st.session_state.input_text = load_sample_file("sample_paper_3_incomplete.txt")
        st.session_state.source_metadata = {"source": "Sample: FastGraph (Missing Limitations)", "chars": len(st.session_state.input_text)}
        st.rerun()

    st.markdown("---")
    if st.button("🔄 Reset Application", use_container_width=True):
        st.session_state.summary_result = None
        st.session_state.input_text = ""
        st.session_state.source_metadata = {}
        st.rerun()


# Main Application View
st.markdown(
    """
    <div class="hero-card">
        <h1 class="hero-title">PaperPilot AI 🎓</h1>
        <p class="hero-subtitle">Intelligent Research Paper Summarization & Source Verification for Undergraduate Students</p>
        <div>
            <span class="badge-pill">Milestone 2</span>
            <span class="badge-pill">3-Stage Prompt Chaining</span>
            <span class="badge-pill">Source Verification</span>
            <span class="badge-pill">Anti-Hallucination Guardrails</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Workflow Explainer Banner
with st.expander("ℹ️ How PaperPilot AI Works (The 3-Stage Prompt Chaining Workflow)", expanded=False):
    st.markdown(
        """
        PaperPilot AI uses a **strictly sequenced 3-stage prompt engineering workflow** to eliminate hallucinations and produce student-ready explanations:
        
        1. **Stage 1: Research Information Extraction (`prompt_1_extraction.txt`)**
           - Scans the paper text for 12 structured dimensions (problem, objective, methodology, datasets, quantitative metrics, explicit limitations, and verbatim quotes).
           - Enforces zero speculation: absent fields are tagged strictly as *"Not specified in the provided text."*
        2. **Stage 2: Student-Friendly Structured Summary (`prompt_2_summary.txt`)**
           - Transforms extracted research facts into an accessible, engaging guide.
           - Adds beginner analogies (*"Explain Like I'm a Beginner"*) and an undergraduate jargon buster.
        3. **Stage 3: Source-Based Verification (`prompt_3_verification.txt`)**
           - Adversarially audits every major factual claim in the summary against the original source text.
           - Classifies claims as **[SUPPORTED]**, **[PARTIALLY SUPPORTED]**, **[UNSUPPORTED]**, or **[NOT VERIFIABLE]**.
           - Highlights discrepancies, suggests corrections, and computes an overall Grounding Confidence Score.
        """
    )


# Input Section: PDF or Pasted Text
st.subheader("1. Provide Research Paper")

input_method = st.radio(
    "Choose Input Method:",
    options=["Upload PDF Document", "Paste Paper Text"],
    horizontal=True,
)

paper_text_to_process = ""
extraction_diagnostics = {}

if input_method == "Upload PDF Document":
    uploaded_file = st.file_uploader(
        "Upload a Research Paper PDF (Max 15MB)",
        type=["pdf"],
        help="Select a digital academic paper PDF. Scanned images without OCR will be flagged.",
    )

    if uploaded_file is not None:
        file_bytes = uploaded_file.read()
        is_pdf_valid, pdf_msg, pdf_meta = validate_pdf_upload(file_bytes, uploaded_file.name)

        if not is_pdf_valid:
            st.error(f"❌ PDF Validation Error: {pdf_msg}")
        else:
            with st.spinner("Extracting text from PDF using PyMuPDF..."):
                pdf_result = extract_text_from_pdf_bytes(file_bytes)

            if not pdf_result["success"]:
                st.error(f"❌ Extraction Error: {pdf_result['error']}")
                if pdf_result.get("is_scanned"):
                    st.warning("💡 Tip: Scanned PDFs require OCR preprocessing before text can be extracted. You can also copy and paste the paper text directly into the 'Paste Paper Text' tab.")
            else:
                paper_text_to_process = pdf_result["text"]
                extraction_diagnostics = {
                    "source": f"PDF: {uploaded_file.name}",
                    "pages": pdf_result["page_count"],
                    "characters": pdf_result["char_count"],
                    "words": len(paper_text_to_process.split()),
                }
                st.success(
                    f"✅ Successfully extracted {extraction_diagnostics['characters']:,} characters "
                    f"({extraction_diagnostics['words']:,} words) across {extraction_diagnostics['pages']} page(s)."
                )

                with st.expander("Preview Extracted Raw Text", expanded=False):
                    st.text_area("Extracted Text Preview", paper_text_to_process[:2000] + "...", height=160, disabled=True)

else:
    pasted_text_input = st.text_area(
        "Paste Research Paper Text (Abstract, Methodology, Results, Discussion):",
        value=st.session_state.input_text,
        height=240,
        placeholder="Paste academic paper content here (minimum 100 characters)...",
    )
    if pasted_text_input:
        paper_text_to_process = pasted_text_input
        extraction_diagnostics = {
            "source": st.session_state.source_metadata.get("source", "Pasted Text"),
            "characters": len(paper_text_to_process),
            "words": len(paper_text_to_process.split()),
        }


# Summarization Action Button
st.markdown("---")
col_btn1, col_btn2 = st.columns([1, 4])
with col_btn1:
    summarize_clicked = st.button("🚀 Run PaperPilot AI", type="primary", use_container_width=True)

if summarize_clicked:
    # Validate input text
    is_valid, validation_msg, text_meta = validate_pasted_text(paper_text_to_process)
    if not is_valid:
        st.error(f"❌ Input Validation Failed: {validation_msg}")
    else:
        ai_service = AIService(api_key=user_api_key, model_name=selected_model)

        progress_bar = st.progress(0, text="Initializing 3-Stage Prompt Chaining Pipeline...")
        status_box = st.empty()

        try:
            # Stage 1: Extraction
            status_box.info("🔍 [Stage 1/3] Executing Research Information Extraction Prompt...")
            progress_bar.progress(25, text="Stage 1: Extracting research objective, methods, metrics & limitations...")
            stage1 = ai_service.run_stage_1_extraction(paper_text_to_process)

            # Stage 2: Synthesis
            status_box.info("✍️ [Stage 2/3] Executing Student-Friendly Structured Summary Prompt...")
            progress_bar.progress(60, text="Stage 2: Synthesizing plain-English explanations & beginner analogies...")
            stage2 = ai_service.run_stage_2_summary(stage1["output_text"], paper_text_to_process)

            # Stage 3: Verification
            status_box.info("🛡️ [Stage 3/3] Executing Source-Based Verification Audit Prompt...")
            progress_bar.progress(85, text="Stage 3: Cross-examining summary claims against source text...")
            stage3 = ai_service.run_stage_3_verification(paper_text_to_process, stage2["output_text"])

            progress_bar.progress(100, text="Pipeline Execution Complete!")
            status_box.empty()

            # Store result in session state
            st.session_state.summary_result = {
                "stage1": stage1,
                "stage2": stage2,
                "stage3": stage3,
                "verification_parsed": parse_verification_output(stage3["output_text"]),
                "source_diagnostics": extraction_diagnostics,
                "paper_text": paper_text_to_process,
                "is_mock": stage1["is_mock"] or stage2["is_mock"] or stage3["is_mock"],
                "api_error": stage1.get("error") or stage2.get("error") or stage3.get("error"),
                "model_used": stage1["model_used"],
            }
            st.success("✅ Summarization and source verification finished successfully!")

        except Exception as e:
            status_box.empty()
            progress_bar.empty()
            st.error(f"❌ An error occurred during pipeline execution: {str(e)}")


# Display Results
if st.session_state.summary_result:
    res = st.session_state.summary_result
    st.markdown("---")
    st.subheader("2. Summary & Verification Results")

    # Banner distinguishing live vs offline simulation mode
    if res["is_mock"]:
        if res.get("api_error"):
            st.error(
                f"❌ **Gemini API Error Encountered:**\n\n`{res['api_error']}`\n\n"
                "⚠️ **Pipeline Fallback:** PaperPilot AI automatically switched to the Offline Heuristic Simulation pipeline to prevent a crash. "
                "Please verify your GEMINI_API_KEY, network connectivity, and model selection in the sidebar."
            )
        else:
            st.warning(
                "⚠️ **Evaluation Notice: Offline Simulation Mode Active**\n\n"
                "Because no live `GEMINI_API_KEY` was configured, PaperPilot AI ran its built-in deterministic heuristic simulation pipeline. "
                "All three stages were strictly exercised. To connect live Gemini API inferences, enter an API key in the sidebar or `.env` file."
            )
    else:
        st.success(
            f"🟢 **Live Google Gemini API Integration Active**\n\n"
            f"All 3 prompt stages were executed live using **Model: `{res['model_used']}`** via the official Google GenAI SDK. "
            "Authentic LLM inferences were generated with zero simulation or mock data."
        )

    # Top Audit Metrics Row
    v_metrics = res["verification_parsed"]["metrics"]
    m_col1, m_col2, m_col3, m_col4, m_col5 = st.columns(5)
    with m_col1:
        st.markdown(
            f"""<div class="metric-card">
                <div class="metric-value">{v_metrics['confidence_score']}%</div>
                <div class="metric-label">Grounding Score</div>
            </div>""",
            unsafe_allow_html=True,
        )
    with m_col2:
        st.markdown(
            f"""<div class="metric-card">
                <div class="metric-value">{v_metrics['total_claims']}</div>
                <div class="metric-label">Claims Audited</div>
            </div>""",
            unsafe_allow_html=True,
        )
    with m_col3:
        st.markdown(
            f"""<div class="metric-card">
                <div class="metric-value" style="color: #059669;">{v_metrics['supported']}</div>
                <div class="metric-label">Supported</div>
            </div>""",
            unsafe_allow_html=True,
        )
    with m_col4:
        st.markdown(
            f"""<div class="metric-card">
                <div class="metric-value" style="color: #D97706;">{v_metrics['partially_supported']}</div>
                <div class="metric-label">Partially Supported</div>
            </div>""",
            unsafe_allow_html=True,
        )
    with m_col5:
        st.markdown(
            f"""<div class="metric-card">
                <div class="metric-value" style="color: #DC2626;">{v_metrics['unsupported']}</div>
                <div class="metric-label">Unsupported</div>
            </div>""",
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # Result Tabs
    tab_summary, tab_verification, tab_extraction, tab_developer_trace = st.tabs([
        "📖 Student-Friendly Summary",
        "🛡️ Source Verification Audit",
        "🔬 Structured Extraction (Stage 1)",
        "💻 Prompt Execution Traces",
    ])

    with tab_summary:
        st.markdown(res["stage2"]["output_text"])

        st.markdown("---")
        # Download summary
        summary_download_text = f"""# PaperPilot AI Summary Report
Generated by PaperPilot AI (Team Token Titans - PE-B49-56)
Source: {res['source_diagnostics'].get('source', 'Academic Paper')}

{res['stage2']['output_text']}

---
## Factual Grounding Verification
Grounding Confidence Score: {v_metrics['confidence_score']}%
Supported Claims: {v_metrics['supported']} / {v_metrics['total_claims']}
Disclaimer: {res['verification_parsed']['disclaimer']}
"""
        st.download_button(
            label="📥 Download Summary (Markdown)",
            data=summary_download_text,
            file_name="PaperPilot_AI_Summary.md",
            mime="text/markdown",
        )

    with tab_verification:
        st.markdown("### 🛡️ Source-Based Claims Audit")
        st.caption("Each major factual claim in the generated summary is rigorously matched against original paper text snippets.")

        claims = res["verification_parsed"]["claims"]
        if claims:
            table_rows = []
            for c in claims:
                table_rows.append({
                    "Claim #": c["claim_num"],
                    "Summary Claim": c["summary_claim"],
                    "Status": c["status"],
                    "Source Evidence Quote": c["evidence"][:180] + ("..." if len(c["evidence"]) > 180 else ""),
                    "Suggested Correction / Discrepancy": c["correction"] if c["correction"] else "Verified consistent.",
                })
            df_claims = pd.DataFrame(table_rows)
            st.dataframe(df_claims, use_container_width=True, hide_index=True)

            st.markdown("#### Claim Details & Evidence")
            for c in claims:
                with st.expander(f"Claim {c['claim_num']}: {format_status_badge(c['status'])} {c['summary_claim'][:90]}..."):
                    st.markdown(f"**Exact Claim:** {c['summary_claim']}")
                    st.markdown(f"**Verification Status:** {format_status_badge(c['status'])}")
                    st.markdown(f"**Source Text Evidence:** *\"{c['evidence']}\"*")
                    if c["correction"]:
                        st.markdown(f"**Discrepancy / Suggested Correction:** {c['correction']}")
        else:
            st.markdown(res["stage3"]["output_text"])

        # Warnings and disclaimer
        if res["verification_parsed"]["critical_warnings"]:
            st.warning("⚠️ **Student Verification Warnings:**\n" + "\n".join([f"- {w}" for w in res["verification_parsed"]["critical_warnings"]]))

        st.info(f"ℹ️ **Ground Truth Disclaimer:** {res['verification_parsed']['disclaimer']}")

    with tab_extraction:
        st.markdown("### 🔬 Stage 1: Structured Information Extraction")
        st.caption("Raw factual extraction output generated directly by `prompt_1_extraction.txt` before student-friendly synthesis.")
        st.markdown(res["stage1"]["output_text"])

    with tab_developer_trace:
        st.markdown("### 💻 Developer & Evaluation Section: 3-Prompt Execution Trace")
        st.caption("Full transparency into each prompt stage executed in the pipeline.")

        for stage_data in [res["stage1"], res["stage2"], res["stage3"]]:
            st.markdown(f"#### Stage {stage_data['stage']}: {stage_data['stage_name']}")
            trace_col1, trace_col2, trace_col3, trace_col4 = st.columns(4)
            with trace_col1:
                st.caption(f"**Template File:** `{stage_data['prompt_file']}`")
            with trace_col2:
                st.caption(f"**Model Used:** `{stage_data['model_used']}`")
            with trace_col3:
                mode_label = "🟡 Offline Simulation" if stage_data.get("is_mock") else "🟢 Live Gemini API"
                st.caption(f"**Execution Mode:** {mode_label}")
            with trace_col4:
                st.caption(f"**Execution Time:** `{stage_data['elapsed_seconds']}s`")

            with st.expander(f"Inspect Rendered Prompt ({stage_data['stage_name']})", expanded=False):
                st.code(stage_data["rendered_prompt"][:1500] + "\n...[truncated for display]", language="text")

            with st.expander(f"Inspect Raw Output ({stage_data['stage_name']})", expanded=False):
                st.code(stage_data["output_text"][:2000] + "\n...[truncated for display]", language="markdown")
            st.markdown("---")
