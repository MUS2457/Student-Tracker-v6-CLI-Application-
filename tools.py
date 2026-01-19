import data_handling
import calculations_oop

def search_students():
    history = data_handling.load_students()
    if not history:
        return None

    while True:
        name_searched = input("Enter student name (or 'exit'): ").strip()
        if name_searched.lower() == "exit":
            return None

        name_capital = name_searched.capitalize()

        for timestamp, students in history.items():
            if name_capital in students:
                return students[name_capital]

        print(f"Student name '{name_searched}' not found. Try again.")

def top_3_students():
    history = data_handling.load_students()
    all_students = {}
    if history:
        for timestamp, students in history.items():
            all_students.update(students)
        averages = calculations_oop.average_per_student(all_students)
        list_student = sorted(averages.items(), key=lambda x: x[1], reverse=True)[:3]
        return list_student

    return []

def student_progress():
    history = data_handling.load_students()
    if not history:
        return {}

    name = input("Enter student name (or 'exit'): ").strip()
    if name.lower() == "exit":
        return None,None

    name = name.capitalize()
    progress = {}

    for timestamp, students in history.items():
        if name in students:
            student = students[name]

            # MAIN IDEA (used):
            # Wrap ONE Student object into a dict
            # so it matches the structure used everywhere else
            student_dict = {name: student}
            # This is equivalent to:
            # student_dict = {}
            # student_dict[name] = student

            average = calculations_oop.average_per_student(student_dict)[name]
            grade = calculations_oop.students_grade(student_dict)[name]
            subject_count = calculations_oop.subjects_counter(student_dict)[name]

            progress[timestamp] = {
                "average": average,
                "grade": grade,
                "subjects_count": subject_count,
                "student": student
            }


            # ALTERNATIVE DESIGN (NOT USED):
            # If I had functions that work on ONE object:
            # average = student.get_average()
            # grade = student.get_grade()
            # subject_count = len(student.subjects)

    return name,progress


