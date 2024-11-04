import random

class guess_game:
    game_mode = 0 # 0 start game,1 easy mode,2 hard mode,3 exit
    seed_game = 1234
    number_to_guess = None

    def generate_random_num(self):
        self.number_to_guess = random.randint(1, 100)

    def __init__(self,seed_user,mode):
        if seed_user is not None:
            self.seed_game=seed_user
        if mode == 1:
            self.game_mode=mode
        elif mode == 2:
            self.game_mode = mode

        random.seed(self.seed_game)
        self.generate_random_num()


class player_game():
    player=""
    guess=None
    guessed_dict = {}
    lives = None

    def request_guess(self,guessgame):
        prompt= "Please enter your guess: "
        self.guessed_dict = {}
        while True:
            try:
                self.guess = int(input(prompt))
                if self.guess in self.guessed_dict:
                    print(f"you have already guess this number and it was wrong.\nAs a reminder this guess was {self.guessed_dict[self.guess]} than the number.")
                else:
                    result = self.compare_guess(guessgame)
                    self.guessed_dict[self.guess] = result
                    if result == "equal":
                        print(f"Congrats you guessed correctly the real number is {guessgame.number_to_guess}")
                        break
                    else:
                        self.lives = self.lives-1
                        print(f"Your guess was {self.guess} which is {result} than the number.\n"
                              f"You have {self.lives} tries left\n")
                        if self.lives <= 0:
                            print(f"you lost, the correct guess was {guessgame.number_to_guess}")
                            break
            except ValueError:
                print("Invalid input. Please enter a valid integer.\n")

    def compare_guess(self,guessgame):
        number_to_guess=guessgame.number_to_guess
        if(number_to_guess>self.guess):
            diff=number_to_guess-self.guess
            if diff <= 5:
                return "slightly lower"
            elif diff <= 10:
                return "lower"
            else:
                return "much lower"
        elif(number_to_guess<self.guess):
            diff = self.guess - number_to_guess
            if diff <= 5:
                return "slightly higher"
            elif diff <= 10:
                return "higher"
            else:
                return "much higher"
        else:
            return "equal"

    def __init__(self,i,player_name,guessgame):
        if player_name is not None:
            self.player=player_name
        else:
            self.player = f"player{i}"
        if guessgame.game_mode == 1:
            self.lives = 10
        elif guessgame.game_mode == 2:
            self.lives = 5

game_on = True
difficulty_game=""
number_of_players=1
while game_on:
    start_game = ""
    while not start_game.lower() in ["y", "yes", "n", "no"]:
        start_game = input("Do you want to start a new game? y/n ")
        if not start_game.lower() in ["y", "yes", "n", "no"]:
            print("please enter a correct answer :)")
    if start_game.lower() in ["y", "yes"]:
        while not difficulty_game.lower() in ["y", "yes", "n", "no"]:
            difficulty_game = input("Do you want a difficult game? y/n ")
            if not difficulty_game.lower() in ["y", "yes", "n", "no"]:
                print("please enter a correct answer :)")
        seed_rand = int(input("Create a seed number: "));
        if difficulty_game in ["y", "yes"]:
            guessgame = guess_game(seed_user=seed_rand,mode=2)
        else:
            guessgame = guess_game(seed_user=seed_rand, mode=1)

        player_name = str(input("Please enter your name: "))
        player=player_game(number_of_players,player_name,guessgame)
        number_of_players=number_of_players+1
        print("game loading ...")
        print(f"\n\n\n Welcome to the number guessing game.\nYou have {player.lives} tries to guess the correct number!\n\t\tEnjoy!\n")
        while guessgame.game_mode != 3:
            start_game = ""
            difficulty_game = ""
            player.request_guess(guessgame)
            while not start_game.lower() in ["y", "yes", "n", "no"]:
                start_game = input("Do you want to play again? y/n ")
                if not start_game.lower() in ["y", "yes", "n", "no"]:
                    print("please enter a correct answer :)")
            if start_game.lower() in ["y", "yes"]:
                while not difficulty_game.lower() in ["y", "yes", "n", "no"]:
                    difficulty_game = input("Do you want to change difficulty of the game? y/n ")
                    if not difficulty_game.lower() in ["y", "yes", "n", "no"]:
                        print("please enter a correct answer :)")
                if difficulty_game in ["y", "yes"]:
                    guessgame.game_mode=guessgame.game_mode%2+1
                guessgame.generate_random_num()
                del player
                player = player_game(number_of_players, player_name, guessgame)
            else:
                guessgame.game_mode=3
    print("\n\n Take care good bye!")
    game_on=False









