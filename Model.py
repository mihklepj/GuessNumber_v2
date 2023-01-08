import os.path
import random
import datetime


class Model:

    def __init__(self):
        self.minimum = 1
        self.maximum = 100
        self.pc_nr = random.randint(self.minimum, self.maximum)
        self.steps = 0
        self.game_over = False
        self.filename = 'scores.txt'

    @staticmethod
    def time_to_score():
        # Fetch time
        return datetime.datetime.now(tz=None).strftime("%Y-%m-%d %H:%M:%S")

    def new_number(self):
        # New PC number
        return random.randint(self.minimum, self.maximum)

    def write_score_to_file(self, name, score):
        if os.path.exists(self.filename):
            '''File exists'''
            with open(self.filename, 'a', encoding='utf-8') as f:
                f.write(name + ';' + str(score) + ';' + str(self.time_to_score()) + '\n')
        else:
            with open(self.filename, 'w', encoding='utf-8') as f:
                f.write(name + ';' + str(score) + ';' + str(self.time_to_score()) + '\n')

    def read_score_file(self):
        scores = []
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                all_lines = f.readlines()
                for score in all_lines:
                    score = score.strip()
                    scores.append(score.split(';'))
        else:
            scores = None
        return sorted(scores, key=lambda x: (float(x[1]), x[2]))
