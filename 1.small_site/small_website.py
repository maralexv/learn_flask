from flask import Flask, render_template, request
app = Flask (__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sign-up")
def sign_up():
	return render_template("sign_up.html")


@app.route("/thank_you")
def thank_you():
	first = request.args.get("first")
	last = request.args.get("last")
	return render_template("thank_you.html", first=first, last=last)


@app.route("/user/<name>")
def user(name="Alex"):
	return render_template("user.html", name=name)


@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404


if __name__ == '__main__':
    app.run(debug=True)
