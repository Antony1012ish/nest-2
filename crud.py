from sqlalchemy.orm import Session
import models, schemas

def create_student(db: Session, student: schemas.StudentCreate):
    new_student = models.Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

def update_student(db: Session, student_id: int, student: schemas.StudentCreate):
    student_data = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student_data:
        return {"error": "Student not found"}
    for key, value in student.dict().items():
        setattr(student_data, key, value)
    db.commit()
    return student_data

def delete_student(db: Session, student_id: int):
    student_data = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student_data:
        return {"error": "Student not found"}
    db.delete(student_data)
    db.commit()
    return {"message": "Student deleted"}

def create_class(db: Session, class_: schemas.ClassCreate):
    new_class = models.Class(**class_.dict())
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    return new_class

def update_class(db: Session, class_id: int, class_: schemas.ClassCreate):
    class_data = db.query(models.Class).filter(models.Class.id == class_id).first()
    if not class_data:
        return {"error": "Class not found"}
    for key, value in class_.dict().items():
        setattr(class_data, key, value)
    db.commit()
    return class_data

def delete_class(db: Session, class_id: int):
    class_data = db.query(models.Class).filter(models.Class.id == class_id).first()
    if not class_data:
        return {"error": "Class not found"}
    db.delete(class_data)
    db.commit()
    return {"message": "Class deleted"}

def register_student_to_class(db: Session, student_id: int, class_id: int):
    registration = models.Registration(student_id=student_id, class_id=class_id)
    db.add(registration)
    db.commit()
    db.refresh(registration)
    return {"message": "Student registered successfully"}

def get_students_in_class(db: Session, class_id: int):
    registrations = db.query(models.Registration).filter(models.Registration.class_id == class_id).all()
    student_list = [db.query(models.Student).filter(models.Student.id == reg.student_id).first() for reg in registrations]
    return student_list
