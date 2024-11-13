class Statis():

    intro = False
    game_active = False
    play_again = True
    high_score = 0
    score = 0
    level = 1
    life = 3

    @staticmethod
    def reset_game():
        Statis.current_score = 0
        Statis.level = 1
        Statis.life = 3