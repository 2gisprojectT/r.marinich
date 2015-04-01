from enum import IntEnum
import unittest

class States(IntEnum):
    full = 0
    hungry = 1

class Signals(IntEnum):
    antelope = 0
    hunter = 1
    tree = 2

def get_singal():
    name_input = input()
    for name, member in Signals.__members__.items():
        if name_input == name:
            return member
    return -1

def lion(how_do, init_list, c_state, c_signal):
    return how_do(c_state.value, c_signal.value, init_list)

def start_lion():
    current_state = States.full
    init_list = [[States.hungry, States.hungry, States.hungry], [States.full, States.hungry, States.hungry]]
    print("default state =", current_state.name)
    print("write next singal: antelope, hunter, tree")
    while True:
        current_signal = get_singal()
        if current_signal != -1:
            current_state = lion(lambda i, j, clist: clist[i][j], init_list, current_state, current_signal)
            print("current state =", current_state.name)
        else:
            print("try again")

class TestLeon(unittest.TestCase):
    def test_FullToAntilopa(self):
        init_list = [[States.hungry, States.hungry, States.hungry], [States.full, States.hungry, States.hungry]]
        self.assertEqual(lion(lambda i, j, clist: clist[i][j], init_list, States.full, Signals.antelope), States.hungry)
    def test_FullToHunter(self):
        init_list = [[States.hungry, States.hungry, States.hungry], [States.full, States.hungry, States.hungry]]
        self.assertEqual(lion(lambda i, j, clist: clist[i][j], init_list, States.full, Signals.hunter), States.hungry)
    def test_FullToTree(self):
        init_list = [[States.hungry, States.hungry, States.hungry], [States.full, States.hungry, States.hungry]]
        self.assertEqual(lion(lambda i, j, clist: clist[i][j], init_list, States.full, Signals.tree), States.hungry)
    def test_HungryToAntilopa(self):
        init_list = [[States.hungry, States.hungry, States.hungry], [States.full, States.hungry, States.hungry]]
        self.assertEqual(lion(lambda i, j, clist: clist[i][j], init_list, States.hungry, Signals.antelope), States.full)
    def test_HungryToHunter(self):
        init_list = [[States.hungry, States.hungry, States.hungry], [States.full, States.hungry, States.hungry]]
        self.assertEqual(lion(lambda i, j, clist: clist[i][j], init_list, States.hungry, Signals.hunter), States.hungry)
    def test_HungryToTree(self):
        init_list = [[States.hungry, States.hungry, States.hungry], [States.full, States.hungry, States.hungry]]
        self.assertEqual(lion(lambda i, j, clist: clist[i][j], init_list, States.hungry, Signals.tree), States.hungry)

if __name__ == '__main__':
    unittest.main()
    #start_lion()