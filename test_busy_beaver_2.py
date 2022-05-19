# -*- coding: utf-8 -*-
"""
Busy beaver Turing machine with 2 states.

Created on Sat Mar 30 13:55:25 2019

@author: shakes
"""
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
        ('a', '1'): ('b', '1', 'L'),

        ('b', '0'): ('a', '1', 'L'),
        ('b', '1'): ('h', '1', 'R'),
    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)

bbeaver.debug('00000000000000', step_limit=1000)

"""
Part 3b
    Source: https://www.freecodecamp.org/news/how-and-why-you-should-use-python-generators-f6fb56650888/

    Generator functions allow user to declare function that behave like an iterator,
    it allows programmer to make an iterator in a fast, easy and clear way. 
    Turing machine need to loop through many states, use generator is faster and save more memory space

Part 3d
    There are only two states in the Turing machine (a, b). 
    The maximum number of 1's printed is 4, which is the same as my result. 
"""