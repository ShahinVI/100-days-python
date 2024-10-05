
def life_in_weeks(age):
    return (90-int(age))*52
def main():
    game_on = True
    while game_on:
        try:
            num = int(input("Enter your age: "))
            print("The age entered is:", num)
            weeks = life_in_weeks(num)
            print(f"You have {weeks} weeks left.")
            game_on = False
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()