"""
Automated Unit Tests for PDF Processing (src/pdf_processing.py).
Tests valid PDF extraction, empty stream, corrupted structure, and scanned PDF detection.
"""

from pathlib import Path
import pymupdf
from src.pdf_processing import extract_text_from_pdf_bytes, extract_text_from_pdf_path

SAMPLE_PDF_PATH = Path(__file__).resolve().parent.parent / "sample_data" / "sample_paper_1_lora.pdf"


def test_extract_valid_sample_pdf():
    assert SAMPLE_PDF_PATH.exists()
    res = extract_text_from_pdf_path(str(SAMPLE_PDF_PATH))
    assert res["success"] is True
    assert res["page_count"] >= 1
    assert res["char_count"] > 500
    assert "Low-Rank Adaptation" in res["text"] or "LoRA" in res["text"]
    assert res["error"] is None


def test_extract_empty_pdf_stream():
    res = extract_text_from_pdf_bytes(b"")
    assert res["success"] is False
    assert "empty" in res["error"].lower()


def test_extract_corrupted_pdf_structure():
    corrupted_bytes = b"%PDF-1.4\nCorrupted binary garbage that cannot be parsed as valid PDF objects"
    res = extract_text_from_pdf_bytes(corrupted_bytes)
    assert res["success"] is False
    assert res["error"] is not None


def test_scanned_image_only_pdf_detection():
    # Create an in-memory PDF with 1 blank page (0 characters)
    doc = pymupdf.open()
    doc.new_page(width=612, height=792)
    pdf_bytes = doc.tobytes()
    doc.close()

    res = extract_text_from_pdf_bytes(pdf_bytes)
    assert res["success"] is False
    assert res["is_scanned"] is True
    assert "scanned" in res["error"].lower() or "image-only" in res["error"].lower()


def test_non_existent_file_path():
    res = extract_text_from_pdf_path("sample_data/non_existent_file_12345.pdf")
    assert res["success"] is False
    assert "not found" in res["error"].lower()
