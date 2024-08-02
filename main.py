from flask import request, render_template, jsonify, redirect, url_for
from app import app, db, AllEmployees


# Route for the main page
@app.route("/")
def home():
    return render_template("base.html")


# Route for the database
@app.route("/employees", methods=['GET'])
def check_database():
    all_employees = AllEmployees.query.all()
    return render_template("database.html", all_employees=all_employees)


# Route for one of the employees by ID
@app.route("/employees/<int:id>", methods=["GET"])
def get_employee(id):
    employee = AllEmployees.query.get_or_404(id)
    return render_template("get_employee.html", employee=employee)


# Add employee
@app.route("/employees/add", methods=["POST", "GET"])
def add_employee():
    if request.method == "POST":
        name = request.form.get("name")
        department = request.form.get("department")
        workflow = request.form.get("workflow") or None
        new_employee = AllEmployees(name=name, department=department, workflow=workflow)
        db.session.add(new_employee)
        db.session.commit()

    return render_template("add_employee.html")


# Edit employee
@app.route("/employees/edit/<int:id>", methods=["POST", "GET"])
def edit_employee(id):
    employee = AllEmployees.query.get_or_404(id)
    if request.method == "GET":
        return render_template("edit_employee.html", employee=employee)
    elif request.method == "POST":
        employee.name = request.form.get("name")
        employee.department = request.form.get("department")
        employee.workflow = request.form.get("workflow") or None
        db.session.commit()
        return redirect(url_for("get_employee", id=employee.id))


# Delete employee
@app.route("/employees/delete/<int:id>", methods=["DELETE", "GET"])
def delete_employee(id):
    employee = AllEmployees.query.get_or_404(id)
    if request.method == "GET":
        return render_template("delete_employee.html", employee=employee)
    elif request.method == "DELETE":
        db.session.delete(employee)
        db.session.commit()
        return redirect(url_for("check_database"))


# Search for an employee by ID
@app.route("/search", methods=["GET"])
def search_by_id():
    id_str = request.args.get("id")
    if id_str is None or not id_str.isdigit():
        return jsonify({"message": "Invalid ID format"}), 400
    id = int(id_str)
    employee = AllEmployees.query.get_or_404(id)
    return redirect(url_for("get_employee", id=employee.id))


# Here you can change the local host number
if __name__ == "__main__":
    app.run('localhost', 90, debug=True)
