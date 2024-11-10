"""This code will take the max and remove it from the list."""
__author__: str = "730465930"

def find_and_remove_max(input: list[int]) -> int:
    if len(input) == 0:
        #if the input list is empty, return -1
        return -1
    # find the max
    maximum: int = max(input)
    max_indices: list[int] = []
    i: int = 0
    while i < len(input) - 1:
        #find all max indices
        if input[i] == maximum:
            max_indices.append(i)
        i += 1
    j: int = len(max_indices) - 1
    print(str(max_indices))
    while j >= 0:
        #remove all instances in the list of the max using the max_indices
        input.pop(max_indices[j])
        j -= 1
    return maximum
