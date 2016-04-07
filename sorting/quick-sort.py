#!/usr/bin/python

def quick_sort(arr, lo=0, hi=None):
	if hi is None:
		hi = len(arr) - 1

	if lo < hi:
		print 'lo < hi', arr
		p = partition(arr, lo, hi)
		quick_sort(arr, lo, p - 1)
		quick_sort(arr, p + 1, hi)
	
	return arr

def partition(array, lo, hi):
	pivot = array[hi]
	print 'pivot', pivot
	i = lo
	for j in range(lo, hi):
		print 'inner iteration', array
		if array[j] <= pivot:
			temp = array[j]
			array[j] = array[i]
			array[i] = temp
			print 'swapping inner', array
			i += 1

	temp = array[hi]
	array[hi] = array[i]
	array[i] = temp
	print 'swapping outer', array

	return i

print quick_sort([3, 5, 2, 1, 4])
