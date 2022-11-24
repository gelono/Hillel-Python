from random import choice

rules = {
    'Rock': 'Scissors',
    'Scissors': 'Paper',
    'Paper': 'Rock',
}


def get_player_figure():
    """
    This function prompts the player to specify the figure for the game 'Rock, Paper, Scissors'
    :return: str
    """
    while True:
        player_figure = input('Enter your figure, please ("Rock", "Scissors" or "Paper"): ')
        player_figure = player_figure.title()
        if player_figure in ('Rock', 'Scissors', 'Paper'):
            break
        else:
            print('Please, select your figure from the list: "Rock", "Scissors" or "Paper"')
    print(' -The rock breaks the scissors,\n', '-The scissors cuts the paper,\n', '-The paper wraps the rock')
    return player_figure


def get_ai_figure():
    """
    This function randomly determines the figure selected by the artificial intelligence for the game 'Rock, paper, scissors'
    :return: str
    """
    figures = ['Rock', 'Scissors', 'Paper']
    ai_figure = choice(figures)
    print(f'AI shows the {ai_figure}')
    return ai_figure


def define_winner(figure_pl, figure_ai, game_rules):
    """
    This function defines who is a winner
    :param figure_pl: str
    :param figure_ai: str
    :param game_rules: dict
    :return: str
    """
    if figure_pl == figure_ai:
        win = 'friendship'
    elif game_rules[figure_pl] == figure_ai:
        win = 'Player'
    else:
        win = 'AI'
    return win


def text_msg(game_winner):
    """
    This function announces who is win
    :param game_winner: str
    :return: str
    """
    print(f'The winner is the {game_winner}')


def put_statistic(player_figure, ai_figure, winner):
    """
    This function adds to the file every figure and the game winner
    :param player_figure: str
    :param ai_figure: str
    :param winner: str
    :return: None
    """
    with open('statistic.txt', 'a') as file:
        file.write(f'The player showed: {player_figure}, the AI showed: {ai_figure}, the winner was {winner}' + '\n')
