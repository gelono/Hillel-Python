from abc import ABC, abstractmethod
from random import choice


class GameFigure:
    __rock: str = 'Rock'
    __paper: str = 'Paper'
    __scissors: str = 'Scissors'
    __rules = {
        'Rock': 'Scissors',
        'Scissors': 'Paper',
        'Paper': 'Rock',
    }

    @property
    def rock(self):
        return self.__rock

    @property
    def paper(self):
        return self.__paper

    @property
    def scissors(self):
        return self.__scissors

    def define_winner(self, figure_human, figure_ai):
        """
        This function defines who is a winner
        :param figure_human: str
        :param figure_ai: str
        :return: str
        """
        if figure_human == figure_ai:
            win = 'friendship'
        elif self.__rules[figure_human] == figure_ai:
            win = 'Player'
        else:
            win = 'AI'
        print(f'The winner is the: {win}')
        return win


class Player(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_figure(self):
        pass


class HumanPlayer(Player):
    _fig_num: int = None
    _game_figure: GameFigure = None

    def __init__(self, game_figure: GameFigure):
        print(' The rules:\n -The rock breaks the scissors,\n', '-The scissors cuts the paper,\n',
              '-The paper wraps the rock\n')
        self.fig_num = int(input('Please, enter a number from the list (1 = Rock, 2 = Paper, 3 = Scissors): '))
        self.game_figure = game_figure

    def get_figure(self):
        """
        This function returns a figure with a choice from human player
        :return: str
        """
        dct = {1: self.game_figure.rock,
               2: self.game_figure.paper,
               3: self.game_figure.scissors}
        human_figure = dct[self.fig_num]
        print(f'The Human shows the {human_figure}')
        return human_figure

    @property
    def fig_num(self):
        return self._fig_num

    @fig_num.setter
    def fig_num(self, value):
        if value not in (1, 2, 3):
            raise ValueError('The number must be from the list: 1, 2, 3')
        self._fig_num = value

    @property
    def game_figure(self):
        return self._game_figure

    @game_figure.setter
    def game_figure(self, value):
        if not isinstance(value, GameFigure):
            raise TypeError
        self._game_figure = value


class AIPlayer(Player):
    _game_figure: GameFigure = None

    def __init__(self, game_figure: GameFigure):
        self.game_figure = game_figure

    def get_figure(self):
        """
        This function returns a random figure for the AI player
        :return: str
        """
        figure_list = [self.game_figure.rock, self.game_figure.paper, self.game_figure.scissors]
        ai_figure = choice(figure_list)
        print(f'The AI shows the {ai_figure}')
        return ai_figure

    @property
    def game_figure(self):
        return self._game_figure

    @game_figure.setter
    def game_figure(self, value):
        if not isinstance(value, GameFigure):
            raise TypeError
        self._game_figure = value


class Game:
    _figure: GameFigure = None

    def __init__(self, figure: GameFigure):
        self.figure = figure

    def start_game(self):
        human = HumanPlayer(self.figure)
        ai = AIPlayer(self.figure)
        human_figure = human.get_figure()
        ai_figure = ai.get_figure()
        winner = self.figure.define_winner(human_figure, ai_figure)
        self.put_statistic(human_figure, ai_figure, winner)

    @staticmethod
    def put_statistic(human_figure, ai_figure, winner):
        """
        This function adds to the file every figure and the game winner
        :param player_figure: str
        :param ai_figure: str
        :param winner: str
        :return: None
        """
        with open('statistic.txt', 'a') as file:
            file.write(
                f'The player showed: {human_figure}, the AI showed: {ai_figure}, the winner was {winner}' + '\n')

    @property
    def figure(self):
        return self._figure

    @figure.setter
    def figure(self, value):
        if not isinstance(value, GameFigure):
            raise TypeError
        self._figure = value
