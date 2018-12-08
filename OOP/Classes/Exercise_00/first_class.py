class FirstClass:
    def __init__(self, saying):
        self.saying = saying
        print(saying)

def main():
    first_class = FirstClass("First!")

if __name__ == "__main__":
    main()