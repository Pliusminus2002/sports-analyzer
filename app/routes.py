from flask import Blueprint, render_template
import json

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/basketball")
def basketball():
    with open("app/data.json", encoding="utf-8") as f:
        data = json.load(f)
    basketball_teams = [team for team in data["teams"] if team["sport"] == "basketball"]
    return render_template("basketball.html", teams=basketball_teams)
@main.route("/football")
def football():
    import json
    with open("app/data.json", encoding="utf-8") as f:
        data = json.load(f)
    football_teams = [team for team in data["teams"] if team["sport"] == "football"]
    return render_template("football.html", teams=football_teams)
