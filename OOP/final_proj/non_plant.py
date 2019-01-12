class Non_Plant(Organism):
    def __init__(self):
        worth = 20
#         super().__init__()
        self.hp = 80
        self.dmg = 5
        
    def attack(self, plant):
        