class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        # print('Controller', model.pc_nr)

    def lets_play(self):
        self.view.cheater = False
        while not self.model.game_over:
            self.view.ask()  # Ask number and check
