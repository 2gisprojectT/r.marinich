

class Lion():
    def __init__(self, list_states, list_signal, list_actions, FS_indexs, FA_indexs):
        self.states  = list_states
        self.signals = list_signal
        self.actions = list_actions
        self.FS = FS_indexs
        self.FA = FA_indexs

    def set_init_states(self, init_states):
        self.state = init_states

    def getIDSt(self, what):
        i = 0
        for item in self.states:
            if item == what:
                return i
            i += 1
        return -1

    def getIDSi(self, what):
        i = 0
        for item in self.signals:
            if item == what:
                return i
            i += 1
        return -1

    def getInitState(self):
        return self.state

    def getState(self):
        self.state = self.FS[self.getIDSt(self.state)][self.getIDSi(self.signal)]
        return self.state

    def getAction(self, signal):
        self.signal = signal
        return self.FA[self.getIDSt(self.state)][self.getIDSi(signal)]


if __name__ == '__main__':

    list_states =  ["full", "hungry"]
    list_signals = ["antelope", "hunter", "tree"]
    list_actions = ["sleep", "run", "see", "eat"]

    FS = [["hungry", "hungry", "hungry"], ["full", "hungry", "hungry"]]
    FA = [["sleep", "run", "see"], ["eat", "run", "sleep"]]

    L = Lion(list_states, list_signals, list_actions, FS, FA)

    L.set_init_states("full")

    print("default state =", L.getInitState())
    print("write next singal: antelope, hunter, tree")
    while True:
        current_signal = input()

        if (L.getIDSi(current_signal) != -1):
            print("Lion", L.getAction(current_signal),". Current state =", L.getState() )

            L.set_init_states("full")
            print("Lion", L.getAction(current_signal),". Current state =", L.getState() )
        else:
            print("try again")