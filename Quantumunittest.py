#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 1 21:25:32 2018
Description: These are unit test functions for the code Quantum_monte_carlo.py

@author: Vidya Venkatesan
"""

import unittest
import Quantum

class TestQuantum(unittest.TestCase):
    
    def test_position(self):
        result = Quantum.position(0,0.1)
        self.assertEqual(result, [0])
    
        def test_wavefunction(self):
            result = Quantum.wavefunction(1)
            self.assertEqual(result, [1])
            
        def test_addzeroes(self):
            result = Quantum.addzeroes(1)
            self.assertEqual(result, [0,1,0])
        
        def test_deletezeroes(self):
            result = Quantum.wavefunction([0,1,0])
            self.assertEqual(result, [1])
            
        def test_kinetic(self):
             result = Quantum.kinetic([1,2,3],1,0.5)
             self.assertEqual(result, [0.0,0.0,8.0])
