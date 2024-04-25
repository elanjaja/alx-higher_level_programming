#!/usr/bin/python3
"""6-peak module"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers
    Args:
        list_of_integers: a list containg integers
    """

    if not list_of_integers:
        return None

    return binary_search(list_of_integers, 0, len(list_of_integers) - 1)


def binary_search(list_of_integers, left, right):
    """
    Binary Search for peak
    Args:
        list_of_integers: a list containg integers
        left: left index
        right: right index
    """
    if left == right:
        return list_of_integers[left]

    mid = (left + right) // 2

    if mid == 0 and list_of_integers[mid] > list_of_integers[mid + 1]:
        return list_of_integers[mid]

    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return binary_search(list_of_integers, mid + 1, right)
    else:
        return binary_search(list_of_integers, left, mid)
