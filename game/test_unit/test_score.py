import unittest
from unittest.mock import mock_open, patch
import json
from datetime import datetime
from game.score import save_result, get_results

class TestGameResults(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    def test_save_result_creates_entry(self, mock_file):
        with patch("json.dump") as mock_json_dump:
            name = "Тестовий гравець"
            rounds = 3
            score = 10
            save_result(name, rounds, score)

            args, _ = mock_json_dump.call_args
            saved_data = args[0]
            self.assertEqual(len(saved_data), 1)
            self.assertEqual(saved_data[0]["Гравець"], name)
            self.assertEqual(saved_data[0]["Кількість рандів"], rounds)
            self.assertEqual(saved_data[0]["Ігровий рахунок"], score)
            self.assertIn("Дата", saved_data[0])

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps([
        {
            "Дата": "2025-04-28 12:00:00",
            "Гравець": "Гравець 1",
            "Кількість рандів": 5,
            "Ігровий рахунок": 15
        }
    ]))
    def test_get_results_prints_data(self, mock_file):
        with patch("builtins.print") as mock_print:
            get_results()

            mock_print.assert_any_call("\n--- Результати ігор ---")
            mock_print.assert_any_call("Дата: 2025-04-28 12:00:00")
            mock_print.assert_any_call("Ім'я гравця: Гравець 1")
            mock_print.assert_any_call("Кількість раундів: 5")
            mock_print.assert_any_call("Підсумковий рахунок: 15")
            mock_print.assert_any_call("-" * 30)

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_get_results_file_not_found(self, mock_file):
        with patch("builtins.print") as mock_print:
            get_results()
            mock_print.assert_any_call("Результати ще не збережені.")

if __name__ == "__main__":
    unittest.main()
