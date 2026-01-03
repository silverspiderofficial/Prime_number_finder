print("=" * 40)
print(">> HI, THIS IS A Prime number finder.")
print("=" * 40)
def is_prime_simple():
    num = int(input("enter your number:  "))

    if num <= 1:
        print(f"{num} is not prime")
    else:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            print(f"{num} is_prime")
        else:
            print(f"{num} is not_prime")
is_prime_simple()