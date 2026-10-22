class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even_nums = [0, 2, 4, 6, 8]
        prime_nums = [2, 3, 5, 7]
        good_count = 0
        def backtrack(index) :
            nonlocal good_count
            if index == n :
                good_count = (good_count + 1) % MOD
                return
            if index % 2 == 0 :
                for digit in even_nums :
                    backtrack(index + 1)
            else :
                for digit in prime_nums :
                    backtrack(index + 1)
        backtrack(0)
        return good_count