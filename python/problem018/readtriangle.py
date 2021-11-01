'''readtriangle module

Home to the function that turns a text file into a list of lists of numbers.
'''


__all__ = ['file2triangle']
__author__ = 'Alexandre Pierre'


def file2triangle(filename):
    '''Gets the numbers in the file in a list of lists format.'''
    with open(filename, 'r', encoding='ascii') as file_ptr:
        triangle = tuple(
            tuple(map(int, line.split(' ')))
            for line in file_ptr)

    return triangle
