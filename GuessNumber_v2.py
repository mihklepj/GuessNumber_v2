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
                self.model.time_to_score()
                self.controller.lets_play()
                if self.model.game_over is True and self.view.cheater is True:
                    print('You used the backdoor!\n'
                          'Your result will not show on scoreboard!')
                    self.model.game_over = False
                    self.model.pc_nr = self.model.new_number()
                elif self.model.game_over and self.view.cheater is False:
                    name = self.view.ask_name()
                    self.model.write_score_to_file(name, self.model.steps)
                    self.model.steps = 0
                    self.model.game_over = False
                    self.model.pc_nr = self.model.new_number()
            elif result == 2:
                if self.view.cheater is False:
                    self.view.show_scoreboard()
                elif self.view.cheater is True:
                    print('Cheaters cannot see the scoreboard!')


if __name__ == '__main__':
    GuessNumber_v2().start()
