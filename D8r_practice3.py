n=int(input('ENTER A NUM'))

even_sum = 0
odd_sum = 0

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit
    n //= 10

if even_sum > odd_sum:
    print("Even sum is greater than Odd sum")
else:
    print("Even sum is NOT greater than Odd sum")
