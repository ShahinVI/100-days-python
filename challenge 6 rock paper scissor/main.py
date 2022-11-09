rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

import random

r_seed = int(input("Create a seed number: "));
random.seed(r_seed);

print("Welcome to the most python ROCK-PAPER-SCISSOR game!");
print("no cheating !! \n");

game_on = 'y'

while (game_on.lower() == 'y'):

    rps_c = random.randint(1, 3);
    rps = input("What do you choose? Type r for Rock, p for Paper or s for Scissors.");

    print("\ncomputer choice:");

    if (rps_c == 1):
        print(rock);
    elif (rps_c == 2):
        print(paper);
    elif (rps_c == 3):
        print(scissors);

    print("you choose:");

    if (rps.lower() == 'r'):
        print(rock);
        if (rps_c == 1):
            print("no one wins");
        elif (rps_c == 2):
            print("you LOSE YOU LOSER!");
        elif (rps_c == 3):
            print("you WIN!");

    elif (rps.lower() == 'p'):
        print(paper);
        if (rps_c == 1):
            print("you WIN!");
        elif (rps_c == 2):
            print("no one wins");
        elif (rps_c == 3):
            print("you LOSE YOU LOSER!");


    elif (rps.lower() == 's'):
        print(scissors);
        if (rps_c == 1):
            print("you LOSE YOU LOSER!");
        elif (rps_c == 2):
            print("you WIN!");
        elif (rps_c == 3):
            print("no one wins");

    game_on = input("\nwant to play again? (Y / N) ");
