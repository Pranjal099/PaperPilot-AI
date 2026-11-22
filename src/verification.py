"""
Verification Parsing and Formatting Module for PaperPilot AI.
Extracts audit metrics, claims verification tables, badges, and warnings
from the Stage 3 Source-Based Verification prompt output.
"""

import re
from typing import Dict, Any, List


def parse_verification_output(raw_output: str) -> Dict[str, Any]:
    """
    Parses the Markdown output from Prompt 3 into structured fields,
    extracting metrics, claim records, student warnings, and disclaimers.
    """
    data: Dict[str, Any] = {
        "raw_text": raw_output,
        "claims": [],
        "metrics": {
            "total_claims": 0,
            "supported": 0,
            "partially_supported": 0,
            "unsupported": 0,
            "not_verifiable": 0,
            "confidence_score": 0.0,
        },
        "critical_warnings": [],
        "disclaimer": "",
    }

    if not raw_output or not raw_output.strip():
        return data

    text = raw_output.strip()

    # Parse Claims Table
    # Looking for markdown table rows with | ... |
    table_lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip().startswith("|") and not line.strip().startswith("|---")
    ]

    header_skipped = False
    for line in table_lines:
        columns = [c.strip() for c in line.split("|")[1:-1]]
        if len(columns) >= 4:
            # Check if this is the header row
            if "claim" in columns[0].lower() or "summary claim" in columns[1].lower():
                header_skipped = True
                continue

            claim_num = columns[0]
            summary_claim = columns[1]
            status_raw = columns[2].upper()
            evidence = columns[3] if len(columns) > 3 else "Not specified"
            correction = columns[4] if len(columns) > 4 else ""

            # Normalize status
            status = "UNKNOWN"
            if "PARTIALLY" in status_raw:
                status = "PARTIALLY SUPPORTED"
            elif "UNSUPPORTED" in status_raw:
                status = "UNSUPPORTED"
            elif "SUPPORTED" in status_raw:
                status = "SUPPORTED"
            elif "NOT VERIFIABLE" in status_raw or "UNVERIFIABLE" in status_raw:
                status = "NOT VERIFIABLE"
            else:
                status = status_raw.replace("[", "").replace("]", "").strip()

            data["claims"].append({
                "claim_num": claim_num,
                "summary_claim": summary_claim,
                "status": status,
                "evidence": evidence,
                "correction": correction,
            })

    # If table parsing didn't pick up claims (e.g. non-table markdown format),
    # use regex fallback for structured claims
    if not data["claims"]:
        claim_blocks = re.findall(
            r"Claim\s*(?:#?\s*(\d+))?[:\s]+(.*?)(?=\n\s*(?:Claim|\n\n|\Z))",
            text,
            re.DOTALL | re.IGNORECASE,
        )
        for idx, (c_num, c_body) in enumerate(claim_blocks, 1):
            status_match = re.search(r"\[?(SUPPORTED|PARTIALLY SUPPORTED|UNSUPPORTED|NOT VERIFIABLE)\]?", c_body, re.IGNORECASE)
            status = status_match.group(1).upper() if status_match else "SUPPORTED"
            data["claims"].append({
                "claim_num": c_num or str(idx),
                "summary_claim": c_body.strip()[:200],
                "status": status,
                "evidence": "Extracted from source context.",
                "correction": "",
            })

    # Calculate or extract metrics
    # Try regex first from SUMMARY AUDIT METRICS
    total_match = re.search(r"Total Claims Audited:\s*(\d+)", text, re.IGNORECASE)
    sup_match = re.search(r"Supported Claims:\s*(\d+)", text, re.IGNORECASE)
    part_match = re.search(r"Partially Supported Claims:\s*(\d+)", text, re.IGNORECASE)
    unsup_match = re.search(r"Unsupported Claims:\s*(\d+)", text, re.IGNORECASE)
    score_match = re.search(r"Grounding Confidence Score:\s*([\d\.]+)%?", text, re.IGNORECASE)

    if data["claims"]:
        data["metrics"]["total_claims"] = len(data["claims"])
        data["metrics"]["supported"] = sum(1 for c in data["claims"] if c["status"] == "SUPPORTED")
        data["metrics"]["partially_supported"] = sum(1 for c in data["claims"] if c["status"] == "PARTIALLY SUPPORTED")
        data["metrics"]["unsupported"] = sum(1 for c in data["claims"] if c["status"] == "UNSUPPORTED")
        data["metrics"]["not_verifiable"] = sum(1 for c in data["claims"] if c["status"] == "NOT VERIFIABLE")

        if data["metrics"]["total_claims"] > 0:
            # Weighted calculation: Supported = 1.0, Partially = 0.5, Unsupported = 0.0, Not Verifiable = 0.5
            weighted_score = (
                data["metrics"]["supported"] * 1.0
                + data["metrics"]["partially_supported"] * 0.5
                + data["metrics"]["not_verifiable"] * 0.5
            ) / data["metrics"]["total_claims"] * 100.0
            data["metrics"]["confidence_score"] = round(weighted_score, 1)

    # Overwrite if explicit in text
    if score_match:
        try:
            data["metrics"]["confidence_score"] = float(score_match.group(1))
        except ValueError:
            pass
    if total_match:
        try:
            data["metrics"]["total_claims"] = int(total_match.group(1))
        except ValueError:
            pass

    # Extract Critical Warnings
    warnings_section = re.search(
        r"###\s*CRITICAL STUDENT WARNINGS\s*\n(.*?)(?=\n###|\Z)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if warnings_section:
        w_text = warnings_section.group(1).strip()
        lines = [line.strip("- *").strip() for line in w_text.splitlines() if line.strip()]
        data["critical_warnings"] = lines

    # Extract Disclaimer
    disclaimer_section = re.search(
        r"###\s*VERIFICATION DISCLAIMER\s*\n(.*?)(?=\n###|\Z)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if disclaimer_section:
        data["disclaimer"] = disclaimer_section.group(1).strip()
    else:
        data["disclaimer"] = (
            "Notice: LLM-based verification is an automated cross-check aid and not a guarantee of mathematical or scientific ground truth. "
            "Students should inspect the primary source text for definitive citations."
        )

    return data


def format_status_badge(status: str) -> str:
    """Returns markdown badge for verification status."""
    norm = status.upper()
    if norm == "SUPPORTED":
        return "🟢 **[SUPPORTED]**"
    elif norm == "PARTIALLY SUPPORTED":
        return "🟡 **[PARTIALLY SUPPORTED]**"
    elif norm == "UNSUPPORTED":
        return "🔴 **[UNSUPPORTED]**"
    elif norm == "NOT VERIFIABLE":
        return "⚪ **[NOT VERIFIABLE]**"
    return f"🔵 **[{status}]**"
