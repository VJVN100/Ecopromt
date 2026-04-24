# 🌱 EcoRouter

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

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** FastAPI (Python)  
- **Local Model:** Ollama (Phi-3)  
- **Cloud Model:** Gemini 1.5 Flash  

---

## 📊 ESIF Formula
ESIF = ((W_model × 100) - (T_total × 5)) / L_tokens


- Local model → higher score  
- Faster response → higher score  
- Fewer tokens → higher score  

