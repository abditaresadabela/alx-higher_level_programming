#!/usr/bin/python3
""" This module contains a function to find a peak in a list of unsorted integers """
def find_peak(list_of_integers):
    """ Find a peak in a list of unsorted integers """
    if not list_of_integers:
        return None

    n = len(list_of_integers)
    if n == 1:
        return list_of_integers[0]

    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if ((mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and
                (mid == n - 1 or list_of_integers[mid] >= list_of_integers[mid + 1])):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            right = mid - 1
        else:
            left = mid + 1
