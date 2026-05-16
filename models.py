from database import students, courses, enrollments

# ================= STUDENTS =================

def add_student(student):
    students.append(student)
    return {"message": "Student added"}

def get_students():
    return students

def update_student(student_id, updated_student):
    for i in range(len(students)):
        if students[i].id == student_id:
            students[i] = updated_student
            return {"message": "Student updated"}
    return {"error": "Student not found"}

def delete_student(student_id):
    for s in students:
        if s.id == student_id:
            students.remove(s)
            return {"message": "Student deleted"}
    return {"error": "Student not found"}


# ================= COURSES =================

def add_course(course):
    courses.append(course)
    return {"message": "Course added"}

def get_courses():
    return courses

def update_course(course_id, updated_course):
    for i in range(len(courses)):
        if courses[i].id == course_id:
            courses[i] = updated_course
            return {"message": "Course updated"}
    return {"error": "Course not found"}

def delete_course(course_id):
    for c in courses:
        if c.id == course_id:
            courses.remove(c)
            return {"message": "Course deleted"}
    return {"error": "Course not found"}


# ================= ENROLLMENT =================

def enroll_student(data):
    student_exists = any(s.id == data.student_id for s in students)
    course_exists = any(c.id == data.course_id for c in courses)

    if not student_exists:
        return {"error": "Student not found"}
    if not course_exists:
        return {"error": "Course not found"}

    enrollments.append(data)
    return {"message": "Enrolled successfully"}

def get_student_courses(student_id):
    result = []
    for e in enrollments:
        if e.student_id == student_id:
            for c in courses:
                if c.id == e.course_id:
                    result.append(c)
    return result

def get_course_students(course_id):
    result = []
    for e in enrollments:
        if e.course_id == course_id:
            for s in students:
                if s.id == e.student_id:
                    result.append(s)
    return result