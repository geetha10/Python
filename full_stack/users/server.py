from flask import Flask, render_template, request,redirect, session
# import the class from friend.py
from user import User

app = Flask(__name__)

@app.route("/users")
def display_all_users():
    # call the get all classmethod to get all friends
    users = User.get_all()
    return render_template("display_all_users.html",users=users)

@app.route('/users/new')
def display_new_user():
    return render_template("create_user.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    print("In create_user func")
    print(request.form)
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    print("Data creates is", data)
    User.save_new_user(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')

@app.route('/users/<int:id>')
def get_user_info_by_id(id):
    user=User.get_user_info_by_id(id)
    print("In server.py",user)
    return render_template("display_user_info.html",user=user)

@app.route('/users/<int:id>/edit')
def update_user_info_by_id(id):
    user=User.get_user_info_by_id(id)
    return render_template("update_user_info.html",user=user)

@app.route('/update_user/<int:id>', methods=["POST"])
def update_user(id):
    data = {
        "id":id,
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    print("Data creates is", data)
    User.update_user(data)
    return redirect(f'/users/{id}')

@app.route('/delete_user/<int:id>')
def delete_user(id):
    User.delete_user(id)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)