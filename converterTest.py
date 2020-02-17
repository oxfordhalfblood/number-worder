import unittest
import argparse
import sys
from converter import Converter, Parameter

# test: https://stackoverflow.com/questions/18160078/how-do-you-write-tests-for-the-argparse-portion-of-a-python-module/18161115#18161115

class ConverterTest(unittest.TestCase):

    def test_parser_for_zero(self):
        param = Parameter()
        parsed = param.parsefunc(['0', '-vv' ])
        self.assertEqual(parsed.num, '0')

    def test_parser_for_negative_zero(self):
        param = Parameter()
        args = ['-0', '-vv' ]
        with self.assertRaises(SystemExit):
            param.parsefunc(args)

    def test_parser_for_alphacharacters(self):
        param = Parameter()
        args = ['ssa', '-vv' ]
        with self.assertRaises(SystemExit):
            param.parsefunc(args)
        
    def test_parser_for_bignumber(self):
        param = Parameter()
        args = ['05243452654324500087252347870', '-vv' ]
        parsed = param.parsefunc(args)
        self.assertEqual(parsed.num, '05243452654324500087252347870')
    
    def test_parser_for_help_option(self):
        param = Parameter()
        args = ['-h']
        
        with self.assertRaises(SystemExit) as cm:
            param.parsefunc(args)
    
        self.assertEqual(cm.exception.code, 0)
        # print("passed")
    
    def test_parser_for_verbose_option(self):
        param = Parameter()
        args = ['-v']
        
        with self.assertRaises(SystemExit) as cm:
            param.parsefunc(args)
    
        self.assertEqual(cm.exception.code, 2)

    def test_parser_for_verbose2_option(self):
        param = Parameter()
        args = ['-vv']
        
        with self.assertRaises(SystemExit) as cm:
            param.parsefunc(args)
    
        self.assertEqual(cm.exception.code, 2)

    def test_converter_for_pos_integer(self):
        converter = Converter()
        converted = converter.num_to_word('052')
        self.assertEqual(converted, 'zerofivetwo')

    def test_converter_for_all_zero(self):
        converter = Converter()
        converted = converter.num_to_word('0000')
        self.assertEqual(converted, 'zerozerozerozero')

    def test_converter_for_ro(self):
        converter = Converter()
        converted = converter.num_to_word('1111111')
        self.assertEqual(converted, 'oneoneoneoneoneoneone')


        # self.assertEqual(param.parse_args(converter), 'two')

        # parsed = self.parser.parse_args(['--something', 'test'])
        # self.assertEqual(parsed.something, 'test')

if __name__ == "__main__":
    unittest.main()