#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import unittest
import bf

from itertools import ifilterfalse,count

class MockStdout(object):
    text = ''
    def write(self,str):
        self.text += str
    

class TestBfOneliner(unittest.TestCase):

    def setUp(self):
        self.stdout = MockStdout()
        self.default_stdout = sys.stdout
        sys.stdout = self.stdout

    def tearDown(self):
        sys.stdout = self.default_stdout
    
    def testBf(self):
        eval(bf.compile('>+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.[-]>++++++++[<++++>-]<.>+++++++++++[<+++++>-]<.>++++++++[<+++>-]<.+++.------.--------.[-]>++++++++[<++++>-]<+.[-]++++++++++.'))
        self.assertEqual(self.stdout.text, 'Hello World!\n')

    def testBf_linebreak(self):
        eval(bf.compile('''
                        >+++++++++[<++++++++>-]<.>+++++++[<++++>-]
                        <+.+++++++..+++.[-]>
                        ++++++++[<++++>-]<.>+++++++++++
                        [<+++++>-]<.>++++++++[<+++>-]<.+++.------.--------.[-]>++++++++[<++++>-]<+.[-]++++++++++.
                        '''))
        self.assertEqual(self.stdout.text, 'Hello World!\n')


if __name__ == '__main__':
    unittest.main()
