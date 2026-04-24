# 🌱 EcoRouter: Intelligent AI Resource Orchestrator

**EcoRouter** is a sustainable AI middleware that prevents *Model Overkill* by intelligently routing prompts between **local LLMs (Ollama)** and **cloud APIs (Gemini)** based on complexity.

---

## 🚀 Why EcoRouter?

Most AI systems send every query to large cloud models — even simple ones.

**Result:**
- ⚡ Wasted compute
- 💰 Higher API cost
- 🌍 Increased carbon footprint

---

## 💡 What We Built

EcoRouter acts as a **smart routing layer**:

- 🧠 **Complexity Engine** → Decides local vs cloud (<200ms)
- ✂️ **Prompt Optimizer** → Reduces token usage (10–20%)
- 📊 **ESIF Score** → Measures efficiency per request
- 🔄 **Failover System** → Ensures reliability

---

## 🏗️ Tech Stack

- **Frontend:** HTML, CSS, Vanilla JavaScript
- **Backend:** FastAPI (Python)
- **Local Model:** Ollama (Phi-3)
- **Cloud Model:** Gemini 1.5 Flash

---

## 📊 ESIF Formula
`ESIF = ((W_model × 100) - (T_total × 5)) / L_tokens`

- Local model → higher score
- Faster response → higher score
- Fewer tokens → higher score

---

## Installation Instructions

1. **Clone the Repository and Navigate to Root:**
   ```bash
   git clone https://github.com/VJVN100/Ecopromt.git
   cd Ecopromt
   ```
2. **Create and Activate a Virtual Environment:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install Core Dependencies:**
   ```bash
   pip install fastapi textblob python-dotenv uvicorn ollama google-generativeai
   ```
4. **Configure your Environment:**
   Ensure the `.env` file exists and input your `GEMINI_API_KEY`.
5. **Install Ollama (Optional for Local Routing):**
   Download the daemon from [ollama.com](https://ollama.com). In a second terminal, run `ollama serve`.
6. **Launch EcoRouter Backend!**
   ```bash
   uvicorn main:app --reload
   ```
7. **Access the application:**
   Navigate to `http://127.0.0.1:8000` to interact with the web interface.

---
*Built for the NEXUS AI Hackathon 2026* | EcoRouter v1.0
