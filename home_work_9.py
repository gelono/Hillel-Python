from Hillel.home_work_8.library import get_player_figure, get_ai_figure, define_winner, text_msg, rules, put_statistic
import time

# Напишіть декоратор, який вимірює і виводить на екран час виконання функції в секундах і задекоруйте ним основну
# функцію гри з попередньої дз. Після закінчення гри декоратор має сповістити, скільки тривала гра.


def decorator_count_time(function):
    """
    This function-decorator counts the function execution time
    :param function:
    :return: str
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function(*args, **kwargs)
        finish_time = time.time()
        result = finish_time - start_time
        print(f'Time of the game took {result} seconds')

    return wrapper


@decorator_count_time
def game():
    """
    This function calls special functions from the library.py for the game "Rock, Scissors, Paper"
    :return: str
    """
    player = get_player_figure()
    ai = get_ai_figure()
    winner = define_winner(player, ai, rules)
    text_msg(winner)
    put_statistic(player, ai, winner)


game()
