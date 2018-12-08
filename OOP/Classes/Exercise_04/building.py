class Building:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
    
    def get_info(self):
        print('Building "{}" can hold {} people'.format(self.name, self.capacity))
    