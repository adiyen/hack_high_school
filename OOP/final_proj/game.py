from linked_list import LinkedList
from hhs_queue import Queue
from stack import Stack
from wave import Wave
from non_plant import Non_Plant
from plant import Plant
from card import Card
import random

class Game:
    def __init__(self, file):
        with open(file, 'r') as f:
            self.cash, self.height, self.width = [int(x) for x in f.readline().split(' ')]
            self.waves = LinkedList()
            self.waves_num = 0
            for line in iter(f.readline, ''):
                self.waves.add(Wave(*[int(x) for x in line.split(' ')]))
                self.waves_num += 1
        # WRITE YOUR ADDITIONAL INIT CODE HERE
        