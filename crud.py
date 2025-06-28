from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_class(c: schemas.ClassCreate):
    with SessionLocal() as db:
        db_class = models.Class(**c.dict())
        db.add(db_class)
        db.commit()
        db.refresh(db_class)
        return db_class

def update_class(class_id: int, c: schemas.ClassCreate):
    with SessionLocal() as db:
        cls = db.get(models.Class, class_id)
        if not cls:
            raise HTTPException(status_code=404, detail="Class not found")
        cls.name, cls.teacher = c.name, c.teacher
        db.commit()
        db.refresh(cls)
        return cls

def delete_class(class_id: int):
    with SessionLocal() as db:
        cls = db.get(models.Class, class_id)
        if not cls:
            raise HTTPException(status_code=404, detail="Class not found")
        db.delete(cls)
        db.commit()

def create_student(s: schemas.StudentCreate):
    with SessionLocal() as db:
        db_student = models.Student(**s.dict())
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student

def update_student(student_id: int, s: schemas.StudentCreate):
    with SessionLocal() as db:
        stu = db.get(models.Student, student_id)
        if not stu:
            raise HTTPException(status_code=404, detail="Student not found")
        stu.name, stu.email, stu.class_id = s.name, s.email, s.class_id
        db.commit()
        db.refresh(stu)
        return stu

def delete_student(student_id: int):
    with SessionLocal() as db:
        stu = db.get(models.Student, student_id)
        if not stu:
            raise HTTPException(status_code=404, detail="Student not found")
        db.delete(stu)
        db.commit()

def get_students():
    with SessionLocal() as db:
        return db.query(models.Student).all()

def get_students_by_class(class_id: int):
    with SessionLocal() as db:
        return db.query(models.Student).filter(models.Student.class_id == class_id).all()
