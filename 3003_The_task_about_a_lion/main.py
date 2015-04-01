from enum import IntEnum
import unittest

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

def leon(c_state, c_signal):
    init_list = [[States.hungry, States.hungry, States.hungry], [States.full, States.hungry, States.hungry]]
    FSM_table = create_enum_table(init_list)
    return FSM_table[c_state.value][c_signal.value]

