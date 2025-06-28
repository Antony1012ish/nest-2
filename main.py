from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI deployed successfully"}

@app.get("/ping")
def ping():
    return {"ping": "pong"}
