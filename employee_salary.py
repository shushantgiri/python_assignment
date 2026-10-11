# Employee Salary System

employees = {
    101: {"name": "Ram", "department": "IT", "salary": 50000},
    102: {"name": "Sita", "department": "HR", "salary": 40000},
    103: {"name": "Hari", "department": "Finance", "salary": 45000},
    104: {"name": "Gita", "department": "Marketing", "salary": 38000},
    105: {"name": "Shyam", "department": "Sales", "salary": 35000}
}


def yearly_salary(salary):
    return salary * 12


def increase_salary(salary, percent):
    return salary + (salary * percent / 100)


emp_id = int(input("Enter employee ID: "))

if emp_id in employees:
    emp = employees[emp_id]

    print("Name:", emp["name"])
    print("Department:", emp["department"])

    percent = float(input("Enter salary increase percentage: "))

    old_salary = emp["salary"]
    new_salary = increase_salary(old_salary, percent)

    emp["salary"] = new_salary

    print("Old Salary:", old_salary)
    print("New Salary:", new_salary)
    print("Yearly Salary:", yearly_salary(new_salary))

else:
    print("Employee not found")