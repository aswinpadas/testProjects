import random
from builtins import range

scrt_code = 4521

def random_number():
    return random.randint(0, 9)

def check_number_exist(limit):
    rn = []
    i = 0
    while i < limit:
        num = random_number()
        if rn.count(num) == 0:
            rn.append(num)
            i += 1
    return rn


print(check_number_exist(4))
