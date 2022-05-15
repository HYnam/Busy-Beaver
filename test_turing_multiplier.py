# -*- coding: utf-8 -*-
"""
Test script for running a Turing machine unary adder

Created on Fri Mar 29 21:57:42 2019

@author: shakes
"""
from turing_machine import TuringMachine

#create the Turing machine
multiplier = TuringMachine( 
    { 
        #Write your transition rules here as entries to a Python dictionary
        #For example, the key will be a pair (state, character)
        #The value will be the triple (next state, character to write, move head L or R)
        #such as ('q0', '1'): ('q1', '0', 'R'), which says if current state is q0 and 1 encountered
        #then transition to state q1, write a 0 and move head right.
        ('q0', '1'): ('q0', '1', 'R'),
        ('q0', '0'): ('q1', '0', 'R'),

        ('q1', '1'): ('q1', '1', 'R'),
        ('q1', ''): ('q2', '0', 'L'),

        ('q2', '1'): ('q2', '1', 'L'),
        ('q2', '0'): ('q3', '0', 'R'),

        ('q3', ''): ('q3', '', 'R'),
        ('q3', '1'): ('q4', '', 'L'),
        ('q3', '0'): ('qa', '', 'R'),

        ('q4', ''): ('q4', '', 'L'),
        ('q4', '0'): ('q5', '0', 'L'),

        ('q5', 'Y'): ('q5', 'Y', 'L'),
        ('q5', '1'): ('q6', 'Y', 'R'),

        ('q6', 'Y'): ('q6', 'Y', 'R'),
        ('q6', '0'): ('q7', '0', 'R'),

        ('q7', '1'): ('q7', '1', 'R'),
        ('q7', ''): ('q7', '', 'R'),
        ('q7', '0'): ('q8', '0', 'R'),

        ('q8', '1'): ('q8', '1', 'R'),
        ('q8', ''): ('q9', '1', 'L'),

        ('q9', '1'): ('q9', '1', 'L'),
        ('q9', '0'): ('q10', '0', 'L'),

        ('q10', '1'): ('q10', '1', 'L'),
        ('q10', ''): ('q10', '', 'L'),
        ('q10', '0'): ('q5', '0', 'L'),

        ('q5', ''): ('q11', '', 'R'),
        ('q11', 'Y'): ('q11', '1', 'R'),
        ('q11', '0'): ('q3', '0', 'R'),
    }
)

multiplier.debug('110111', step_limit=300)
