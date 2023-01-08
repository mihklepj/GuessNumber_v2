from Controller import Controller
from Model import Model
from View import View


class GuessNumber_v2:

    def __init__(self):
        self.model = Model()
        self.view = View(self.model)
        self.controller = Controller(self.model, self.view)
        self.running = True

    def start(self):
        while self.running:
            result = self.view.menu()
            if result == 3:
                self.running = False
            elif result == 1:
                self.controller.lets_play()
                if self.model.game_over:
                    name = self.view.ask_name()
                    self.model.write_score_to_file(name, self.model.steps)
                    self.model.steps = 0
                    self.model.game_over = False
                    self.model.pc_nr = self.model.new_number()
            elif result == 2:
                self.view.show_scoreboard()




if __name__ == '__main__':
    GuessNumber_v2().start()