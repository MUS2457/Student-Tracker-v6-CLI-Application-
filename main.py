import input_students_data
import calculations_oop
import tools
import data_handling

def menu() :
    print("==== Welcome to Student tracker v 6 ==== ")
    print("1 . Add student data")
    print("2 . Search student data")
    print("3 .  Top 3 students")
    print("4 . track student progress")
    print("5 . Exit program")

def main():
    while True:
        menu()
        user_choice = input("Enter your choice by entering a number from 1 to 5 : ").strip()
        if user_choice == "1" :
            user = input_students_data.get_data() #set data

            # run calculations
            averages = calculations_oop.average_per_student(user)
            grade = calculations_oop.students_grade(user)
            subject_count = calculations_oop.subjects_counter(user)
            class_average = calculations_oop.get_class_average(user)
            class_grade = calculations_oop.class_grade(user)
            (
                top_student,
                low_student,
                top_student_score,
                low_student_score
            ) = calculations_oop.get_students(user)
            fails, succeed = calculations_oop.failed_succeed_student(user)

            #show results
            print("\n--- Average Per Student ---")
            for name, avg in averages.items():
                print(f"{name}: {avg}")

            print(f"\nTop student: {top_student}, score : {top_student_score}")
            print(f"Lowest student: {low_student}, score : {low_student_score}")
            print(f"Class average: {class_average}, class grade : {class_grade}")

            print("\n--- Grade Per Student ---")
            for name, grades in grade.items():
                print(f"{name}: {grades}")

            print("\n--- Subjects Per Student ---")
            for name, count in subject_count.items():
                print(f"{name}: {count}")
            print("\n--- the student who fails ---")
            for name, score in fails.items():
                print(f"{name}: {score}")
            print("serious warning ⚠️!,Do more efforts")

            print("\n--- Student who succeeds ---")
            for name, score in succeed.items():
                print(f"{name}: {score}")
            print("Good job 💯🎉,continue !")

            # save data
            data_handling.save_students(user)
            print("data saved successfully 💾")
        elif user_choice == "2" :
            student = tools.search_students() #student here refers to the object

            if student is None :
                print("returning to the menu...")
                continue  # i tried (break) but it stops the program immediately,so continue restart the loop so take us back to menu ,I understand it clearly because of a bug
            print(f"the student {student.name} was found,with information {student.subjects}")

        elif user_choice == "3" :
            top_3_students = tools.top_3_students()
            print("---the top 3 students---\n")
            print("--- the top 3 students ---\n")

            if len(top_3_students) >= 1:
                print(f"Top 1: {top_3_students[0]}")
            if len(top_3_students) >= 2:
                print(f"Top 2: {top_3_students[1]}")
            if len(top_3_students) >= 3:
                print(f"Top 3: {top_3_students[2]}")


        elif user_choice == "4" :
            name,progress = tools.student_progress()
            if name is None :
                print("returning to the menu...")
                continue
            print(f"===The progress of student {name} over time ===\n")
            for timestamp,result in progress.items():
                print(f"{timestamp}: {result}")

        elif user_choice == "5" :
            print("The program will exit now...")
            break
        else :
            print("Enter a valid choice")
            continue



if __name__ == '__main__':
    main()