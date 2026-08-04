def digit_in_number(number) :
    total_no_digit = 0
    while (number > 0) :
        last_digit = number % 10
        total_no_digit += 1
        number = number // 10
    print(total_no_digit)
number = 579
digit_in_number(number)

a = 12 
print(a)
a = "shreyas"
print(a)