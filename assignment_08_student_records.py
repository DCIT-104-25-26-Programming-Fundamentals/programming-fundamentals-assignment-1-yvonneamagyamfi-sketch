def calculate_average_score(scores):
    if not scores:
        return 0

    total = 0
    for score in scores:
        total += score
    return total / len(scores)


def find_student(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def add_student(students, name=None, student_id=None, scores=None):
    if name is None:
        name = input("Student name: ").strip()
    if student_id is None:
        try:
            student_id = int(input("Student ID: "))
        except ValueError:
            print("Error: Student ID must be a number.")
            return False

    if find_student(students, student_id) is not None:
        print("Error: That student ID already exists.")
        return False

    if scores is None:
        try:
            score_count = int(input("How many scores? "))
        except ValueError:
            print("Error: Number of scores must be a positive integer.")
            return False
        if score_count <= 0:
            print("Error: Number of scores must be a positive integer.")
            return False

        scores = []
        for index in range(score_count):
            try:
                scores.append(float(input(f"Enter score {index + 1}: ")))
            except ValueError:
                print("Error: Scores must be numbers.")
                return False

    student = {"name": name, "id": student_id, "scores": scores}
    students.append(student)
    print(f'Student "{name}" added successfully.')
    return True


def display_students(students):
    if not students:
        print("No students have been added yet.")
        return

    print("-" * 65)
    print(f"{'Name':<20}{'ID':<12}{'Scores':<20}{'Average':>10}")
    print("-" * 65)
    for student in students:
        score_text = ", ".join(
            str(int(score)) if score == int(score) else str(score)
            for score in student["scores"]
        )
        average = calculate_average_score(student["scores"])
        print(f"{student['name']:<20}{student['id']:<12}{score_text:<20}{average:>10.2f}")
    print("-" * 65)


def find_student_average(students, student_id):
    student = find_student(students, student_id)
    if student is None:
        return None
    return calculate_average_score(student["scores"])


def print_menu():
    print("\n================================")
    print("     STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def main():
    students = []
    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            try:
                student_id = int(input("Enter student ID: "))
            except ValueError:
                print("Error: Student ID must be a number.")
                continue
            average = find_student_average(students, student_id)
            student = find_student(students, student_id)
            if student is None:
                print("Error: Student ID not found.")
            else:
                print(f"{student['name']}'s average score: {average:.2f}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Please choose a number from 1 to 4.")


if __name__ == "__main__":
    main()
