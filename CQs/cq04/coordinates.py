"""This is the cq04!"""
__author__: str = "730465930"

def get_coords(xs: str, ys: str) -> None:
    i: int = 0
    j: int = 0
    result: str
    while i < len(xs):
        while j < len(ys):
            print("(" + xs[i] + "," + ys[j] + ")")
            j += 1
        i += 1
        j = 0

