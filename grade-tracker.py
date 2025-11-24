import os
import sys
import datetime

def clear_screen():
    # Clears the terminal screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_valid_mark(subject_name):
    while True:
        try:
            user_input = input("Enter marks for " + subject_name + " (0-100): ")
            mark = float(user_input)
            
            if mark < 0 or mark > 100:
                print("Error: Marks must be between 0 and 100.")
            else:
                return mark
        except ValueError:
            print("Error: That is not a number. Please try again.")


def calculate_grade(marks_list):
    total = sum(marks_list)
    count = len(marks_list)
    if count == 0:
        return None
    percentage = (total / (count * 100)) * 100
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "Fail"
    return {
        "total": total,
        "percentage": round(percentage, 2),
        "grade": grade
    }

def save_to_file(student_name, results):
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d %H:%M:%S")
    line = f"{date_str} | {student_name} | Total: {results['total']} | {results['percentage']}% | Grade: {results['grade']}\n"
    
    try:
        f = open("report_card.txt", "a")
        f.write(line)
        f.close()
        print("\n[Saved successfully to report_card.txt]")
    except Exception as e:
        print("Error saving file:", e)

def view_history():
    print("\n--- PAST REPORTS ---")
    try:
        f = open("report_card.txt", "r")
        content = f.read()
        print(content)
        f.close()
    except FileNotFoundError:
        print("No reports found yet.")
    print("--------------------")

def main():
    while True:
        clear_screen()
        print("===============================")
        print(" STUDENT GRADE CALCULATOR")
        print("===============================")
        print("1. New Calculation")
        print("2. View History")
        print("3. Exit")
        print("===============================")
        choice = input("Select Option (1-3): ")
        if choice == '1':
            print("\n--- NEW ENTRY ---")
            name = input("Student Name: ")
            subjects = ["Maths", "Physics", "Chemistry", "English", "CS"]
            student_marks = []
            for sub in subjects:
                m = get_valid_mark(sub)
                student_marks.append(m)
            result = calculate_grade(student_marks)
            print("\n--- RESULT ---")
            print("Total Marks:", result['total'])
            print("Percentage: ", result['percentage'], "%")
            print("Final Grade:", result['grade'])
            save_choice = input("\nSave to file? (y/n): ")
            if save_choice.lower() == 'y':
                save_to_file(name, result)

            input("\nPress Enter to return...")
            
        elif choice == '2':
            view_history()
            input("\nPress Enter to return...")
        elif choice == '3':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            input("Press Enter...")

if __name__ == "__main__":
    main()