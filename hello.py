"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def hello():
    return render_template('hello.html')

@app.route('/login', methods = ['POST'])
def profile():
    if request.method == 'POST':
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        age=request.form['age']
        if firstname and lastname and age:
            return render_template('profile.html',firstname=firstname, lastname=lastname, age=age)
        else:
            return redirect(url_for('error'))

@app.route('/error', methods = ['GET','POST'])
def error():
    if request.method == 'POST':
        return redirect(url_for('hello'))
    return render_template('error.html')

if __name__ == '__main__':
    app.run()
