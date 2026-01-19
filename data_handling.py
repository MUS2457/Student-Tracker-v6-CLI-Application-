from datetime import datetime
import json
from json import JSONDecodeError
from student_class_oop import Student

FILE = "students.json"

def save_students(students):
    # Snapshot time → used as history key
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    try:
        with open(FILE, "r") as file:
            history = json.load(file)
    except (FileNotFoundError, JSONDecodeError):
        # First run or corrupted file
        history = {}

    # Convert objects → JSON-safe dictionaries
    students_dict = {}
    for name, student in students.items():
        students_dict[name] = student.to_dictionary()

    # Each save is a full snapshot
    history[timestamp] = students_dict

    with open(FILE, "w") as file:
        json.dump(history, file, indent=4)

def load_students():
    try:
        with open(FILE, "r") as file:
            history = json.load(file)
    except (FileNotFoundError, JSONDecodeError):
        # No saved data yet
        return {}

    all_students = {}

    for timestamp, students_data in history.items():
        # Rebuild one snapshot at a time
        students = {}

        for name, data in students_data.items():
            students[name] = Student.from_dictionary(data)

        all_students[timestamp] = students

    # Returns full history → tools choose what to use
    return all_students