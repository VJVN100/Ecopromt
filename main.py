import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv

from app.core.complexity import optimize_prompt, analyze_complexity
from app.core.router import call_ollama, call_gemini

load_dotenv()

app = FastAPI(title="EcoRouter API")

# Ensure static directory exists
STATIC_DIR = os.path.join(os.path.dirname(__file__), "app", "static")
os.makedirs(STATIC_DIR, exist_ok=True)

# Mount the static directory
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

class PromptRequest(BaseModel):
    prompt: str
    engine: str = "Auto"

@app.get("/")
async def root():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))

@app.post("/api/route")
async def route_prompt(req: PromptRequest):
    if not req.prompt:
        raise HTTPException(status_code=400, detail="Prompt is required")
        
    gemini_key = os.environ.get("GEMINI_API_KEY", "")
    
    opt_prompt = optimize_prompt(req.prompt)
    score = analyze_complexity(opt_prompt)
    
    target = req.engine
    if req.engine == "Auto":
        target = "Local" if score == "LOW" else "Cloud"
        
    result = {}
    if target == "Local":
        result = call_ollama(opt_prompt)
        # Trigger Fallback if Local Fails
        if "error" in result and req.engine == "Auto":
            if not gemini_key:
                result["error"] += " (Auto-fallback failed: No Gemini Key)"
            else:
                result["fallback_triggered"] = True
                result = call_gemini(opt_prompt, gemini_key)
                result["fallback_triggered"] = True
    else:
        if target == "Cloud" and not gemini_key:
             result = {"error": "Cloud forced but API Key is missing!"}
        else:
             result = call_gemini(opt_prompt, gemini_key)
             
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
        
    result["complexity_score"] = score
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
