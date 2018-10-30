from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!</h1>"

@app.route("/info")
def info():
    return "<h2>Here you can learn more about us.</h2>"

@app.route("/user/<name>")
def user(name):
    return "<h3>This is the page for {}.</h3>".format(name)

@app.route("/admin/<login>")
    def admin(login):
        return "10th letter in the Admin Login: {}".format(name[9])

if __name__ == "__main__":
    app.run(debug=True)
