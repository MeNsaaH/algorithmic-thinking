import sys

sys.setrecursionlimit(10000)


class Search():
    def linear_search(A_list, x):
        '''
        linear search algorithm to find element x in array A_list
        '''
        for i in range(len(A_list)):
            if A_list[i] == x:
                return i
        return None

    def bin_search(A_list, start, stop, key):
        '''
        uses binary search to search for key in A_list
        '''
        m = (start + stop)//2
        if A_list[m] == key:
            return m
        if start > stop:
            return None
        if key < A_list[m]:
            return bin_search(A_list, start, m - 1, key)
        else:
            return bin_search(A_list, m + 1, stop, key)

