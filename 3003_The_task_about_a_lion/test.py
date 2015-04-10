import unittest
import main

class TestLeon(unittest.TestCase):
    states = None
    signals = None
    actions = None

    transition_table = None
    action_table = None
    error_state = None

    def setUp(self):
        self.states =  ["test_states"]
        self.signals = ["test_signal"]
        self.actions = ["test_action"]

        self.transition_table = [["test_states"], ["test_states"]]
        self.action_table = [["test_action"], ["test_action"]]

        self.stateFull = "test"
        self.stateHungry = "test"
        self.error_state = "test"

    def test_send_signal(self):
        L = main.Lion(self.states, self.signals, self.actions, self.transition_table, self.action_table, self.stateFull, self.error_state)
        L.send_signal("test_signal")
        self.assertEqual(L.signal, "test_signal")
        L.send_signal("abc")
        self.assertEqual(L.signal, None)

    def test_getState(self):
        L = main.Lion(self.states, self.signals, self.actions, self.transition_table, self.action_table, self.stateFull, self.error_state)
        L.signal = self.signals[0]
        self.assertEqual("test_states", L.getState())

    def test_GetAction(self):
        L = main.Lion(self.states, self.signals, self.actions, self.transition_table, self.action_table, self.stateFull, self.error_state)
        L.signal = self.signals[0]
        self.assertEqual("test_action", L.getAction())

    def test_Constructor(self):
        L = main.Lion(self.states, self.signals, self.actions, self.transition_table, self.action_table, self.stateFull, self.error_state)
        self.assertEqual(L.states, self.states)
        self.assertEqual(L.signals, self.signals)
        self.assertEqual(L.actions, self.actions)
        self.assertEqual(L.transition_table, self.transition_table)
        self.assertEqual(L.action_table, self.action_table)
        self.assertEqual(L.state, self.stateFull)
        self.assertEqual(L.error_state, self.error_state)

if __name__ == '__main__':
    unittest.main()