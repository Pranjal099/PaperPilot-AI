"""
Automated Unit Tests for API Client Configuration and Fallback Behavior.
Tests invalid API key handling and offline mode switching.
"""

from src.ai_service import AIService


def test_ai_service_initialization_without_key():
    service = AIService(api_key="")
    assert not service.is_api_available()
    assert service.api_key == ""


def test_ai_service_with_dummy_key_graceful_fallback():
    # When initialized with an invalid dummy key, attempting to call Gemini API will fail,
    # and the system must gracefully fall back to mock without crashing or breaking the pipeline.
    service = AIService(api_key="AIzaSyDummyKeyForTestingOnly123456789")
    # Even if client is created, live calls will fail auth and fallback
    test_text = (
        "Title: Test Sample\nAbstract: This paper demonstrates efficient prompt chaining. "
        "We achieved 95% accuracy on benchmark tests using modern transformer architectures."
    )
    res = service.run_stage_1_extraction(test_text)
    assert res is not None
    assert "output_text" in res
    assert res["stage"] == 1
    # Fallback took effect
    assert res["is_mock"] is True
    assert res["error"] is not None
