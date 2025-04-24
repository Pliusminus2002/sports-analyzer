def compare_teams(team1, team2):
    strength1 = team1.calculate_strength()
    strength2 = team2.calculate_strength()

    if strength1 > strength2:
        return f"{team1.name} has a higher chance to win ({strength1:.2f} vs {strength2:.2f})"
    elif strength2 > strength1:
        return f"{team2.name} has a higher chance to win ({strength2:.2f} vs {strength1:.2f})"
    else:
        return "Teams have equal chances to win"
