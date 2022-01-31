from recipe_app import app
from flask import redirect,render_template, session, request, url_for,flash
from flask_bcrypt import Bcrypt
from recipe_app.models.recipe import Recipe
from recipe_app.models.user import User
bcrypt = Bcrypt(app)

# Login related routes

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_validation', methods=['POST'])
def login_validation():
    print("ENtered Login Validation method")
    if not User.validate_login_form(request.form):
        return redirect('/login')
    print("Login form is validated")
    user = User.get_by_email(request.form)
    if not user:
        flash("Invalid Email","login")
        return redirect('/login')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/login')
    session['user_id'] = user.id
    return redirect('/dashboard')


@app.route('/register', methods=['post'])
def register():
    if not User.validate_registration_form(request.form):
        return redirect('/login')

    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("dashboard.html",user=User.get_by_id(data), recipes=Recipe.get_all_recipes())

# Recipes table related routes
@app.route('/recipes/new')
def add_recipe():
    return render_template("add_new_recipe.html")

@app.route('/recipes/add',methods=['post'])
def save_recipe():
    print(request.form)
    data={
        'name':request.form['name'],
        'description':request.form['description'],
        'instructions':request.form['instructions'],
        'date_made':request.form['date_made'],
        'user_id':session['user_id'],
        'under30':request.form['under30']
    }
    Recipe.add_recipe(data)
    return redirect('/dashboard')

@app.route('/recipes/view/<int:id>')
def view_recipe(id):
    recipe = Recipe.get_all_recipes_id(id)
    return render_template("view_recipe.html",recipe=recipe)

@app.route('/recipes/edit/<int:id>')
def fetch_recipe(id):
    recipe = Recipe.get_all_recipes_id(id)
    return render_template("edit_recipe.html",recipe=recipe)

@app.route('/recipes/update/<int:id>', methods=['post'])
def update_recipe(id):
    data={
        'id':id,
        'name':request.form['name'],
        'description':request.form['description'],
        'instructions':request.form['instructions'],
        'date_made':request.form['date_made'],
        'under30':request.form['under30']
    }
    Recipe.update_recipe(data)
    return redirect('/dashboard')

@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    data={
        'id':id
    }
    Recipe.delete_recipe(data)
    return redirect('/dashboard')