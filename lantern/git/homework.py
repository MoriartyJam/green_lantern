import typing
from typing import List


class OurAwesomeException(Exception):

    pass


def is_two_object_has_same_value(first: typing.Any, second: typing.Any) -> bool:
    if first == second:
        return True
    else:
        return False


def is_two_objects_has_same_type(first: typing.Any, second: typing.Any) -> bool:
    if type(first) == type(second):
        return True
    else:
        return False


def is_two_objects_is_the_same_objects(first: typing.Any, second: typing.Any) -> bool:
    if first is not second:
        return False
    else:
        return True


def multiple_ints(first_value: int, second_value: int):
    if type(first_value * second_value) == int:
        return first_value * second_value
    else:
        raise TypeError


def multiple_ints_with_conversion(first_value: typing.Any, second_value: typing.Any):
    a = int(first_value) * int(second_value)
    return(a)


def is_word_in_text(word: str, text: str) -> bool:
    if text.find(word) != -1:
        return True
    else:
        return False


def some_loop_exercise()-> list:
    list1 = []
    for i in range(13):
        list1.append(i)
        if i == 6 or i == 7:
            list1.remove(i)

    return list1


def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    return [item for item in data if item >= 0]


    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
        >>> [1, 5, 8]
    """



def alphabet():
    return dict(zip(range(1, 27),'abcdefghijklmnopqrstuvwxyz'))



def simple_sort(data: List[int]) -> List[list]:
    for j in range(len(data)):
        swapped = False
        i = 0
        while i < len(data) - 1:
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
            i = i + 1
        if swapped == False:
            break
    return(data)