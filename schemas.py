from pydantic import BaseModel
from datetime import date

class StudentCreate(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    age: int
    city: str

class ClassCreate(BaseModel):
    class_name: str
    description: str
    start_date: date
    end_date: date
    hours: int

class StudentClassRegister(BaseModel):
    student_id: int
    class_id: int
