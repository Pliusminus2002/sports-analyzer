import unittest
from app.models import Player, Team, PlayerFactory

class TestPlayer(unittest.TestCase):
    def test_player_availability(self):
        player = Player("Jonas", 10, 5, 7)
        self.assertTrue(player.is_available())
        injured_player = Player("Petras", 12, 3, 4, injury_status=True)
        self.assertFalse(injured_player.is_available())

class TestTeam(unittest.TestCase):
    def test_team_strength_calculation(self):
        team = Team("Žalgiris")
        player1 = Player("Jonas", 10, 5, 7)
        player2 = Player("Petras", 15, 4, 6, injury_status=True)  # bus ignoruojamas
        team.add_player(player1)
        team.add_player(player2)
        expected_strength = 10*0.5 + 5*0.3 + 7*0.2
        self.assertAlmostEqual(team.calculate_strength(), expected_strength)

class TestFactory(unittest.TestCase):
    def test_factory_creates_player(self):
        player = PlayerFactory.create_player("basketball", "Domantas", 20, 6, 8)
        self.assertIsInstance(player, Player)
        self.assertEqual(player.name, "Domantas")
        self.assertEqual(player.points_avg, 20)

if __name__ == '__main__':
    unittest.main()
