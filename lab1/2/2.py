def jaccard(set1: set, set2: set) -> float:
    intersec_size = 0
    union_size = len(set1) + len(set2)
    for item in set1:
        if item in set2:
            intersec_size += 1
            union_size -= 1
    return intersec_size / union_size

if __name__ == '__main__':
    import random as rnd
    for i in range(1):
        set1 = set([rnd.randint(1, 15) for i in range(rnd.randint(5, 10))])
        set2 = set([rnd.randint(1, 15) for i in range(rnd.randint(5, 10))])
        print(f"set 1: {set1}", f"set 2: {set2}", '', sep='\n')
    print("Метрика Жаккарда: " + str({round(jaccard(set1, set2), 3)}))
