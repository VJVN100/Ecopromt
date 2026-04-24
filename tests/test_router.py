import sys
import os
import pytest

# Ensure the app module is in the path for testing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.core.complexity import optimize_prompt, analyze_complexity
from app.core.router import calculate_esif, estimate_tokens

# ==========================================
# 1. ESIF Formula Tests
# ==========================================

def test_esif_safeguards():
    """Ensure math handles 0 tokens gracefully without ZeroDivisionError."""
    esif = calculate_esif(model_type="local", time_taken=1.5, token_count=0)
    assert isinstance(esif, float)
    
    esif_negative = calculate_esif(model_type="local", time_taken=1.0, token_count=-10)
    assert isinstance(esif_negative, float)

def test_esif_time_impact():
    """Ensure a faster response yields a higher ESIF efficiency score."""
    fast_esif = calculate_esif(model_type="local", time_taken=0.1, token_count=50)
    slow_esif = calculate_esif(model_type="local", time_taken=10.0, token_count=50)
    
    assert fast_esif > slow_esif

def test_esif_model_weights():
    """Ensure Local models always score significantly higher than Cloud models for the exact same input."""
    local_score = calculate_esif(model_type="local", time_taken=2.0, token_count=50)
    cloud_score = calculate_esif(model_type="cloud", time_taken=2.0, token_count=50)
    
    assert local_score > cloud_score

# ==========================================
# 2. Complexity Logic Tests
# ==========================================

def test_complexity_simple_queries():
    """Math and basic questions should route to LOW (Local)."""
    assert analyze_complexity("what is 2 + 2?") == "LOW"
    assert analyze_complexity("hello there!") == "LOW"

def test_complexity_keyword_triggers():
    """Using terms like 'code' or 'analyze' should instantly bump to HIGH (Cloud)."""
    assert analyze_complexity("can you write code to analyze this?") == "HIGH"
    assert analyze_complexity("generate a story about eco-tech") == "HIGH"

def test_complexity_length_triggers():
    """A very long prompt, regardless of keywords, should bump to HIGH."""
    long_prompt = "A" * 305
    assert analyze_complexity(long_prompt) == "HIGH"

# ==========================================
# 3. Prompt Optimizer Tests
# ==========================================

def test_prompt_optimizer_removes_fillers():
    """Check if 'please tell me' style words are aggressively stripped out."""
    original = "Could you please tell me how to build a house"
    optimized = optimize_prompt(original)
    
    assert len(optimized) < len(original)
    assert "please" not in optimized
    assert "build a house" in optimized

def test_prompt_optimizer_double_spaces():
    """Check that resulting awkward punctuation and double spaces are removed."""
    original = "What is the,,,,      weather?"
    optimized = optimize_prompt(original)
    
    assert "  " not in optimized
    assert ",,,," not in optimized

def test_prompt_optimizer_safety_fallback():
    """If a prompt ONLY consists of fillers, it should NOT return an empty string."""
    original = "Please tell me"
    optimized = optimize_prompt(original)
    
    # We shouldn't drop the whole prompt if it leaves nothing to route
    assert len(optimized) > 0
    assert optimized == original
