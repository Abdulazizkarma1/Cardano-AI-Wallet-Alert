# Backend - Cardano AI Wallet Alerts

FastAPI backend for the Cardano AI Wallet Alerts prototype.

## Structure

```
backend/
├── app/
│   ├── routes/          # API endpoints
│   ├── models/          # Pydantic models
│   ├── services/        # Business logic (parser, listener, notifications)
│   ├── utils/           # Utility functions
│   └── main.py          # FastAPI application entry point
├── requirements.txt
└── README.md
```

## Installation

1. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Locally

Start the development server:
```bash
uvicorn app.main:app --reload --port 8000
```

The API will be available at:
- API: http://localhost:8000
- Interactive docs: http://localhost:8000/docs
- Alternative docs: http://localhost:8000/redoc

## API Endpoints

### Rules Management

- `POST /rules` - Create a new alert rule
- `GET /rules` - List all rules
- `GET /rules/{id}` - Get a specific rule
- `DELETE /rules/{id}` - Delete a rule

### Natural Language Parsing

- `POST /parse` - Convert natural language instruction into rule structure

## Example API Calls

### Create a Rule

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

### Parse Natural Language

```bash
curl -X POST "http://localhost:8000/parse" \
  -H "Content-Type: application/json" \
  -d '{
    "instruction": "Alert me when wallet addr_test1... receives more than 100 ADA in the next hour"
  }'
```

### List All Rules

```bash
curl -X GET "http://localhost:8000/rules"
```

## Mock Services

All services are currently mock implementations:

- **Parser** (`services/parser.py`): Simulates natural language parsing
- **Listener** (`services/listener.py`): Simulates blockchain event monitoring
- **Notifications** (`services/notifications.py`): Simulates notification delivery

## Future Expansion

- Replace mock parser with actual LLM integration (OpenAI, Anthropic, etc.)
- Integrate with Cardano APIs (Blockfrost, Koios) for real blockchain data
- Add database persistence (PostgreSQL, MongoDB)
- Implement background task queue (Celery, RQ) for continuous monitoring
- Add authentication and user management
- Implement rate limiting and request validation


