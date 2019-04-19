from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session, jsonify


from model import 

import requests
import json
from pprint import pprint

import os 


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """Homepage."""

    return render_template("homepage.html")


@app.route("/resume")
def resume():
   


    return render_template("resume.html")


@app.route("/projects")
def projects():

    return render_template("projects.html")


@app.route("/contact")
def contact():
      

    return render_template("contact.html")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    #DebugToolbarExtension(app)

    app.run(host="0.0.0.0")