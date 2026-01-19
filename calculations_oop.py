def average_per_student(data):
    average = {}
    if data:
        for name, student in data.items():
            scores = list(student.subjects.values())

            if len(scores) == 0:
                average[name] = 0
                continue
            average[name] = sum(scores) / len(scores)

        return average

    return {}

def get_class_average(data) :
    if data :
        average = average_per_student(data)
        class_average= sum(average.values()) / len(average)
        return class_average
    return None

def get_students(data):
    if not data:
        return None, None, None, None

    averages = average_per_student(data)
    top_student = max(averages, key=averages.get)
    lowest_student = min(averages, key=averages.get)

    return (
        top_student,
        lowest_student,
        averages[top_student],
        averages[lowest_student],
    )

def students_grade(data):
    if not data :
        return {}
    averages = average_per_student(data)
    grades = {}
    for name, score in averages.items() :
        if 90 <= score <= 100:
            grade = "A"
        elif 70 <= score <= 89:
            grade = "B"
        elif 50 <= score <= 69:
            grade = "C"
        else:
            grade = "F"

        grades[name] = grade

    return grades

def class_grade(data):
    class_average = get_class_average(data)
    if class_average is None:
        return None

    if class_average >= 80:
        return "A"
    elif class_average >= 60:
        return "B"
    elif class_average >= 50:
        return "C"
    else:
        return "F"


def subjects_counter(data):
    if not data :
        return {}
    counter = {}
    for name, student in data.items() :
        counter[name] = len(student.subjects)
    return counter

def failed_succeed_student(data):
    if not data :
        return {}
    averages = average_per_student(data)
    fails = {}
    succeeds = {}
    for name, score in averages.items() :
        if score < 50 :
            fails[name] = score
        else :
            succeeds[name] = score
    return fails , succeeds
