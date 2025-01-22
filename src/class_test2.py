#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)

import argparse
from typing import List, Text
from pathlib import Path
from pydantic import BaseModel
from time import sleep

class ClassTestConfig(BaseModel):
    name: Text = 'Class Test'
    data: List[int] = []


class ClassTest(ClassTestConfig):
    def __init__(self, number: int, digit: int = 10):
        super().__init__()
        self.data = [i for i in range(number)]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx: int):
        return self.data[idx]

    def __add__(self, other):
        return self.data + other.data

    def __str__(self):
        return str(f"Your class name is: {self.name} and data is {self.data}")

    def make_dir(self, path: Path):
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)

    def make_file(self, path: Text, data: Text):
        Path(path).write_text(data)

        # I want to delete the file after 5 seconds
        sleep(5)
        Path(path).unlink()
        Path('test').rmdir()


    def tuple_test(self):
        return len(self.data), self.data


def main():
    parser = argparse.ArgumentParser(description='Class Test')

    parser.add_argument(
        '-n',
        '--number',
        type=int,
        required=True,
        help='Number of test',
    )

    args = parser.parse_args()

    # Create a class instance & make a list with the given number
    app = ClassTest(
        digit=10,
        number=args.number,
    )

    # Print the name in the class
    print ("Your class name is: ", app.name)

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

    # Test tuple
    size, _ = app.tuple_test()
    print(f"Number of data: {size}")

    # Test make_dir
    app.make_dir(Path('test'))

    # Test make_file
    app.make_file('test/a.txt', 'Hello World')


if __name__ == '__main__':
    main()