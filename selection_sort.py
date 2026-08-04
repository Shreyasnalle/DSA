n = int(input("Enter the number of elements to be present in the array : "))
unsorted_array = []
for i in range(n) :
    num = int(input(f"Enter the {i+1} number :"))
    unsorted_array.append(num)
print(f"The unsorted array is: {unsorted_array}")
for i in range(len(unsorted_array)) :
    minimum = unsorted_array[i]
    for j in range(1, len(unsorted_array)) :
        if minimum > unsorted_array[j] :
            minimum = unsorted_array[j]
            unsorted_array[j] = unsorted_array[i]
            unsorted_array[i] = minimum
print(unsorted_array)
