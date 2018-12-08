from animal import Animal
from dog import Dog
from cat import Cat

def main():
    animal = Animal()
    dog = Dog()
    cat = Cat()
    
    animal.speak()
    dog.speak()
    cat.speak()

    animal.sleep()
    dog.sleep()
    cat.sleep()

if __name__ == "__main__":
    main()