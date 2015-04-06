class Lion():

    def __init__(self, list_states, list_signal, list_actions, transition_table, action_table, init_state, error_state):
        self.states = list_states
        self.signals = list_signal
        self.actions = list_actions
        self.transition_table = transition_table
        self.action_table = action_table
        self.state = init_state
        self.error_state = error_state

    def send_signal(self, signal):
        if signal in self.signals:
            self.signal = signal
        else:
            self.signal = None

    def getID(self, what, where):
        i = 0
        for item in where:
            if item == what:
                return i
            i += 1
        return -1

    def getState(self):
        try: self.signal
        except: return self.state
        if self.signal is None:
            return self.state
        self.state = self.transition_table[self.getID(self.state, self.states)][self.getID(self.signal, self.signals)]
        return self.state

    def getAction(self):
        if self.signal is not None:
            return self.action_table[self.getID(self.state, self.states)][self.getID(self.signal, self.signals)]
        else:
            return "doing nothing"

if __name__ == '__main__':

    states =  ["full", "hungry"]
    signals = ["antelope", "hunter", "tree"]
    actions = ["sleep", "run", "see", "eat"]

    transition_table = [["hungry", "hungry", "hungry"], ["full", "hungry", "hungry"]]
    action_table = [["sleep", "run", "see"], ["eat", "run", "sleep"]]

    state = "full"
    error_state = "doing nothing"

    L = Lion(states, signals, actions, transition_table, action_table, state, error_state)

    print("default state =", L.getState())
    print("write next singal: antelope, hunter, tree")

    while True:
        L.send_signal(input())
        print("Lion", L.getAction(),". Current state =", L.getState() )