from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/survey')
def index():
    return render_template("dojo_survey.html") 

@app.route('/submitted_survey', methods=['POST'])
def survey_submitted():
    print(request.form)
    session['user_name']=request.form['name']
    session['user_location']=request.form['location']
    session['user_fav_lang']=request.form['fav_lang']
    session['user_comments']=request.form['comments']
    return redirect('/summary')

@app.route('/summary')
def survey_summary():
    return render_template("summary.html")
            
if __name__ == "__main__":
    app.run(debug=True)