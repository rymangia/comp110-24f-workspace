from utils import only_evens
from utils import sub
from utils import add_at_index

# only_evens tests
def test_only_evens1() -> None:
    #tests a simple list to see if only evens works correctly
    list1: list[int] = [1, 2, 3, 4, 5]
    new_list: list[int] = only_evens(list1)
    assert new_list == [2, 4]

def test_only_evens2() -> None:
    #tests to see if only evens works correctly when numbers are all the same
    list1: list[int] = [2, 2, 2, 2]
    new_list: list[int] = only_evens(list1)
    assert new_list == [2, 2, 2, 2]

def test_only_evens3() -> None:
    #tests to see if only evens works correctly when all numbers are even
    list1: list[int] = [2, 4, 6, 8, 10]
    new_list: list[int] = only_evens(list1)
    assert new_list == [2, 4, 6, 8, 10]


# sub tests
def test_sub1() -> None:
    #tests a simple list to see if sub works correctly
    list1: list[int] = [1, 2, 3, 4, 5]
    new_list: list[int] = sub(list1, 1, 4)
    assert new_list == [2, 3, 4]

def test_sub2() -> None:
    #tests to see if sub works correctly when the start is less than 0
    list1: list[int] = [1, 2, 3, 4, 5]
    new_list: list[int] = sub(list1, -1, 4)
    assert new_list == [1, 2, 3, 4]

def test_sub3() -> None:
    #tests to see if only evens works correctly when all numbers are even
    list1: list[int] = [1, 2, 3, 4, 5]
    new_list: list[int] = sub(list1, 2, 7)
    assert new_list == [3, 4, 5]


# add_at_index tests
def test_add_at_index1() -> None:
    #tests a simple list to see if add_at_index works correctly
    list1: list[int] = [1, 3, 4, 5]
    add_at_index(list1, 2, 1)
    assert list1 == [1, 2, 3, 4, 5]

def test_add_at_index2() -> None:
    #tests a list with only one element to see if add_at_index works correctly
    list1: list[int] = [1]
    add_at_index(list1, 2, 1)
    assert list1 == [1, 2]

def test_add_at_index3() -> None:
    #tests a complex list to see if add_at_index works correctly
    list1: list[int] = [1, 2, 3, 4, 5]
    add_at_index(list1, 6, 5)
    assert list1 == [1, 2, 3, 4, 5, 6]