from app import app, db, AllEmployees

# Creating a database with already prefilled information for the employees
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        employee_1 = AllEmployees("Lukas", "CSM", 10.56)
        employee_2 = AllEmployees("Eglė", "HR")
        employee_3 = AllEmployees("Martynas", "AI")
        employee_4 = AllEmployees("Saulė", "CSM", 11)
        employee_5 = AllEmployees("Povilas", "CSM", 13.02)
        employee_6 = AllEmployees("Evelina", "TA")
        employee_7 = AllEmployees("Paulius", "TA")
        employee_8 = AllEmployees("Kristina", "AI")
        employee_9 = AllEmployees("Saulius", "CSM", 9.95)
        employee_10 = AllEmployees("Ieva", "CSM", 7.65)
        db.session.add_all(
            [employee_1, employee_2, employee_3, employee_4, employee_5, employee_6, employee_7, employee_8, employee_9,
             employee_10])
        db.session.commit()
