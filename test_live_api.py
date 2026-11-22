"""
Live Gemini API Integration Test Script for PaperPilot AI.
Extracts text from sample_data/sample_paper_1_lora.pdf,
executes all 3 prompt stages against Google Gemini API,
and validates that authentic LLM inferences are generated with 0 mock data.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load .env
load_dotenv()

from src.ai_service import AIService, mask_api_key
from src.pdf_processing import extract_text_from_pdf_path
from src.verification import parse_verification_output


def run_live_test():
    api_key = os.getenv("GEMINI_API_KEY", "").strip()

    print("=" * 70)
    print("PaperPilot AI — Live Gemini API Verification Test")
    print("=" * 70)

    if not api_key:
        print("\n❌ GEMINI_API_KEY is not set.")
        print("\nTo test live Gemini API inferences:")
        print("1. Get an API key from Google AI Studio: https://aistudio.google.com/")
        print("2. Set it in .env file in the workspace:")
        print("   GEMINI_API_KEY=AIzaSy...")
        print("   OR run in terminal:")
        print("   export GEMINI_API_KEY=AIzaSy...")
        print("3. Re-run this script: python3 test_live_api.py\n")
        sys.exit(1)

    print(f"\n[1/5] Detected API Key: {mask_api_key(api_key)}")

    # Extract text from sample PDF
    pdf_path = Path("sample_data/sample_paper_1_lora.pdf")
    print(f"[2/5] Reading research paper PDF: {pdf_path}")
    pdf_res = extract_text_from_pdf_path(str(pdf_path))

    if not pdf_res["success"]:
        print(f"❌ PDF extraction failed: {pdf_res['error']}")
        sys.exit(1)

    print(f"      Extracted {pdf_res['char_count']} characters across {pdf_res['page_count']} page(s).")

    # Initialize live AI Service
    model_name = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")
    print(f"[3/5] Initializing AIService with model: {model_name}")
    service = AIService(api_key=api_key, model_name=model_name)

    if not service.is_api_available():
        print("❌ Could not initialize GenAI client.")
        sys.exit(1)

    print("\n[4/5] Executing 3-Stage Prompt Chaining Pipeline against Gemini API...")

    # Stage 1: Extraction
    print("      -> Calling Stage 1 (Research Information Extraction)...", end="", flush=True)
    s1 = service.run_stage_1_extraction(pdf_res["text"])
    if s1["is_mock"]:
        print(f" FAILED (Fell back to mock: {s1.get('error')})")
        sys.exit(1)
    fb1 = f" [Fallback Note: {s1['fallback_note']}]" if s1.get("fallback_note") else ""
    print(f" SUCCESS ({s1['elapsed_seconds']}s, Model: {s1['model_used']}{fb1}, {len(s1['output_text'])} chars)")

    # Stage 2: Synthesis
    print("      -> Calling Stage 2 (Student-Friendly Summary Synthesis)...", end="", flush=True)
    s2 = service.run_stage_2_summary(s1["output_text"], pdf_res["text"])
    if s2["is_mock"]:
        print(f" FAILED (Fell back to mock: {s2.get('error')})")
        sys.exit(1)
    fb2 = f" [Fallback Note: {s2['fallback_note']}]" if s2.get("fallback_note") else ""
    print(f" SUCCESS ({s2['elapsed_seconds']}s, Model: {s2['model_used']}{fb2}, {len(s2['output_text'])} chars)")

    # Stage 3: Verification
    print("      -> Calling Stage 3 (Source-Based Verification Audit)...", end="", flush=True)
    s3 = service.run_stage_3_verification(pdf_res["text"], s2["output_text"])
    if s3["is_mock"]:
        print(f" FAILED (Fell back to mock: {s3.get('error')})")
        sys.exit(1)
    fb3 = f" [Fallback Note: {s3['fallback_note']}]" if s3.get("fallback_note") else ""
    print(f" SUCCESS ({s3['elapsed_seconds']}s, Model: {s3['model_used']}{fb3}, {len(s3['output_text'])} chars)")

    # Verification Parsing
    print("\n[5/5] Parsing Verification Audit Output...")
    parsed_audit = parse_verification_output(s3["output_text"])
    metrics = parsed_audit["metrics"]

    print("=" * 70)
    print("LIVE PIPELINE VERIFICATION RESULTS:")
    print("=" * 70)
    print(f"Model Inferences:    LIVE {model_name} (Zero Mocks)")
    print(f"Total Pipeline Time: {round(s1['elapsed_seconds'] + s2['elapsed_seconds'] + s3['elapsed_seconds'], 2)}s")
    print(f"Total Claims Audited: {metrics['total_claims']}")
    print(f"Supported Claims:    {metrics['supported']}")
    print(f"Partially Supported: {metrics['partially_supported']}")
    print(f"Unsupported Claims:  {metrics['unsupported']}")
    print(f"Grounding Score:     {metrics['confidence_score']}%")

    print("\n--- SAMPLE EXTRACT (STAGE 1 PREVIEW) ---")
    print(s1["output_text"][:400] + "...\n")

    print("--- SAMPLE SUMMARY (STAGE 2 PREVIEW) ---")
    print(s2["output_text"][:400] + "...\n")

    print("--- CLAIMS AUDIT TABLE (STAGE 3 PREVIEW) ---")
    for c in parsed_audit["claims"][:3]:
        print(f"[{c['status']}] Claim {c['claim_num']}: {c['summary_claim'][:80]}...")

    print("\n✅ LIVE GEMINI INTEGRATION 100% VERIFIED AND WORKING PROPERLY!")
    print("=" * 70)


if __name__ == "__main__":
    run_live_test()
