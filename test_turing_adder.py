# -*- coding: utf-8 -*-
"""
Test script for running a Turing machine unary adder

Created on Fri Mar 29 21:57:42 2019

@author: shakes
"""
from turing_machine import TuringMachine

#create the Turing machine
adder = TuringMachine( 
    { 
        #Write your transition rules here as entries to a Python dictionary
        #For example, the key will be a pair (state, character)
        #The value will be the triple (next state, character to write, move head L or R)
        #such as ('q0', '1'): ('q1', '0', 'R'), which says if current state is q0 and 1 encountered
        #then transition to state q1, write a 0 and move head right.
        ('q0', '1'): ('q1', 'x', 'R'),
        ('q1', '1'): ('q1', '1', 'R'),
        ('q1', '0'): ('q2', '0', 'R'),
        ('q2', '1'): ('q2', '1', 'R'),
        ('q2', ''): ('q3', '1', 'L'),
        ('q3', '1'): ('q3', '1', 'L'),
        ('q3', '0'): ('q4', '0', 'L'),
        ('q4', '1'): ('q4', '1', 'L'),
        ('q4', 'x'): ('q0', 'x', 'R'),
        ('q0', '0'): ('qa', '', 'R'),
    }
)

adder.debug('11101111')
