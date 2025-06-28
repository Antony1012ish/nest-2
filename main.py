from fastapi import FastAPI
from database import engine
import models
from routers import students, classes

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI app deployed successfully"}

app.include_router(students.router, prefix="/students", tags=["Students"])
app.include_router(classes.router, prefix="/classes", tags=["Classes"])
