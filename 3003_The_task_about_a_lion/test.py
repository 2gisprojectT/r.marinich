import unittest
import main

class TestLeon(unittest.TestCase):

    L = main.Lion()

    def test_CorrectInput(self):
        self.L.send_signal("fdafg")
        self.assertEqual( "doing nothing", self.L.getAction() )

    def test_FullToAntilopa(self):
        self.L.set_init_states("full")
        self.L.send_signal("antelope")
        self.assertEqual( "hungry", self.L.getState() )
    def test_FullToHunter(self):
        self.L.set_init_states("full")
        self.L.send_signal("hunter")
        self.assertEqual( "hungry", self.L.getState() )
    def test_FullToTree(self):
        self.L.set_init_states("full")
        self.L.send_signal("tree")
        self.assertEqual( "hungry", self.L.getState() )
    def test_HungryToAntilopa(self):
        self.L.set_init_states("hungry")
        self.L.send_signal("antelope")
        self.assertEqual( "full", self.L.getState() )
    def test_HungryToHunter(self):
        self.L.set_init_states("hungry")
        self.L.send_signal("hunter")
        self.assertEqual( "hungry", self.L.getState() )
    def test_HungryToTree(self):
        self.L.set_init_states("hungry")
        self.L.send_signal("tree")
        self.assertEqual( "hungry", self.L.getState() )

    def test_ActionSleep1(self):
        self.L.set_init_states("full")
        self.L.send_signal("antelope")
        self.assertEqual( "sleep", self.L.getAction() )
    def test_ActionSleep2(self):
        self.L.set_init_states("hungry")
        self.L.send_signal("tree")
        self.assertEqual( "sleep", self.L.getAction() )

    def test_ActionRun1(self):
        self.L.set_init_states("full")
        self.L.send_signal("hunter")
        self.assertEqual( "run", self.L.getAction() )
    def test_ActionRun2(self):
        self.L.set_init_states("hungry")
        self.L.send_signal("hunter")
        self.assertEqual( "run", self.L.getAction() )

    def test_ActionSee(self):
        self.L.set_init_states("full")
        self.L.send_signal("tree")
        self.assertEqual( "see", self.L.getAction() )

    def test_ActionEat(self):
        self.L.set_init_states("hungry")
        self.L.send_signal("antelope")
        self.assertEqual( "eat", self.L.getAction() )

if __name__ == '__main__':
    unittest.main()