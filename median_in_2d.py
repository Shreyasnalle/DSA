def upper_bound(arr: list[int], x: int, n: int) -> int:
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def count_small_equal(matrix: list[list[int]], n: int, m: int, x: int) -> int:
    cnt = 0
    for i in range(n):
        cnt += upper_bound(matrix[i], x, m)
    return cnt

def median(matrix: list[list[int]], n: int, m: int) -> int:
    low = min(row[0] for row in matrix)
    high = max(row[m - 1] for row in matrix)
    req = (n * m) // 2
    while low <= high:
        mid = (low + high) // 2
        small_equal = count_small_equal(matrix, n, m, mid)
        if small_equal <= req:
            low = mid + 1
        else:
            high = mid - 1
    return low