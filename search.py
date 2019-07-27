import sys

sys.setrecursionlimit(10000)


class Search():
    def linear_search(A_list, x):
        '''
        linear search algorithm to find element x in array A_list
        '''
        A_list = tuple(A_list)
        tmp = []
        for i in A_list:
            if i == x:
                tmp.append(i)
        return tmp

    def bin_search(A_list, start, stop, key):
        '''
        uses binary search to search for key in A_list
        '''
        m = (start + stop)//2
        if A_list[m] == key:
            return m
        if start > stop:
            toret = None
        if key < A_list[m]:
            toret =  bin_search(A_list, start, m - 1, key)
        else:
            toret =  bin_search(A_list, m + 1, stop, key)
        return toret

