#!/usr/bin/env python3
'''main module
'''


__author__ = 'Alexandre Pierre'


from sys import argv
import readtriangle as rt
import traversetree as tt

if __name__ == '__main__':
    TRIANGLE = rt.file2triangle(argv[1])
    print(tt.maximum_pathsum(TRIANGLE))
