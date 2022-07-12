# -*- coding: utf-8 -*-

from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template("indexe.html")

@app.route("/forbidden")
def forbidden():
    abort(405)

@app.route('/goodbye.html')
def goodbye():
    return render_template('goodbye.html')

@app.errorhandler(405)
def forbidden_page(e):
    return render_template("forbidden_page.html"), 405

@app.route('/forbidden_page')
def forbidden_page():
    return render_template('forbidden_page.html')

if __name__ == "__main__":
    app.run(debug=True)


