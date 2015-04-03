class Lion():
    def __init__(self, list_states, list_signal, list_actions, FS_indexs, FA_indexs):
        self.states  = list_states
        self.signals = list_signal
        self.actions = list_actions
        self.FS = FS_indexs
        self.FA = FA_indexs

    def set_init_states(self, init_states):
        self.state = init_states

    def set_signal(self, signal):
        self.signal = signal

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
        try: self.state
        except: return -1
        return self.state

    def getInitSignal(self):
        try: self.signal
        except: return -1
        return self.signal

    def getState(self):
        try: self.state and self.signal and self.FS
        except: return -1
        self.state = self.FS[self.getIDSt(self.state)][self.getIDSi(self.signal)]
        return self.state

    def getAction(self):
        try: self.state and self.signal and self.FA
        except: return -1
        return self.FA[self.getIDSt(self.state)][self.getIDSi(self.signal)]

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
            L.set_signal(current_signal)
            print("Lion", L.getAction(),". Current state =", L.getState() )
        else:
            print("try again")