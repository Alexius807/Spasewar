class Game_info():

    def __init__(self):
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    # информация, меняющаяся по ходу игры
    def reset_stats(self):
        self.main_lives = 2
        self.score = 0
