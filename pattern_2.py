def print_pattern(n) :
    for i in range(1, n+1) :
        ch = chr(ord("A") + i - 1)
        for j in range(1, i + 1) :
            print(ch, end = "")
        print()
n = 4
print_pattern(4)