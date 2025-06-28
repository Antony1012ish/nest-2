from fastapi import FastAPI, HTTPException
from database import SessionLocal, engine, Base
import models, schemas, crud

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI deployed successfully"}

@app.post("/classes/", response_model=schemas.Class)
def create_class(c: schemas.ClassCreate):
    return crud.create_class(c)

@app.put("/classes/{class_id}", response_model=schemas.Class)
def update_class(class_id: int, c: schemas.ClassCreate):
    return crud.update_class(class_id, c)

@app.delete("/classes/{class_id}")
def delete_class(class_id: int):
    crud.delete_class(class_id)
    return {"ok": True}

@app.post("/students/", response_model=schemas.Student)
def create_student(s: schemas.StudentCreate):
    return crud.create_student(s)

@app.put("/students/{student_id}", response_model=schemas.Student)
def update_student(student_id: int, s: schemas.StudentCreate):
    return crud.update_student(student_id, s)

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    crud.delete_student(student_id)
    return {"ok": True}

@app.get("/students/", response_model=list[schemas.Student])
def read_students():
    return crud.get_students()

@app.get("/classes/{class_id}/students", response_model=list[schemas.Student])
def get_class_students(class_id: int):
    return crud.get_students_by_class(class_id)
