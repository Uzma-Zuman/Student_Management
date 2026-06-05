from pydantic import BaseModel
from typing import List
# Student
class Student(BaseModel):
    id: int
    name: str
    age: int

# Course
class Course(BaseModel):
    id: int
    title: str
    teacher: str

# Enrollment
class Enrollment(BaseModel):
    student_id: int
    course_id: int