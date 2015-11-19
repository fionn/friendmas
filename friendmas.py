#!/usr/bin/env python3
# Pairs up friends randomly in a cyclic graph

import random

def relationshiptest(friends):
    n = len(friends)
    for i in range(len(friends)):
        if ((len(friends[i]) == len(friends[(i + 1) % n]) == 2) and
            (friends[i][1] == friends[(i + 1) % n][1])):
            return False
    return True

def knoweachother(criteria, friends):
    for i in range(len(friends)):
        for criterion in criteria:
            if (friends[i] == criterion[0] and 
                (friends[(i + 1) % len(friends)] not in criterion or
                 friends[(i - 1) % len(friends)] not in criterion)):
                return False
    return True

def randomise(friends, criteria):
    random.shuffle(friends)
    while not (relationshiptest(friends) and 
               knoweachother(criteria, list(map(lambda s: s[0], friends)))):
        random.shuffle(friends)
    return list(map(lambda s: s[0], friends))


friends = open("friends.txt", "r").read().splitlines()
friends = list(map(lambda s: s.split(), friends))

criteria = open("criteria.txt", "r").read().splitlines()
criteria = list(map(lambda s: s.split(), criteria))

friends = randomise(friends, criteria)

for i in range(len(friends)):
    print(friends[i], "-->", friends[(i + 1) % len(friends)])

