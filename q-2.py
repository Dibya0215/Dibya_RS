#natural number n as inpuy
n = int(input("Enter how many numbers you want to sum: "))
i = 1
total = 0

while i <= n:
    num = int(input(f"Enter number {i}: "))
    total += num
    i += 1

print(f"The sum of {n} numbers is: {total}")
