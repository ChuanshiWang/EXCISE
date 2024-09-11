# Accepting a list of 10 student names and grades
names_input = input("Enter 10 student names, separated by a comma: ")
grades_input = input("Enter 10 student grades (0-5), separated by a comma: ")

# Converting inputs into lists
names_list = names_input.split(",")
grades_list = list(map(int, grades_input.split(",")))

# Combining the names and grades into a list of tuples
student_data = list(zip(names_list, grades_list))

# Displaying options to the user
while True:
    print("\nOptions:")
    print("1. View the student with the highest grade")
    print("2. View top three students with the highest grades")
    print("3. View the student with the lowest grade")
    print("4. Get the total number of students that failed (grade < 3)")
    print("5. Quit the program")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        # Finding the student with the highest grade
        highest_grade_student = max(student_data, key=lambda x: x[1])
        print(f"Highest grade student: {highest_grade_student[0]} - {highest_grade_student[1]}")

    elif choice == '2':
        # Sorting students by grade in descending order and displaying the top three
        top_three_students = sorted(student_data, key=lambda x: x[1], reverse=True)[:3]
        print("Top 3 students:")
        for student in top_three_students:
            print(f"{student[0]} - {student[1]}")

    elif choice == '3':
        # Finding the student with the lowest grade
        lowest_grade_student = min(student_data, key=lambda x: x[1])
        print(f"Lowest grade student: {lowest_grade_student[0]} - {lowest_grade_student[1]}")

    elif choice == '4':
        # Counting the number of students with grades less than 3 (failed)
        failed_students = [student for student in student_data if student[1] < 3]
        print(f"Number of students that failed: {len(failed_students)}")

    elif choice == '5':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
