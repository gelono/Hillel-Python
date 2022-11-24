from Hillel.home_work_8.library import get_player_figure, get_ai_figure, define_winner, text_msg, rules, put_statistic


# Візьміть гру з попереднього ДЗ ('rock scissors paper lizard spock') і модифікуйте наступним чином:
# винесіть всі функції в окремий файл (нехай буде library.py) і імпортуцте їх звідти для роботи в основний файл
# додайте запис статистики в файл (які фігури грали і хто переміг на кожному ході), використовуйте open.


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
