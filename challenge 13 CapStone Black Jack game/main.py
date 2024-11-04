import random

class black_jack():
    seed_rand= 1234
    one_hand = True
    two_hand = False
    deck = [
        "Ace of Clubs", "Ace of Hearts", "Ace of Diamond", "Ace of Spades",
        "2 Clubs", "2 Hearts", "2 Diamond", "2 Spades",
        "3 Clubs", "3 Hearts", "3 Diamond", "3 Spades",
        "4 Clubs", "4 Hearts", "4 Diamond", "4 Spades",
        "5 Clubs", "5 Hearts", "5 Diamond", "5 Spades",
        "6 Clubs", "6 Hearts", "6 Diamond", "6 Spades",
        "7 Clubs", "7 Hearts", "7 Diamond", "7 Spades",
        "8 Clubs", "8 Hearts", "8 Diamond", "8 Spades",
        "9 Clubs", "9 Hearts", "9 Diamond", "9 Spades",
        "10 Clubs", "10 Hearts", "10 Diamond", "10 Spades",
        "Jack of Clubs", "Jack of Hearts", "Jack of Diamond", "Jack of Spades",
        "Queen of Clubs", "Queen of Hearts", "Queen of Diamond", "Queen of Spades",
        "King of Clubs", "King of Hearts", "King of Diamond", "King of Spades"
    ]
    value = {
        "Ace of Clubs": 1, "Ace of Hearts": 1, "Ace of Diamond": 1, "Ace of Spades": 1,
        "2 Clubs": 2, "2 Hearts": 2, "2 Diamond": 2, "2 Spades": 2,
        "3 Clubs": 3, "3 Hearts": 3, "3 Diamond": 3, "3 Spades": 3,
        "4 Clubs": 4, "4 Hearts": 4, "4 Diamond": 4, "4 Spades": 4,
        "5 Clubs": 5, "5 Hearts": 5, "5 Diamond": 5, "5 Spades": 5,
        "6 Clubs": 6, "6 Hearts": 6, "6 Diamond": 6, "6 Spades": 6,
        "7 Clubs": 7, "7 Hearts": 7, "7 Diamond": 7, "7 Spades": 7,
        "8 Clubs": 8, "8 Hearts": 8, "8 Diamond": 8, "8 Spades": 8,
        "9 Clubs": 9, "9 Hearts": 9, "9 Diamond": 9, "9 Spades": 9,
        "10 Clubs": 10, "10 Hearts": 10, "10 Diamond": 10, "10 Spades": 10,
        "Jack of Clubs": 10, "Jack of Hearts": 10, "Jack of Diamond": 10, "Jack of Spades": 10,
        "Queen of Clubs": 10, "Queen of Hearts": 10, "Queen of Diamond": 10, "Queen of Spades": 10,
        "King of Clubs": 10, "King of Hearts": 10, "King of Diamond": 10, "King of Spades": 10
    }

    dealt_card = []

    def __init__(self,seed_rand_u=None):
        if not seed_rand_u == None:
            self.seed_rand=seed_rand_u
        #seed_rand = int(input("Create a seed number: "));
        random.seed(self.seed_rand);

        card_order = list(range(0, 51))
        random.shuffle(card_order)

        for i in card_order:
            next_card = self.deck[i]
            self.dealt_card.append(next_card)


class hand():
    player=""
    card_hand=[]
    card_score=0
    ace_in_cards=False
    ace_is_eleven=False

    def ace_eleven(self):
        self.card_score=self.card_score+10
        return self

    def print_hand(self):
        print(f"{self.player} cards are {[i for i in self.card_hand]} with total score {self.card_score}")

    def calculate_score(self,blackjack):
        score = 0
        for c in self.card_hand:
            score = score+blackjack.value[c]
        self.card_score=score
        return self

    def draw_card(self,blackjack,pos=0):
        self.card_hand.append(blackjack.dealt_card[pos])
        self.card_score = self.card_score + blackjack.value[blackjack.dealt_card[pos]]
        if not blackjack.dealt_card[pos].find("Ace") == -1:
            self.ace_in_cards=True
        blackjack.dealt_card.pop(pos)
        return self
        #return hand.card_hand

    def split_cards(self, blackjack):
        hand2 = hand(player="second hand", card_hand=self.card_hand[1])
        hand2 = hand2.draw_card(blackjack=blackjack)
        hand2 = hand2.calculate_score(blackjack=blackjack)
        self.card_hand.pop(1)
        self = self.draw_card(blackjack=blackjack)
        self = self.calculate_score(blackjack=blackjack)
        return  hand2

    def __init__(self,player=None,card_hand=None):
        if not player == None:
            self.player=player
        if not card_hand== None:
            self.card_hand=[]
            self.card_hand.append(card_hand)
        else:
            self.card_hand=[]

        self.card_score = 0
        ace_in_cards = False
        ace_is_eleven = False


game_on = True

while game_on:
    start_game = ""
    hand_list = []
    while not start_game.lower() in ["y","yes","n","no"]:
        start_game = input("Do you want to start a new game? y/n ")
        if not start_game.lower() in ["y","yes","n","no"]:
            print("please enter a correct answer :)")
    if start_game.lower() in ["y","yes"]:
        start_game=""
        seed_rand = int(input("Create a seed number: "));
        blackjack = black_jack(seed_rand=seed_rand)
        computer_hand = hand(player="computer")
        first_hand = hand(player="first hand")
        hand_list.append(first_hand)

        computer_hand = computer_hand.draw_card(blackjack=blackjack)
        first_hand  = first_hand.draw_card(blackjack=blackjack)
        computer_hand  = computer_hand.draw_card(blackjack=blackjack)
        first_hand  = first_hand.draw_card(blackjack=blackjack)


        while computer_hand.card_score < 17:
            if computer_hand.ace_in_cards:
                if computer_hand.card_score + 10 <= 21:
                    computer_hand=computer_hand.ace_eleven()
            else:
                computer_hand = computer_hand.draw_card(blackjack=blackjack)

        first_hand.print_hand()
        split=""
        while not split.lower() in ["y", "yes", "n", "no"]:
            split = input("do you want to split your cards? y/n ")
            if not split.lower() in ["y", "yes", "n", "no"]:
                print("please enter a correct answer :)")
            elif split.lower() in ["y", "yes"]:
                second_hand = first_hand.split_cards(blackjack=blackjack)
                hand_list.append(second_hand)
        print("\n")
        for hands in hand_list:
            hands.print_hand()

        draw_cards=True
        while draw_cards:
            for hands in hand_list:
                draw_cardq = ""
                while not draw_cardq.lower() in ["y", "yes", "n", "no"]:
                    draw_cardq = input(f"do you want to draw a card for {hands.player}? y/n ")
                    if not draw_cardq.lower() in ["y", "yes", "n", "no"]:
                        print("please enter a correct answer :)")
                if draw_cardq.lower() in ["y", "yes"]:
                    hands = hands.draw_card(blackjack=blackjack)
            print("\n")
            for hands in hand_list:
                hands.print_hand()
            draw_cardq = ""
            while not draw_cardq.lower() in ["y", "yes", "n", "no"]:
                draw_cardq = input(f"do you want to show cards and see if you won? y/n ")
                if not draw_cardq.lower() in ["y", "yes", "n", "no"]:
                    print("please enter a correct answer :)")
            if draw_cardq.lower() in ["y", "yes"]:
                draw_cards = False

        print("\n")
        for hands in hand_list:
            if hands.ace_in_cards:
                hands.print_hand()
                ace_is_eleven=""
                while not ace_is_eleven.lower() in ["y", "yes", "n", "no"]:
                    ace_is_eleven = input("do you want one ace to be valued 11 instead of 1? y/n ")
                    if not ace_is_eleven.lower() in ["y", "yes", "n", "no"]:
                        print("please enter a correct answer :)")
                if ace_is_eleven.lower() in ["y", "yes"]:
                    hands.ace_eleven()
        print("\n")
        for hands in hand_list:
            hands.print_hand()
        computer_hand.print_hand()
        print("\n")
        for hands in hand_list:
            if hands.card_score<=21:
                if hands.card_score> computer_hand.card_score:
                    print(f"your {hands.player} cards win")
                elif hands.card_score == computer_hand.card_score:
                    print(f"your {hands.player} cards draw with computer")
                elif computer_hand.card_score > 21:
                    print(f"your {hands.player} cards wins")
                else:
                    print(f"your {hands.player} card lost")
            else:
                print(f"your {hands.player} exceeds 21. your card lose")
    else:
        print("Take care of yourself. Goodbye :)")
        game_on = False