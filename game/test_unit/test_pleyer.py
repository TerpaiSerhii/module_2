from unittest import TestCase, mock
from unittest.mock import patch

from game.models import BasePlayer

name = "TestUser"

class TestInit(TestCase):

    def test_init_correct_name(self):
        player = BasePlayer(name)
        self.assertEqual(player.name, name)
        self.assertEqual(player.score, 0)


class TestUpdateScore(TestCase):

    def test_update_score_pozitive_num(self):
        player = BasePlayer(name)
        player.update_score(5)
        self.assertEqual(player.score, 5)

    def test_update_score_negative_num(self):
        player = BasePlayer(name)
        player.update_score(-5)
        self.assertEqual(player.score, -5)

    def test_update_score_update_num(self):
        player = BasePlayer(name)
        player.update_score(5)
        player.update_score(3)
        self.assertEqual(player.score, 8)

    def test_update_score_update_pozitive_num(self):
        player = BasePlayer(name)
        player.update_score(-5)
        player.update_score(3)
        self.assertEqual(player.score, -2)


class TestRoollDice(TestCase):

    @patch('game.models.random.randint', return_value = 5)
    def test_roll_dice(self, mock_random):
        player = BasePlayer(name)
        self.assertEqual(player.roll_dice(), 5)