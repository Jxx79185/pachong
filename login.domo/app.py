from flask import Flask,render_template

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/index')
def index():
    return'主页'

app.run(debug=True)
