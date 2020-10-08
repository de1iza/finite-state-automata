def dump_minimization_table(table, filename):
    with open(filename, 'w') as file:
        file.writelines(table)


def update_minimization_table(states, transitions, table=[]):
    new_table = []
    if len(table) == 0:
        table = [''] * len(states)
    for line, i, transitions_from_i in zip(table, states, transitions):
        to_add = str(i) + ' ' + ' '.join(map(str, transitions_from_i)) + ' | \n'
        new_table.append(' '.join([line.strip(), to_add]))
    return new_table


class Automaton:
    def __init__(self, states, transitions, finite_states=None):
        self.transitions = transitions
        if finite_states is None:
            self.finite_states = set()
            for st in states:
                if st[-1] == 'F':
                    self.finite_states.add(int(st[0]))
            self.states = [int(st[0]) for st in states]
        else:
            self.states = states
            self.finite_states = set(finite_states)

    def __eq__(self, other):
        return self.states == other.states \
           and self.finite_states == other.finite_states \
           and self.transitions == other.transitions

    def __update(self, renamed_states, renamed_transitions):
        new_finite_states = set()
        new_states, new_transitions = set(), []
        for i in range(len(renamed_states)):
            if i in self.finite_states:
                new_finite_states.add(renamed_states[i])
            if renamed_states[i] not in new_states:
                new_states.add(renamed_states[i])
                new_transitions.append(renamed_transitions[i])

        self.finite_states = new_finite_states
        self.states = list(new_states)
        self.transitions = new_transitions

    def dump(self, filename="automaton.txt"):
        dumped_states = []
        with open(filename, 'w') as file:
            for i, transitions_from_i in zip(self.states, self.transitions):
                state = str(i) + ('F ' if i in self.finite_states else ' ')
                if state not in dumped_states:
                    file.write(state + ' '.join(map(str, transitions_from_i)) + '\n')
                    dumped_states.append(state)

    def minimize(self, out_filename="minimization_table.txt",
                 res_filename="minimized.txt"):
        states = [int(st in self.finite_states) for st in self.states]
        init_transitions = list(self.transitions)
        transitions = list(self.transitions)
        minimization_table = []
        while True:
            transitions_new = []
            for transitions_from in init_transitions:
                transitions_from_new = [states[st] for st in transitions_from]
                transitions_new.append(transitions_from_new)

            minimization_table = update_minimization_table(states,
                                                           transitions_new, minimization_table)
            transitions = list(transitions_new)
            rename_states_dict = {}
            states_cnt = 0
            states_new = []
            for i, transitions_from_i in zip(states, transitions):
                key = str(i) + ''.join(map(str, transitions_from_i))
                if key not in rename_states_dict:
                    rename_states_dict[key] = states_cnt
                    states_cnt += 1
                states_new.append(rename_states_dict[key])
            states_prev = list(states)
            states = list(states_new)
            if states == states_prev:
                break

        dump_minimization_table(minimization_table, out_filename)
        self.__update(states, transitions)
        self.dump(res_filename)
