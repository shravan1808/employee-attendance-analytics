import csv
from pathlib import Path

ATTENDANCE_FILE= Path("data")/"attendance.csv"

def load_attendance():
    # load_attendance is a function which loads the attendance file
    try:
        with ATTENDANCE_FILE.open('r',newline='') as file:
            reader=csv.DictReader(file)
            report = list(reader)
    except FileNotFoundError:
        print("Attendance file not found\n")
    else:
        print("Attendance Loaded Successfully.\n")
        return report
    return

def display_first_employee(result):
    # Function that prints the details of first employee
    data=result[0]
    print("First Employee\n")
    print(f"Employee ID : {data['EmployeeID']}")
    print(f"Name        : {data['Name']}")
    print(f"Department  : {data['Department']}")
    print(f"Date        : {data['Date']}")

def display_departments(result):
    # Function that displays all the departments
    depts=[emp['Department'] for emp in result]
    print("Departments\n")
    for dept in depts:
        print(dept)    

def main():
    print("Employee Attendance Analytics System\n")
    print("Loading attendance...\n")
    attendance_result = load_attendance()
    if attendance_result is None:
        return
    if not attendance_result:
        print("Attendance file is empty")
        return

    count=len(attendance_result)
    print(f"Total Employees : {count}\n")
    
    display_first_employee(attendance_result)
    print()
    display_departments(attendance_result)
   

if __name__=="__main__":
    main()

