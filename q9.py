#number is power of 2
num = int(input("Enter a number: "))

if num <= 0:
    print(num, "is NOT a power of 2")
else:
    while num % 2 == 0:
        num = num // 2
    if num == 1:
        print("It is a power of 2")
    else:
        print("It is NOT a power of 2")
