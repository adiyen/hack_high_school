class Campus:
    def __init__(self):
        self.buildings = []
        self.num_buildings = 0
        self.capacity = 0

    def get_info(self):
        print("The campus has {} buildings(s) with a combined capacity of {} people".format(self.num_buildings, self.capacity))

    def add_building(self, building):
        self.buildings.append(building)
        self.num_buildings +=1
        self.capacity += building.capacity