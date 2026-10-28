# Student Result Management System (Beginner Level)

def calculate_grade(average):
    """Helper function to calculate grade based on average marks"""
    if average >= 90:
        return 'A+'
    elif average >= 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'Fail'

def main():
    # Dictionary to store student records: {roll_no: {'name': name, 'marks': [m1, m2, m3]}}
    students = {}
    
    while True:
        print("\n--- Student Result Management System ---")
        print("1. Add Student & Marks")
        print("2. View All Students")
        print("3. Search Student by Roll Number")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            roll_no = input("Enter Roll Number: ")
            if roll_no in students:
                print("Roll number already exists!")
                continue
            
            name = input("Enter Student Name: ")
            
            # Using try-except to handle non-numeric inputs gracefully
            try:
                m1 = float(input("Enter marks in Subject 1: "))
                m2 = float(input("Enter marks in Subject 2: "))
                m3 = float(input("Enter marks in Subject 3: "))
            except ValueError:
                print("Invalid marks! Please enter numbers.")
                continue
            
            # Store data in the dictionary
            students[roll_no] = {
                'name': name,
                'marks': [m1, m2, m3]
            }
            print(f"Student {name} added successfully!")
            
        elif choice == '2':
            if not students:
                print("No student records found.")
            else:
                print("\n--- All Student Results ---")
                for roll, data in students.items():
                    name = data['name']
                    marks = data['marks']
                    total = sum(marks)
                    average = total / len(marks)
                    grade = calculate_grade(average)
                    print(f"Roll No: {roll} | Name: {name} | Marks: {marks} | Total: {total:.2f} | Avg: {average:.2f} | Grade: {grade}")
                    
        elif choice == '3':
            roll_no = input("Enter Roll Number to search: ")
            if roll_no in students:
                data = students[roll_no]
                name = data['name']
                marks = data['marks']
                total = sum(marks)
                average = total / len(marks)
                grade = calculate_grade(average)
                
                print(f"\n--- Student Found ---")
                print(f"Roll Number: {roll_no}")
                print(f"Name: {name}")
                print(f"Marks: {marks}")
                print(f"Total Marks: {total:.2f}")
                print(f"Average: {average:.2f}")
                print(f"Grade: {grade}")
            else:
                print("Student not found!")
                
        elif choice == '4':
            print("Exiting Student Result Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please select between 1 and 4.")

if __name__ == "__main__":
    main()