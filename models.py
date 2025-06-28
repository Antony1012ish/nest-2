from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    city = Column(String)
    registrations = relationship("Registration", back_populates="student")

class Class(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String)
    description = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    hours = Column(Integer)
    registrations = relationship("Registration", back_populates="class_")

class Registration(Base):
    __tablename__ = "registrations"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    class_id = Column(Integer, ForeignKey("classes.id"))

    student = relationship("Student", back_populates="registrations")
    class_ = relationship("Class", back_populates="registrations")
