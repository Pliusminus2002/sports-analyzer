from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def index():
    @main.route("/basketball")
def basketball():
    import json
    with open("app/data.json", encoding="utf-8") as f:
        data = json.load(f)
    basketball_teams = [team for team in data["teams"] if team["sport"] == "basketball"]
    return render_template("basketball.html", teams=basketball_teams)
    return render_template("index.html")
