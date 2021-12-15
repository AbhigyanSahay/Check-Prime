# Check Prime Program
# This program can check whether a number is a prime number or not

print("Welcome to the Check Prime program.")
print("This program can check whether a number is a prime number or not.\n")


def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

print("Enter the number:")
num = int(input())

check_prime = is_prime(num)

if check_prime:
    print(f"{num} is a Prime Number.")

else:
    print(f"{num} is not a Prime Number i.e. it is a Composite Number.")
