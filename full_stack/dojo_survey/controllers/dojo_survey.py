from flask import render_template,redirect,session,request, url_for
from dojo_survey import app
from dojo_survey.models.survey import Survey

@app.route('/survey')
def index():
    print("in index")
    return render_template("dojo_survey.html") 

@app.route('/submitted_survey', methods=['POST'])
def survey_submitted():
    print(Survey.validate_survey(request.form))
    if not Survey.validate_survey(request.form):
        return redirect('/survey')
    # data={
    #     'name':request.form['name'],
    #     'location':request.form['location'],
    #     'fav_lang':request.form['fav_lang'],
    #     'comments':request.form['comments']
    # }
    print(type(request.form), request.form)
    Survey.save(request.form)
    return redirect('/summary')

@app.route('/summary')
def survey_summary():
    data=Survey.get_last_survey()
    print("Result From DB:", data)
    return render_template("summary.html",data=data)