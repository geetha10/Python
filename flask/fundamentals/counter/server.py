from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/counter')
def index():
    if 'count' in session:
        session['count'] = int(session['count'])+1
    else:
        session['count']=1
    return render_template("index.html")  

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)