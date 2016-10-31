"""
Very simple Flask web site, with one page
displaying a course schedule.
"""

import flask
from flask import render_template
from flask import request
from flask import url_for

import json
import logging

# Date handling 
import arrow # Replacement for datetime, based on moment.js
import datetime # But we still need time
from dateutil import tz  # For interpreting local times

# Our own module
import pre  # Preprocess schedule file


###
# Globals
###
app = flask.Flask(__name__)


###
# Pages
###



@app.route("/")
@app.route("/index")
@app.route("/loaction")
def index():
  print("Main page entry")

  return flask.render_template('google_api.html')


@app.errorhandler(404)
def page_not_found(error):
    print("Page not found")
    flask.session['linkback'] =  flask.url_for("index")
    return flask.render_template('page_not_found.html'), 404


#############
#    
# Set up to run from cgi-bin script, from
# gunicorn, or stand-alone.
#

app.logger.setLevel(logging.DEBUG)
if __name__ == "__main__":
    print("Opening for global access on port {}".format(5000))
    app.run(port=5000, host="0.0.0.0")