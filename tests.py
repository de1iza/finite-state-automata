import unittest
from automaton import Automaton


class TestAutomaton(unittest.TestCase):
    def setUp(self):
        states = [0, 1, 2, 3, 4, 5]
        transitions = [[1, 3], [2, 0], [4, 5], [5, 3], [1, 3], [2, 0]]
        finite_states = [3, 4]
        self.automaton = Automaton(states, transitions, finite_states)

    def testMinimize(self):
        states = [0, 1, 2, 3]
        transitions = [[1, 3], [2, 0], [3, 1], [1, 3]]
        finite_states = [3]
        minimized = Automaton(states, transitions, finite_states)
        self.automaton.minimize()
        self.assertEqual(self.automaton, minimized)


if __name__ == "__main__":
  unittest.main()
