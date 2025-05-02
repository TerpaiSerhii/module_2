from game.models import Player, Computer
from game.settings import GAME_LEVELS, GAME_LEVELS_CONVERT
from game.score import save_result
from game.exceptions import InvalidInputError

def start_game():
    name = input("Введіть своє ім'я: ")
    player = Player(name)
    computer = Computer()

    print("\nОберіть рівень гри:")
    print("1 - Коротка гра (5 раундів)")
    print("2 - Середня гра (8 раундів)")
    print("3 - Довга гра (10 раундів)")

    while True:
        level_choice = input("Ваш вибір: ")
        if level_choice in GAME_LEVELS:
            total_rounds = GAME_LEVELS[level_choice]
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

    print(f"\nГра почалася! Рівень: {GAME_LEVELS_CONVERT[total_rounds]}")
    
    current_round = 1
    while current_round <= total_rounds:
        print(f"\nРаунд {current_round}:")

        while True:
            roll_input = input("Киньте кубик (натисніть Enter): ")
            if roll_input == "":
                player_roll = player.roll_dice()
                computer_roll = computer.roll_dice()
                print(f"Ви кинули кубик: {player_roll}")
                print(f"Комп'ютер кинув кубик: {computer_roll}")

                if player_roll > computer_roll:
                    delta = player_roll - computer_roll
                    print(f"Ви виграли цей раунд! +{delta} очок")
                    player.update_score(delta)
                    break
                elif player_roll < computer_roll:
                    delta = player_roll - computer_roll
                    print(f"Комп'ютер виграв цей раунд. {delta} очок")
                    player.update_score(delta)
                    break
                else:
                    print("Нічия! Повторіть бросок.")
            else:
                print("Бросок не зроблено! Натисніть Enter для повторного броска.")

        current_round += 1

    print("\n--- Гру завершено ---")
    print(f"Гравець: {player.name}")
    print(f"Рівень гри: {GAME_LEVELS_CONVERT[total_rounds]}")
    print(f"Підсумковий рахунок: {player.score} очок")

    save_result(player.name, total_rounds, player.score)
