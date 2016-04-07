#!/usr/bin/python


def selection_sort(arr):
    for j in range(len(arr) - 1):
        print 'outer iteration', arr
        i_min = j
        for i in range(j + 1, len(arr)):
            print 'inner iteration', arr
            if arr[i] < arr[i_min]:
                i_min = i

        if not i_min == j:
            temp = arr[i_min]
            arr[i_min] = arr[j]
            arr[j] = temp
            print 'swapping elements', arr

    return arr

print selection_sort([4, 2, 5, 3, 1])
