class Lion():

    states =  ["full", "hungry"]
    signals = ["antelope", "hunter", "tree"]
    actions = ["sleep", "run", "see", "eat"]

    transition_table = [["hungry", "hungry", "hungry"], ["full", "hungry", "hungry"]]
    action_table = [["sleep", "run", "see"], ["eat", "run", "sleep"]]

    state = "full"

    def set_init_states(self, init_states):
        self.state = init_states

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

    L = Lion()

    print("default state =", L.getState())
    print("write next singal: antelope, hunter, tree")

    while True:
        L.send_signal(input())
        print("Lion", L.getAction(),". Current state =", L.getState() )