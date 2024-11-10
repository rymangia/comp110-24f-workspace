"""Ex 06 - Dictionary Utility Functions"""
__author__: str = "730465930"

def invert(old_dict: dict[str, str]) -> dict[str, str]:
    """This function inverts the key-value pairs in a list"""
    new_dict: dict[str, str] = {}
    for key in old_dict:
        value: str = old_dict[key]
        if value in new_dict:
            raise KeyError("error message of your choice here!")
        else:
            new_dict[value] = key
    return new_dict

def favorite_color(old_color_dict: dict[str, str]) -> str:
    """This function returns the most frequently ocurring color"""
    new_color_dict: dict[str, int] = {}
    #count the max values
    for person in old_color_dict:
        color: str = old_color_dict[person]
        if color in new_color_dict:
            new_color_dict[color] += 1
        else:
            new_color_dict[color] = 1
    #check which is max and return that
    max: int = 0
    color_max: str = ""
    for value in new_color_dict:
        count: int = new_color_dict[value]
        if count > max:
            max = count
            color_max = value
    return color_max

def count(list1: list[str]) -> dict[str, int]:
    """Counts the iterations of each item in the list"""
    result_dict: dict[str, int] = {}
    for x in list1:
        if x in result_dict:
            result_dict[x] += 1
        else:
            result_dict[x] = 1
    return result_dict

def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """alphabetizes the list by the first character."""
    final_dict: dict[str, list[str]] = {}
    for x in input_list:
        if x[0] not in final_dict:
            final_dict[x[0]] = []
    for char in final_dict:
        for word in input_list:
            if word[0] == char:
                final_dict[char].append(word)
    return final_dict

def update_attendance(att_dict: dict[str, list[str]], week_day: str, student: str) -> None:
    """This function adds student names to days of the week for attendance"""
    if week_day not in att_dict:
        att_dict[week_day] = [student]
    else:
        for x in att_dict[week_day]:
            if student in att_dict[week_day]:
                return None
        else:
            att_dict[week_day].append(student)
    return None


dictionary: dict[str, list[str]] = {
    "Monday": ["ryan", "jake", "liam"],
    "Tuesday": ["isobel, molly"],
    "Wednesday": ["jamal, leonte"]
}

update_attendance(dictionary, "Monday", "jose")
print(dictionary)