from find_max import find_and_remove_max

def test_returns_expected_value() -> None:
    #tests to see if find_and_remove_max returns the expected value
    list1: list[int] = [3, 4, 6, 3, 1]
    maximum = find_and_remove_max(list1)
    assert maximum == 6

def test_mutates_as_expected() -> None:
    #tests to see if find_and_remove_max mutates the list as expected
    list1: list[int] = [3, 4, 6, 3, 1]
    find_and_remove_max(list1)
    assert list1 == [3, 4, 3, 1]

def test_returns_correct_value() -> None:
    #tests to see if find_and_remove_max returns the correct value in an unconventional case
    list2: list[int] = [2, 2, 2, 2, 1]
    find_and_remove_max(list2)
    assert list2 == [1]