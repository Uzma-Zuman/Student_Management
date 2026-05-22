import json
import shutil
from datetime import datetime

FILE = "data.json"


# ================= FILE HANDLING =================

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {
            "students": [],
            "courses": [],
            "enrollments": []
        }


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

    # 🔥 AUTO BACKUP FILE (DOWNLOAD TYPE)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"backup_{timestamp}.json"

    shutil.copy(FILE, backup_file)


# ================= STUDENTS =================

def add_student(student):
    data = load_data()

    if any(s["id"] == student.id for s in data["students"]):
        return {"error": "Student with this ID already exists"}

    data["students"].append(student.dict())
    save_data(data)

    return {"message": "Student added"}


def get_students():
    data = load_data()
    return data["students"]


def update_student(student_id, updated_student):
    data = load_data()

    for i in range(len(data["students"])):
        if data["students"][i]["id"] == student_id:
            data["students"][i] = updated_student.dict()
            save_data(data)
            return {"message": "Student updated"}

    return {"error": "Student not found"}


def delete_student(student_id):
    data = load_data()

    new_students = [
        s for s in data["students"] if s["id"] != student_id
    ]

    if len(new_students) == len(data["students"]):
        return {"error": "Student not found"}

    data["students"] = new_students
    save_data(data)

    return {"message": "Student deleted"}


def add_multiple_students(new_students):
    data = load_data()

    added = []
    errors = []

    for student in new_students:
        if any(s["id"] == student.id for s in data["students"]):
            errors.append(f"Student {student.id} already exists")
        else:
            data["students"].append(student.dict())
            added.append(student.dict())

    save_data(data)

    return {
        "added": added,
        "errors": errors
    }


# ================= COURSES =================

def add_course(course):
    data = load_data()

    if any(c["id"] == course.id for c in data["courses"]):
        return {"error": "Course with this ID already exists"}

    data["courses"].append(course.dict())
    save_data(data)

    return {"message": "Course added"}


def get_courses():
    data = load_data()
    return data["courses"]


def update_course(course_id, updated_course):
    data = load_data()

    for i in range(len(data["courses"])):
        if data["courses"][i]["id"] == course_id:
            data["courses"][i] = updated_course.dict()
            save_data(data)
            return {"message": "Course updated"}

    return {"error": "Course not found"}


def delete_course(course_id):
    data = load_data()

    new_courses = [
        c for c in data["courses"] if c["id"] != course_id
    ]

    if len(new_courses) == len(data["courses"]):
        return {"error": "Course not found"}

    data["courses"] = new_courses
    save_data(data)

    return {"message": "Course deleted"}


def add_multiple_courses(new_courses):
    data = load_data()

    added = []
    errors = []

    for course in new_courses:
        if any(c["id"] == course.id for c in data["courses"]):
            errors.append(f"Course {course.id} already exists")
        else:
            data["courses"].append(course.dict())
            added.append(course.dict())

    save_data(data)

    return {
        "added": added,
        "errors": errors
    }


# ================= ENROLLMENTS =================

def enroll_student(e):
    data = load_data()

    if not any(s["id"] == e.student_id for s in data["students"]):
        return {"error": "Student not found"}

    if not any(c["id"] == e.course_id for c in data["courses"]):
        return {"error": "Course not found"}

    already = any(
        x["student_id"] == e.student_id and
        x["course_id"] == e.course_id
        for x in data["enrollments"]
    )

    if already:
        return {"error": "Already enrolled"}

    data["enrollments"].append(e.dict())
    save_data(data)

    return {"message": "Enrolled successfully"}


def enroll_multiple(data_list):
    data = load_data()

    added = []
    errors = []

    for e in data_list:
        if not any(s["id"] == e.student_id for s in data["students"]):
            errors.append(f"Student {e.student_id} not found")
            continue

        if not any(c["id"] == e.course_id for c in data["courses"]):
            errors.append(f"Course {e.course_id} not found")
            continue

        already = any(
            x["student_id"] == e.student_id and
            x["course_id"] == e.course_id
            for x in data["enrollments"]
        )

        if already:
            errors.append(f"Already enrolled: {e.student_id}-{e.course_id}")
            continue

        data["enrollments"].append(e.dict())
        added.append(e.dict())

    save_data(data)

    return {
        "added": added,
        "errors": errors
    }


def get_all_enrollments():
    data = load_data()
    return data["enrollments"]


def get_student_courses(student_id):
    data = load_data()

    result = []

    for e in data["enrollments"]:
        if e["student_id"] == student_id:
            for c in data["courses"]:
                if c["id"] == e["course_id"]:
                    result.append(c)

    return result


def get_course_students(course_id):
    data = load_data()

    result = []

    for e in data["enrollments"]:
        if e["course_id"] == course_id:
            for s in data["students"]:
                if s["id"] == e["student_id"]:
                    result.append(s)

    return result