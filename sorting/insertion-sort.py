#!/usr/bin/python

def insertion_sort(arr):
	for i in range(1, len(arr)):
		print "outer iteration", arr
		j = i
		while j > 0 and arr[j-1] > arr[j]:
			print "inner iteration", arr
			temp = arr[j-1]
			arr[j-1] = arr[j]
			arr[j] = temp
			j = j - 1

	return arr

print insertion_sort([2, 4, 5, 1, 3])
