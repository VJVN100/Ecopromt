import os

def validate_gemini_key(api_key: str) -> bool:
    """
    Validates the format or presence of a Gemini API key.
    For this MVP, we check if it is non-empty and starts with "AIza" (standard GCP API key prefix).
    """
    if not api_key:
        return False
        
    # Gemini API keys typically start with AIza
    if api_key.startswith("AIza") and len(api_key) > 30:
        return True
        
    return False

def get_gemini_key() -> str:
    """Retrieves the API key from environment variables if set."""
    return os.getenv("GEMINI_API_KEY", "")
