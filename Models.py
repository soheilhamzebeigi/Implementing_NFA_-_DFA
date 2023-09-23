class Node:
    def __init__(self, state_name, is_final):
        self.state_name = state_name
        self.is_final = is_final

    def __str__(self):
        return '''StateName:{0},\tIs Final:{1}'''.format(self.state_name, self.is_final)


class Transition:
    def __init__(self, alphabet, starting_state, ending_state):
        self.alphabet = alphabet
        self.starting_state = starting_state
        self.ending_state = ending_state

    def __str__(self):
        return '''Alphabet:{0},\tStartingState:{1},\tEndingState:{2}'''.format(self.alphabet, self.starting_state, self.ending_state)
