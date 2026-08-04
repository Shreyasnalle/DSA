def print_name(name, count, n) :
    if count == n :
        return
    print(name)
    print_name(name, count + 1, n)
n = int(input("Enter the number of times you want your name to be printed :"))
print_name("shreyas", 0, n)