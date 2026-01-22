from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Mini API",
    description="Portfolio-ready FastAPI project with clean structure",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"status": "ok", "message": "FastAPI is running"}

@app.get("/health")
def health_check():
    return {"health": "green"}
