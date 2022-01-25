from flask import render_template,redirect,session,request
from dojos_and_ninjas_app import app
from dojos_and_ninjas_app.models.dojo import Dojo
from dojos_and_ninjas_app.models.ninja import Ninja

@app.route("/dojos")
def display_all_dojos():
    dojos= Dojo.get_all_dojos()
    print("Printing dodjos in controller: ", str(dojos))
    return render_template("dojos.html",dojos=dojos)

@app.route("/ninjas")
def add_new_ninja():
    names=Dojo.get_all_dojo_names
    return render_template("add_new_ninja.html")

@app.route("/dojos/<int:id>")
def display_ninjas_by_dojo_id(id):
    ninjas=Ninja.get_all_ninjas_by_id(id)
    return render_template("ninjas.html",ninjas=ninjas)

# @app.route("/users")
# def display_all_users():
#     # call the get all classmethod to get all friends
#     users = User.get_all()
#     return render_template("display_all_users.html",users=users)

# @app.route('/create_user', methods=["POST"])
# def create_user():
#     # First we make a data dictionary from our request.form coming from our template.
#     # The keys in data need to line up exactly with the variables in our query string.
#     print("In create_user func")
#     print(request.form)
#     data = {
#         "fname": request.form["fname"],
#         "lname" : request.form["lname"],
#         "email" : request.form["email"]
#     }
#     # We pass the data dictionary into the save method from the Friend class.
#     print("Data creates is", data)
#     User.save_new_user(data)
#     # Don't forget to redirect after saving to the database.
#     return redirect('/users')