#!/usr/bin/env python3
# Pairs up friends randomly in a cyclic graph

import random

friends = open("friends.txt", "r").read().splitlines()
friends = list(map(lambda s: s.split(), friends))

def relationshiptest(friends):
    n = len(friends)
    for i in range(len(friends)):
        if ((len(friends[i]) == len(friends[(i + 1) % n]) == 2) and
            (friends[i][1] == friends[(i + 1) % n][1])):
            return False
    return True

def randomise(friends):
    random.shuffle(friends)
    while not relationshiptest(friends):
        random.shuffle(friends)
    return list(map(lambda s: s[0], friends))


friends = randomise(friends)

for i in range(len(friends)):
    print(friends[i], "-->", friends[(i + 1) % len(friends)])

