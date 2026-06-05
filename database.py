from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# ================= MONGODB CONNECTION =================

client = MongoClient(
    "mongodb://localhost:27017",
    serverSelectionTimeoutMS=5000
)

try:
    client.admin.command("ping")
    print("✅ MongoDB Connected")
except ConnectionFailure:
    print("❌ MongoDB Connection Failed")

# ================= DATABASE =================

db = client["student_management"]

# ================= COLLECTIONS =================

students_collection = db["students"]
courses_collection = db["courses"]
enrollments_collection = db["enrollments"]

# ================= INDEXES =================

students_collection.create_index(
    "id",
    unique=True
)

courses_collection.create_index(
    "id",
    unique=True
)

enrollments_collection.create_index(
    [
        ("student_id", 1),
        ("course_id", 1)
    ],
    unique=True
)