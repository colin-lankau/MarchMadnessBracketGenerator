'''
This is the site blueprint.  It manages basic routes for the application
'''

from flask import Blueprint, render_template, session, url_for, redirect, request

from REST.Utils.Bracket import Bracket, teams
from REST.Utils.Scraper import get_html, write_data
from REST.Utils.Parser import parse
import os.path
import webbrowser

site = Blueprint('site', __name__)


@site.route('/', methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template('index.html', teams=sorted(teams))
    elif request.method == "POST":
        bias = request.form.get("bias")
        winner = request.form.get("winner") if request.form.get("winner") != "" else "default"
        preferences = []
        for i in range(5):
            temp = request.form.get(f"preferences{i}")
            if temp:
                preferences.append(temp)
        return redirect(url_for("site.bracket", bias=bias, winner=winner, preferences=preferences))

@site.route('/bracket/<bias>/<winner>/<preferences>')
def bracket(bias, winner, preferences):

    # get rounds data
    if not os.path.isfile('data.txt'):
        response = get_html('https://www.betfirm.com/seeds-national-championship-odds/')
        write_data(response)
    round_odds = parse('data.txt')
    
    # generate bracket
    bracket1 = Bracket()
    preferences = preferences.strip('[]').replace("'","")
    pref = preferences.split(", ")
    bracket1.generate_rounds(round_odds, int(bias), winner, pref)
    # bracket1.view_bracket()

    return render_template("bracket.html", r64=bracket1.rounds[0], r32=bracket1.rounds[1], s16=bracket1.rounds[2], e8=bracket1.rounds[3], f4=bracket1.rounds[4], final=bracket1.rounds[5], champ=bracket1.rounds[6][0].name)

# v1 
# 1) created a Bracket and Team class to store those complex objects
# 2) added a generate_bracket method to Bracket class to randomly generate a bracket
# 3) created a simple text based bracket in the terminal

# v2 
# 1) designed a web scraper to obtain win rates by seed number and saved it into "data.txt"
# 2) wrote methods to parse through "data.txt"
# 3) turned python code into a Flask app and broke project into organized heirarchy
# 4) broke out parser and web scraper into their own classes
# 5) designed a simple html web bracket to better present data to user ("bracket-OLD.html")
# 6) wrote a stylesheet for the web bracket
# 7) integrated Jinja into the html to dynamically load bracket values

# v3
# 1) designed a home page for the project ("index.html")
# 2) added a bias factor the user can input to give underdogs or favorites special treatment
# 3) added a way for user's to enter their winner if they want to specify one
# 4) redesigned bracket to look far better ("bracket.html")
# 5) used SCSS to create a better stylesheet and used a vscode plugin to convert it to regular CSS
# 6) refactored Bracket class to be way more dynamic and halved the number of lines

# v4
# 1) added javascript front-end form checking ("formValidation.js")
# 2) added a preferences option to show bias to certain teams
# 3) added javascript to allow for multiple teams to be given preference, but maxes out at 5
# 4) retrieve preferences from front end and pass to backend for calculation

# TODO
# add route between generation and bracket viewing
# add preferences into bracket generation algorithm (give either top or bottom an extra 25 points if they appear in preferences)
# add a regenerate button to bracket.html
# add an export function to export the bracket as a pdf