from building import Building
from campus import Campus

def main():
    math_building = Building("Math Building", 25)
    math_building.get_info()

    science_building = Building("Science Building", 17)
    science_building.get_info()

    my_campus = Campus()
    my_campus.add_building(math_building)
    my_campus.add_building(science_building)
    my_campus.get_info()
    
if __name__ == "__main__":
    main()