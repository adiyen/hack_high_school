from classroom import Classroom

def main():
    classroom1 = Classroom("Wesley")
    classroom2 = Classroom("Anand")
    classroom1.add_student("Alice")
    classroom2.add_student("Bob")
    classroom1.add_student("Carol")
    classroom2.add_student("Dave")
    classroom1.add_student("Eve")
    classroom1.status()
    classroom2.status()
    classroom1.begin_class()
    classroom2.begin_class()

if __name__ == "__main__":
    main()