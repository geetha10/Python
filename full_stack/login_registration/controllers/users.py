from login_registration import app
from flask import redirect,render_template, session, request, url_for,flash
from flask_bcrypt import Bcrypt
from login_registration.models.user import User
bcrypt = Bcrypt(app)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_validation', methods=['POST'])
def login_validation():
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
    if not User.validate_form(request.form):
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

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("dashboard.html",user=User.get_by_id(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')