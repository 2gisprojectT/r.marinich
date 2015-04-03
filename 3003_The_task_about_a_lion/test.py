import main

import unittest


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
        self.L.getAction("antelope")
        self.assertEqual( "hungry", self.L.getState() )
    def test_FullToHunter(self):
        self.L.set_init_states("full")
        self.L.getAction("hunter")
        self.assertEqual( "hungry", self.L.getState() )
    def test_FullToTree(self):
        self.L.set_init_states("full")
        self.L.getAction("tree")
        self.assertEqual( "hungry", self.L.getState() )
    def test_HungryToAntilopa(self):
        self.L.set_init_states("hungry")
        self.L.getAction("antelope")
        self.assertEqual( "full", self.L.getState() )
    def test_HungryToHunter(self):
        self.L.set_init_states("hungry")
        self.L.getAction("hunter")
        self.assertEqual( "hungry", self.L.getState() )
    def test_HungryToTree(self):
        self.L.set_init_states("hungry")
        self.L.getAction("tree")
        self.assertEqual( "hungry", self.L.getState() )

if __name__ == '__main__':
    unittest.main()