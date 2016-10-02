#!/usr/bin/env python

import random

if __name__ == "__main__":
    # rd = input()
    # print(rd)
    list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    rand = random.Random()
    i = rand.randint(0, len(list) - 1)
    print(i)
    print(list[i])

