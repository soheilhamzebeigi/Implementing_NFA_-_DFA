from DrawGraph import *
from Models import *


class DFA:
    def __init__(self):
        super().__init__()
        self.all_states = []
        self.alphabet = []
        self.final_states = []
        self.transition_list = []

    def isAcceptByDFA(self, string):
        state = self.all_states[0]
        for v in string:
            for f in self.transition_list:
                if v == f.alphabet and state == f.starting_state:
                    state = f.ending_state
                    break
        return state in self.final_states

    def showSchematicDFA(self):
        dg = DrawGraph(self.all_states, self.transition_list)
        dg.DrawWin()

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
                raise Exception('DFA cant have landa!')
            else:
                t_alphabet = transition[2]
            transition_list.append(Transition(t_alphabet, s_index, e_index))
        for i in all_states:
            ss = [s for s in transition_list if s.starting_state.state_name == i]
            if len(ss) != len(self.alphabet):
                raise Exception('Not All states Implemented!')
        self.all_states = states
        self.alphabet = alphabet
        self.transition_list = transition_list
        self.final_states = f_states

    def setDefaultForTest(self):
        all_states = ['q0', 'q1', 'q2', 'q3', 'q4']
        t_list = [
            ['q0', 'q1', '0'],
            ['q0', 'q3', '1 '],
            ['q1', 'q2', '0'],
            ['q1', 'q4', '1'],
            ['q2', 'q1', '0'],
            ['q2', 'q4', '1'],
            ['q3', 'q2', '0'],
            ['q3', 'q4', '1'],
            ['q4', 'q4', '0'],
            ['q4', 'q4', '1'],
        ]
        alphabet = ['0', '1']
        final_states = ['q4']
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
                raise Exception('DFA cant have landa!')
            else:
                t_alphabet = transition[2]
            transition_list.append(Transition(t_alphabet, s_index, e_index))
        for i in states:
            ss = [s for s in transition_list if s.starting_state.state_name == i]
            if len(ss) != len(self.alphabet):
                raise Exception('Not All states Implemented!')
        self.all_states = states
        self.alphabet = alphabet
        self.transition_list = transition_list
        self.final_states = f_states
        print('Well Done!')

    # def isAcceptByDFA(self, language):  # written by ali akbar shahi
    #     # is lambda accepted?
    #     if len(language) == 0:
    #         return self.all_states[0].is_final
    #     # check to see all alphabets exists
    #     for i in language:
    #         if i not in self.alphabet:
    #             return False

    #     current_state = self.all_states[0]
    #     for index, item in enumerate(language):
    #         state = [
    #             s for s in self.transition_list if s.starting_state == current_state and s.alphabet == item]
    #         if len(state) == 0 and index != len(language)-1:
    #             return False
    #         current_state = state[0].ending_state
    #     return current_state.is_final

    def isReachable(self, stateToCheck):
        currentStates = [self.all_states[0]]
        while len(currentStates) != 0:
            state = currentStates.pop(0)
            for t in self.transition_list:
                if t.starting_state == state:
                    if t.ending_state == stateToCheck:
                        return True
                    currentStates.append(t.ending_state)
        return False

    def reGenNewFields(self):
        newTransList = []
        for t in self.transition_list:
            start = None
            end = None
            for s in self.all_states:
                if t.starting_state.state_name == s.state_name:
                    start = s
                if t.ending_state.state_name == s.state_name:
                    end = s
            newTransList.append(Transition(t.alphabet, start, end))
        self.transition_list = newTransList

    def makeSimpleDFA(self):
        # start of not reachable
        notReachableStates = []
        startingState = self.all_states[0]
        for state in self.all_states:
            if startingState == state:
                continue
            if not self.isReachable(state):
                notReachableStates.append(state)

        for state in notReachableStates:
            for t in self.transition_list:
                if t.starting_state == state or t.ending_state == state:
                    self.transition_list.remove(t)

        # print(notReachableStates)
        for state in notReachableStates:
            for s in self.all_states:
                if s == state:
                    self.all_states.remove(state)
        # end of not reachable
        # start equvaliant states
        end = False
        while not end:
            end = True
            nonFinalStates = []
            finalStates = []
            # index = 0
            for s in self.all_states:
                if s.is_final:
                    finalStates.append(s)
                else:
                    nonFinalStates.append(s)
            # non final states
            addedStates = []
            stateCmpnts = []
            for in1 in range(len(nonFinalStates)):
                s = nonFinalStates[in1]
                if s in addedStates:
                    continue
                addedStates.append(s)
                component = [s]
                for in2 in range(in1+1, len(nonFinalStates)):
                    s2 = nonFinalStates[in2]
                    s_list = []
                    s2_list = []
                    for t in self.transition_list:
                        if t.starting_state == s2:
                            s2_list.append(t)
                        if t.starting_state == s:
                            s_list.append(t)
                    count = 0
                    for i in s_list:
                        for j in s2_list:
                            if i.alphabet == j.alphabet and i.ending_state == j.ending_state:
                                count += 1
                    if count == 2:
                        component.append(s2)
                        addedStates.append(s2)
                stateCmpnts.append(component)
            index = 0
            for cmpnt in stateCmpnts:
                if len(cmpnt) > 1:
                    end = False
                    alp = []
                    for i in cmpnt:
                        alp.append(i.state_name)
                    for state in self.all_states:
                        if state.state_name in alp:
                            state.state_name = 'g'+str(index)
                index += 1
            l = []
            newTList = []
            for t in self.transition_list:
                if str(t) not in l:
                    l.append(str(t))
                    newTList.append(t)
            self.transition_list = newTList
            l = []
            newSList = []
            for t in self.all_states:
                if str(t) not in l:
                    l.append(str(t))
                    newSList.append(t)
            self.all_states = newSList
            self.reGenNewFields()
        # end equvaliant states
        print('Done!')
