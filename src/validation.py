"""
Input Validation Module for PaperPilot AI.
Validates raw text, file uploads, file sizes, and extracts edge-case warnings.
"""

from typing import Tuple, Dict, Any, Optional

MIN_TEXT_CHARS = 100
MIN_WORD_COUNT = 25
MAX_TEXT_CHARS = 150_000
MAX_FILE_SIZE_BYTES = 15 * 1024 * 1024  # 15 MB


def validate_pasted_text(text: Optional[str]) -> Tuple[bool, str, Dict[str, Any]]:
    """
    Validates user-pasted academic text.
    Returns (is_valid, message, metadata).
    """
    if text is None:
        return False, "Input text is null or missing.", {"char_count": 0, "word_count": 0}

    cleaned = text.strip()
    char_count = len(cleaned)
    word_count = len(cleaned.split())

    metadata = {
        "char_count": char_count,
        "word_count": word_count,
    }

    if char_count == 0:
        return False, "Input is empty. Please paste the text of a research paper.", metadata

    # Check for repetitive garbage / gibberish (e.g. repeated single characters)
    unique_chars = len(set(cleaned.lower().replace(" ", "").replace("\n", "")))
    if unique_chars < 5 and char_count >= 50:
        return (
            False,
            "Input appears to be repetitive gibberish or non-text characters.",
            metadata,
        )

    if char_count < MIN_TEXT_CHARS or word_count < MIN_WORD_COUNT:
        return (
            False,
            f"Input text is too short ({char_count} chars, {word_count} words). "
            f"A research paper excerpt must contain at least {MIN_TEXT_CHARS} characters and {MIN_WORD_COUNT} words for meaningful summarization.",
            metadata,
        )

    if char_count > MAX_TEXT_CHARS:
        return (
            False,
            f"Input text exceeds maximum allowable limit of {MAX_TEXT_CHARS:,} characters (current: {char_count:,}). "
            "Please provide a shorter section or the abstract and main sections of the paper.",
            metadata,
        )

    return True, "Input text is valid.", metadata


def validate_pdf_upload(file_bytes: Optional[bytes], filename: str = "") -> Tuple[bool, str, Dict[str, Any]]:
    """
    Validates uploaded PDF binary data before parsing.
    Returns (is_valid, message, metadata).
    """
    if file_bytes is None or len(file_bytes) == 0:
        return False, "Uploaded file is empty (0 bytes).", {"size_bytes": 0}

    size_bytes = len(file_bytes)
    metadata = {
        "filename": filename,
        "size_bytes": size_bytes,
        "size_mb": round(size_bytes / (1024 * 1024), 2),
    }

    if size_bytes > MAX_FILE_SIZE_BYTES:
        return (
            False,
            f"File exceeds maximum size limit of {MAX_FILE_SIZE_BYTES // (1024 * 1024)}MB (uploaded size: {metadata['size_mb']}MB).",
            metadata,
        )

    # Validate PDF magic header '%PDF-'
    if not file_bytes.startswith(b"%PDF-"):
        return (
            False,
            "Corrupted or invalid file: File does not possess a valid PDF header format (%PDF-).",
            metadata,
        )

    return True, "PDF file upload is valid.", metadata
