#!/usr/bin/env python3
# Pairs up friends randomly in a cyclic graph

import random

friends = open("friends.txt", "r").read().splitlines()

random.shuffle(friends)

for i in range(len(friends)):
    if i != len(friends) - 1:
        print(friends[i], "-->", friends[i + 1])
    else:
        print(friends[i], "-->", friends[0])

