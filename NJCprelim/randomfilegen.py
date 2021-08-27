import json
import random

with open('RESTAURANTS.json', 'w') as target:
    j = []
    for i in range(100):
        random_string = ''
        for _ in range(random.randint(3,15)):
            random_integer = random.randint(97, 97 + 26 - 1)
            random_integer = random_integer - 32 if random.randint(0, 1) == 1 else random_integer
            random_string += (chr(random_integer))
        d = dict()
        d['name'] = random_string
        d['rating'] = round(
            random.random() * 100, 2) if random.randint(0, 1) == 1 else ''
        j.append(d)

    js = json.dumps(j,indent=2)
    target.write(js)
