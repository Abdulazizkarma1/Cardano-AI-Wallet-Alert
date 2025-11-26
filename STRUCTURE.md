# Repository Structure

Complete folder tree for Cardano AI Wallet Alerts prototype:

```
ai-wallet/
├── .gitignore
├── README.md
├── STRUCTURE.md
│
├── backend/
│   ├── README.md
│   ├── requirements.txt
│   └── app/
│       ├── __init__.py
│       ├── main.py
│       ├── models/
│       │   └── rule.py
│       ├── routes/
│       │   ├── __init__.py
│       │   ├── rules.py
│       │   └── parse.py
│       ├── services/
│       │   ├── parser.py
│       │   ├── listener.py
│       │   └── notifications.py
│       └── utils/
│           └── __init__.py
│
└── frontend/
    ├── README.md
    ├── package.json
    ├── .gitignore
    ├── public/
    │   └── index.html
    └── src/
        ├── index.js
        ├── index.css
        ├── App.js
        ├── App.css
        ├── components/
        │   ├── RuleForm.js
        │   └── RulesList.js
        └── services/
            └── api.js
```

## File Count Summary

- **Backend**: 12 files
- **Frontend**: 10 files
- **Documentation**: 3 files
- **Total**: 25 files

## Key Files

### Backend
- `app/main.py` - FastAPI application entry point
- `app/models/rule.py` - Pydantic models for rules
- `app/routes/rules.py` - Rule management endpoints
- `app/routes/parse.py` - Natural language parsing endpoint
- `app/services/parser.py` - Mock AI parser
- `app/services/listener.py` - Mock blockchain listener
- `app/services/notifications.py` - Mock notification service

### Frontend
- `src/App.js` - Main React component
- `src/components/RuleForm.js` - Rule creation form
- `src/components/RulesList.js` - Rules display component
- `src/services/api.js` - API client


