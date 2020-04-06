with open('/usr/share/dict/words') as f:
    words = f.read().splitlines()

words = [w for w in words if not w[0].isupper() and len(w) <= 5]

import random

random.shuffle(words)

import json

print(json.dumps(words[:100]))