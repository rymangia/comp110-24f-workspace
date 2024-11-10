"""Ex 05"""
__author__: str = "730465930"

def only_evens(list_all: list[int]) -> list[int]:
    """This function returns only the evens"""
    list_evens: list[int] = []
    for x in list_all:
        if x % 2 == 0:
            list_evens.append(x)
    return list_evens

def sub(list_1: list[int], start: int, end: int) -> list[int]:
    """This function returns the elements of the list between start and end parameters"""
    new_list: list[int] = []
    if start < 0:
        start = 0
    if end > len(list_1):
        end = len(list_1)
    if (len(list_1) == 0) or (start >= len(list_1) or (end <= 0)):
        return new_list
    while start < end:
        new_list.append(list_1[start])
        start += 1
    return new_list

def add_at_index(list1: list[int], element: int, index: int) -> None:
    """This function returns the original list but adds in an element at the given index"""
    if (index < 0) or (index > len(list1)):
        raise IndexError("Index is out of bounds for the input list")
    list_added: list[int] = []
    i: int = 0
    while i < index:
        list_added.append(list1[i])
        i += 1
    list_added.append(element)
    while index < len(list1):
        list_added.append(list1[index])
        index += 1
    i = 0
    #manually change every element of list1 to be the elements of list_added
    while i < len(list_added) - 1:
        list1[i] = list_added[i]
        i += 1
    list1.append(list_added[len(list_added) - 1])
    return None

