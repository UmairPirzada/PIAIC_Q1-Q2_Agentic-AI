# Number of students
num_students = 3

# Loop through each student
for i in range(num_students):
    print(f"\nEnter details for Student {i + 1}:\n")
    
    # Input student details
    name = input("Enter student's name: ")
    roll_number = input("Enter roll number: ")

    # Input marks for three subjects
    subject1 = input("Enter name of subject 1: ")
    marks1 = float(input(f"Enter marks for {subject1}: "))

    subject2 = input("Enter name of subject 2: ")
    marks2 = float(input(f"Enter marks for {subject2}: "))

    subject3 = input("Enter name of subject 3: ")
    marks3 = float(input(f"Enter marks for {subject3}: "))

    # Calculate total marks and percentage
    total_marks = marks1 + marks2 + marks3
    percentage = (total_marks / 300) * 100  # Assuming each subject is out of 100 marks

    # Generate the report card template
    report_card = f"""
    ---------------------------------
             Report Card
    ---------------------------------
    Name: {name}
    Roll Number: {roll_number}

    Subject          Marks
    ---------------------------------
    {subject1:<15} {marks1:<10}
    {subject2:<15} {marks2:<10}
    {subject3:<15} {marks3:<10}

    ---------------------------------
    Total Marks:      {total_marks}
    Percentage:       {percentage:.2f}%
    ---------------------------------
    """

    # Display the report card
    print(report_card)
