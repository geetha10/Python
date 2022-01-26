import email
from flask import render_template,redirect,session,request, url_for
from email_validation import app
from email_validation.models.email import Email

@app.route('/email')
def home_page():
    return render_template("index.html")

@app.route('/save_email', methods=['POST'])
def save_email():
    if not Email.validatex_email(request.form):
        return redirect('/email')
    print("Email Validation Done")
    Email.save(request.form)
    return redirect('/success')

@app.route('/success')
def success():
    emails=Email.get_all_emails()
    return render_template("success.html", last_email=Email.get_one(), emails=emails)

@app.route('/delete_one/<int:id>')
def delete_one(id):
    data ={
        'id':id
    }
    print("Deleted email: ",Email.delete_one(data))
    return redirect('/success')