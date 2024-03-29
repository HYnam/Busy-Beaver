from turing_machine import TuringMachine

#create the Turing machine
bbeaver = TuringMachine( 
    { 
        #Write your transition rules here as entries to a Python dictionary
        #For example, the key will be a pair (state, character)
        #The value will be the triple (next state, character to write, move head L or R)
        #such as ('q0', '1'): ('q1', '0', 'R'), which says if current state is q0 and 1 encountered
        #then transition to state q1, write a 0 and move head right.
        
        ('a', '0'): ('b', '1', 'R'),
        ('a', '1'): ('h', '1', 'R'),

        ('b', '0'): ('c', '0', 'R'),
        ('b', '1'): ('b', '1', 'R'),

        ('c', '0'): ('c', '1', 'L'),
        ('c', '1'): ('a', '1', 'L'),
    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)

bbeaver.debug('00000000000000', step_limit=1000)