from student_class_oop import Student


def get_students():
    while True :
        name = input("Enter the students names ,'done' to finish or 'exit' to quit : ").strip()
        if name in ('done', 'exit'):
            return name.lower()
        elif any(char.isdigit() for char in name) or name == '' :
            print("Please enter a valid student name.")
            continue
        else:
            return name.capitalize()

def get_subjects(name):
    while True :
        subject = input(f"enter the subject name of {name} ,'done' to finish : ").strip()
        if subject.lower() == 'done':
            return 'done'
        elif any(char.isdigit() for char in subject) or subject == '' :
            print("Please enter a valid subject name.")
            continue
        return subject.capitalize()

def get_scores(name,subject):
    while True :
        try :
            score = int(input(f"Score of {name} in {subject}: "))
            if score < 0 :
                print("Please enter a valid score,score needs to be positive.")
                continue
            return score
        except ValueError :
            print("Please enter a valid score")
            continue

def get_data():
    students = {}
    while True :
        name = get_students()
        if name == 'exit' :
            print("Exiting program")
            break
        elif name == 'done' :
            break
        student = Student(name)

        while True :
            subject = get_subjects(name)
            if subject == 'done' :
                break
            score = get_scores(name,subject)

            student.add_subject(subject, score)

        students[name] = student

    return students
