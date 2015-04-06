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
        self.states =  ["full", "hungry"]
        self.signals = ["antelope", "hunter", "tree"]
        self.actions = ["sleep", "run", "see", "eat"]

        self.transition_table = [["hungry", "hungry", "hungry"], ["full", "hungry", "hungry"]]
        self.action_table = [["sleep", "run", "see"], ["eat", "run", "sleep"]]

        self.error_state = "doing nothing"

    def test_CorrectInputSinnal(self):
        L = main.Lion(self.states, self.signals, self.actions, self.transition_table, self.action_table, "full", self.error_state)
        L.send_signal("fdafg")
        self.assertEqual( "doing nothing", L.getAction() )

    def test_Constructor(self):
        L = main.Lion(self.states, self.signals, self.actions, self.transition_table, self.action_table, "full", self.error_state)
        self.assertEqual(L.states, self.states)
        self.assertEqual(L.signals, self.signals)
        self.assertEqual(L.actions, self.actions)
        self.assertEqual(L.transition_table, self.transition_table)
        self.assertEqual(L.action_table, self.action_table)
        self.assertEqual(L.state, "full")
        self.assertEqual(L.error_state, self.error_state)

    def test_SendSignalAndGetState(self):
        L = main.Lion(self.states, self.signals, self.actions, self.transition_table, self.action_table, "full", self.error_state)
        L.send_signal("antelope")
        self.assertEqual( "hungry", L.getState() )

        L.send_signal("hunter")
        self.assertEqual( "hungry", L.getState() )

        L.send_signal("tree")
        self.assertEqual( "hungry", L.getState() )

        L = main.Lion(self.states, self.signals, self.actions, self.transition_table, self.action_table, "hungry", self.error_state)
        L.send_signal("antelope")
        self.assertEqual( "full", L.getState() )

    def test_SendSignalAndGetAction(self):
        L = main.Lion(self.states, self.signals, self.actions, self.transition_table, self.action_table, "full", self.error_state)
        L.send_signal("antelope")
        self.assertEqual( "sleep", L.getAction() )

        L.send_signal("tree")
        self.assertEqual( "see", L.getAction() )

        L.send_signal("hunter")
        self.assertEqual( "run", L.getAction() )

if __name__ == '__main__':
    unittest.main()