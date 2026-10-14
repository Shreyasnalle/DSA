class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 :
            return 1.0
        if n > 0 :
            loop = n 
        else :
            loop = n * -1 
        answer = 1.0
        for i in range(loop) :
            answer *= x 
        if n < 0 :
            answer = 1 / answer
        return answer

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1 / x
            n = -n
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return x * half * half