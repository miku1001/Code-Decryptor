# Import pyfiglet module
import pyfiglet
from tqdm import tqdm
import time

# Create header
name = input("What's your name? ")
print(pyfiglet.figlet_format(f"Hello {name} ! Welcome !", font="Ogre"))
print("=" * 45)

# Loading Bar
for i in tqdm(range(5), desc="Loading", leave=False):
    # Simulating some processing time
    time.sleep(1)
print()
print(("\033[34mDecrypt your text here!\033[0m").center(52," "))
print("_" * 45)

# Create a dictionary for characters
dict_char = {'*': 'a',
             '&': 'e',
             '#': 'i',
             '+': 'o',
             '!': 'u'}

# Substitute the character given by the user based on dictionary
def decryption(input_char):
    output_char = ""
    for symbol in input_char:
        if symbol in dict_char:
            output_char += dict_char[symbol]
        else:
            output_char += symbol
    print()
    print("\033[35mThe Plain Text:\033[0m", output_char, end='')

# Enter the text that user wants to decrypt
decryption(input("Enter a string to decrypt: "))

# Let the user continue the process or stop
while True:
    print()
    choice = input("\nDo you want to continue? Type \033[32mY\033[0m if yes or \033[31mN\033[0m if no: ")
    if choice.upper() == "Y":
        print()
        decryption(input("Enter a string to decrypt: "))
    elif choice.upper() == "N":
        print()
        print("Exiting program bye!..." + "\U0001F600" + "\U0001F600")
        quit()
    else:
        choice = input("\nInvalid key, do you want to continue? Type \033[32mY\033[0m if yes "
                       "or \033[31mN\033[0m if no: ")
        if choice.upper() == "Y":
            print()
            decryption(input("Enter a string to decrypt: "))
        elif choice.upper() == "N":
            print()
            print("Exiting program bye!..." + "\U0001F600" + "\U0001F600")
            quit()