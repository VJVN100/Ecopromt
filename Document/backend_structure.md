## 📄 BACKEND_STRUCTURE.md — EcoRouter

**Main Features:**
* **Prompt Complexity Engine:** Keyword and length-based routing logic.
* **Dual-Model Integration:** Seamless switching between Ollama (Local) and Gemini (Cloud).
* **ESIF Scoring:** Real-time efficiency and environmental impact calculation.
* **Usage Analytics:** Tracking savings and token usage history.

---

### 🏗️ 1. Architecture Overview
* **Pattern:** REST API built with **FastAPI**.
* **Auth Strategy:** JWT-based authentication stored in **HTTP-only cookies** to prevent XSS.
* **Data Flow:** 1. Client sends prompt + Engine preference.
    2. Backend optimizes prompt and calculates complexity.
    3. Backend routes to either Ollama (local) or Gemini (cloud).
    4. Response is logged to PostgreSQL and ESIF score is returned.
* **Caching:** Redis stores frequent query results (e.g., common definitions) to bypass LLM calls entirely.

---

### 🗄️ 2. Database Schema (PostgreSQL)

#### **Table: users**
| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | UUID | PRIMARY KEY, DEFAULT uuid_generate_v4() | Unique user identifier. |
| `email` | VARCHAR(255) | UNIQUE, NOT NULL | User's email address. |
| `password_hash` | TEXT | NOT NULL | Argon2 hashed password. |
| `gemini_api_key` | TEXT | ENCRYPTED | User-specific cloud API key. |
| `created_at` | TIMESTAMPTZ | NOT NULL, DEFAULT NOW() | Record creation time. |
| `updated_at` | TIMESTAMPTZ | NOT NULL, DEFAULT NOW() | Last update time. |

#### **Table: prompt_history**
| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | UUID | PRIMARY KEY | Unique log identifier. |
| `user_id` | UUID | FOREIGN KEY (users.id) | Links to the user. |
| `prompt_text` | TEXT | NOT NULL | The original user input. |
| `response_text` | TEXT | NOT NULL | The AI generated answer. |
| `model_used` | VARCHAR(50) | NOT NULL | "ollama" or "gemini". |
| `complexity_score` | INTEGER | NOT NULL | Calculated score (0-10). |
| `esif_score` | FLOAT | NOT NULL | The efficiency factor. |
| `tokens_saved` | INTEGER | DEFAULT 0 | Tokens removed via optimization. |
| `created_at` | TIMESTAMPTZ | DEFAULT NOW() | Interaction timestamp. |
| `updated_at` | TIMESTAMPTZ | DEFAULT NOW() | - |

**Indexes:** * `idx_history_user_id`: For fast retrieval of a specific user's logs.
* `idx_created_at`: For time-series analytics.

---

### 🌐 3. Complete API Endpoints

#### **POST /api/v1/route**
* **Auth Required:** Yes
* **Request Body:**
    ```json
    {
      "prompt": "Explain Quantum Physics simply.",
      "engine_preference": "auto"
    }
    ```
* **Validation:** `prompt` min_length: 1, max_length: 2000. `engine_preference` must be in [auto, local, cloud].
* **Success Response (200 OK):**
    ```json
    {
      "status": "success",
      "data": {
        "response": "Quantum physics is...",
        "routingDecision": "local",
        "esifScore": 88.5,
        "ecoImpact": "1.2g CO2 saved"
      }
    }
    ```
* **Error Responses:** * `401`: Token expired/missing.
    * `429`: Rate limit exceeded.
    * `503`: Both Ollama and Gemini are unreachable.

---

### 🔑 4. Authentication & Authorization
* **JWT Structure:**
    * `sub`: User UUID
    * `exp`: 24 hours from issue.
    * `iat`: Issued at.
* **Protection Levels:**
    * `Level 0 (Public)`: Login/Register, Health Check.
    * `Level 1 (User)`: Routing, History, Profile settings.
    * `Level 2 (Admin)`: System-wide analytics (not in MVP).

---

### 🧪 5. Data Validation Rules
* **Email:** Regex `^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$`.
* **Password:** Min 8 chars, 1 uppercase, 1 special character.
* **Sanitization:** All prompt inputs pass through HTML stripping to prevent injection.

---

### 🚨 6. Standardized Error Response
```json
{
  "errorCode": "ERR_OLLAMA_OFFLINE",
  "message": "Local engine is not responding. Please check your local server.",
  "timestamp": "2026-03-22T14:30:00Z"
}
```

---

### ⚡ 7. Caching Strategy
* **Tool:** Redis (v7.2)
* **What to cache:** Complexity analysis results for repetitive prompts.
* **TTL:** 1 hour for complexity scores; 5 minutes for "System Status" (Local vs Cloud availability).
* **Key Format:** `complexity:{hash_of_prompt}`

---

### 🚦 8. Rate Limiting
* **General API:** 60 requests per minute per user.
* **Auth (Login/Register):** 5 attempts per 15 minutes.
* **Routing Endpoint:** 20 requests per minute (to protect API costs).

---

### 🔄 9. Database Migration Strategy
* **Tool:** **Alembic** (Python).
* **Process:** Every schema change requires a migration script.
* **Rollback:** `alembic downgrade -1` for immediate reversal of the last change.

---

### 💾 10. Backup & Recovery
* **Frequency:** Daily automated snapshots (3 AM IST).
* **Retention:** Keep for 30 days.
* **Restore:** Point-in-time recovery via AWS RDS or managed Postgres instances.

---

### 📍 11. API Versioning
* **Strategy:** URL Versioning.
* **Current Path:** `/api/v1/`
* **Policy:** The previous version remains supported for 3 months after a new version launch.