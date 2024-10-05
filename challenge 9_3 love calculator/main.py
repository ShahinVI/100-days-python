def calculate_love_score(name1,name2):
    for i in "true":
        count1 = name1.count(i)
        count2 = name2.count(i)
    for i in "love":
        count3 = name1.count(i)
        count4 = name2.count(i)
    print(f"Your love score is {count1+count2}{count3+count4}")
def main():
    game_on = True
    while game_on:
        name1 = input("Enter the first person name: ")
        while not all(char.isalpha() or char.isspace() for char in name1):
            print("Invalid input. Please enter characters only.")
            name1 = input("Enter the first person name: ")
        name2 = input("Enter the first person name: ")
        while not all(char.isalpha() or char.isspace() for char in name2):
            print("Invalid input. Please enter characters only.")
            name2 = input("Enter the first person name: ")
        print(f"calculating love between {name1} and {name2}")
        calculate_love_score(name1.lower(), name2.lower())
        game_on = False


if __name__ == "__main__":
    main()