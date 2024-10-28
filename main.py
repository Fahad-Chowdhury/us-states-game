from game_screen import GameScreen
from read_us_states import CsvHandler
from map_writer import MapWriter


def main():
    """ The user is asked to guess the states of USA, on correct answer the states are labelled on the map.
    The game goes on untill the user is able to guess all the states correctly. At the end, it creates a
    CSV file that has list of all the states that the user failed to guess. """
    states_coord = {}
    guessed_states = []
    title = "Guess the state"

    screen = GameScreen()
    map_writer = MapWriter()

    csv_handler = CsvHandler()
    states_coord = csv_handler.read_states_coordinates()

    while len(guessed_states) < 50:
        user_guess = screen.get_user_guess(title)
        user_guess = user_guess.title() if user_guess else ''
        if user_guess == "Exit":
            break
        if user_guess in states_coord and user_guess not in guessed_states:
            map_writer.add_state_label(state=user_guess,
                                       coord=states_coord[user_guess])
            guessed_states.append(user_guess)
            title = f"{len(guessed_states)}/50 States Correct"

    csv_handler.generate_state_to_learn(guessed_states)

    screen.exit_screen_on_click()


if __name__ == "__main__":
    main()
