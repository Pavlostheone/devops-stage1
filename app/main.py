from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", "service": "stage1-demo"}

@app.get("/health")
def health_check():
    return{"status": "healthy"}
