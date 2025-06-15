import cowsay
import pyjokes

print(pyjokes.get_joke())
cowsay.cow('Hello World')

joke = pyjokes.get_joke()
cowsay.cow(joke)

#using the module and colorama
from myjokes import get_funny_joke
from colorama import init, Fore

init()

# printing two extra jokes - using my own module & different cowsay characters
print(Fore.GREEN)
cowsay.tux(get_funny_joke())
print(Fore.RESET)

print(Fore.RED)
cowsay.dragon(get_funny_joke())
print(Fore.RESET)