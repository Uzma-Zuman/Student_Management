from fastapi import FastAPI
import models
import schemas
from typing import List

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ================= STUDENTS =================

@app.post("/students/bulk")
def create_students(students: List[schemas.Student]):
    return models.add_multiple_students(students)

@app.get("/students")
def read_students():
    return models.get_students()

@app.put("/students/{student_id}")
def update_student(student_id: int, student: schemas.Student):
    return models.update_student(student_id, student)

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    return models.delete_student(student_id)


# ================= COURSES =================

@app.post("/courses/bulk")
def create_courses(courses: List[schemas.Course]):
    return models.add_multiple_courses(courses)

@app.get("/courses")
def read_courses():
    return models.get_courses()

@app.put("/courses/{course_id}")
def update_course(course_id: int, course: schemas.Course):
    return models.update_course(course_id, course)

@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    return models.delete_course(course_id)


# ================= ENROLLMENT =================

@app.post("/enroll/bulk")
def enroll_bulk(data: List[schemas.Enrollment]):
    return models.enroll_multiple(data)

@app.get("/students/{student_id}/courses")
def student_courses(student_id: int):
    return models.get_student_courses(student_id)

@app.get("/courses/{course_id}/students")
def course_students(course_id: int):
    return models.get_course_students(course_id)

@app.get("/enrollments")
def get_all_enrollments():
    return models.get_all_enrollments()