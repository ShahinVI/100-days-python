alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    if direction == "decode":
        shift = -1 * shift
        max = -1 * 26
    else:
        max = 26
    cipher_text = ""
    print(f"plain_text = {text}")
    for l in text:
        # TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"
        if not l in alphabet:
            cipher_text += l
            continue

        i = alphabet.index(l)
        if i + shift >= len(alphabet) or i + shift < 0:
            i = i + shift - max
        else:
            i = i + shift
        cipher_text += alphabet[i]

    print(f"shift = {shift}\ncipher_text = {cipher_text}\nThe {direction}d text is {cipher_text}")


# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo

print(logo)

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
playgame = True
while playgame:
    answer = input("do you want to play game ? y/n ")
    if answer.lower() in ["no", "n"]:
        playgame = False
        print("\nbye bye\n")
        continue
    elif answer.lower() in ["yes", "y"]:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
    else:
        print("wrong input try again")
    # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    # Try running the program and entering a shift number of 45.
    # Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    # Hint: Think about how you can use the modulus (%).
    if (shift >= 26):
        shift = shift % 26
    caesar(text, shift, direction)
