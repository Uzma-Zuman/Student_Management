from database import *


# ================= STUDENTS =================

def add_student(student):

    existing = students_collection.find_one({
        "id": student.id
    })

    if existing:
        return {
            "error": "Student already exists"
        }

    students_collection.insert_one(
        student.dict()
    )

    return {
        "message": "Student added"
    }


def get_students():
    return list(students_collection.find({}, {"_id": 0}))


def update_student(student_id, updated_student):

    result = students_collection.update_one(
        {"id": student_id},
        {"$set": updated_student.dict()}
    )

    if result.modified_count:
        return {"message": "Student updated"}

    return {"error": "Student not found"}


def delete_student(student_id):

    result = students_collection.delete_one(
        {"id": student_id}
    )

    if result.deleted_count:
        return {"message": "Student deleted"}

    return {"error": "Student not found"}

def add_multiple_students(new_students):

    added = []
    errors = []

    for student in new_students:

        existing = students_collection.find_one({
            "id": student.id
        })

        if existing:
            errors.append(
                f"Student {student.id} already exists"
            )

        else:

            data = student.dict()

            students_collection.insert_one(data)

            added.append(data)

    return {
        "added": added,
        "errors": errors
    }
# ================= COURSES =================

def add_course(course):

    existing = courses_collection.find_one({
        "id": course.id
    })

    if existing:
        return {
            "error": "Course already exists"
        }

    courses_collection.insert_one(
        course.dict()
    )

    return {
        "message": "Course added"
    }

def get_courses():
    return list(
        courses_collection.find(
            {},
            {"_id": 0}
        )
    )


def update_course(course_id, updated_course):

    result = courses_collection.update_one(
        {"id": course_id},
        {"$set": updated_course.dict()}
    )

    if result.modified_count:
        return {"message": "Course updated"}

    return {"error": "Course not found"}


def delete_course(course_id):

    result = courses_collection.delete_one(
        {"id": course_id}
    )

    if result.deleted_count:
        return {"message": "Course deleted"}

    return {"error": "Course not found"}


def add_multiple_courses(new_courses):

    added = []
    errors = []

    for course in new_courses:

        existing = courses_collection.find_one({
            "id": course.id
        })

        if existing:
            errors.append(
                f"Course {course.id} already exists"
            )

        else:

            data = course.dict()

            courses_collection.insert_one(data)

            added.append(data)

    return {
        "added": added,
        "errors": errors
    }

# ================= ENROLLMENTS =================

def enroll_student(e):

    student = students_collection.find_one({
        "id": e.student_id
    })

    course = courses_collection.find_one({
        "id": e.course_id
    })

    if not student:
        return {
            "error": "Student not found"
        }

    if not course:
        return {
            "error": "Course not found"
        }

    already = enrollments_collection.find_one({
        "student_id": e.student_id,
        "course_id": e.course_id
    })

    if already:
        return {
            "error": "Already enrolled"
        }

    enrollments_collection.insert_one(
        e.dict()
    )

    return {
        "message": "Enrolled successfully"
    }


def enroll_multiple(data_list):

    added = []
    errors = []

    for e in data_list:

        student = students_collection.find_one({
            "id": e.student_id
        })

        course = courses_collection.find_one({
            "id": e.course_id
        })

        if not student:
            errors.append(
                f"Student {e.student_id} not found"
            )
            continue

        if not course:
            errors.append(
                f"Course {e.course_id} not found"
            )
            continue

        already = enrollments_collection.find_one({
            "student_id": e.student_id,
            "course_id": e.course_id
        })

        if already:
            errors.append(
                f"Already enrolled"
            )
            continue

        enrollments_collection.insert_one(
            e.dict()
        )

        added.append(
            e.dict()
        )

    return {
        "added": added,
        "errors": errors
    }

def delete_enrollment(
    student_id,
    course_id
):

    result = enrollments_collection.delete_one({
        "student_id": student_id,
        "course_id": course_id
    })

    if result.deleted_count:
        return {
            "message": "Enrollment deleted"
        }

    return {
        "error": "Enrollment not found"
    }
def get_all_enrollments():

    return list(
        enrollments_collection.find(
            {},
            {"_id": 0}
        )
    )


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