from player import Player

class PointGaurd(Player):
    def run_play(self, play_name):
        self._say_play(play_name, "Point Gaurd")

class ShootingGaurd(Player):
    def run_play(self, play_name):
        self._say_play(play_name, "Shooting Gaurd")

class SmallForward(Player):
    def run_play(self, play_name):
        self._say_play(play_name, "Small Forward")

class PowerForward(Player):
    def run_play(self, play_name):
        self._say_play(play_name, "Power Forward")

class Center(Player):
    def run_play(self, play_name):
        self._say_play(play_name, "Center")
