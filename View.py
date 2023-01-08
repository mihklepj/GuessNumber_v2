from datetime import datetime


class View:

    def __init__(self, model):
        self.model = model
        self.cheater = False

    @staticmethod
    def menu():
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
            self.cheater = True

    @staticmethod
    def ask_name():
        return input('What is your name? ')

    def show_scoreboard(self):
        ranking = 0
        scores = self.model.read_score_file()
        justification = 22
        if scores is not None:
            print()
            print('SCOREBOARD')
            print(' #', 'NAME'.rjust(4), 'SCORE'.rjust(justification-4), 'DATE & TIME'.rjust(justification-10))
            for score in scores:
                ranking += 1
                if int(len(score[0])) <= 15:
                    if ranking < 10:
                        rankjust = 2
                    else:
                        rankjust = 1
                    print(str(ranking).rjust(rankjust), score[0], score[1].rjust(justification-len(score[0]), '_'),
                          datetime.strptime(score[2], '%Y-%m-%d %H:%M:%S').strftime('%d.%m.%Y %T').rjust(20))
                elif int(len(score[0])) > 15:
                    if ranking < 10:
                        rankjust = 2
                    else:
                        rankjust = 1
                    short_score_0 = score[0][0:15] + '...'
                    justification_15 = justification - len(short_score_0)
                    print(str(ranking).rjust(rankjust), short_score_0, score[1].rjust(justification_15, '_'),
                          datetime.strptime(score[2], '%Y-%m-%d %H:%M:%S').strftime('%d.%m.%Y %T').rjust(20))
            print()
        else:
            print('First play the game!')
