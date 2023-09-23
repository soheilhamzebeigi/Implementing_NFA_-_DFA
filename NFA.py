from itertools import chain, combinations
from DrawGraph import *
from Regex import *
from Models import *
from DFA import DFA


class NFA:
    def __init__(self):
        super().__init__()
        self.all_states = []
        self.final_states = []
        self.alphabet = []
        self.transition_list = []

    def isAcceptByNFA(self, string, s_state=None):
        if s_state == None:
            s_state = self.all_states[0]
        state = [s_state]
        string = list(string)
        i = 0
        while len(string) > i:
            h = string[i]
            af = []
            for s in state:
                for f in self.transition_list:
                    if (h == f.alphabet and s == f.starting_state):
                        af.append(f.ending_state)
                    elif(s == f.starting_state and f.alphabet == ":L"):
                        if(self.isAcceptByNFA(''.join(string)[i:], f.ending_state)):
                            return True
            i += 1
            state = af
        for j in state:
            print(j)
        for t in self.final_states:
            if t in state:
                return True
        return False

    def findRegExp(self):
        states = []
        for i in self.all_states:
            states.append(i.state_name)
        states.append('N')
        # end
        alphabets = self.alphabet.copy()
        # end
        init_state = self.all_states[0].state_name
        # end
        final_states = []
        for i in self.final_states:
            final_states.append(i.state_name)
        # end
        transition_matrix = []
        for i in states:
            lis = []
            trans = [
                s for s in self.transition_list if s.starting_state.state_name == i]
            for j in alphabets:
                trans2 = [s for s in trans if s.alphabet == j]
                if len(trans2) == 1:
                    lis.append(trans2[0].ending_state.state_name)
                elif len(trans2) == 0:
                    lis.append('N')
                else:
                    lis.append(trans2[0].ending_state.state_name)
            transition_matrix.append(lis)
        transition_funct = dict(zip(states, transition_matrix))
        r = ''
        for f in final_states:
            dfa = Regex(states, alphabets, init_state,
                        final_states, transition_funct)
            regex = dfa.genRegex()
            dfa = Regex(states, alphabets, init_state, [f], transition_funct)
            r += '+' + dfa.genRegex()
        return r[1:]

    def showSchematicNFA(self):
        dnfa = DrawGraph(self.all_states, self.transition_list)
        dnfa.DrawWin()

    def takeInputs(self):
        all_states = input(
            'Enter All States in One Line:(Ex. q1,q2,q3,q4 ...) : ').split(',')
        alphabet = input(
            'Enter All alphabets in One Line:(Ex. a,b,c,d ...) : ').split(',')
        final_states = input(
            'Enter All final states in One Line:(Ex. q1,q2,q3,q4 ...) : ').split(',')
        transition_count = int(
            input('Enter Number of transitions:(Ex. 5 ...) : '))

        states = []
        f_states = []
        transition_list = []

        for item in all_states:
            isFinal = item in final_states
            states.append(Node(item, isFinal))

        for item in final_states:
            s_index = [s for s in states if s.state_name == item][0]
            f_states.append(s_index)

        for i in range(transition_count):
            transition = input().split(',')
            s_index = [s for s in states if s.state_name == transition[0]][0]
            e_index = [s for s in states if s.state_name == transition[1]][0]
            t_alphabet = ''
            if(transition[2] == ' '):
                t_alphabet = ':L'
            else:
                t_alphabet = transition[2]
            transition_list.append(Transition(t_alphabet, s_index, e_index))
        self.all_states = states
        self.alphabet = alphabet
        self.transition_list = transition_list
        self.final_states = f_states

    def setDefaultForTest(self):
        all_states = ['q0', 'q1', 'q2', 'q3', 'q4']
        t_list = [
            ['q0', 'q1', 'a'],
            ['q1', 'q2', 'b'],
            ['q1', 'q3', ' '],
            ['q3', 'q4', 'b'],
            ['q2', 'q3', 'a'],
            ['q4', 'q2', 'a'],
        ]
        alphabet = ['a', 'b']
        final_states = ['q1', 'q3']
        # end
        states = []
        f_states = []
        transition_list = []

        for item in all_states:
            isFinal = item in final_states
            states.append(Node(item, isFinal))

        for item in final_states:
            s_index = [s for s in states if s.state_name == item][0]
            f_states.append(s_index)

        for i in range(len(t_list)):
            transition = t_list[i]
            s_index = [s for s in states if s.state_name == transition[0]][0]
            e_index = [s for s in states if s.state_name == transition[1]][0]
            t_alphabet = ''
            if(transition[2] == ' '):
                t_alphabet = ':L'
            else:
                t_alphabet = transition[2]
            transition_list.append(Transition(t_alphabet, s_index, e_index))
        self.all_states = states
        self.alphabet = alphabet
        self.transition_list = transition_list
        self.final_states = f_states
        print('Well Done!')

    def powerset(self, iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

    def move(self, shoro, payan, label, state, harf):
        a = []
        for sh in range(len(shoro)):
            if shoro[sh] == state and (label[sh] == harf or label[sh] == ":L"):
                a.append(payan[sh])
        return a

    def createEquivalentDFA(self):
        shoro = []
        payan = []
        label = []
        for i in self.transition_list:
            shoro.append(i.starting_state.state_name)
            payan.append(i.ending_state.state_name)
            label.append(i.alphabet)
        alephba = self.alphabet
        final_states = []
        for i in self.final_states:
            final_states.append(i.state_name)
        all = []
        for i in self.all_states:
            all.append(i.state_name)
        power_set = list(self.powerset(all))

        shoro_jadid = []
        payan_jadid = []
        label_jadid = []

        for h in alephba:
            s = self.move(shoro, payan, label, 'q0', h)
            s = tuple(s)
            ss = list(s)
            shoro_jadid.append('q0')
            payan_jadid.append(ss)
            label_jadid.append(h)

        pa = []
        ss = []
        for v in payan_jadid:
            for vv in v:
                for h in alephba:
                    dd = ss
                    s = self.move(shoro, payan, label, str(vv), h)
                    s = tuple(s)
                    ss = list(s)
                    ss = ss + dd
            shoro_jadid.append(v)
            pa.append(ss)
            label_jadid.append(h)

        for t in pa:
            payan_jadid.append(t)

        payan_ha = []

        for v in payan_jadid:
            for vv in v:
                for h in alephba:
                    dd = ss
                    s = self.move(shoro, payan, label, str(vv), h)
                    s = tuple(s)
                    ss = list(s)
                    ss = ss + dd
            shoro_jadid.append(v)
            pa.append(ss)
            label_jadid.append(h)

        for t in pa:
            payan_jadid.append(t)
        for v in payan_jadid:
            for j in v:
                if v.count(j) > 1:
                    v.remove(j)

        final_states_jadid = []
        for v in shoro_jadid:
            for vv in v:
                if vv in final_states and vv not in final_states_jadid:
                    final_states_jadid.append(v)
                    break

        print('shoro jadid : ', shoro_jadid)
        print('payan jadid : ', payan_jadid)
        print('label jadid : ', label_jadid)
        print('final states jadid : ', final_states_jadid)


if __name__ == '__main__':
    nfa = NFA()
    nfa.setDefaultForTest()
    nfa.createEquivalentDFA()
    # input();
