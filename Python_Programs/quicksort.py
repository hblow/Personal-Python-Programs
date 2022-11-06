# Quicksort Program
# Created May 2022 By Harrison Low
# A simple quicksort program as I wanted to test out what I learned in theory as we did not get the chance to make a quicksort program in class

def partition(low, high, array):
    '''
    Partitions the array where all values smaller than the pivot are in front of it and all values larger to the right of it
    inputs:
       low - (int): The lowest index of the part of the array being partitioned
       high - (int): The highest index of the part of the array being partitioned
       array - (list): The array being partitioned
    returns: The index of the final position of the pivot
    '''
    # Index is where the pivot originally is and updated index will be it's final position
    index = low
    # Pivot will be the first value on the leftmost side of the array
    pivot = array[low]
    for i in range(low+1, high):
        if array[i] < pivot:
            index += 1
            # Sorts in place
            array[index], array[i] = array[i], array[index]
    # Moves the pivot to it's designated space
    array[index], array[low] = array[low], array[index]
    return index

def quicksort(low, high, array):
    '''
    Sorts the array recursively with pivots and partitioning
    inputs:
       low - (int): The lowest index of the part of the array being partitioned
       high - (int): The highest index of the part of the array being partitioned
       array - (list): The array being partitioned
    returns: None
    '''
    # If array is empty or only has 1 element, return array
    if len(array) <= 1:
        return array
    # Continue recursion until both high and low are equal
    if low != high:
        pivot_index = partition(low, high, array)
        quicksort(low, pivot_index, array)
        quicksort(pivot_index+1, high, array)
# Basic Testing
# x=[5,4,3,2,1]
# quicksort(0, len(x), x)
# print(x)
