## 📄 APP_FLOW.md — EcoRouter

**App Name:** EcoRouter  
**Description:** An intelligent AI routing middleware that analyzes prompt complexity to redirect queries between local models (Ollama) and cloud APIs (Gemini), optimizing for cost, speed, and carbon footprint.

---

### 🟢 1. Entry Points
* **Direct URL:** `https://ecorouter.ai` (Main Landing/App page).
* **Localhost:** `http://localhost:8501` (For developers running the local instance).
* **GitHub/Docs:** Link from project documentation to the live demo.
* **Shared Results:** Direct links to specific ESIF score reports or "Savings Summaries."

---

### 🔄 2. Core User Flows

#### **A. Onboarding / Initial Setup**
* **Happy Path:** 1. User lands on page. 
    2. User enters Gemini API Key in the settings/sidebar.
    3. System pings Ollama (Local) to check status. 
    4. "Systems Ready" indicator turns green.
* **Error States:** * *Invalid API Key:* System rejects key; user prompted to re-enter.
    * *Ollama Not Found:* Message appears: "Ollama not detected. Please start Ollama locally to enable Eco-Routing."
* **Edge Case:** User has no internet (Local mode only enabled; Cloud options greyed out).

#### **B. Main Feature: Smart Prompt Routing**
* **Happy Path:** 1. User selects "Auto-Route" from the dropdown.
    2. User enters a prompt.
    3. Complexity Engine analyzes (Low/High).
    4. Prompt is optimized (token trimming).
    5. Response is fetched from the chosen model.
    6. UI displays Response + ESIF Score + Environmental Impact.
* **Error States:** * *Local Model Timeout:* If Ollama hangs, system auto-switches to Gemini and notifies user.
    * *Empty Input:* "Please enter a prompt" shake animation.
* **Edge Case:** Prompt is exactly on the complexity threshold (System defaults to Local to save energy).

---

### 🗺️ 3. Navigation Map (Hierarchical)
```text
Root (Main Dashboard)
├── Header (Logo, System Status)
├── Main Workspace
│   ├── Input Area (Search Bar + Engine Dropdown)
│   └── Output Area (Response + ESIF Stats)
├── Sidebar (Settings)
│   ├── API Configurations (Gemini Key)
│   ├── Model Preferences (Phi-3 vs Llama 3)
│   └── Session History (P1 Feature)
└── Footer (GitHub Link, Documentation)
```

---

### 📱 4. Screen Inventory

| Screen | Route | Access | Purpose | Key Elements | Actions |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Dashboard** | `/` | Public | Core interaction | Search Bar, Dropdown, Result Card | Input prompt, Change Engine |
| **Settings** | Sidebar | Public | Config | API Key fields, Local Model status | Save Key, Toggle Privacy mode |
| **History** | `/history`| Public | Tracking | List of past ESIF scores | Delete entry, View details |

---

### ⚖️ 5. Decision Points (IF-THEN Logic)

* **Authentication Logic:**
    * `IF` API Key is missing `AND` User tries Cloud route `THEN` Show "Key Required" tooltip.
* **Routing Logic:**
    * `IF` Complexity Score < 5 `THEN` Route to Ollama.
    * `IF` Complexity Score ≥ 5 `THEN` Route to Gemini API.
* **Empty State:**
    * `IF` No prompt history `THEN` Show "Start by asking a question" illustration in results area.

---

### ⚠️ 6. Error Handling

* **404 (Not Found):** Redirect user back to the Main Dashboard.
* **500 (API Failure):** Display: "Cloud API is currently unreachable. Switching to Local fallback."
* **Network Offline:** * *Success Path:* User can still use Ollama (Local). 
    * *Failure Path:* Gemini options are disabled; user notified of "Local-Only Mode."
* **Permission Denied:** Occurs if local firewall blocks Ollama port (11434). UI displays setup guide.

---

### 📱 7. Responsive Behavior

* **Desktop:** * Wide search bar (per sketch).
    * Side-by-side view: Prompt on left, Stats/ESIF on right.
    * Sidebar always visible for easy config.
* **Mobile:** * Search bar takes full width.
    * Stats stack vertically below the response.
    * Sidebar collapses into a "Hamburger" menu.
    * Font sizes increase for readability on small screens.

---

### 🏁 Final Logic Check
* **Action:** Click "Route" -> **Next Step:** Show "Analyzing Complexity..." loader.
* **Action:** Input API Key -> **Next Step:** Verify and update "System Status" light to Green.
* **Action:** Local Model Fails -> **Next Step:** Trigger Gemini Fallback + Display warning toast.