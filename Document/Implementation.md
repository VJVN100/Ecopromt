## 📄 IMPLEMENTATION_PLAN.md — EcoRouter

**Tech Stack:** FastAPI, Streamlit, Ollama, Gemini API  
**MVP Features:** Complexity Analysis, Routing Engine, ESIF Scoring, Web UI  
**Timeline:** 7 Days (Hackathon Sprint)

---

### 🏗️ Phase 1: Project Setup & Foundation
**Duration:** 1 Day  
**Goal:** Initialize environment, repository, and service connectivity.

1.  **Environment Initialization (4 hrs):** ```bash
    python -m venv venv
    source venv/bin/activate  # venv\Scripts\activate on Windows
    pip install streamlit==1.32.0 fastapi==0.110.0 google-generativeai==0.4.1 ollama==0.1.7 python-dotenv==1.0.1
    ```
2.  **Project Scaffolding (4 hrs):**
    Create a structure following `BACKEND_STRUCTURE.md`.
    ```text
    ├── app/
    │   ├── core/         # Routing & Logic
    │   ├── api/          # FastAPI Routes
    │   └── ui/           # Streamlit Frontend
    ├── .env              # GEMINI_API_KEY, OLLAMA_BASE_URL
    └── main.py           # Entry point
    ```
* **Success Criteria:**
    * [ ] `pip freeze` shows exact versions from `TECH_STACK.md`.
    * [ ] `.env` loaded successfully without hardcoded keys.
    * [ ] Ollama service reachable via `curl http://localhost:11434`.

---

### 🎨 Phase 2: Design System & UI Skeleton
**Duration:** 1 Day  
**Goal:** Implement the "Eco-Search" interface based on `FRONTEND_GUIDELINES.md` and user sketch.

1.  **Styling Foundation (4 hrs):**
    Inject custom CSS into Streamlit for the rounded search bar.
    ```python
    # app/ui/styles.py
    CUSTOM_CSS = """
    <style>
    .stTextInput > div > div > input {
        border-radius: 25px;
        border: 2px solid #22C55E;
    }
    </style>
    """
    ```
2.  **Layout Implementation (4 hrs):**
    Build the main container with the engine dropdown and input field.
* **Success Criteria:**
    * [ ] Search bar matches sketch (Rounded + Dropdown).
    * [ ] Mobile responsiveness works on browser resize (min 44px touch targets).

---

### 🔐 Phase 3: Authentication & Security
**Duration:** 1 Day  
**Goal:** Secure the backend and manage User/API sessions as per `BACKEND_STRUCTURE.md`.

1.  **JWT Utility (4 hrs):**
    Implement HTTP-only cookie logic for session management.
2.  **API Key Management (4 hrs):**
    Create a settings sidebar to securely input/verify `GEMINI_API_KEY`.
* **Success Criteria:**
    * [ ] 401 Unauthorized returned if routing is called without a key.
    * [ ] Key is stored in `st.session_state` and never logged.

---

### 🧠 Phase 4: Core Features (The Routing Brain)
**Duration:** 2 Days  
**Goal:** Implement the P0 features from `PRD.md`.

1.  **Complexity & Optimization Engine (Backend) (8 hrs):**
    ```python
    # app/core/complexity.py
    def analyze_prompt(text: str):
        keywords = ["explain", "analyze", "code", "compare"]
        score = sum(2 for k in keywords if k in text.lower())
        return "HIGH" if score > 4 or len(text) > 500 else "LOW"
    ```
2.  **Routing & ESIF Logic (8 hrs):**
    Implement the ESIF formula: $ESIF = \frac{(W_{model} \times 100) - (T_{total} \times 5)}{L_{tokens}}$
3.  **Frontend Integration (4 hrs):**
    Connect the "Route" button to the API and display results.
* **Success Criteria:**
    * [ ] "2+2" routes to Ollama (Local).
    * [ ] "Write a neural network in Python" routes to Gemini (Cloud).
    * [ ] ESIF Score displays immediately after response.

---

### 🧪 Phase 5: Testing
**Duration:** 1 Day  
**Goal:** Ensure reliability and fallback logic.

1.  **Unit Tests (4 hrs):**
    Run `pytest` on the ESIF formula and complexity logic.
2.  **Fallback Testing (4 hrs):**
    Manually turn off Ollama; verify system reroutes to Gemini automatically.
* **Success Criteria:**
    * [ ] 80% code coverage on core logic.
    * [ ] Zero failures in the "Local Fails -> Cloud Fallback" scenario.

---

### 🚢 Phase 6: Deployment
**Duration:** 1 Day  
**Goal:** Deploy to Streamlit Cloud for judge access.

1.  **Staging Deploy (4 hrs):**
    Push to a private GitHub branch; connect to Streamlit Cloud.
2.  **Production Polish (4 hrs):**
    Finalize README, documentation, and metadata for the demo.
* **Success Criteria:**
    * [ ] Live URL accessible with < 2s load time.
    * [ ] "System Ready" indicator is Green on first load.

---

### 📅 Milestones & Risks

| Target Date | Milestone | Deliverable |
| :--- | :--- | :--- |
| Day 2 | **UI Ready** | Fully functional sketch-based search bar. |
| Day 4 | **The Brain Ready** | Auto-routing logic + ESIF score working. |
| Day 7 | **Production Ready** | Live URL with documentation. |

**Risk Table:**
| Risk | Severity | Mitigation |
| :--- | :--- | :--- |
| Ollama Latency | High | Use the smallest model (Phi-3) to ensure < 3s response. |
| API Rate Limits | Medium | Implement the prompt optimizer to reduce token count. |
| Hardware mismatch | Medium | Clearly state system requirements (8GB RAM) for Local mode. |

---

### 🏆 Overall MVP Success Criteria
* **Accuracy:** 90% of "simple" prompts must correctly route to Local.
* **Efficiency:** Average ESIF score should be > 70 across 10 random prompts.
* **UX:** Response time for local queries must be ≤ 3 seconds.

### 🗺️ Post-MVP Roadmap (P1/P2)
* **History Dashboard:** Visual charts of carbon savings over 30 days.
* **WhisperFlow:** Voice-to-prompt routing.
* **Multi-Model Selection:** Allow users to choose between Llama 3, Mistral, and GPT-4.