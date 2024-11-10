"""Mutating functions."""
__author__: str = "730465930"

def manual_append(list_before_append: list[int], number: int) -> None:
    """This function manually does the same thing as the append function"""
    list_before_append.append(number)
    return None

def double(list_before_double: list[int]) -> None:
    """This function doubles each item in the list"""
    i: int = 0
    while i < len(list_before_double):
        list_before_double[i] *= 2
        i += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(str(list_1))
print(str(list_2))


