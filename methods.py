import random
import time


def coin_flip():
    value = random.randint(1,2)
    if value == 1:
        value = "'Решка'"
    else:
        value = "'Орёл'"

    return value

def write(value,variables):
	print(eval(str(value),variables),end='')

def sleep(value):
	time.sleep(int(value))

def random_int(value,variables):
	return random.randint(int(eval(str(value.split(',')[0].replace('random(','')),variables)),int(eval(str(value.split(',')[1][:-1]),variables)))
