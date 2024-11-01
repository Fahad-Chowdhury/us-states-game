import os
import pandas


DATA_FILE = "50_states.csv"
STATES_TO_LEARN_FILE = "states_to_learn.csv"


class CsvHandler:

    def __init__(self):
        self.states_coord = {}

    def read_states_coordinates(self):
        """ Read the states coordinates from DATA_FILE and returns it as a Python
        dictionary. """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(current_dir, DATA_FILE)
        data = pandas.read_csv(filepath)
        for state in data.state:
            state_data = data[data.state == state]
            self.states_coord[state] = (state_data.x.item(), state_data.y.item())
        return self.states_coord

    def generate_state_to_learn(self, guessed_states):
        """ Generate a CSV file with the states list that the user failed to guess. """
        missed_states = [state for state in self.states_coord if state not in guessed_states]
        states = {"Missing States": missed_states,}
        data_frame = pandas.DataFrame(states)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(current_dir, STATES_TO_LEARN_FILE)
        data_frame.to_csv(filepath)
