#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "mwilliamson with help from Piero"

import sys
import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    parser.add_argument('-u', '--upper', action='store_true')
    parser.add_argument('--lower', action='store_true')
    parser.add_argument('--title', action='store_true')
    parser.add_argument('text', help='convert text to uppercase')
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    # pass in actual arg list to parse instead of using sys.argv default
    namespace = parser.parse_args(args)
    print("Cmd line arguments: {}".format(namespace))

    # Get the raw text input, unchanged
    text = namespace.text
    upper_flag = namespace.upper
    lower_flag = namespace.lower
    title_flag = namespace.title

    # Perform the requested text transformation:
    if upper_flag:
        text = text.upper()
    if lower_flag:
        text = text.lower()
    if title_flag:
        text = text.title()

    return text


if __name__ == '__main__':  # This is called an "import guard"
    print("My name is {}".format(__name__))
    print("I'm running direct from cmd line")
    # give cmd line arguments to main, get result back, print result
    print(main(sys.argv[1:]))

else:
    print("I've been imported from somewher else")
