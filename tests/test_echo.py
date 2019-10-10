#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess


# Your test case class goes here
class TestEcho(unittest.TestCase):

    def setUp(self):
        """This method is called only once during test setup"""
        self.parser = echo.create_parser()

    def test_help(self):
        """ Running the program without arguments should show usage. """
        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()
        self.assertEquals(stdout, usage)

    def test_upper(self):
        parser = echo.create_parser()
        args = parser.parse_args(['-u', 'hello'])
        print(args)
        result = echo.upper('hello'.upper())
        self.assertEquals(result, 'HELLO')
        self.assertEquals(args.upper, True)

    def test_upper_short(self):
        args = ['--upper', 'Hello World']
        # test that the option flag gets parsed into namespace correctly
        p = echo.create_parser()
        ns = p.parse_args(args)
        self.assertTrue(ns.upper)
        # test that the text gets transformed correctly
        result = echo.main(args)
        self.assertEqual(result, 'HELLO WORLD')

    def test_lower(self):
        args = ['HELLO', '--lower']
        result = echo.main(args)
        self.assertEqual(result, 'hello')

    def test_upper_options(self):
        args = ['-u', 'Hello World']
        p = echo.create_parser()
        ns = p.parse_args(args)
        self.assertTrue(ns.upper)
        # test the text gets transformed correctly
        result = echo.main(args)
        self.assertEqual(result, 'HELLO WORLD')

    def test_upper_long(self):
        arg_list = ['--upper', 'hello']
        namespace = self.parser.parse_args(arg_list)
        self.assertTrue(namespace.upper)

    def test_title(self):
        args = ['HeLlo', '--title']
        result = echo.main(args)
        self.assertEqual(result, 'Hello')

    def test_all(self):
        """ Running with -ult returns title cased text """
        arg_list = ['-ult', "hello"]
        namespace = self.parser.parse_args(arg_list)
        self.assertTrue(namespace.title and namespace.upper
                        and namespace.lower)


if __name__ == '__main__':
    unittest.main()
