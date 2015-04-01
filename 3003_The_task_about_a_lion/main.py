from enum import IntEnum
import unittest
# import numpy

class States(IntEnum):
    full = 0
    hungry = 1

class Signals(IntEnum):
    antelope = 0
    hunter = 1
    tree = 2

def create_enum_table(init_list):
    enum_table = []
    for i in range(len(States)):
        enum_table.append([])
        for j in range(len(Signals)):
            enum_table[i].append(init_list[i][j])
    return enum_table

def get_singal():
    name_input = input()
    for name, member in Signals.__members__.items():
        if name_input == name:
            return member
    return -1

def lion(c_state, c_signal):
    init_list = [[States.hungry, States.hungry, States.hungry], [States.full, States.hungry, States.hungry]]
    #return numpy.fromfunction(lambda i, j: init_list[i][j], (len(Signals), len(States)), dtype=IntEnum)[c_state.value][c_signal.value]
    return create_enum_table(init_list)[c_state.value][c_signal.value]

def start_lion():
    current_state = States.full
    while True:
        current_signal = get_singal()
        if current_signal != -1:
            current_state = lion(current_state, current_signal)
            print(current_state.name)
        else:
            print("try again")

class TestLeon(unittest.TestCase):
    def test_FullToAntilopa(self):
        self.assertEqual(lion(States.full, Signals.antelope), States.hungry)
    def test_FullToHunter(self):
        self.assertEqual(lion(States.full, Signals.hunter), States.hungry)
    def test_FullToTree(self):
        self.assertEqual(lion(States.full, Signals.tree), States.hungry)
    def test_HungryToAntilopa(self):
        self.assertEqual(lion(States.hungry, Signals.antelope), States.full)
    def test_HungryToAntilopa(self):
        self.assertEqual(lion(States.hungry, Signals.hunter), States.hungry)
    def test_HungryToAntilopa(self):
        self.assertEqual(lion(States.hungry, Signals.tree), States.hungry)

if __name__ == '__main__':
    unittest.main()
    #start_lion()
