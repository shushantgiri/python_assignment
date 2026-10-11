# Student Result System

students = [
    {"name": "Ram", "math": 80, "science": 75, "english": 70},
    {"name": "Sita", "math": 90, "science": 85},
    {"name": "Hari", "math": 60, "science": 65, "english": 72},
    {"name": "Gita", "math": 95, "science": 88, "english": 91},
    {"name": "Shyam", "math": 45, "science": 50, "english": 55}
]


def show_result(name):
    for student in students:
        if student["name"].lower() == name.lower():

            total = 0

            print("Name:", student["name"])

            if "math" in student:
                total = total + student["math"]
            else:
                print("Math marks are missing")

            if "science" in student:
                total = total + student["science"]
            else:
                print("Science marks are missing")

            if "english" in student:
                total = total + student["english"]
            else:
                print("English marks are missing")

            percentage = total / 300 * 100

            print("Total Marks:", total)
            print("Percentage:", round(percentage, 2), "%")
            return

    print("Student not found")


name = input("Enter student name: ")

show_result(name)
