from NFA import *
from DFA import *


def onDFA():
    dfa = DFA()
    while True:
        answr = input(
            'to create a DFA :\n\t1.Enter Inputs\n\t2.default\n\t3.Back\n\n answer: ')
        if answr.lower().strip() == '1':
            dfa.takeInputs()
            break
        elif answr.lower().strip() == '2':
            dfa.setDefaultForTest()
            break
        elif answr.lower().strip() == '3':
            return
        else:
            print('Wrong Input!')
    while True:
        answr = input(
            'Choose from Options(enter numbers):\n\t1.isAcceptByDFA\n\t2.makeSimpleDFA\n\t3.showSchematicDFA\n\t4.Back\n\n answer: ')
        if answr.lower().strip() == '1':
            language = input('Enter your string: ')
            print("Is '{0}' acceptable by this DFA? {1} ".format(
                language, dfa.isAcceptByDFA(language)))
        elif answr.lower().strip() == '2':
            dfa.makeSimpleDFA()
            dfa.showSchematicDFA()
        elif answr.lower().strip() == '3':
            dfa.showSchematicDFA()
        elif answr.lower().strip() == '4':
            return
        else:
            print('Wrong Input!')


def onNFA():
    nfa = NFA()
    while True:
        answr = input(
            'to create a NFA :\n\t1.Enter Inputs\n\t2.default\n\t3.Back\n\n answer: ')
        if answr.lower().strip() == '1':
            nfa.takeInputs()
            break
        elif answr.lower().strip() == '2':
            nfa.setDefaultForTest()
            break
        elif answr.lower().strip() == '3':
            return
        else:
            print('Wrong Input!')
    while True:
        answr = input(
            'Choose from Options(enter numbers):\n\t1.isAcceptByNFA\n\t2.createEquivalentNFA\n\t3.findRegExp\n\t4.showSchematicNFA\n\t5.Back\n\n answer: ')
        if answr.lower().strip() == '1':
            language = input('Enter your string: ')
            print("Is '{0}' acceptable by this NFA? {1} ".format(
                language, nfa.isAcceptByNFA(language)))
        elif answr.lower().strip() == '2':
            nfa.createEquivalentDFA()
        elif answr.lower().strip() == '3':
            print('Your Regex is: ')
            print(nfa.findRegExp())
        elif answr.lower().strip() == '4':
            nfa.showSchematicNFA()
        elif answr.lower().strip() == '5':
            return
        else:
            print('Wrong Input!')


def main():
    while True:
        answr = input('DFA, NFA or Exit?')
        if answr.lower().strip() == 'dfa':
            onDFA()
        elif answr.lower().strip() == 'nfa':
            onNFA()
        else:
            print('Well Done!')
            break


if __name__ == '__main__':
    print('Wellcome!')
    main()
