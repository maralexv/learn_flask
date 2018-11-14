from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/report')
def report():
	username = request.args.get('username')
	# Initialise collector for issues
	issues = []
	# Check for uppercase
	if not any(element.isupper() for element in username):
		issues.append("Your User Name does not have an uppercase letter.")
	# Check for lowercase
	if not any(element.islower() for element in username):
		issues.append("Your user Name does not have lowercase letters.")
	# Check for digit
	if not (username[-1].isdigit()):
		issues.append("Your User Name does not end with a digit.")
	# Count the number of issues
	count_issues=len(issues)

	return render_template('report.html', username=username, count_issues=count_issues, issues=issues)


@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404


if __name__=='__main__':
	app.run(debug=True)