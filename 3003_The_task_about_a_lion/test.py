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

    def test_CorrectInput(self):
        L = main.Lion(self.states, self.signals, self.actions, self.transition_table, self.action_table, "full", self.error_state)
        L.send_signal("fdafg")
        self.assertEqual( "doing nothing", L.getAction() )

    def test_FullToAntilopa(self):
        L = main.Lion(self.states, self.signals, self.actions, self.transition_table, self.action_table, "full", self.error_state)
        L.send_signal("antelope")
        self.assertEqual( "hungry", L.getState() )

    def test_FullToHunter(self):
        L = main.Lion(self.states, self.signals, self.actions, self.transition_table, self.action_table, "full", self.error_state)
        L.send_signal("hunter")
        self.assertEqual( "hungry", L.getState() )

    def test_FullToTree(self):
        L = main.Lion(self.states, self.signals, self.actions, self.transition_table, self.action_table, "full", self.error_state)
        L.send_signal("tree")
        self.assertEqual( "hungry", L.getState() )

    def test_HungryToAntilopa(self):
        L = main.Lion(self.states, self.signals, self.actions, self.transition_table, self.action_table, "hungry", self.error_state)
        L.send_signal("antelope")
        self.assertEqual( "full", L.getState() )

    def test_HungryToHunter(self):
        L = main.Lion(self.states, self.signals, self.actions, self.transition_table, self.action_table, "hungry", self.error_state)
        L.send_signal("hunter")
        self.assertEqual( "hungry", L.getState() )

    def test_HungryToTree(self):
        L = main.Lion(self.states, self.signals, self.actions, self.transition_table, self.action_table, "hungry", self.error_state)
        L.send_signal("tree")
        self.assertEqual( "hungry", L.getState() )

    def test_ActionSleep1(self):
        L = main.Lion(self.states, self.signals, self.actions, self.transition_table, self.action_table, "full", self.error_state)
        L.send_signal("antelope")
        self.assertEqual( "sleep", L.getAction() )

    def test_ActionSleep2(self):
        L = main.Lion(self.states, self.signals, self.actions, self.transition_table, self.action_table, "hungry", self.error_state)
        L.send_signal("tree")
        self.assertEqual( "sleep", L.getAction() )

    def test_ActionRun1(self):
        L = main.Lion(self.states, self.signals, self.actions, self.transition_table, self.action_table, "full", self.error_state)
        L.send_signal("hunter")
        self.assertEqual( "run", L.getAction() )

    def test_ActionRun2(self):
        L = main.Lion(self.states, self.signals, self.actions, self.transition_table, self.action_table, "hungry", self.error_state)
        L.send_signal("hunter")
        self.assertEqual( "run", L.getAction() )

    def test_ActionSee(self):
        L = main.Lion(self.states, self.signals, self.actions, self.transition_table, self.action_table, "full", self.error_state)
        L.send_signal("tree")
        self.assertEqual( "see", L.getAction() )

    def test_ActionEat(self):
        L = main.Lion(self.states, self.signals, self.actions, self.transition_table, self.action_table, "hungry", self.error_state)
        L.send_signal("antelope")
        self.assertEqual( "eat", L.getAction() )

if __name__ == '__main__':
    unittest.main()