from greeter import Greeter
from insult_comic import Insult

def main():
    greeter = Greeter()
    insult = Insult()

    greeter.speak("Wesley")
    insult.speak("Wesley")

if __name__ == "__main__":
    main()