#!/usr/bin/python


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    left = []
    right = []
    for i, x in enumerate(arr):
        if i % 2 == 0:
            right.append(x)
        else:
            left.append(x)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    while left:
        result.append(left[0])
        left = left[1:]
    while right:
        result.append(right[0])
        right = right[1:]

    return result

print merge_sort([3, 1, 4, 5, 2])
