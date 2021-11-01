'''traversetree module

Module with functions to traverse our triangle.
'''


__all__ = ['maximum_path_topdown']
__author__ = 'Alexandre Pierre'


import heapq
from collections import namedtuple


Call = namedtuple('Call', ['acc', 'column', 'row'])

def last_index(indexable):
    '''Returns the last index of an indexable data structure'''
    return len(indexable) - 1

def maximum_path_topdown(triangle, row=0, column=0, acc=0):
    '''Calculates the maximum topdown path sum'''
    acc += triangle[row][column]

    if row == last_index(triangle):
        return acc

    left = maximum_path_topdown(triangle, row+1, column, acc)
    right = maximum_path_topdown(triangle, row+1, column+1, acc)

    return left if left > right else right

"""def maximum_path_topdown(triangle):
    '''Calculates the maximum topdown path sum'''
    heap = [Call(column=0, row=0, acc=0)]
    
    ROWS_COUNT = len(triangle)
    max_acc = -1
    while heap:
        left, right = evaluate_call(triangle, heapq.heappop(heap))
        max_acc = max(max_acc, left.acc, right.acc)
        conditional_push(
            heap, left,
            check_call(left, ROWS_COUNT, max_acc)
            and not end_of_triangle(left, ROWS_COUNT))
        conditional_push(
            heap, right,
            check_call(right, ROWS_COUNT, max_acc)
            and not end_of_triangle(right, ROWS_COUNT))

    return max_acc

def evaluate_call(triangle, call):
    ''' '''
    node = triangle[call.row][call.column]
    acc = call.acc + node
    left = Call(acc=acc, row=call.row + 1, column=call.column)
    right = Call(acc=acc, row=call.row + 1, column=call.column + 1)

    return left, right

def check_call(call, rows_count, max_acc, max_number=99):
    '''Checks whether the call can lead to the maximum path sum or not'''
    return call.acc + (rows_count - call.row) * max_number > max_acc

def end_of_triangle(call, rows_count):
    '''Checks whether or not the limit of triangle rows have been exceed'''
    return call.row >= rows_count

def conditional_push(heap, item, condition):
    '''Pushes to the heap if conditions are true'''
    if condition:
        heapq.heappush(heap, item)
"""
