from random import random, randrange

def ucid_gen():
    a = []
    while len(a) != 7:
        x = randrange(10)
        a.append(x)
    for i in a:
        print(i)



ucid_gen()