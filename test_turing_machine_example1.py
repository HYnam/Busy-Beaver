from turing_machine import TuringMachine


machine = TuringMachine(
    {
        ('q0', '#'): ('saw_#', '#', 'R'),
        ('saw_#', '#'): ('saw_##', '#', 'R'),
        ('saw_##', ''): ('qa', '', 'R'),
    }
)

w = "##" #try some strings here to find out what the machine accepts and rejects
print("Input:",w)
print("Accepted?", machine.accepts(w))
machine.debug(w)

"""
Part 1a: 
    State q0
    State saw_#
    State saw_##

part 1c:
    in start state (q0) and # is encounter, then transition to state saw_#, write a # and move right
    in saw_# state and # is encounter, then transition to state saw_##, write a # and move right
    in saw_## state and '' or is blank, then transition to state accept (qa), write '' and move right
"""
