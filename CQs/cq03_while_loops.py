"""CQ03 While Loops"""
__author__: str = "730465930"

def num_instances(phrase: str, search_char: str) -> int:
    i: int = 0
    count: int = 0
    while i < len(phrase):
        if phrase[i] == search_char:
            count += 1
            i += 1
        else:
            i += 1
    return count


