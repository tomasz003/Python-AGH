def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

n=int(input("Please type in a number: "))

while n>0:
    print(f"The factorial of the number {n} is {factorial(n)}")
    n = int(input("Please type in a number: "))

print("Thanks and bye!")