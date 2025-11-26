# Cardano AI Wallet Alerts - Prototype

A prototype repository demonstrating the structure and approach for a natural language wallet alert system for Cardano blockchain.

## 🎯 Project Overview

This is a **prototype** repository that demonstrates the architecture and feasibility of a system that:
- Converts natural language instructions into structured wallet alert rules
- Monitors Cardano wallets for specified conditions
- Sends notifications when conditions are met

**Important**: This is a mock/prototype implementation. No real blockchain integrations or AI services are used.

## 📁 Repository Structure

```
ai-wallet/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── routes/         # API endpoints
│   │   ├── models/         # Pydantic data models
│   │   ├── services/       # Business logic (parser, listener, notifications)
│   │   ├── utils/          # Utility functions
│   │   └── main.py         # FastAPI application
│   ├── requirements.txt
│   └── README.md
├── frontend/                # React frontend
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── services/       # API service layer
│   │   └── ...
│   ├── package.json
│   └── README.md
└── README.md               # This file
```

## 🏗️ Architecture Overview

### Backend (FastAPI)

The backend is organized into modular components:

- **Routes** (`/routes`): API endpoints for rule management and parsing
- **Models** (`/models`): Pydantic schemas for data validation
- **Services** (`/services`):
  - `parser.py`: Mock natural language → rule parser
  - `listener.py`: Mock blockchain event listener
  - `notifications.py`: Mock notification dispatcher
- **Utils** (`/utils`): Shared utility functions

### Frontend (React)

Simple React application with:
- Rule creation form (with natural language parsing option)
- Rules list view
- API integration layer

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 14+
- npm or yarn

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Start the server:
```bash
uvicorn app.main:app --reload --port 8000
```

The API will be available at:
- API: http://localhost:8000
- Interactive docs: http://localhost:8000/docs

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The app will open at http://localhost:3000

## 📡 API Endpoints

### Rules Management

- `POST /rules` - Create a new alert rule
- `GET /rules` - List all rules
- `GET /rules/{id}` - Get a specific rule
- `DELETE /rules/{id}` - Delete a rule

### Natural Language Parsing

- `POST /parse` - Convert natural language instruction into rule structure

### Example API Calls

#### Create a Rule

```bash
curl -X POST "http://localhost:8000/rules" \
  -H "Content-Type: application/json" \
  -d '{
    "wallet_address": "addr_test1...",
    "condition": "receive > 100 ADA",
    "timeframe": "1h",
    "notification_channel": "email"
  }'
```

#### Parse Natural Language

```bash
curl -X POST "http://localhost:8000/parse" \
  -H "Content-Type: application/json" \
  -d '{
    "instruction": "Alert me when wallet addr_test1... receives more than 100 ADA in the next hour"
  }'
```

#### List All Rules

```bash
curl -X GET "http://localhost:8000/rules"
```

## 🔧 Mock Implementation Details

All services are currently **mock implementations**:

### Parser Service (`services/parser.py`)
- Uses simple regex pattern matching
- Extracts wallet addresses, amounts, conditions, and timeframes
- In production: Would use LLM (OpenAI, Anthropic) or NLP models

### Listener Service (`services/listener.py`)
- Simulates blockchain event detection with random results
- In production: Would connect to Cardano APIs (Blockfrost, Koios) or Cardano node

### Notification Service (`services/notifications.py`)
- Prints notifications to console
- In production: Would integrate with email (SendGrid), SMS (Twilio), push (FCM), or webhooks

## 🔮 Future Module Expansion

### Backend Enhancements

1. **AI Integration**
   - Replace mock parser with OpenAI GPT-4 or Anthropic Claude
   - Add prompt engineering for better rule extraction
   - Implement confidence scoring for parsed rules

2. **Blockchain Integration**
   - Integrate with Blockfrost API or Koios API
   - Add real-time transaction monitoring
   - Implement WebSocket connections for live updates

3. **Database Persistence**
   - Add PostgreSQL or MongoDB for rule storage
   - Implement user authentication and multi-tenancy
   - Add rule history and event logging

4. **Background Processing**
   - Implement Celery or RQ for async task processing
   - Add scheduled polling for wallet monitoring
   - Implement retry logic and error handling

5. **Notification Channels**
   - Email: SendGrid, AWS SES
   - SMS: Twilio, AWS SNS
   - Push: Firebase Cloud Messaging
   - Webhook: HTTP POST with retry logic

### Frontend Enhancements

1. **User Interface**
   - Add user authentication
   - Implement rule editing
   - Add rule testing/preview
   - Create dashboard with statistics

2. **Features**
   - Real-time updates via WebSocket
   - Rule templates and presets
   - Notification history
   - Export/import rules

## 📝 Development Notes

- **Data Storage**: Currently uses in-memory storage. Rules are lost on server restart.
- **Error Handling**: Basic error handling implemented. Production would need comprehensive error handling.
- **Security**: No authentication/authorization. CORS is open for development.
- **Testing**: No tests included in prototype. Production would need unit and integration tests.

## 🎓 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [Cardano Developer Portal](https://developers.cardano.org/)
- [Blockfrost API](https://blockfrost.io/)

## 📄 License

This is a prototype repository for demonstration purposes.

## 🤝 Contributing

This is a prototype repository. For production development, consider:
- Adding comprehensive tests
- Implementing proper error handling
- Adding authentication and security
- Setting up CI/CD pipelines
- Adding monitoring and logging

---

**Note**: This prototype demonstrates structure and feasibility. All implementations are mock/dummy services and should not be used in production without proper integration and security measures.

# Cardano-AI-Wallet-Alert

