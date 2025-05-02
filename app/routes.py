# File: app/routes.py
from flask import Blueprint, render_template, request
import json

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")


def load_data():
    with open("app/data.json", encoding="utf-8") as f:
        return json.load(f)["teams"]


def calculate_strength(team, keys):
    strength = 0
    for player in team["players"]:
        for key in keys:
            strength += player.get(key, 0)
    return strength


def predict(team1, team2, keys):
    s1 = calculate_strength(team1, keys)
    s2 = calculate_strength(team2, keys)
    if s1 + s2 == 0:
        return "Abiejų komandų statistika per silpna prognozei."
    p1 = round((s1 / (s1 + s2)) * 100)
    p2 = 100 - p1
    return f"{team1['name']} tikimybė laimėti: {p1}%, {team2['name']} - {p2}%"


@main.route("/basketball", methods=["GET", "POST"])
def basketball():
    teams = [t for t in load_data() if t["sport"] == "basketball"]
    result = None
    if request.method == "POST":
        t1 = request.form["team1"]
        t2 = request.form["team2"]
        team1 = next((t for t in teams if t["name"] == t1), None)
        team2 = next((t for t in teams if t["name"] == t2), None)
        if team1 and team2:
            result = predict(team1, team2, ["points_avg", "assists_avg", "rebounds_avg"])
    return render_template("basketball.html", teams=teams, result=result)


@main.route("/football", methods=["GET", "POST"])
def football():
    teams = [t for t in load_data() if t["sport"] == "football"]
    result = None
    if request.method == "POST":
        t1 = request.form["team1"]
        t2 = request.form["team2"]
        team1 = next((t for t in teams if t["name"] == t1), None)
        team2 = next((t for t in teams if t["name"] == t2), None)
        if team1 and team2:
            result = predict(team1, team2, ["goals", "assists"])
    return render_template("football.html", teams=teams, result=result)


@main.route("/volleyball", methods=["GET", "POST"])
def volleyball():
    teams = [t for t in load_data() if t["sport"] == "volleyball"]
    result = None
    if request.method == "POST":
        t1 = request.form["team1"]
        t2 = request.form["team2"]
        team1 = next((t for t in teams if t["name"] == t1), None)
        team2 = next((t for t in teams if t["name"] == t2), None)
        if team1 and team2:
            result = predict(team1, team2, ["spikes", "blocks", "aces"])
    return render_template("volleyball.html", teams=teams, result=result)
