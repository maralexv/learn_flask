import os

from flask import Flask, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = os.urandom(16)
Session(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:aE8-Gu4-qaI3@localhost:5432/mydb'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route('/', methods=['GET', 'POST'])
def home():

	if request.method == 'POST':
		test = request.form.get('test')
		db.execute(
			'INSERT INTO strings (string) VALUES (:test)',
			{'test': test}
			)
		db.commit()

	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)