import random
import pandas as pd

class IowaGamblingModel:
    def __init__(self):
        self.balance = 1000
        self.deck_values = [50, -50, 100, -100, 200, -200]
        self.game_data = []

    def draw_card(self):
        return random.choice(self.deck_values)

    def play_game(self, deck_index):
        result = self.draw_card()
        self.balance += result
        self.game_data.append((deck_index + 1, result))
        return result, self.balance

    def is_game_over(self):
        return self.balance < 1000

    def save_game_data(self, filename="game_data.csv"):
        df = pd.DataFrame(self.game_data, columns=["Deck", "Result"])
        df.to_csv(filename, index=False)
