def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean =sum(value) / len(value)
    return the_mean

k1 = {"Sam":10, "Suresh": 25, "Lion": 5, "Don": 6}

print(mean(k1))