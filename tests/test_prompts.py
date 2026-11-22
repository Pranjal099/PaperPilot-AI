"""
Automated Unit Tests for Prompt Templates and Iteration Versions.
Verifies file existence, required placeholder variables, and prompt constraints.
"""

from pathlib import Path
from src.ai_service import load_prompt_template, PROMPTS_DIR


def test_final_three_prompts_exist():
    prompt_1 = PROMPTS_DIR / "prompt_1_extraction.txt"
    prompt_2 = PROMPTS_DIR / "prompt_2_summary.txt"
    prompt_3 = PROMPTS_DIR / "prompt_3_verification.txt"

    assert prompt_1.exists(), "Prompt 1 (Extraction) template must exist."
    assert prompt_2.exists(), "Prompt 2 (Summary) template must exist."
    assert prompt_3.exists(), "Prompt 3 (Verification) template must exist."


def test_prompt_1_placeholders_and_constraints():
    content = load_prompt_template("prompt_1_extraction.txt")
    assert "{paper_text}" in content
    assert "Not specified in the provided text" in content
    assert "1. Paper Title:" in content
    assert "8. Explicit Limitations:" in content


def test_prompt_2_placeholders_and_sections():
    content = load_prompt_template("prompt_2_summary.txt")
    assert "{extracted_info}" in content
    assert "{source_excerpt}" in content
    assert "SECTION 10: \"Explain Like I'm a Beginner\"" in content
    assert "SECTION 11: Technical Glossary" in content


def test_prompt_3_placeholders_and_labels():
    content = load_prompt_template("prompt_3_verification.txt")
    assert "{paper_text}" in content
    assert "{generated_summary}" in content
    assert "[SUPPORTED]" in content
    assert "[PARTIALLY SUPPORTED]" in content
    assert "[UNSUPPORTED]" in content
    assert "[NOT VERIFIABLE]" in content
    assert "CLAIMS VERIFICATION TABLE" in content


def test_prompt_iteration_versions_exist():
    v_dir = PROMPTS_DIR / "prompt_versions"
    assert (v_dir / "v1_baseline.txt").exists()
    assert (v_dir / "v2_structured.txt").exists()
    assert (v_dir / "v3_role_refined.txt").exists()
    assert (v_dir / "v4_chained_workflow.txt").exists()
