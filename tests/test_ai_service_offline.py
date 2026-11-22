"""
Automated Unit Tests for AIService Pipeline in Offline/Mock Simulation Mode.
Ensures the 3-stage chain executes deterministically, respects missing fields,
and generates structured outputs without requiring a live Gemini API key.
"""

from pathlib import Path
from src.ai_service import AIService

SAMPLE_DIR = Path(__file__).resolve().parent.parent / "sample_data"


def test_full_offline_pipeline_execution():
    lora_text = (SAMPLE_DIR / "sample_paper_1_lora.txt").read_text(encoding="utf-8")
    service = AIService(api_key=None)

    assert not service.is_api_available()

    result = service.run_full_pipeline(lora_text)

    # Verify Stage 1
    s1 = result["stage1"]
    assert s1["stage"] == 1
    assert s1["is_mock"] is True
    assert "LoRA: Low-Rank Adaptation" in s1["output_text"]
    assert "10,000" in s1["output_text"] or "3x" in s1["output_text"]

    # Verify Stage 2
    s2 = result["stage2"]
    assert s2["stage"] == 2
    assert "SECTION 10: \"Explain Like I'm a Beginner\"" in s2["output_text"]
    assert "SECTION 11: Technical Glossary" in s2["output_text"]

    # Verify Stage 3
    s3 = result["stage3"]
    assert s3["stage"] == 3
    assert "CLAIMS VERIFICATION TABLE" in s3["output_text"]
    assert "[SUPPORTED]" in s3["output_text"]

    # Verify overall pipeline
    assert result["total_elapsed_seconds"] >= 0.0
    assert result["is_mock"] is True


def test_offline_pipeline_detects_missing_limitations():
    incomplete_text = (SAMPLE_DIR / "sample_paper_3_incomplete.txt").read_text(encoding="utf-8")
    service = AIService(api_key=None)

    s1 = service.run_stage_1_extraction(incomplete_text)
    assert "Not specified in the provided text." in s1["output_text"]
    assert "Fast distributed graph" in s1["output_text"].lower() or "fastgraph" in s1["output_text"].lower()

    s2 = service.run_stage_2_summary(s1["output_text"], incomplete_text)
    assert "Not specified in the provided text." in s2["output_text"]
