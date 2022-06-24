# -*- coding: utf-8 -*-

from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("indexe.html")

@app.route("/forbidden")
def forbidden():
    abort(405)

@app.route('/goodbye')
def goodbye():
    return render_template('goodbye.html')

if __name__ == "__main__":
    app.run(debug=True)


