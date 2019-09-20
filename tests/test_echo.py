#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo


# Your test case class goes here
class TestEcho(unittest.TestCase):

    def setUp(self):
        """This method is called only once during test setup"""
        self.parser = echo.create_parser()

    def test_no_Change(self):
        args = ['cat']
        result = echo.main(args)
        self.assertEqual(result, 'cat')

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

    def test_title(self):
        args = ['HeLlo', '--title']
        result = echo.main(args)
        self.assertEqual(result, 'Hello')


if __name__ == '__main__':
    unittest.main()
