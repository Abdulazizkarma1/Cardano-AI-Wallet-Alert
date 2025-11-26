"""
FastAPI main application entry point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import rules, parse

app = FastAPI(
    title="Cardano AI Wallet Alerts API",
    description="Prototype API for natural language wallet alert rules",
    version="0.1.0"
)

# CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(rules.router)
app.include_router(parse.router)


@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "name": "Cardano AI Wallet Alerts API",
        "version": "0.1.0",
        "status": "running",
        "endpoints": {
            "POST /rules": "Create a new alert rule",
            "GET /rules": "List all rules",
            "GET /rules/{id}": "Get a specific rule",
            "DELETE /rules/{id}": "Delete a rule",
            "POST /parse": "Parse natural language into rule structure"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


