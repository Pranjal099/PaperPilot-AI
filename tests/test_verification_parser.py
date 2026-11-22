"""
Automated Unit Tests for Verification Parser and Badge Formatter (src/verification.py).
Tests markdown table parsing, metric counts, grounding calculations, and badge styles.
"""

from src.verification import parse_verification_output, format_status_badge


def test_parse_valid_markdown_verification_table():
    sample_raw = """### CLAIMS VERIFICATION TABLE
| Claim # | Summary Claim | Verification Status | Source Evidence Quote | Discrepancy & Suggested Correction |
|---|---|---|---|---|
| 1 | Low-rank adaptation reduces parameter count by 10,000x | [SUPPORTED] | "reduce the number of trainable parameters by 10,000 times" | Verified. Exact quantitative match. |
| 2 | GPU memory requirement is cut in half | [PARTIALLY SUPPORTED] | "GPU memory requirement by 3 times" | Paper says 3x reduction, not 2x. Correction: Update to 3x. |
| 3 | Model was tested on quantum computing simulator | [UNSUPPORTED] | No supporting evidence found in text. | Unsupported hallucination. Remove quantum claim. |

### SUMMARY AUDIT METRICS
- Total Claims Audited: 3
- Supported Claims: 1
- Partially Supported Claims: 1
- Unsupported Claims: 1
- Grounding Confidence Score: 50.0%

### CRITICAL STUDENT WARNINGS
- Notice quantum computing claim was uncorroborated by source text.

### VERIFICATION DISCLAIMER
Notice: LLM-based verification is an automated cross-check aid. Readers should inspect the primary source text.
"""
    parsed = parse_verification_output(sample_raw)

    assert len(parsed["claims"]) == 3
    assert parsed["claims"][0]["status"] == "SUPPORTED"
    assert parsed["claims"][1]["status"] == "PARTIALLY SUPPORTED"
    assert parsed["claims"][2]["status"] == "UNSUPPORTED"

    assert parsed["metrics"]["total_claims"] == 3
    assert parsed["metrics"]["supported"] == 1
    assert parsed["metrics"]["partially_supported"] == 1
    assert parsed["metrics"]["unsupported"] == 1
    assert parsed["metrics"]["confidence_score"] == 50.0

    assert len(parsed["critical_warnings"]) == 1
    assert "quantum" in parsed["critical_warnings"][0].lower()
    assert "automated cross-check" in parsed["disclaimer"]


def test_parse_empty_or_whitespace_output():
    parsed = parse_verification_output("")
    assert parsed["metrics"]["total_claims"] == 0
    assert parsed["claims"] == []


def test_format_status_badge():
    assert "🟢" in format_status_badge("SUPPORTED")
    assert "🟡" in format_status_badge("PARTIALLY SUPPORTED")
    assert "🔴" in format_status_badge("UNSUPPORTED")
    assert "⚪" in format_status_badge("NOT VERIFIABLE")
