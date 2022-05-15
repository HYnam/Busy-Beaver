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
        
        ('q0', '1'): ('q2','#','R'),

        ('q2', '1'): ('q2','1','R'),
        ('q2', '0'): ('q3','#','R'),
        ('q2', '#'): ('q3','#','R'),

        ('q3', '1'): ('q4','#','R'),
        ('q3', '0'): ('q15','#','L'),
        ('q3', '#'): ('q4','#','R'),

        ('q4', '1'): ('q4','1','R'),
        ('q4', ''): ('q5','#','R'),
        ('q4', '#'): ('q5','#','R'),


        ('q5', '1'): ('q5','1','R'),
        ('q5', ''): ('q6','1','L'),

        ('q6', '#'): ('q7','#','L'),
        ('q6', '1'): ('q6','1','L'),

        ('q7', '#'): ('q9','1','L'),
        ('q7', '1'): ('q8','1','L'),

        ('q8', '#'): ('q3','1','R'),
        ('q8', '1'): ('q8','1','L'),

        ('q9', '#'): ('q10','#','L'),
        ('q9', '1'): ('q9','1','L'),

        ('q10', '#'): ('q12','','R'),
        ('q10', '1'): ('q11','1','L'),

        ('q11', '#'): ('q0','','R'),
        ('q11', '1'): ('q11','1','L'),

        ('q12', '#'): ('q12','','R'),
        ('q12', '1'): ('q13','#','R'),

        ('q13', '#'): ('q14','','L'),
        ('q13', '1'): ('q13','#','R'),
        ('q13', ''): ('qa','','L'),

        ('q14', '#'): ('q14','','L'),
        ('q14', '1'): ('q14','#','R'),
        ('q14', ''): ('qa','','L'),

        ('q15', '#'): ('q16','','L'),
        ('q15', '1'): ('q15','#','L'),
        ('q15', ''): ('qa','','L'),

        ('q16', '#'): ('qa','','L'),
        ('q16', ''): ('qa','','L'),
        ('q16', '1'): ('q16','#','L'),
    }
)

multiplier.debug('111011111', step_limit=500)
