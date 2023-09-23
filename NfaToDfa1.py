
def createEquivalentDFA(self):
    # not implemented
    alphabetDFA = self.alphabet
    initialStateDFA = self.all_states[0]
    allStatesDFA = [initialStateDFA]
    finalStatesDFA = []
    RulesDFA = []
    over = False
    i = 0
    while(not over):
        tempList2 = []
        for alphabet in self.alphabet:
            tempList = []
            for state in allStatesDFA:
                if type(allStatesDFA[i]) != list:
                    state = allStatesDFA[i]

                tmp = [item for item in self.transition_list if item.starting_state
                       == state and item.alphabet == alphabet]
                tempNewState = [item.ending_state for item in tmp]

                if len(tempNewState) == 1:
                    tempNewState = tempNewState[0]
                    if not tempNewState in tempList:
                        tempList.append(tempNewState)

                elif len(tempNewState) == 0:
                    continue

                elif not tempNewState in tempList and tempNewState != tempList:
                    for j in tempNewState:
                        tempList.append(j)
                    # tempList.append(tempNewState)
                if len(allStatesDFA) == 1:
                    break
                # if type(allStatesDFA[i]) != list:
                #     break

            if len(tempList) == 1:
                tempList = tempList[0]

            RulesDFA.append([allStatesDFA[i], tempList, alphabet])

            if not tempList in allStatesDFA:
                tempList2.append(tempList)

        for j in tempList2:
            allStatesDFA.append(j)
        if len(tempList2) == 0 and i == len(allStatesDFA):
            over = True
        if i < len(allStatesDFA)-1:
            i += 1
        else:
            break

    if [] in allStatesDFA:
        for alphabet in alphabetDFA:
            if not [[], [], alphabet] in RulesDFA:
                RulesDFA.append([[], [], alphabet])

    for finalState in self.final_states:
        for state in [allStatesDFA]:
            if (finalState in state) and (state not in [finalStatesDFA]):
                finalStatesDFA.append(state)

    # print(allStatesDFA)
    # print(alphabetDFA)
    # print(initialStateDFA)
    print(finalStatesDFA)
    print(RulesDFA)
    t_list = []
    for i in RulesDFA:
        t_list.append(Transition(i[2], i[0], i[1]))
    dfa = DFA()
    dfa.all_states = allStatesDFA
    dfa.alphabet = alphabet
    dfa.transition_list = t_list
    dfa.final_states = finalStatesDFA
    # dfa.setDefaultForTest()
    dfa.showSchematicDFA()
    return dfa
