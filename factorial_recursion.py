def factorial_by_recursion(n):
    if n <= 1:
        return 1
    return n * factorial_by_recursion(n - 1)
result = factorial_by_recursion(5)
print(result)