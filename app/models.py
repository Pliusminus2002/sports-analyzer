class Player:
    def __init__(self, name, points_avg, assists_avg, rebounds_avg, injury_status=False):
        self.name = name
        self.points_avg = points_avg
        self.assists_avg = assists_avg
        self.rebounds_avg = rebounds_avg
        self.injury_status = injury_status

    def is_available(self):
        return not self.injury_status


class Team:
    def __init__(self, name, sport="basketball"):
        self.name = name
        self.sport = sport
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def calculate_strength(self):
        total_strength = 0
        for player in self.players:
            if player.is_available():
                total_strength += (
                    player.points_avg * 0.5 +
                    player.assists_avg * 0.3 +
                    player.rebounds_avg * 0.2
                )
        return total_strength
