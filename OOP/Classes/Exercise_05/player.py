class Player:

    def __init__(self, playbook):
        self.playbook = playbook

    def _say_play(self, play_name, player_pos):
        play_val = self.playbook.get(play_name)
        if play_val:
            print(f"{player_pos}: {self.playbook[play_name]}")
        else:
            print(f"{player_pos}: I don't know that play...")