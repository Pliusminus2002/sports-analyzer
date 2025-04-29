from flask import Blueprint, render_template, request
import json

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")


@main.route("/basketball", methods=["GET", "POST"])
def basketball():
    result = None
    with open("app/data.json", encoding="utf-8") as f:
        data = json.load(f)
    basketball_teams = [team for team in data["teams"] if team["sport"] == "basketball"]

    if request.method == "POST":
        team1_name = request.form["team1"]
        team2_name = request.form["team2"]

        def get_strength(team):
            return sum(
                player.get("points_avg", 0) +
                player.get("assists_avg", 0) +
                player.get("rebounds_avg", 0)
                for player in team["players"]
            )

        team1 = next((t for t in basketball_teams if t["name"] == team1_name), None)
        team2 = next((t for t in basketball_teams if t["name"] == team2_name), None)

        if team1 and team2:
            s1 = get_strength(team1)
            s2 = get_strength(team2)
            if s1 > s2:
                result = f"{team1_name} yra stipresnė ({s1} prieš {s2})"
            elif s2 > s1:
                result = f"{team2_name} yra stipresnė ({s2} prieš {s1})"
            else:
                result = f"{team1_name} ir {team2_name} yra lygios ({s1} taškai)"

    return render_template("basketball.html", teams=basketball_teams, result=result)


@main.route("/football", methods=["GET", "POST"])
def football():
    result = None
    with open("app/data.json", encoding="utf-8") as f:
        data = json.load(f)
    football_teams = [team for team in data["teams"] if team["sport"] == "football"]

    if request.method == "POST":
        team1_name = request.form["team1"]
        team2_name = request.form["team2"]

        def get_strength(team):
            return sum(
                player.get("goals", 0) +
                player.get("assists", 0) -
                player.get("yellow_cards", 0) * 0.5
                for player in team["players"]
            )

        team1 = next((t for t in football_teams if t["name"] == team1_name), None)
        team2 = next((t for t in football_teams if t["name"] == team2_name), None)

        if team1 and team2:
            s1 = get_strength(team1)
            s2 = get_strength(team2)
            if s1 > s2:
                result = f"{team1_name} yra stipresnė ({s1} prieš {s2})"
            elif s2 > s1:
                result = f"{team2_name} yra stipresnė ({s2} prieš {s1})"
            else:
                result = f"{team1_name} ir {team2_name} yra lygios ({s1} taškai)"

    return render_template("football.html", teams=football_teams, result=result)


@main.route("/volleyball", methods=["GET", "POST"])
def volleyball():
    result = None
    with open("app/data.json", encoding="utf-8") as f:
        data = json.load(f)
    volleyball_teams = [team for team in data["teams"] if team["sport"] == "volleyball"]

    if request.method == "POST":
        team1_name = request.form["team1"]
        team2_name = request.form["team2"]

        def get_strength(team):
            return sum(
                player.get("spikes", 0) +
                player.get("blocks", 0) +
                player.get("aces", 0)
                for player in team["players"]
            )

        team1 = next((t for t in volleyball_teams if t["name"] == team1_name), None)
        team2 = next((t for t in volleyball_teams if t["name"] == team2_name), None)

        if team1 and team2:
            s1 = get_strength(team1)
            s2 = get_strength(team2)
            if s1 > s2:
                result = f"{team1_name} yra stipresnė ({s1} prieš {s2})"
            elif s2 > s1:
                result = f"{team2_name} yra stipresnė ({s2} prieš {s1})"
            else:
                result = f"{team1_name} ir {team2_name} yra lygios ({s1} taškai)"

    return render_template("volleyball.html", teams=volleyball_teams, result=result)
