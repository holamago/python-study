#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)


import argparse
from typing import List


class ClassTest:
    def __init__(self, number: int):
        self.data = [i for i in range(number)]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx: int):
        return self.data[idx]

    def __add__(self, other):
        return self.data + other.data

    def __str__(self):
        return str(self.data)



def main():
    parser = argparse.ArgumentParser(description='Class Test')

    parser.add_argument(
        '-n',
        '--number',
        type=int,
        required=True,
        help='Number of test'
    )

    args = parser.parse_args()

    # Create a class instance & make a list with the given number
    app = ClassTest(args.number)

    # Print the class information with `__str__`
    print (app)

    # Print the length of the list
    print(len(app))

    # Print the list with `__getitem__`
    for i in range(len(app)):
        print(app[i])

    # Add two classes
    app2 = ClassTest(100)
    print(app + app2)



if __name__ == '__main__':
    main()