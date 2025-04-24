from flask import Blueprint, render_template
import json
import flask


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
@main.route("/analyze", methods=["GET", "POST"])
def analyze():
    import json
    result = None
    with open("app/data.json", encoding="utf-8") as f:
        data = json.load(f)
    teams = data["teams"]

    if flask.request.method == "POST":
        team1_name = flask.request.form["team1"]
        team2_name = flask.request.form["team2"]

        def get_team_strength(team):
            strength = 0
            for player in team["players"]:
                for key, value in player.items():
                    if isinstance(value, (int, float)):
                        strength += value
            return strength

        team1 = next((t for t in teams if t["name"] == team1_name), None)
        team2 = next((t for t in teams if t["name"] == team2_name), None)

        if team1 and team2:
            strength1 = get_team_strength(team1)
            strength2 = get_team_strength(team2)

            if strength1 > strength2:
                result = f"{team1_name} yra statistiškai stipresnė komanda ({strength1} prieš {strength2})"
            elif strength2 > strength1:
                result = f"{team2_name} yra statistiškai stipresnė komanda ({strength2} prieš {strength1})"
            else:
                result = f"{team1_name} ir {team2_name} yra vienodai stiprios ({strength1} taškai kiekviena)"

    return render_template("analyze.html", teams=teams, result=result)
