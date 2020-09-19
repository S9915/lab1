def jaccar(set1, set2):
    union = len(set1) + len(set2)
    inter = 0
    for item in set1:
        if item in set2:
            inter += 1
            union -= 1
    return inter / union

import random as rnd
for i in range(3):
    set1 = set([rnd.randint(1, 15) for i in range(rnd.randint(5, 10))])
    set2 = set([rnd.randint(1, 15) for i in range(rnd.randint(5, 10))])
    print(f"set 1: {set1}", f"set 2: {set2}", '', sep='\n')
    print("Метрика Жаккара: " + str({round(jaccar(set1, set2), 4)}), '\n')
