# Cardano AI Wallet Alerts — Prototype  
**AI-powered event trigger framework for Cardano (Prototype Version)**  
![status](https://img.shields.io/badge/status-prototype-blue)  
![license](https://img.shields.io/badge/license-MIT-green)  
![language](https://img.shields.io/badge/language-Python%20%7C%20FastAPI-orange)  

This repository contains a **minimal, structured prototype** demonstrating the architecture of the *Cardano AI Wallet Alerts* system.  
It is **not** a full implementation — the goal is to show feasibility, structure, and developer capability for future development.

---

## 🚀 Overview

**Cardano AI Wallet Alerts** allows users to set real-time Cardano wallet alerts using **plain English**, such as:

> "Notify me on Telegram when my wallet receives more than 200 ADA in one hour."

This prototype demonstrates:

- Modular backend architecture  
- Mock AI natural-language parser  
- Mock blockchain event listener  
- Mock notification system  
- FastAPI endpoints  
- Optional minimal frontend  

---

## 📁 Repository Structure



## 📁 Repository Structure

```
/
├── backend/
│ ├── app/
│ │ ├── routes/
│ │ ├── services/
│ │ ├── models/
│ │ ├── utils/
│ │ └── main.py
│ ├── requirements.txt
│ └── README.md
│
├── frontend/ (optional UI prototype)
│ ├── src/
│ ├── package.json
│ └── README.md
│
└── docs/
├── ARCHITECTURE.md
├── API_REFERENCE.md
└── ROADMAP.md


---

## 🧠 Key Prototype Components

### 1️⃣ Mock AI Rule Parser  
Located in `backend/app/services/parser.py`

```python
def parse_instruction(text: str):
    return {
        "instruction": text,
        "parsed_rule": {
            "wallet": "addr_test1...",
            "condition": "receive > 100 ADA",
            "timeframe": "1h"
        }
    }

2️⃣ Mock Blockchain Listener

backend/app/services/listener.py

def check_wallet_events(rule):
    return {"event_detected": False}

3️⃣ Mock Notification Dispatcher

backend/app/services/notifications.py

def send_notification(channel, message):
    print(f"[{channel.upper()}] {message}")

4️⃣ FastAPI Endpoints

POST /parse – Convert natural-language → rule

POST /rules – Create rule

GET /rules – List rules

GET /health – System status

▶️ Running the Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

🧪 Example API Test
Parse instruction
curl -X POST http://localhost:8000/parse \
  -H "Content-Type: application/json" \
  -d '{"instruction": "Notify me when wallet X gets 50 ADA"}'

🛠 Technologies Used

Python + FastAPI

Mock AI parsing logic

Mock Cardano listener

Mock notification system

React/Next.js (optional UI prototype)

📚 Documentation
Document	Description
ARCHITECTURE.md
	System design + diagrams
API_REFERENCE.md
	All mock API endpoints
ROADMAP.md
	Future development plan
🧭 Project Status

This repository represents Phase 0 – Prototype feasibility.
It provides the foundation required to proceed toward a full implementation.

🤝 Contributing

This project is open-source under the MIT License.
Issues, suggestions, and PRs are welcome.

🧵 Related Proposal

This prototype supports the Catalyst proposal:

"Cardano AI Wallet Alerts for Instant Blockchain Events" (Fund 1)


---

# ✅ **`docs/ARCHITECTURE.md` (GitHub Ready)**  
Copy to: `docs/ARCHITECTURE.md`

---

```markdown
# 🏗 Architecture Overview — Cardano AI Wallet Alerts

This document describes the prototype architecture for the Cardano AI Wallet Alerts system.

---

## 🧱 High-Level System Overview



User → Natural Instruction → AI Parser → Rule Engine → Event Listener → Notification System


Each module in this prototype is implemented in **mock mode** to demonstrate structure and feasibility.

---

## 🔧 Modules

### **1. AI Rule Parser**
Converts plain English instructions into structured rule JSON.

Example:
```json
{
  "wallet": "addr...",
  "condition": "receive > 100 ADA",
  "timeframe": "1h"
}

2. Rule Engine

Handles:

Rule creation

Rule storage (in-memory prototype)

Rule listing

3. Blockchain Listener

Monitors blockchain activity (mock).

Real implementation will use:

Koios

Blockfrost

Optional lightweight listener

4. Notification System

Sends alerts through:

Telegram

Email

Discord

SMS

Webhooks

In the prototype, notifications print to console.

📦 Folder Structure Visualization
backend/app
│
├── routes/        # API endpoints
├── services/      # Core business logic
├── models/        # Data models
└── utils/         # Helpers

📈 Real Project Scaling Path

Replace mock parser → real LLM

Replace mock listener → Koios / Blockfrost streams

Add database for rule persistence

Add authentication

Add SDK & developer tools


---

# ✅ **`docs/API_REFERENCE.md` (GitHub Ready)**  
Copy to: `docs/API_REFERENCE.md`

---

```markdown
# 📘 API Reference — Prototype Version

This document lists the API endpoints available in this prototype.

---

## **GET /health**
Returns system status.

### Response:
```json
{"status": "ok"}

POST /parse

Converts a natural-language instruction into a structured rule.

Request:
{
  "instruction": "Notify me when wallet X receives 50 ADA"
}

Response (mock):
{
  "instruction": "...",
  "parsed_rule": { ... }
}

POST /rules

Create a new rule.

Request:
{
  "wallet": "addr_test1...",
  "rule": "receive > 50 ADA"
}

GET /rules

Lists stored rules.


---

# ✅ **`docs/ROADMAP.md` (GitHub Ready)**  
Copy to: `docs/ROADMAP.md`

---

```markdown
# 🛣 Roadmap — From Prototype to Full System

This roadmap outlines the progression from this prototype to a complete production system.

---

## 🚀 Phase 0 — Prototype (This Repo)
- Mock AI parser  
- Mock blockchain listener  
- Mock notifications  
- FastAPI endpoints  
- Minimal UI structure  
- Documentation  

---

## 🚀 Phase 1 — AI Integration
- Connect real LLMs (OpenAI or open-source)  
- Build training data for event rules  
- Add validation engine  

---

## 🚀 Phase 2 — Blockchain Integration
- Koios API indexing  
- Blockfrost API indexing  
- Event streaming  
- Error handling and retries  

---

## 🚀 Phase 3 — Persistence Layer
- PostgreSQL or SQLite  
- User accounts  
- Rule history  
- Event logs  

---

## 🚀 Phase 4 — Notification Channels
- Telegram bot  
- Email integration  
- Discord bot  
- SMS  
- Webhooks  

---

## 🚀 Phase 5 — Web Dashboard
- Rule creator  
- Rule management  
- Real-time event view  
- Analytics dashboard  

---

## 🚀 Phase 6 — SDK + Developer Tools
- Python SDK  
- JavaScript SDK  
- Webhooks API  
- CLI tools  

---

## 🚀 Phase 7 — Production Deployment
- CI/CD  
- Load balancing  
- Monitoring & alerting  
- Full open-source release  

---


# Cardano-AI-Wallet-Alert

