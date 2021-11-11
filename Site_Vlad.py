from flask import Flask, redirect, url_for, render_template, send_from_directory
from flask_admin import Admin
from flask_basicauth import BasicAuth

app = Flask(__name__)

@app.route("/admin")
def admin():
	return render_template("admin.html")

@app.route("/_static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)

@app.route("/")
def Index():
	return render_template("index.html")

@app.route("/shower_cabins")
def shower_cabins():
	return render_template("shower_cabins.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/contacts")
def contacts():
	return render_template("contacts.html")

if __name__ == '__main__':
	app.run(debug=True)