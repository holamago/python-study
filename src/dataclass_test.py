#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)


from dataclasses import dataclass


@dataclass
class my_data:
    today: str
    work: str
    with_whom: str
    where: str


def main():
    today = my_data("2024-09-09", "Coding", "Galois", "Home")

    print (today.today)
    print (today.work)
    print (today.with_whom)
    print (today.where)


if __name__ == '__main__':
    main()