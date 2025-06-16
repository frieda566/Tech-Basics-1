import cowsay
import pyjokes
from art import tprint
from myjokes import get_funny_joke
from colorama import init, Fore

# initialize colorama
init(autoreset=True)

# title
tprint("Joke Time!", font="slant")


joke = pyjokes.get_joke()
cowsay.cow(joke)

init()

# printing two extra jokes - using my own module & different cowsay characters
print(Fore.GREEN)
cowsay.tux(get_funny_joke())
print(Fore.RESET)

print(Fore.RED)
cowsay.dragon(get_funny_joke())
print(Fore.RESET)