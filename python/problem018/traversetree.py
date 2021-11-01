'''traversetree module

Module with functions to traverse our triangle.
'''


__all__ = ['maximum_pathsum']
__author__ = 'Alexandre Pierre'


def pairs(iterator):
    '''Given an iterator yields its elements in pairs in which the first
element will assume values from first to second-last and the second element
of the pair will range from second to last iterator elements.'''
    try:
        previous = next(iterator)
    except StopIteration:
        return

    for current in iterator:
        yield previous, current
        previous = current

def maximum_pathsum(triangle):
    '''Given a triangle returns the maximum topdown path sum'''
    acc = (0 for _ in triangle[-1])
    for triangle_row in triangle[:0:-1]:
        row = map(sum, zip(acc, triangle_row))
        acc = map(max, pairs(row))

    return triangle[0][0] + next(acc)
