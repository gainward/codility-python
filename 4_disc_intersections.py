def BinSearch(a, v, l=None, r=None):
    """Binary search in sorted array a for value v.
    
    Returns smallest index where val >= v. If no such
    val exists, return None.
    """
    if not l and not r:
        l, r = 0, len(a) - 1
    while l < r:
        mid = (l + r) / 2
        if a[mid] < v:
            l = mid + 1
        else:
            r = mid
    
    if a[l] < v:
        return None
    return l


def solution(A):
    N = len(A)
    discs_r = map(lambda (i, r): i+r, enumerate(A))
    discs_r.sort()
    discs_l = map(lambda (i, r): i-r, enumerate(A))
    discs_l.sort()
    count = 0
    for i, r in enumerate(A):
        l, r = i-r, i+r
        # Find number of discs starting after r, or ending before l.
        ending_before = BinSearch(discs_r, l)
        starting_after = N - (BinSearch(discs_l, r+1) or N)
        intersect = N - ending_before - starting_after - 1
        count += intersect
        if count > 20000000:
            return -1
    return count / 2
