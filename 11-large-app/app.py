# app.py at the same level as 'project' dir

from project import app
from flask import Flask, render_template

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run (debug=True)
