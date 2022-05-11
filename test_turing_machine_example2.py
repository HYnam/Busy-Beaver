from turing_machine import TuringMachine


machine = TuringMachine(
    {
        ('q0', '#'): ('End', '#', 'R'),
        ('End', ''): ('qa', '', 'R'), # true when only one #

        ('q0', '0'): ('FindDelimiter0', 'X', 'R'),
        ('FindDelimiter0', '#'): ('Check0', '#', 'R'),
        ('Check0', '0'): ('FindLeftmost', 'X', 'L'),    # true when 0#0

        ('q0', '1'): ('FindDelimiter1', 'X', 'R'),
        ('FindDelimiter1', '#'): ('Check1', '#', 'R'),
        ('Check1', '1'): ('FindLeftmost', 'X', 'L'),    # true when 1#1

        ('FindLeftmost', '0'): ('FindLeftmost', '0', 'L'),
        ('FindLeftmost', '1'): ('FindLeftmost', '1', 'L'),
        ('FindLeftmost', 'X'): ('FindLeftmost', 'X', 'L'),
        ('FindLeftmost', '#'): ('FindLeftmost', '#', 'L'),
        ('FindLeftmost', ''): ('FindNext', '', 'R'),

        ('FindNext', 'X'): ('FindNext', 'X', 'R'),
        ('FindNext', '0'): ('FindDelimiter0', 'X', 'R'),
        ('FindNext', '1'): ('FindDelimiter1', 'X', 'R'),
        ('FindNext', '#'): ('End', '#', 'R'),

        ('FindDelimiter0', '0'): ('FindDelimiter0', '0', 'R'),
        ('FindDelimiter0', '1'): ('FindDelimiter0', '1', 'R'),
        ('FindDelimiter1', '0'): ('FindDelimiter1', '0', 'R'),
        ('FindDelimiter1', '1'): ('FindDelimiter1', '1', 'R'),

        ('Check0', 'X'): ('Check0', 'X', 'R'),
        ('Check1', 'X'): ('Check1', 'X', 'R'),

        ('End', 'X'): ('End', 'X', 'R')
    }
)

w = "XX" #try some strings here to find out what the machine accepts and rejects
print("Input:",w)
print("Accepted?", machine.accepts(w))

"""
Part 1a: 
    State "q0"
    State "End"
    State "qa"
    State "FindDelimiter0"
    State "Check0"
    State "FindDelimiter1"
    State "Check1"
    State "FindLeftmost"
    State "FindNext"
    State "End"

Part 1c: 
    starting state(q0) and # is encountered then transition to state "End", write # and move right
    state End and "" is encountered then transition to accept state (qa), write "" and move right

    starting state(q0) and 0 is encountered then transition to state "FindDelimiter0", write X and move right
    "FindDelimiter0" state and # is encountered then transition to state "Check0", write # and move to right
    "Check0" state and 0 is encountered then transition to state "FindLeftmost", write X and move to left

    starting state(q0) and  1 is encountered then transition to state "FindDelimiter1", write X and move right
    "FindDelimiter1" state and # is encountered then transition to state "Check1", write # and move to right
    "Check1" state and 1 is encountered then transition to state "FindLeftmost", write X and move left

    "FindLeftmost" state and 0 is encountered then transition to state "FindLeftmost", write 0 and move left
    "FindLeftmost" state and 1 is encountered then transition to state "FindLeftmost", write 1 and move left
    "FindLeftmost" state and X is encountered then transition to state "FindLeftmost", write x and move left
    "FindLeftmost" state and # is encountered then transition to state "FindLeftmost", write # and move to left
    "FindLeftmost" state and "" is encountered then transition to state "FindNext", write "" and move right

    "FindNext" state and X is encountered then transition to state "FindNext", write X and move right
    "FindNext" state and 0 is encountered then transition to state "FindDelimiter0", write X and move right
    "FindNext" state and 1 is encountered then transition to state "FindDelimiter1", write X and move right
    "FindNext" state and # is encountered then transition to state "End", write # and move right

    "FindDelimiter0" state and 0 is encountered then transition to state "FindDelimiter0", write 0 and move right
    "FindDelimiter0" state and 1 is encountered then transition to state "FindDelimiter0", write 1 and move right
    "FindDelimiter1" state and 0 is encountered then transition to state "FindDelimiter1", write 0 and move right
    "FindDelimiter1" state and 1 is encountered then transition to state "FindDelimiter1", write 1 and move right

    "Check0" state and X is encountered then transition to state "Check0", write X and move to right
    "Check1" state and X is encountered then transition to state "Check1", write X and mover to right

    "End" state and X is encountered then transition to state "End", write X and move right
"""