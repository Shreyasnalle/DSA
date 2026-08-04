def print_pattern(n) :
    for i in range(1, n+1) :
        for j in range(1, i+1) :
            print(j, end = "")
        space = 2 * (n - i)
        for k in range(space) :
            print(" ", end = "")
        for j in range(i, 0, -1) :
            print(j, end = "")
        print()
n = 5
print_pattern(n)