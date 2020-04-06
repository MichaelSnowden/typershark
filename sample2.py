with open('common.txt') as f:
    words = [w for w in f.read().splitlines() if len(w) > 3][10:200]

import random

random.shuffle(words)

import json

print(json.dumps(words))