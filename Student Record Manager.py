# Student Record Manager

import re

FILE_NAME = "students.txt"

# Function to validate email using regex
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    return False


# Function to add student
def add_student():
    try:
        name = input("Enter student name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty")

        age = int(input("Enter age: "))
        if age <= 0:
            raise ValueError("Age must be positive")

        email = input("Enter email: ").strip()
        if not validate_email(email):
            raise ValueError("Invalid email format")

        # Save to file
        with open(FILE_NAME, "a") as file:
            file.write(f"{name},{age},{email}\n")

        print("✅ Student added successfully!\n")

    except ValueError as ve:
        print("❌ Error:", ve)
    except Exception as e:
        print("❌ Unexpected Error:", e)


# Function to read student data
def read_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()

            if not data:
                print("📂 No records found.\n")
                return

            print("\n📋 Student Records:")
            print("-" * 30)
            for line in data:
                name, age, email = line.strip().split(",")
                print(f"Name: {name}, Age: {age}, Email: {email}")
            print()

    except FileNotFoundError:
        print("📂 File not found. No data yet.\n")
    except Exception as e:
        print("❌ Error reading file:", e)


# Main menu
def main():
    while True:
        print("===== Student Record Manager =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            read_students()
        elif choice == "3":
            print("👋 Exiting program...")
            break
        else:
            print("❌ Invalid choice. Try again.\n")


# Run program
if __name__ == "__main__":
    main()