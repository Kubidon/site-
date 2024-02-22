from flask import Flask, render_template

app = Flask(__name__)

@app.route("/squirell")
def pg1():
    return render_template('pg1.html')
@app.route("/hamster")
def pg2():
    return render_template('pg2.html')
@app.route("/ferret")
def pg3():
    return render_template('pg3.html')
@app.route("/youtube")
def pg4():
    return render_template('video.html')
@app.route('/')
def menu():
    return render_template('main.html') 

if __name__ == '__main__':
    app.run(debug=True)