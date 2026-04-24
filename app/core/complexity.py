import re

def optimize_prompt(text: str) -> str:
    """
    Aggressively strips filler words and redundant punctuation 
    to visibly reduce standard token footprint.
    """
    # High-impact filler mappings commonly used in conversational queries
    fillers = [
        r"\b(please|can you|could you|could we|i want to know|tell me|explain to me|if you can|i'd like to|i would like to|show me|how do i)\b",
        r"\b(what is the|how to|about the|a detailed|in detail|give me)\b"
    ]
    
    optimized = text.lower()
    for pattern in fillers:
        optimized = re.sub(pattern, "", optimized, flags=re.IGNORECASE)
    
    # Remove awkward resulting punctuation and excessive spaces
    optimized = re.sub(r'[,;.!?\s]+', ' ', optimized).strip()
    
    # If optimization stripped the entire query (e.g. user literally typed "please tell me"), 
    # fall back to the original text safely.
    return optimized if len(optimized) > 2 else text

def analyze_complexity(text: str) -> str:
    """
    Analyzes the complexity of an input prompt to determine routing.
    Returns "HIGH" for complex queries (Cloud) and "LOW" for simple queries (Local).
    """
    keywords = ["analyze", "code", "compare", "write", "generate", "create", "summarize", "debug"]
    
    # +2 points for every complex keyword found
    score = sum(2 for k in keywords if k in text.lower())
    
    # Criteria: Score > 1 OR Length > 300 chars (approx 75 tokens)
    return "HIGH" if score > 1 or len(text) > 300 else "LOW"
