import math


def get_distance(a: tuple, b: tuple):
    # calculates distance using the theorem of pythagoras
    distance = math.sqrt(math.pow(b[0]-a[0], 2) + math.pow(b[1]-a[1],2))
    return distance
