class View:

    def __init__(self, model):
        self.model = model
        # print('View',model.pc_nr)  # Test

    def menu(self):
        print('1. Lets Play Game')
        print('2. Show Leaderboard')
        print('3. Exit')
        return int(input('Input choice 1, 2 or 3: '))

    def ask(self):
        mn = str(self.model.minimum)
        mx = str(self.model.maximum)
        user_input = int(input('Input number '+mn+' - '+mx+': '))
        self.model.steps += 1
        if user_input > self.model.pc_nr and user_input != 10000:
            print('Smaller')
        elif user_input < self.model.pc_nr and user_input != 10000:
            print('Bigger')
        elif user_input == self.model.pc_nr and user_input != 10000:
            print('You guessed the number in ' + str(self.model.steps) + ' steps.')
            self.model.game_over = True
        elif user_input == 10000:
            print('You found the back door! The correct number is', self.model.pc_nr)

    def ask_name(self):
        return input('What is your name? ')

    def show_scoreboard(self):
        scores = self.model.read_score_file()
        if scores is not None:
            print('===SCOREBOARD===')
            for score in scores:
                print(score[0], score[1], score[2])  # Name and steps and timestamp
        else:
            print('First play the game!')