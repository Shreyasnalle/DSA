def nth_root(self, num) -> float :
    if num < 2 :
        return 1
    low = 1 
    high = num
    mid = (low + high) // 2
    