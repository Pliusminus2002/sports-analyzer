from flask import Blueprint, render_template
import json
import flask

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/basketball", methods=["GET", "POST"])
def basketball():
    with open("app/data.json", encoding="utf-8") as f:
        data = json.load(f)
    basketball_teams = [team for team in data["teams"] if team["sport"] == "basketball"]

    result = None
    if flask.request.method == "POST":
        team1_name = flask.request.form["team1"]
        team2_name = flask.request.form["team2"]

        def get_strength(team):
            return sum(
                p.get("points_avg", 0) + p.get("assists_avg", 0) + p.get("rebounds_avg", 0)
                for p in team["players"]
            )

        team1 = next(t for t in basketball_teams if t["name"] == team1_name)
        team2 = next(t for t in basketball_teams if t["name"] == team2_name)
        s1 = get_strength(team1)
        s2 = get_strength(team2)

        if s1 + s2 > 0:
            percent = int((s1 / (s1 + s2)) * 100)
            result = f"{team1_name} yra {percent}% stipresnė už {team2_name}"
        else:
            result = "Abi komandos neturi pakankamai duomenų palyginimui."

    return render_template("basketball.html", teams=basketball_teams, result=result)

@main.route("/football")
def football():
    with open("app/data.json", encoding="utf-8") as f:
        data = json.load(f)
    football_teams = [team for team in data["teams"] if team["sport"] == "football"]
    return render_template("football.html", teams=football_teams)

@main.route("/volleyball")
def volleyball():
    with open("app/data.json", encoding="utf-8") as f:
        data = json.load(f)
    volleyball_teams = [team for team in data["teams"] if team["sport"] == "volleyball"]
    return render_template("volleyball.html", teams=volleyball_teams)

@main.route("/analyze", methods=["GET", "POST"])
def analyze():
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
