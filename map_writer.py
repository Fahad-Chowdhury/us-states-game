from turtle import Turtle


ALIGNMENT = "center"
FONT = ('Arial', 10, 'normal')

class MapWriter(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.penup()

    def add_state_label(self, state, coord):
        """ Add state label on the given coordinate on the image. """
        self.goto(coord)
        self.write( f"{state}", move=False, align=ALIGNMENT, font=FONT)
