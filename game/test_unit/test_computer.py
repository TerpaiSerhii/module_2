from unittest import TestCase, mock

from game.models import Computer



class TestComputer(TestCase):

    def test_init_correct_name(self):
        player = Computer()
        self.assertEqual(player.name, "Комп'ютер")
        self.assertEqual(player.score, 0)