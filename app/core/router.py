import time
import ollama
import google.generativeai as genai

def estimate_tokens(text: str) -> int:
    """Uses character heuristics (len/4) since we lack tiktoken in strict TECH_STACK."""
    return max(1, len(text) // 4)

def calculate_esif(model_type: str, time_taken: float, token_count: int) -> float:
    """
    ESIF = ((W_model * 100) - (T_total * 5)) / L_tokens
    """
    w_model = 1.0 if model_type == "local" else 0.4
    
    if token_count <= 0:
        token_count = 1
        
    esif = ((w_model * 100) - (time_taken * 5)) / token_count
    return round(esif, 2)

def generate_co2_savings(model_type: str, token_count: int) -> float:
    """Estimates CO2 saved vs Cloud execution."""
    if model_type == "cloud":
        return 0.0
    # Conservative estimate: local execution saves ~0.05g per token 
    return round(token_count * 0.05, 2)

def call_ollama(prompt: str) -> dict:
    start = time.time()
    try:
        # Defaulting to phi3 as requested
        response = ollama.chat(model='phi3', messages=[{'role': 'user', 'content': prompt}])
        answer = response['message']['content']
    except Exception as e:
        return {"error": f"Local Model failure: {e}"}
        
    t_total = time.time() - start
    tokens = estimate_tokens(prompt) + estimate_tokens(answer)
    esif = calculate_esif("local", t_total, tokens)
    co2 = generate_co2_savings("local", tokens)
    
    return {
        "engine": "Local (Phi-3)",
        "response": answer, 
        "esif": esif, 
        "co2": co2, 
        "time": round(t_total, 2),
        "tokens": tokens
    }

def call_gemini(prompt: str, key: str) -> dict:
    start = time.time()
    if not key:
         return {"error": "Missing Gemini API Key."}
         
    try:
        genai.configure(api_key=key)
        model = genai.GenerativeModel('gemini-flash-latest')
        res = model.generate_content(prompt)
        answer = res.text
    except Exception as e:
        return {"error": f"Cloud API failure: {e}"}
        
    t_total = time.time() - start
    tokens = estimate_tokens(prompt) + estimate_tokens(answer)
    esif = calculate_esif("cloud", t_total, tokens)
    co2 = generate_co2_savings("cloud", tokens)
    
    return {
        "engine": "Cloud (Gemini)",
        "response": answer, 
        "esif": esif, 
        "co2": co2, 
        "time": round(t_total, 2),
        "tokens": tokens
    }
