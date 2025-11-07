def repeat_str(n, s):
    return s * n


def solution(string):
    return string[::-1]


def other_angle(a, b):
    return 180 - (a + b)


import math

def litres(time):
    return math.floor(time * 0.5)


def cookie(x):
    if isinstance(x, str):
        name = "Zach"
    elif isinstance(x, (int, float)) and not isinstance(x, bool):
        name = "Monica"
    else:
        name = "the dog"
    return f"Who ate the last cookie? It was {name}!"
