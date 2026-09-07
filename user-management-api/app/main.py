from fastapi import FastAPI

app = FastAPI(
    title="QA User Management API",
    description="Production-style User Management REST API",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "user-management-api",
    }