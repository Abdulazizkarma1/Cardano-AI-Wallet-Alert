# Frontend - Cardano AI Wallet Alerts

React frontend for the Cardano AI Wallet Alerts prototype.

## Structure

```
frontend/
├── public/
│   └── index.html
├── src/
│   ├── components/      # React components
│   │   ├── RuleForm.js
│   │   └── RulesList.js
│   ├── services/        # API service layer
│   │   └── api.js
│   ├── App.js
│   ├── App.css
│   ├── index.js
│   └── index.css
├── package.json
└── README.md
```

## Installation

1. Install dependencies:
```bash
npm install
```

## Running Locally

Start the development server:
```bash
npm start
```

The app will open at http://localhost:3000

Make sure the backend API is running on http://localhost:8000

## Features

- **Create Rules**: Form to create new wallet alert rules
- **Natural Language Parsing**: Option to input natural language instructions and parse them into structured rules
- **Rules List**: View all created rules
- **Mock Backend Integration**: Connects to FastAPI backend

## Environment Variables

Create a `.env` file to configure the API URL:

```
REACT_APP_API_URL=http://localhost:8000
```

## Build for Production

```bash
npm run build
```

This creates an optimized production build in the `build/` folder.


