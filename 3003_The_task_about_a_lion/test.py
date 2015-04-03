import unittest
import main

class TestLeon(unittest.TestCase):

    list_states =  ["full", "hungry"]
    list_signals = ["antelope", "hunter", "tree"]
    list_actions = ["sleep", "run", "see", "eat"]

    FS = [["hungry", "hungry", "hungry"], ["full", "hungry", "hungry"]]
    FA = [["sleep", "run", "see"], ["eat", "run", "sleep"]]

    L = main.Lion(list_states, list_signals, list_actions, FS, FA)
    L.set_init_states("full")

    def test_FullToAntilopa(self):
        self.L.set_init_states("full")
        self.L.set_signal("antelope")
        self.assertEqual( "hungry", self.L.getState() )
    def test_FullToHunter(self):
        self.L.set_init_states("full")
        self.L.set_signal("hunter")
        self.assertEqual( "hungry", self.L.getState() )
    def test_FullToTree(self):
        self.L.set_init_states("full")
        self.L.set_signal("tree")
        self.assertEqual( "hungry", self.L.getState() )
    def test_HungryToAntilopa(self):
        self.L.set_init_states("hungry")
        self.L.set_signal("antelope")
        self.assertEqual( "full", self.L.getState() )
    def test_HungryToHunter(self):
        self.L.set_init_states("hungry")
        self.L.set_signal("hunter")
        self.assertEqual( "hungry", self.L.getState() )
    def test_HungryToTree(self):
        self.L.set_init_states("hungry")
        self.L.set_signal("tree")
        self.assertEqual( "hungry", self.L.getState() )

    def test_ActionSleep1(self):
        self.L.set_init_states("full")
        self.L.set_signal("antelope")
        self.assertEqual( "sleep", self.L.getAction() )
    def test_ActionSleep2(self):
        self.L.set_init_states("hungry")
        self.L.set_signal("tree")
        self.assertEqual( "sleep", self.L.getAction() )

    def test_ActionRun1(self):
        self.L.set_init_states("full")
        self.L.set_signal("hunter")
        self.assertEqual( "run", self.L.getAction() )
    def test_ActionRun2(self):
        self.L.set_init_states("hungry")
        self.L.set_signal("hunter")
        self.assertEqual( "run", self.L.getAction() )

    def test_ActionSee(self):
        self.L.set_init_states("full")
        self.L.set_signal("tree")
        self.assertEqual( "see", self.L.getAction() )

    def test_ActionEat(self):
        self.L.set_init_states("hungry")
        self.L.set_signal("antelope")
        self.assertEqual( "eat", self.L.getAction() )

if __name__ == '__main__':
    unittest.main()