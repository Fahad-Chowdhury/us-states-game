import turtle
import os

class GameScreen:

    def __init__(self):
        self.screen = turtle.Screen()
        self._setup_screen()

    def _setup_screen(self):
        """ Setup screen. """
        self.screen.title("U.S. States Game")
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image = os.path.join(current_dir, "blank_states_img.gif")
        self.screen.addshape(image)
        turtle.shape(image)

    def get_user_guess(self, title):
        """ Get a state name as an input from the user. """
        user_guess = self.screen.textinput(title=title,
                                           prompt="What's another states name?")
        return user_guess

    def exit_screen_on_click(self):
        """ Close screen on mouseclick. """
        self.screen.exitonclick()
