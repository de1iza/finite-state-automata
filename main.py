from automaton import Automaton


def main():
    with open("in.txt", "r") as file:
        lines = file.readlines()
    states = []
    transitions = []
    for line in lines:
        states.append(line.split()[0])
        transitions.append(list(map(int, line.split()[1:])))

    at = Automaton(states, transitions)
    at.minimize()


if __name__ == "__main__":
  main()
