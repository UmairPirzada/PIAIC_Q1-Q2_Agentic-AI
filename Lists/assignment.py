num_students = 3

# Lists to store student details
names = []
roll_numbers = []
subjects_list = []
marks_list = []

# Function to validate marks
def validate_marks(marks):
    return 0 <= marks <= 100

# Loop through each student
for i in range(num_students):
    print(f"\nEnter details for Student {i + 1}:\n")
    
    # Input student details
    name = input("Enter student's name: ")
    roll_number = input("Enter roll number: ")
    
    names.append(name)
    roll_numbers.append(roll_number)

    # Input marks for three subjects
    subjects = []
    marks = []
    
    for j in range(3):
        subject = input(f"Enter name of subject {j + 1}: ")
        subjects.append(subject)
        while True:
            try:
                mark = float(input(f"Enter marks for {subject}: "))
                if validate_marks(mark):
                    marks.append(mark)
                    break
                else:
                    print("Marks should be between 0 and 100. Please enter again.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    
    subjects_list.append(subjects)
    marks_list.append(marks)

# Function to generate the report card
def generate_report_card(index):
    name = names[index]
    roll_number = roll_numbers[index]
    subjects = subjects_list[index]
    marks = marks_list[index]
    
    total_marks = sum(marks)
    percentage = (total_marks / 300) * 100  # Assuming each subject is out of 100 marks
    
    # Determine class distinction based on percentage
    if percentage >= 90:
        distinction = "First Class with Distinction"
    elif percentage >= 60:
        distinction = "First Class"
    elif percentage >= 50:
        distinction = "Second Class"
    else:
        distinction = "Pass"
    
    # Generate the report card template
    report_card = f"""
    ---------------------------------
             Report Card
    ---------------------------------
    Name: {name}
    Roll Number: {roll_number}

    Subject          Marks
    ---------------------------------
    {subjects[0]:<15} {marks[0]:<10}
    {subjects[1]:<15} {marks[1]:<10}
    {subjects[2]:<15} {marks[2]:<10}

    ---------------------------------
    Total Marks:      {total_marks}
    Percentage:       {percentage:.2f}%
    Class:            {distinction}
    ---------------------------------
    """

    # Display the report card
    print(report_card)

# Generate and display report cards for all students
for i in range(num_students):
    generate_report_card(i)
