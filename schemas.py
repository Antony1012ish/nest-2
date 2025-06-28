from pydantic import BaseModel

class ClassBase(BaseModel):
    name: str
    teacher: str

class ClassCreate(ClassBase):
    pass

class Class(ClassBase):
    id: int
    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    name: str
    email: str
    class_id: int

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    class Config:
        orm_mode = True
