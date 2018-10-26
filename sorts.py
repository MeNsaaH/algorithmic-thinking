
"""Sorting algorithms"""


def bubble_sort(A_list):
    '''
    uses bubblesort algorithm to sort array A_list
    '''
    passes = True
    while(passes):
        passes = False
        for i in range(len(A_list)):
            if i == len(A_list)-1:
                break
            if A_list[i] > A_list[i+1]:
                A_list[i], A_list[i+1] = A_list[i+1], A_list[i]
                passes = True
    return A_list


def selection_sort(A_list):
    '''
    uses selection sort algorithm to sort array A_list
    '''
    for i in range(len(A_list)-1, 0, -1):
        max_pos = 0
        for x in range(i+1):
            if A_list[x] > A_list[max_pos]:
                max_pos = x
        A_list[i], A_list[max_pos] = A_list[max_pos], A_list[i]
        
    return A_list


def insertion_sort(A_list):
    '''
    uses insertion algorithm to sort array A_list
    '''
    for index in range(1, len(A_list)):
        current_value = A_list[index]
        position = index
        while position > 0 and A_list[position - 1] > current_value:
            A_list[position] = A_list[position - 1]
            position = position - 1
        A_list[position] = current_value

    return A_list


def shell_sort(A_list):
    '''
    uses shell sort algorithm to sort and return sorted array A_list
    '''
    sublist_count = len(A_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(A_list, start_position, sublist_count)
        sublist_count = sublist_count // 2
    return A_list


def gap_insertion_sort(A_list, start, gap):
    '''
    sets gap for insertion sort
    '''
    for i in range(start + gap, len(A_list), gap):
        current_value = A_list[i]
        position = i
        while position >= gap and A_list[position - gap] > current_value:
            A_list[position] = A_list[position - gap]
            position = position - gap
        A_list[position] = current_value


def merge_sort(A_list):
    if len(A_list) <= 1:
        return A_list
    m = len(A_list)//2
    left = A_list[:m]
    right = A_list[m:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    a = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a.append(left[i])
            i += 1
        else:
            a.append(right[j])
            j += 1
        
    while i < len(left):
        a.append(left[i])
        i += 1
    while j < len(right):
        a.append(right[j])
        j += 1
    return a


def quick_sort(A_list):
    quick_sort_helper(A_list, 0, len(A_list) - 1)
    return A_list


def quick_sort_helper(A_list, first, last):
    if first < last:
        split_point = partition(A_list, first, last)
        quick_sort_helper(A_list, first, split_point - 1)
        quick_sort_helper(A_list, split_point + 1, last)


def partition(A_list, first, last):
    pivot_value = A_list[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and A_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        while A_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            A_list[left_mark], A_list[right_mark] = A_list[right_mark], A_list[left_mark]

        A_list[first], A_list[right_mark] = A_list[right_mark], A_list[first]
    return right_mark