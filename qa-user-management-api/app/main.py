
from fastapi import FastAPI

app = FastAPI(
    title="User Management API",
    description="A REST API for managing users",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "User Management API is running",
        "status": "success"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }