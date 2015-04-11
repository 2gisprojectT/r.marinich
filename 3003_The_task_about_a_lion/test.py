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
        self.L = main.Lion(self.states, self.signals, self.actions, self.transition_table, self.action_table, self.stateFull, self.error_state)

    def test_send_signal(self):
        self.L.send_signal("test_signal")
        self.assertEqual(self.L.signal, "test_signal")
        self.L.send_signal("abc")
        self.assertEqual(self.L.signal, None)

    def test_getState(self):
        self.L.signal = self.signals[0]
        self.assertEqual("test_states", self.L.getState())

    def test_GetAction(self):
        self.L.signal = self.signals[0]
        self.assertEqual("test_action", self.L.getAction())

    def test_Constructor(self):
        self.assertEqual(self.L.states, self.states)
        self.assertEqual(self.L.signals, self.signals)
        self.assertEqual(self.L.actions, self.actions)
        self.assertEqual(self.L.transition_table, self.transition_table)
        self.assertEqual(self.L.action_table, self.action_table)
        self.assertEqual(self.L.state, self.stateFull)
        self.assertEqual(self.L.error_state, self.error_state)

if __name__ == '__main__':
    unittest.main()