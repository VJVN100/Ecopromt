## 📄 TECH_STACK.md — EcoRouter

**App Details:**
* **Type:** Web Application
* **Scale:** MVP (Hackathon/Startup Prototype)
* **Team Size:** 1 Developer (Vijay)
* **MVP Date:** March 28, 2026

---

### 🎨 1. Frontend Stack

| Category | Technology | Version | License | Reason |
| :--- | :--- | :--- | :--- | :--- |
| **Framework** | **Streamlit** | 1.28.0+ | Apache 2.0 | Fastest way to build Python-based UIs with interactive widgets. |
| **Language** | **Python** | 3.9.7 | PSF | Unified language for Frontend and AI logic. |
| **Styling** | **Custom CSS** | N/A | N/A | Injected via `st.markdown` to achieve the rounded search bar look. |
| **State** | **Streamlit Session State** | 1.32.0 | Apache 2.0 | Built-in state management for prompt history and API keys. |
| **UI Components** | **Streamlit-Extras** | 0.4.0 | Apache 2.0 | Used for the "Impact Gauges" and status pills. |

* **Alternatives Considered:** **React/Next.js** (Rejected: Too high overhead for a 48-hour hackathon).

---

### ⚙️ 2. Backend Stack

| Category | Technology | Version | License | Reason |
| :--- | :--- | :--- | :--- | :--- |
| **Runtime** | **Python** | 3.9.7 | PSF | Native support for AI libraries and local system calls. |
| **Framework** | **FastAPI** | 0.110.0 | MIT | Asynchronous handling of concurrent LLM requests. |
| **AI (Cloud)** | **Google Generative AI** | 0.4.1 | Apache 2.0 | SDK for Gemini 1.5 Flash integration. |
| **AI (Local)** | **Ollama-Python** | 0.1.7 | MIT | Official Python client to interact with the local Ollama server. |
| **Analysis** | **TextBlob** | 0.18.0 | MIT | Lightweight sentiment/complexity analysis without heavy models. |

* **Alternatives Considered:** **Node.js** (Rejected: Python has superior native support for the AI ecosystem).

---

### 🚀 3. DevOps & Hosting

| Category | Technology | Version | License | Reason |
| :--- | :--- | :--- | :--- | :--- |
| **Version Control** | **Git** | 2.43.0 | GPL-2.0 | Industry standard for branch management. |
| **Hosting (App)** | **Streamlit Cloud** | N/A | Free Tier | Easiest deployment for Streamlit apps with GitHub sync. |
| **CI/CD** | **GitHub Actions** | v4 | MIT | Automates linting and deployment on every push. |
| **Testing** | **Pytest** | 8.0.2 | MIT | Simple framework for testing the ESIF formula logic. |

---

### 🛠️ 4. Development Tools
* **IDE:** Visual Studio Code (v1.87.0)
* **Linter:** **Flake8** (v7.0.0)
* **Formatter:** **Black** (v24.2.0)
* **Git Hooks:** **Pre-commit** (v3.6.2) to ensure no unformatted code is pushed.

---

### 🔑 5. Environment Variables

| Variable Name | Description | Required |
| :--- | :--- | :--- |
| `GEMINI_API_KEY` | Your Google AI Studio API key for cloud routing. | Yes |
| `OLLAMA_BASE_URL` | URL for local Ollama instance (default: `http://localhost:11434`). | Yes |
| `APP_ENV` | Mode of operation (`development` or `production`). | No |

---

### 📜 6. Scripts (Requirements.txt approach)
Since this is a Python project, `package.json` logic is handled via `Makefile` or CLI:
* **Dev:** `streamlit run main.py`
* **Build:** `pip install -r requirements.txt`
* **Test:** `pytest tests/`

---

### 📦 7. Exact Dependency Versions

```json
{
  "dependencies": {
    "streamlit": "latest compatible",
    "fastapi": "0.110.0",
    "google-generativeai": "0.4.1",
    "ollama": "0.1.7",
    "textblob": "0.18.0.post0",
    "python-dotenv": "1.0.1",
    "uvicorn": "0.27.1",
    "pytest": "8.0.2",
    "streamlit-extras": "0.4.0"
  }
}
```

---

### 🛡️ 8. Security Considerations
* **Auth Flow:** API keys are never hardcoded; they are stored in a `.env` file or Streamlit Secrets.
* **CORS:** FastAPI is configured with `CORSMiddleware` to allow requests only from the Streamlit frontend.
* **Rate Limits:** Basic logic implemented in the Backend to prevent "Prompt Spamming" to the Gemini API.
* **Input Sanitization:** Regex filters to prevent prompt injection attacks before routing.

---

### 🔄 9. Version Upgrade Policy
* **Hackathon Phase:** No upgrades will be performed during the 48-hour build to ensure stability.
* **Post-MVP:** Monthly audits of dependencies. Security patches will be applied within 48 hours of release. Major framework shifts (e.g., Streamlit 2.0) will require a dedicated "Migration Branch" for testing before merging.