"""
PDF Processing Module for PaperPilot AI.
Extracts text from PDF documents using PyMuPDF (pymupdf),
detects scanned documents, and handles corrupted or unreadable files.
"""

from typing import Dict, Any
import pymupdf


def extract_text_from_pdf_bytes(pdf_bytes: bytes) -> Dict[str, Any]:
    """
    Extracts text from PDF raw bytes.
    Returns a dictionary with status, extracted text, page count, and diagnostic flags.
    """
    result: Dict[str, Any] = {
        "success": False,
        "text": "",
        "page_count": 0,
        "char_count": 0,
        "is_scanned": False,
        "error": None,
        "pages_info": [],
    }

    if not pdf_bytes or len(pdf_bytes) == 0:
        result["error"] = "Empty PDF stream provided."
        return result

    try:
        # Open PDF document from memory
        doc = pymupdf.open(stream=pdf_bytes, filetype="pdf")
        page_count = len(doc)
        result["page_count"] = page_count

        if page_count == 0:
            result["error"] = "PDF document contains 0 pages."
            doc.close()
            return result

        full_text_parts = []
        total_chars = 0

        for page_idx in range(page_count):
            page = doc[page_idx]
            page_text = page.get_text("text") or ""
            cleaned_page_text = page_text.strip()
            page_chars = len(cleaned_page_text)
            total_chars += page_chars

            result["pages_info"].append({
                "page_num": page_idx + 1,
                "char_count": page_chars,
            })

            if cleaned_page_text:
                full_text_parts.append(f"--- [Page {page_idx + 1}] ---\n" + cleaned_page_text)

        doc.close()

        extracted_text = "\n\n".join(full_text_parts).strip()
        result["text"] = extracted_text
        result["char_count"] = len(extracted_text)

        # Detect image-only or scanned PDFs
        # If there are pages but very few extractable characters (< 60 chars per page on average or < 100 overall)
        if total_chars < 80:
            result["is_scanned"] = True
            result["error"] = (
                "Scanned or Image-Only PDF Detected: The document contains pages but almost no extractable selectable text "
                f"({total_chars} characters extracted across {page_count} page(s)). "
                "PaperPilot AI requires digital selectable text. Please upload an OCR-processed PDF or paste the text directly."
            )
            return result

        result["success"] = True
        return result

    except pymupdf.FileDataError as e:
        result["error"] = f"Corrupted or invalid PDF structure: {str(e)}"
        return result
    except Exception as e:
        result["error"] = f"Unexpected error while reading PDF: {str(e)}"
        return result


def extract_text_from_pdf_path(pdf_path: str) -> Dict[str, Any]:
    """
    Convenience function to extract text from a local PDF file path.
    """
    try:
        with open(pdf_path, "rb") as f:
            pdf_bytes = f.read()
        return extract_text_from_pdf_bytes(pdf_bytes)
    except FileNotFoundError:
        return {
            "success": False,
            "text": "",
            "page_count": 0,
            "char_count": 0,
            "is_scanned": False,
            "error": f"File not found at path: {pdf_path}",
            "pages_info": [],
        }
    except Exception as e:
        return {
            "success": False,
            "text": "",
            "page_count": 0,
            "char_count": 0,
            "is_scanned": False,
            "error": f"Failed to read file: {str(e)}",
            "pages_info": [],
        }
