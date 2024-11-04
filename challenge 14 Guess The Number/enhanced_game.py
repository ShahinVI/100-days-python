
import random

class GuessGame:
    def __init__(self, seed_user=None, mode=1):
        self.seed_game = seed_user or 1234
        self.game_mode = mode
        random.seed(self.seed_game)
        self.generate_random_num()

    def generate_random_num(self):
        self.number_to_guess = random.randint(1, 100)

class PlayerGame:
    def __init__(self, player_name, guessgame):
        self.player = player_name or "player"
        self.guessed_dict = {}
        self.lives = 10 if guessgame.game_mode == 1 else 5
        self.guess = None

    def request_guess(self, guessgame):
        while self.lives > 0:
            self.guess = self.get_integer_input("Please enter your guess: ")
            if self.guess in self.guessed_dict:
                print(f"You have already guessed {self.guess} which was {self.guessed_dict[self.guess]}.")
                continue
            result = self.compare_guess(guessgame.number_to_guess)
            self.guessed_dict[self.guess] = result
            if result == "equal":
                print(f"Congrats! The correct number is {guessgame.number_to_guess}")
                return True
            else:
                self.lives -= 1
                print(f"Your guess of {self.guess} is {result}. {self.lives} tries left.\n")
        print(f"You lost! The correct number was {guessgame.number_to_guess}")
        return False

    def compare_guess(self, number_to_guess):
        diff = abs(self.guess - number_to_guess)
        if self.guess < number_to_guess:
            return "slightly lower" if diff <= 5 else "lower" if diff <= 10 else "much lower"
        elif self.guess > number_to_guess:
            return "slightly higher" if diff <= 5 else "higher" if diff <= 10 else "much higher"
        return "equal"

    @staticmethod
    def get_integer_input(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

def main():
    game_on = True
    start_game = input("Do you want to start a new game? (y/n): ").lower()
    if start_game in ["y", "yes"]:
        while game_on:
            difficulty_game = input("Do you want a difficult game? (y/n): ").lower()
            mode = 2 if difficulty_game in ["y", "yes"] else 1
            seed_rand = PlayerGame.get_integer_input("Create a seed number: ")
            player_name = input("Please enter your name: ").strip() or "Player"

            guessgame = GuessGame(seed_user=seed_rand, mode=mode)
            player = PlayerGame(player_name, guessgame)

            print(f"\nWelcome to the number guessing game, {player.player}!")
            print(f"You have {player.lives} tries to guess the correct number. Enjoy!\n")

            if not player.request_guess(guessgame):
                print("Game Over.")

            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again not in ["y", "yes"]:
                game_on = False

    print("\nTake care, goodbye!")

if __name__ == "__main__":
    main()
