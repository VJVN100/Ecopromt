# EcoRouter Demo Guide (NEXUS AI Hackathon 2026)

## 🎤 1. The Hook (Intro Script)
"Generating a single AI image or asking a massive frontier model to solve '2+2' uses enough energy to charge a smartphone. The AI revolution is incredible, but it's causing an unseen environmental crisis. Hi, I'm Vijay, and this is **EcoRouter**. EcoRouter is an intelligent, zero-dependency middleware. It analyzes your complexity in real-time. If an open-source local model can efficiently handle it, the query never leaves your laptop. If it's complex, it seamlessly routes to Gemini in the cloud. Faster answers, lower API bills, and verifiable CO2 reduction."

## 💻 2. The Live Workflow

**Step 1: The Simple Request**
*   **Action:** Select the `Auto` engine.
*   **Prompt to type:** `"What is the capital of France?"`
*   **What to point out:** 
    * "Look how fast that was. Our Complexity Engine scored it 'LOW' and pushed it straight to our local Phi-3 model using Ollama."
    * "Look at the Dashboard below. Our ESIF Score is over 90—highly Eco-Friendly."
    * "We bypassed the data center completely and actively tracked the grams of CO2 saved."

**Step 2: The Complex Request**
*   **Action:** Keep the `Auto` engine selected.
*   **Prompt to type:** `"Write a Python script to detect fraudulent credit card transactions and summarize the architecture."`
*   **What to point out:**
    * "The system hits our keyword and length triggers. It automatically scores it 'HIGH'."
    * "It delegates to Gemini 1.5 in the cloud because Phi-3 would struggle with architectural code."
    * "No manual intervention needed. It accurately routes the heavy-lifting upward."

**Step 3: Manual Override & Optimization (The Wow Factor)**
*   **Action:** Select the `Cloud` engine explicitly.
*   **Prompt to type:** `"Could you please tell me how to build a treehouse? I would like to know in detail if you can show me."`
*   **What to point out:**
    * "Notice the caption at the bottom? Our Prompt Optimizer stripped out all the polite conversational filler words before sending the payload."
    * "We aggressively eliminated over 10 extra tokens from being processed by the API. Across a massive enterprise, this simple proxy cuts thousands of dollars in cloud bills and huge amounts of computing energy for exactly the same response."

## 🚨 3. The Edge Case (Unbreakable Fallback Demo)
*   **Setup:** Before demoing this phase, go to your terminal and stop your Ollama server (`Ctrl+C` or quit Ollama).
*   **Action:** Leave engine on `Auto`. Type `"What is 2+2?"` again.
*   **What happens:** 
    * The frontend triggers a routing check to Local.
    * Instantly, a toast notification pops up: *"Local Engine failed. Auto-falling back to Cloud! 🚀"*
    * The UI displays the response via Gemini without throwing a nasty 500 server error to the user.
*   **The Pitch:** "What happens if a user's laptop goes offline or struggles? EcoRouter acts as an unbreakable bridge. It immediately caught the local failure and routed seamlessly to the cloud to guarantee uptime while preserving the UX."
