# 🌱 EcoRouter: Intelligent AI Resource Orchestrator

## The Vision
Sustainability meets Efficiency. The AI revolution is rapidly increasing global carbon emissions and API costs. EcoRouter solves this unseen environmental crisis by acting as a lightweight, intelligent middleware proxy. EcoRouter dynamically analyzes your prompt's complexity—if it's a simple query, it routes it to a local machine with zero emissions. If it requires heavy lifting, it fails over to the cloud. You get faster responses, lower API bills, and a verified reduction in your carbon footprint via our custom Efficiency impact formula.

## Technical Architecture
EcoRouter's orchestration layer leverages a split-brain approach:
- **FastAPI / Python Core**: Analyzes complexity and optimizes strings in < 200ms using zero external NLP dependencies.
- **Local Engine (Ollama/Phi-3)**: Handles lightweight mathematical queries, basic definitions, and greetings locally without invoking remote networks.
- **Cloud Engine (Gemini 1.5)**: Deeply integrates with Google Generative AI for complex, multi-stage reasoning or coding queries.
- **Streamlit Interface**: Provides a dynamic "Eco-Growth Green" Dashboard showcasing live impact metrics (ESIF Score, CO2 Saved, and Tokens Bypassed).

## Installation Instructions

1. **Clone the Repository and Navigate to Root:**
   ```bash
   cd Eco_prompt
   ```
2. **Create and Activate a Virtual Environment:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install Core Dependencies:**
   ```bash
   pip install streamlit fastapi textblob python-dotenv uvicorn ollama google-generativeai
   ```
4. **Configure your Environment:**
   Open the `.env` template or the Streamlit sidebar inside the app to input your `GEMINI_API_KEY`.
5. **Install Ollama (Optional for Local Routing):**
   Download the daemon from [ollama.com](https://ollama.com). In a second terminal, run `ollama serve`.
6. **Launch EcoRouter!**
   ```bash
   streamlit run app/ui/main_page.py
   ```

---
*Built for the NEXUS AI Hackathon 2026* | EcoRouter v1.0
