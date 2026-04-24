This is the comprehensive master plan for **EcoRouter**. It integrates your hackathon PRD, the architectural logic for efficiency, and the specific UI layout from your sketch. This is designed to be your "source of truth" for development and your pitch.

---

## 🌎 EcoRouter: Project Overview
**EcoRouter** is an intelligent AI middleware that optimizes LLM usage by analyzing prompt complexity and routing requests between **Local Models (Ollama)** and **Cloud APIs (Gemini)**. It aims to reduce carbon footprints, minimize API costs, and improve latency.

---

## 🎨 1. User Interface (UI) Design
*Based on your sketch, the UI follows a "Minimalist Search" philosophy.*

### **A. Main Input Section**
* **Search Bar:** A prominent, rounded horizontal bar positioned centrally.
* **Engine Dropdown:** Integrated at the left or right edge of the bar.
    * `Auto-Route (Smart)`: Default logic decides Local vs Cloud.
    * `Ollama (Local)`: Forces local execution.
    * `Gemini (Cloud)`: Forces cloud execution.
* **Execution Button:** A 🔍 icon or a "Route" button to trigger the process.

### **B. Post-Submission Display**
* **Response Area:** Clean typography for the AI-generated answer.
* **Metadata Pills:** Small tags showing the **Model Used** (e.g., *Phi-3 via Ollama*) and **Latency** (e.g., *1.2s*).
* **Impact Dashboard:**
    * **ESIF Score:** A circular gauge or numerical value (0–100).
    * **Eco-Statement:** A text summary: *"By routing locally, you saved **1.4g of CO2** and **₹0.15** in API costs."*

---

## ⚙️ 2. The Core Engine Logic
This is the "Brain" of EcoRouter that differentiates it from a standard chatbot.

### **Step 1: Prompt Optimization**
Before routing, the system cleans the input:
* Removes redundant "filler" words (e.g., "please," "I want to know").
* Trims excessive whitespace.
* **Goal:** Reduce token count by **≥ 10%** without losing intent.

### **Step 2: Complexity Analysis**
A lightweight scoring script runs in **< 200ms**:
* **Low Complexity:** Mathematical queries, definitions, greetings, or short summaries.
* **High Complexity:** Coding tasks, deep analysis, multi-step reasoning, or prompts > 500 characters.

### **Step 3: The ESIF Calculation**
Your unique success metric:
$$ESIF = \frac{(W_{model} \times 100) - (T_{total} \times 5)}{L_{tokens}}$$
* **$W_{model}$:** Weight (Local = 1.0 | Cloud = 0.4).
* **$T_{total}$:** Total response time in seconds.
* **$L_{tokens}$:** Final token count used.
* **Interpretation:** A score of **80+** is "Green/Eco-Friendly"; **<50** is "Resource Intensive."

---

## 🛠️ 3. Technical Implementation Stack

| Layer | Technology | Role |
| :--- | :--- | :--- |
| **Frontend** | **Streamlit** or **Next.js** | Handles the UI/UX and the dropdown logic. |
| **Backend** | **FastAPI (Python)** | Manages routing logic and complexity analysis. |
| **Local LLM** | **Ollama (Phi-3 / Llama 3)** | Processes "Low Complexity" tasks on the local machine. |
| **Cloud LLM** | **Gemini 1.5 Flash** | Processes "High Complexity" tasks via API. |
| **Environment** | **Environment Variables** | Securely stores Gemini API keys. |

---

## 📊 4. Success Metrics for Judges
* **Local Routing Rate:** Aim for **40%** of total traffic handled locally.
* **Cost Reduction:** Achieve **25%** savings vs. 100% cloud routing.
* **Carbon Impact:** Estimated CO2 savings displayed in real-time.

---

## 🚀 5. Demo Day Strategy
1.  **The "Simple" Test:** Input "What is 2+2?" → Show the dropdown on `Auto` → System routes to **Ollama** → High ESIF Score (90+).
2.  **The "Complex" Test:** Input "Write a Python script for a neural network." → System routes to **Gemini** → Lower ESIF Score, but higher accuracy.
3.  **The Fallback Demo:** Simulate a local model failure; show the system instantly rerouting to Gemini so the user experience is never interrupted.

---

### **Final Impact Note**
EcoRouter isn't just a tool; it's a **sustainable AI framework**. It solves the problem of "API Overkill," where massive cloud models are used for trivial tasks, wasting both money and energy.