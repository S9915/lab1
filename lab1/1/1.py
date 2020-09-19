def ardic(array):
    return {array[i]: [item[0] for item in list(enumerate(array)) if item[1] == array[i]] for i in range(len(array))}

ardic(['a', 'b', 'c', 'd', 'e', 'a', 'a', 'b', 'c'])
