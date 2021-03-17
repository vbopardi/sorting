#!/bin/python3
import random


def cmp_standard(a, b):
    '''
    used for sorting from lowest to highest

    >>> cmp_standard(125, 322)
    -1
    >>> cmp_standard(523, 322)
    1
    '''
    if a < b:
        return -1
    if b < a:
        return 1
    return 0


def cmp_reverse(a, b):
    '''
    used for sorting from highest to lowest

    >>> cmp_reverse(125, 322)
    1
    >>> cmp_reverse(523, 322)
    -1
    '''
    if a < b:
        return 1
    if b < a:
        return -1
    return 0


def cmp_last_digit(a, b):
    '''
    used for sorting based on the last digit only

    >>> cmp_last_digit(125, 322)
    1
    >>> cmp_last_digit(523, 322)
    1
    '''
    return cmp_standard(a % 10, b % 10)


def _merged(xs, ys, cmp=cmp_standard):
    '''
    Assumes that both xs and ys are sorted,
    and returns a new list containing the elements of both xs and ys.
    Runs in linear time.

    NOTE:
    In python, helper functions are frequently prepended with the _.
    and not part of the "public interface".

    >>> _merged([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    '''

    if xs == []:
        return ys
    elif ys == []:
        return xs

    if (len(xs) == 1) and (len(ys) == 1):
        if cmp(xs[0], ys[0]) == -1:
            return [xs[0], ys[0]]
        else:
            return [ys[0], xs[0]]

    new = []

    i = 0
    j = 0

    while (i < len(xs)) and (j < len(ys)):
        if cmp(xs[i], ys[j]) == -1:
            new.append(xs[i])
            i += 1
        elif cmp(ys[j], xs[i]) == -1:
            new.append(ys[j])
            j += 1
        else:
            new.append(xs[i])
            new.append(ys[j])
            i += 1
            j += 1

    if len(xs[i:]) > 0:
        new = new + xs[i:]
    elif len(ys[j:]) > 0:
        new = new + ys[j:]

    return new


def merge_sorted(xs, cmp=cmp_standard):
    '''
    Merge sort is the standard O(n log n) sorting algorithm.
    Recall that the merge sort pseudo code is:

        if xs has 1 element
            it is sorted, so return xs
        else
            divide the list into two halves left,right
            sort the left
            sort the right
            merge the two sorted halves

    You should return a sorted version of the input list xs.
    You should not modify the input list xs in any way.
    '''

    import copy

    xs_2 = copy.deepcopy(xs)

    if len(xs_2) <= 1:
        return xs_2

    else:
        mid = len(xs_2) // 2
        lefthalf = xs_2[:mid]
        righthalf = xs_2[mid:]

    return _merged(merge_sorted(lefthalf, cmp),
                   merge_sorted(righthalf, cmp), cmp)


def quick_sorted(xs, cmp=cmp_standard):
    '''
    Quicksort is like mergesort,
    but it uses a different strategy to split the list.
    Instead of splitting the list down the middle,
    a "pivot" value is randomly selected,

    The pseudocode is:

        if xs has 1 element
            it is sorted, so return xs
        else
            select a pivot value p
            put all the values less than p in a list
            put all the values greater than p in a list
            put all the values equal to p in a list
            sort the greater/less than lists recursively

    You should return a sorted version of the input list xs.
    You should not modify the input list xs in any way.
    '''

    import copy

    xs_2 = copy.deepcopy(xs)

    if len(xs) <= 1:
        return xs

    else:
        rnum = random.choice(xs_2)

        less = [x for x in xs_2 if x < rnum]
        greater = [x for x in xs_2 if x > rnum]
        eq = [x for x in xs_2 if x == rnum]

        if cmp == cmp_standard:
            return quick_sorted(less, cmp) + eq + quick_sorted(greater, cmp)
        else:
            return quick_sorted(greater, cmp) + eq + quick_sorted(less, cmp)


def _partition(xs, lo, hi, cmp):
    pivot = lo
    for i in range(lo + 1, hi + 1):
        if xs[i] <= xs[lo]:
            pivot += 1
            xs[i], xs[pivot] = xs[pivot], xs[i]
    xs[pivot], xs[lo] = xs[lo], xs[pivot]

    return pivot


def _helper(xs, lo, hi, cmp):
    if lo >= hi:
        return xs
    pivot = _partition(xs, lo, hi, cmp)
    _helper(xs, lo, pivot - 1, cmp)
    _helper(xs, pivot + 1, hi, cmp)

    return xs


def quick_sort(xs, cmp=cmp_standard):

    def all_same(items):
        return all(x == items[0] for x in items)

    if all_same(xs):
        return xs

    if len(xs) <= 1:
        return xs

    if len(xs) == 2:
        if xs[0] < xs[1]:
            if cmp == cmp_standard:
                return xs
            else:
                xs.extend(xs[::-1])
                a = len(xs)
                while len(xs) > a // 2:
                    xs.pop(0)
                return xs

        else:
            if cmp == cmp_standard:
                xs.extend(xs[::-1])
                a = len(xs)
                while len(xs) > a // 2:
                    xs.pop(0)
                return xs
            else:
                return xs

    lo = 0
    hi = len(xs) - 1
    if cmp == cmp_standard:
        a = _helper(xs, lo, hi, cmp)
        xs.extend(a)
        mid = len(a) // 2
        a = a[mid:]
        while len(xs) > len(a):
            xs.pop(0)
        return a
    else:
        a = _helper(xs, lo, hi, cmp)[::-1]
        xs.extend(a)
        print(xs)
        print(a)
        if len(xs) == len(a):
            mid = len(a) // 2
            a = a[mid:]
        while len(xs) > len(a):
            xs.pop(0)
        return a
