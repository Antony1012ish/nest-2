from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Class(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    teacher = Column(String, index=True)
    students = relationship("Student", back_populates="class_")

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    class_id = Column(Integer, ForeignKey("classes.id"))
    class_ = relationship("Class", back_populates="students")
