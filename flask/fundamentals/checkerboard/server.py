from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def default_checker_board():
    return render_template('default.html')

@app.route("/checker_board/<int:num>")
def checker_board_with_num(num):
    return render_template('with_num.html',num=num)

@app.route("/checker_board/<int:num>/<color1>")
def checker_board_with_color1(num,color1):
    return render_template('with_color1.html',num=num,color1=color1)

@app.route("/checker_board/<int:num>/<color1>/<color2>")
def checker_board_with_color2(num,color1,color2):
    return render_template('with_color2.html',num=num,color1=color1,color2=color2)

if __name__=='__main__':
    app.run(debug=True)
