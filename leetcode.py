from basic_data_structures import *

#nums - array of numbers
#target - number
#return [i, j] such that nums[i] + nums[j] = target
def leetcode1(nums, target):
    res = []
    for i, num in enumerate(nums):
        if target / 2 == num:
            res.append(i)

    if len(res) >= 2:
        return res

    res = []
    d = {}
    for i, num in enumerate(nums):
        d[num] = i

    for i, num in enumerate(nums):
        if target - num in d and d[target - num] != i:
            res = [i, d[target - num]]

    return res

#list1 and list2 are list of digits that each represent an integer.
#i.e. 1->7->6 represent 671 and 2->5 represent 52
#return list that represent thier sum, i.e 3->2->7
def leetcode2(list1, list2):
    p = list1.head
    q = list2.head
    res = List()
    extra = 0
    while p is not None and q is not None:
        num = p.val + q.val + extra
        if num >= 10:
            extra = 1
            digit = num - 10
        else:
            extra = 0
            digit = num

        res.insert_to_tail(digit)
        p = p.next
        q = q.next

    while p is not None:
        num = p.val + extra
        if num >= 10:
            extra = 1
            digit = num - 10
        else:
            extra = 0
            digit = num

        res.insert_to_tail(digit)
        p = p.next

    while q is not None:
        num = q.val + extra
        if num >= 10:
            extra = 1
            digit = num - 10
        else:
            extra = 0
            digit = num

        res.insert_to_tail(digit)
        q = q.next

    if extra == 1:
        res.insert_to_tail(1)

    return res

#s is a string
#return the longest substring without repeating characters
def leetcode3(s):
    curr_start, curr_end = 0, 0
    best_start, best_end = 0, 0
    char_used = {}
    while curr_end < len(s):
        if not s[curr_end] in char_used:
            char_used[s[curr_end]] = None
            curr_end += 1
        else:
            if curr_end - curr_start > best_end - best_start:
                best_start, best_end = curr_start, curr_end

            char_used = {}
            curr_start = curr_end

    if curr_end - curr_start > best_end - best_start:
        best_start, best_end = curr_start, curr_end

    return s[best_start: best_end]

#arr1, arr2 are sorted arrays of numbers
#return the median of the all numbers in arr1 and arr2
def leetcode4(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    k = (n + m) // 2
    which_arr = 0
    i, j = 0, 0
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            i += 1
            which_arr = 1
        else:
            j += 1
            which_arr = 2

        if k == i + j:
            if which_arr == 1:
                return arr1[i - 1]
            else:
                return arr2[j - 1]

    if i == n:
        return arr2[k - n - 1]
    else:
        return arr1[k - m - 1]

#s is a string
#return the longest palindrom in s
def leetcode5(s):
    if s == '':
        return ''

    n = len(s)
    is_pal = np.empty((n, n), dtype=np.bool_)
    for i in range(n):
        is_pal[i, i] = True

    for i in range(n - 1):
        is_pal[i, i + 1] = s[i] == s[i + 1]

    for j in range(2, n):
        for i in range(j - 1):
            is_pal[i, j] = is_pal[i + 1, j - 1] and s[i] == s[j]

    longest_pal = s[0]
    len_longest_pal = 1
    for i in range(n):
        for j in range(i, n):
            if is_pal[i, j] and j - i + 1 > len_longest_pal:
                longest_pal = s[i: j + 1]
                len_longest_pal = j - i + 1

    return longest_pal
