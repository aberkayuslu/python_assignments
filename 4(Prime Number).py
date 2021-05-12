prime = int(input("Enter a random number: "))
count = 0
for i in range(1, prime+1) :
    if not prime % i :
        count += 1
if (prime == 0) or (prime == 1) or (count >= 3) :
    print(prime, "is not a prime number.")
else :
    print(prime, "is a prime number.")