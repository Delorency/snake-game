from game import Game
from snake import Snake
from food import Food
from menu import Menu


class Start:
    def __init__(self):
        self.game = Game()
        self.snake = Snake(self.game.white, self.game.coefficient, self.game.sc_width, self.game.sc_height)
        self.food = Food(self.game.sc_width, self.game.sc_height, self.game.coefficient)
        self.menu = Menu()

        self.game.initialization()
        self.menu.initialization_menu()

    @property
    def game_status(self):
        return self.game.start

    def game_menu(self):
        self.menu.draw_items(self.game.sc, self.game.get_score)
        self.menu.keys_animation()

        self.menu.check_key()

        self.game.start, self.food.food_pos = self.menu.begin_game(self.game.start, self.game.sc_width,
                                                                   self.game.sc_height, self.food.food_pos,
                                                                   self.game.coefficient)

    def snake_game(self):
        self.snake.change_to = self.game.check_key(self.snake.change_to)

        self.snake.change_direction()

        self.snake.change_head_pos(self.game.coefficient)

        self.game.score, self.food.food_pos = self.snake.body_mechanism(self.game.sc_width, self.game.sc_height,
                                                                        self.food.food_pos, self.game.score,
                                                                        self.game.coefficient)

        self.snake.snake_draw(self.game.sc, self.game.black, self.game.coefficient)
        self.food.food_draw(self.game.sc, self.game.red, self.game.coefficient)
        self.snake.check_for_boundaries(self.game.game_over, self.game.sc_width, self.game.sc_height, self.game.coefficient)
        self.game.score_draw()

    def update_screen(self):
        return self.game.update_screen()

    def game_decision(self):
        if self.game_status:
            return self.snake_game()
        elif not self.game_status:
            return self.game_menu()


start = Start()

while True:
    start.game_decision()
    start.update_screen()
