import cowsay
import pyjokes

print(pyjokes.get_joke())
cowsay.cow('Hello World')

joke = pyjokes.get_joke()
cowsay.cow(joke)