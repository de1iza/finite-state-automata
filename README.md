# finite-state-automata
# Usage
```python
from automaton import Automaton
states = [0, 1, 2, 3, 4, 5]
transitions = [[1, 3], [2, 0], [4, 5], [5, 3], [1, 3], [2, 0]]
finite_states = [3, 4]
automaton = Automaton(states, transitions, finite_states) 
automaton.minimize() 
automaton.dump("out.txt") # dumps to file
```
# Testing
```bash
python tests.py
```
