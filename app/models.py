from abc import ABC, abstractmethod

class BasePlayer(ABC):
    def __init__(self, name, injury_status=False):
        self.name = name
        self.injury_status = injury_status

    def is_available(self):
        return not self.injury_status

    @abstractmethod
    def calculate_strength(self):
        pass


class BasketballPlayer(BasePlayer):
    def __init__(self, name, points_avg, assists_avg, rebounds_avg, injury_status=False):
        super().__init__(name, injury_status)
        self.points_avg = points_avg
        self.assists_avg = assists_avg
        self.rebounds_avg = rebounds_avg

    def calculate_strength(self):
        return (self.points_avg * 0.5 + self.assists_avg * 0.3 + self.rebounds_avg * 0.2)


class FootballPlayer(BasePlayer):
    def __init__(self, name, goals, assists, yellow_cards, injury_status=False):
        super().__init__(name, injury_status)
        self.goals = goals
        self.assists = assists
        self.yellow_cards = yellow_cards

    def calculate_strength(self):
        return (self.goals * 0.6 + self.assists * 0.3 - self.yellow_cards * 0.1)


class VolleyballPlayer(BasePlayer):
    def __init__(self, name, spikes, blocks, aces, injury_status=False):
        super().__init__(name, injury_status)
        self.spikes = spikes
        self.blocks = blocks
        self.aces = aces

    def calculate_strength(self):
        return (self.spikes * 0.4 + self.blocks * 0.4 + self.aces * 0.2)


class Team:
    def __init__(self, name, sport):
        self.name = name
        self.sport = sport
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def calculate_strength(self):
        return sum(player.calculate_strength() for player in self.players if player.is_available())


class PlayerFactory:
    @staticmethod
    def create_player(sport, **kwargs):
        if sport == "basketball":
            return BasketballPlayer(**kwargs)
        elif sport == "football":
            return FootballPlayer(**kwargs)
        elif sport == "volleyball":
            return VolleyballPlayer(**kwargs)
        else:
            raise ValueError("Unsupported sport type")
