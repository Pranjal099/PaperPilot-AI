"""
Automated Unit Tests for Input Validation (src/validation.py).
Tests empty inputs, boundary limits, corrupted headers, and edge cases.
"""

import pytest
from src.validation import validate_pasted_text, validate_pdf_upload, MIN_TEXT_CHARS, MAX_TEXT_CHARS


def test_empty_pasted_text():
    is_valid, msg, meta = validate_pasted_text("")
    assert not is_valid
    assert "empty" in msg.lower()
    assert meta["char_count"] == 0


def test_none_pasted_text():
    is_valid, msg, meta = validate_pasted_text(None)
    assert not is_valid
    assert "missing" in msg.lower() or "null" in msg.lower()


def test_too_short_text():
    short_text = "This is a tiny note about AI."
    is_valid, msg, meta = validate_pasted_text(short_text)
    assert not is_valid
    assert "too short" in msg.lower()
    assert meta["char_count"] < MIN_TEXT_CHARS


def test_repetitive_gibberish():
    gibberish = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    is_valid, msg, meta = validate_pasted_text(gibberish)
    assert not is_valid
    assert "gibberish" in msg.lower() or "repetitive" in msg.lower()


def test_valid_academic_text():
    text = (
        "This paper investigates Parameter-Efficient Fine-Tuning (PEFT) using Low-Rank Adaptation (LoRA). "
        "We freeze pre-trained Transformer weights and inject trainable rank decomposition matrices. "
        "Our experiments on RoBERTa and GPT-3 show a 10,000x reduction in trainable parameters and 3x GPU memory savings "
        "while maintaining parity with full fine-tuning. We evaluate on GLUE benchmarks and discuss multi-task batching limitations."
    )
    is_valid, msg, meta = validate_pasted_text(text)
    assert is_valid
    assert "valid" in msg.lower()
    assert meta["word_count"] > 30


def test_empty_pdf_upload():
    is_valid, msg, meta = validate_pdf_upload(b"", "empty.pdf")
    assert not is_valid
    assert "empty" in msg.lower()


def test_none_pdf_upload():
    is_valid, msg, meta = validate_pdf_upload(None, "none.pdf")
    assert not is_valid


def test_corrupted_pdf_header():
    fake_bytes = b"This is a plaintext file pretending to be PDF"
    is_valid, msg, meta = validate_pdf_upload(fake_bytes, "fake.pdf")
    assert not is_valid
    assert "corrupted" in msg.lower() or "%pdf-" in msg.lower()


def test_valid_pdf_header():
    dummy_pdf_bytes = b"%PDF-1.4\n1 0 obj\n<<>>\nendobj\ntrailer\n<<>>\n%%EOF"
    is_valid, msg, meta = validate_pdf_upload(dummy_pdf_bytes, "test.pdf")
    assert is_valid
    assert "valid" in msg.lower()


def test_oversized_pdf_upload():
    huge_bytes = b"%PDF-" + b"0" * (16 * 1024 * 1024)  # 16 MB
    is_valid, msg, meta = validate_pdf_upload(huge_bytes, "oversized.pdf")
    assert not is_valid
    assert "exceeds maximum size" in msg.lower()
