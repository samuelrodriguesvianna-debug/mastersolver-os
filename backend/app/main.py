from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="MasterSolver-OS",
    description="Operating System for Governance, Risk and Decision Intelligence",
    version="0.1.0-mvp"
)

@app.get("/")
def root():
    return {
        "product": "MasterSolver-OS",
        "status": "running",
        "message": "Governance intelligence engine online"
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat(),
        "engine": "mastersolver-os"
    }
