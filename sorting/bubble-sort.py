#!/usr/bin/python


def bubble_sort(arr):
    for i in range(1, len(arr)):
        print 'outer iteration', arr
        for j in range(i):
            print 'inner iteration', arr
            if arr[j] > arr[j + 1]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp

    return arr

print bubble_sort([3, 1, 4, 2, 5])
