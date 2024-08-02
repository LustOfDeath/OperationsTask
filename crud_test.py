from app import app, AllEmployees, db

# This part of the code is for testing purposes to see if the database is created without needing to start the website
if __name__ == "__main__":
    with app.app_context():
        all_employees = AllEmployees.query.all()
        for employee in all_employees:
            if employee.workflow is None:
                print(employee.id, employee.name, employee.department)
            else:
                print(employee.id, employee.name, employee.department, employee.workflow)
