from game.game import start_game
from game.score import get_results
from game.exceptions import InvalidInputError

def main_menu():
    while True:
        print("\n--- Гра 'Кості' ---")
        print("1. Грати")
        print("2. Переглянути результати")
        print("3. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            start_game()
        elif choice == "2":
            get_results()
        elif choice == "3":
            print("Дякуємо за гру!")
            break
        else:
            print("Невірний вибір. Спробуйте ще.")

if __name__ == "__main__":
    main_menu()
