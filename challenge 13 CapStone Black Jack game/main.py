import random
seed_rand = int(input("Create a seed number: "));
random.seed(seed_rand);

deck=[
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
value={
    "Ace of Clubs":1, "Ace of Hearts":1, "Ace of Diamond":1, "Ace of Spades":1,
    "2 Clubs":2, "2 Hearts":2, "2 Diamond":2, "2 Spades":2,
    "3 Clubs":3, "3 Hearts":3, "3 Diamond":3, "3 Spades":3,
    "4 Clubs":4, "4 Hearts":4, "4 Diamond":4, "4 Spades":4,
    "5 Clubs":5, "5 Hearts":5, "5 Diamond":5, "5 Spades":5,
    "6 Clubs":6, "6 Hearts":6, "6 Diamond":6, "6 Spades":6,
    "7 Clubs":7, "7 Hearts":7, "7 Diamond":7, "7 Spades":7,
    "8 Clubs":8, "8 Hearts":8, "8 Diamond":8, "8 Spades":8,
    "9 Clubs":9, "9 Hearts":9, "9 Diamond":9, "9 Spades":9,
    "10 Clubs":10, "10 Hearts":10, "10 Diamond":10, "10 Spades":10,
    "Jack of Clubs":10, "Jack of Hearts":10, "Jack of Diamond":10, "Jack of Spades":10,
    "Queen of Clubs":10, "Queen of Hearts":10, "Queen of Diamond":10, "Queen of Spades":10,
    "King of Clubs":10, "King of Hearts":10, "King of Diamond":10, "King of Spades":10
}
dealt_card=[]
card_order = list(range(0, 51))
random.shuffle(card_order)

your_cards=[]
computer_cards=[]

ace_in_comp=False
value_comp=0

for i in card_order:
    next_card = deck[i]
    dealt_card.append(next_card)


your_cards.append(dealt_card[0])
dealt_card.pop(0)
computer_cards.append(dealt_card[0])
dealt_card.pop(0)
your_cards.append(dealt_card[0])
dealt_card.pop(0)
computer_cards.append(dealt_card[0])
dealt_card.pop(0)

for c in computer_cards:
    if not c.find("Ace")==-1:
        ace_in_comp = True
    value_comp=value_comp+value[c]

while value_comp<17:
    if ace_in_comp:
        if value_comp+10 <= 21:
            value_comp=value_comp+10
    else:
        computer_cards.append(dealt_card[0])
        value_comp = value_comp + value[dealt_card[0]]
        dealt_card.pop(0)

playing = True
one_hand=True
two_hand=False
ask_once=True
split=""
your_cards1=[]
your_cards2=[]
print(f"Your cards are {[i for i in your_cards]}")
if ask_once:
    while not split.lower() in ["y","yes","n","no"]:
        split=input("do you want to split your cards? y/n ")
        if not split.lower() in ["y","yes","n","no"]:
            print("please enter a correct answer :)")
        elif split.lower() in ["y","yes"]:
            one_hand=False
            two_hand=True
            your_cards1.append(your_cards[0])
            your_cards1.append(dealt_card[0])
            dealt_card.pop(0)
            your_cards2.append(your_cards[1])
            your_cards2.append(dealt_card[0])
            dealt_card.pop(0)
            print(f"Your first hand are {[i for i in your_cards1]}")
            print(f"Your second hand are {[i for i in your_cards2]}")
    ask_once=False

value_hand=0
value_hand1=0
value_hand2=0
while playing:
    draw_card = ""
    draw_card1 = ""
    draw_card2 = ""
    show_cards = ""
    ace_is_eleven = ""
    ace_is_eleven1 = ""
    ace_is_eleven2 = ""
    ace_in_cards = False
    ace_in_cards1 = False
    ace_in_cards2 = False
    if one_hand:
        while not draw_card.lower() in ["y", "yes", "n", "no"]:
            draw_card = input("do you want to draw a card? y/n ")
            if not draw_card.lower() in ["y", "yes", "n", "no"]:
                print("please enter a correct answer :)")
        if draw_card.lower() in ["y", "yes"]:
            your_cards.append(dealt_card[0])
            dealt_card.pop(0)
            print(f"Your cards are {[i for i in your_cards]}")
        else:
            while not show_cards.lower() in ["y", "yes", "n", "no"]:
                show_cards = input("do you want to show cards and end game? y/n ")
                if not show_cards.lower() in ["y", "yes", "n", "no"]:
                    print("please enter a correct answer :)")

    elif two_hand:
        while not draw_card1.lower() in ["y", "yes", "n", "no"]:
            draw_card1 = input("do you want to draw a card for first hand? y/n ")
            if not draw_card1.lower() in ["y", "yes", "n", "no"]:
                print("please enter a correct answer :)")
        if draw_card1.lower() in ["y", "yes"]:
            your_cards1.append(dealt_card[0])
            dealt_card.pop(0)
        while not draw_card2.lower() in ["y", "yes", "n", "no"]:
            draw_card2 = input("do you want to draw a card for second hand? y/n ")
            if not draw_card2.lower() in ["y", "yes", "n", "no"]:
                print("please enter a correct answer :)")
        if draw_card2.lower() in ["y", "yes"]:
            your_cards2.append(dealt_card[0])
            dealt_card.pop(0)
        else:
            while not show_cards.lower() in ["y", "yes", "n", "no"]:
                show_cards = input("do you want to show cards and end game? y/n ")
                if not show_cards.lower() in ["y", "yes", "n", "no"]:
                    print("please enter a correct answer :)")
        print(f"Your first hand are {[i for i in your_cards1]}")
        print(f"Your second hand are {[i for i in your_cards2]}")

    if show_cards.lower() in ["y", "yes"]:
        playing=False
        if one_hand:
            for c in your_cards:
                if not c.find("Ace") == -1:
                    ace_in_cards = True
                value_hand = value_hand + value[c]
            if ace_in_cards:
                while not ace_is_eleven.lower() in ["y", "yes", "n", "no"]:
                    ace_is_eleven = input("do you want one ace to be valued 11 instead of 1? y/n ")
                    if not ace_is_eleven.lower() in ["y", "yes", "n", "no"]:
                        print("please enter a correct answer :)")
                    if ace_is_eleven.lower() in ["y", "yes"]:
                        value_hand = value_hand+10
            print(f"your cards are {[i for i in your_cards]} with sum value of {value_hand}")
        elif two_hand:
            for c in your_cards1:
                if not c.find("Ace") == -1:
                    ace_in_cards1 = True
                value_hand1 = value_hand1 + value[c]
            if ace_in_cards1:
                while not ace_is_eleven1.lower() in ["y", "yes", "n", "no"]:
                    ace_is_eleven1 = input("do you want one ace to be valued 11 instead of 1 in first hand? y/n ")
                    if not ace_is_eleven1.lower() in ["y", "yes", "n", "no"]:
                        print("please enter a correct answer :)")
                    if ace_is_eleven1.lower() in ["y", "yes"]:
                        value_hand1 = value_hand1+10
            for c in your_cards2:
                if not c.find("Ace") == -1:
                    ace_in_cards2 = True
                value_hand2 = value_hand2 + value[c]
            if ace_in_cards2:
                while not ace_is_eleven2.lower() in ["y", "yes", "n", "no"]:
                    ace_is_eleven2 = input("do you want one ace to be valued 11 instead of 1 in second hand? y/n ")
                    if not ace_is_eleven2.lower() in ["y", "yes", "n", "no"]:
                        print("please enter a correct answer :)")
                    if ace_is_eleven2.lower() in ["y", "yes"]:
                        value_hand2 = value_hand2+10
            print(f"your cards are {[i for i in your_cards1]} with sum value of {value_hand1}")
            print(f"your cards are {[i for i in your_cards2]} with sum value of {value_hand2}")

        print(f"Computer cards are {[i for i in computer_cards]} with sum value of {value_comp}")

if one_hand:
    if value_hand<=21:
        if value_hand>value_comp:
            print("your cards win")
        elif value_hand>value_comp:
            print("draw")
        elif value_comp>21:
            print("your cards wins")
        else:
            print("your card lost")
    else:
        print("your card exceeds 21. your card lose")
elif two_hand:
    if value_hand1<=21:
        if value_hand1>value_comp:
            print("your first hand wins")
        elif value_hand1==value_comp:
            print("your first hand draws")
        elif value_comp>21:
            print("your first hand wins")
        else:
            print("your first hand lost")
    else:
        print("your first hand cards exceeds 21. your cards lose")
    if value_hand2<=21:
        if value_hand2>value_comp:
            print("your second hand wins")
        elif value_hand2==value_comp:
            print("your second hand draws")
        elif value_comp>21:
            print("your second hand wins")
        else:
            print("your second hand lost")
    else:
        print("your second hand cards exceeds 21. your cards lose")