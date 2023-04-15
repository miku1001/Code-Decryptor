# Import pyfiglet module
import pyfiglet

# Create header
name = input("What's your name? ")
print(pyfiglet.figlet_format(f"Hello {name} ! Welcome !", font="Ogre"))
print("=" * 45)
print(("\033[34mDecrypt your text here!\033[0m").center(52," "))
print("_" * 45)

# Create a dictionary for characters
dict_char = {'*': 'a',
             '&': 'e',
             '#': 'i',
             '+': 'o',
             '!': 'u'}
    
# Substitute the character given by the user based on dictionary
# Enter the text that user wants to decrypt
# Let the user continue the process or stop