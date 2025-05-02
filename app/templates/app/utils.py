def compare_teams(team1, team2):
    strength1 = team1.calculate_strength()
    strength2 = team2.calculate_strength()

    total = strength1 + strength2
    if total == 0:
        return "Abi komandos neturi aktyvių žaidėjų."

    percent1 = (strength1 / total) * 100
    percent2 = (strength2 / total) * 100

    if strength1 > strength2:
        return f"{team1.name} turi {percent1:.1f}% tikimybę laimėti prieš {team2.name} ({percent1:.1f}% vs {percent2:.1f}%)"
    elif strength2 > strength1:
        return f"{team2.name} turi {percent2:.1f}% tikimybę laimėti prieš {team1.name} ({percent2:.1f}% vs {percent1:.1f}%)"
    else:
        return "Komandos turi vienodą tikimybę laimėti (50% vs 50%)"
