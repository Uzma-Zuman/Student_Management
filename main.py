from fastapi import FastAPI
import models
import schemas

app = FastAPI()

# ================= STUDENTS =================

@app.post("/students")
def create_student(student: schemas.Student):
    return models.add_student(student)

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

@app.post("/courses")
def create_course(course: schemas.Course):
    return models.add_course(course)

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

@app.post("/enroll")
def enroll(data: schemas.Enrollment):
    return models.enroll_student(data)

@app.get("/students/{student_id}/courses")
def student_courses(student_id: int):
    return models.get_student_courses(student_id)

@app.get("/courses/{course_id}/students")
def course_students(course_id: int):
    return models.get_course_students(course_id)