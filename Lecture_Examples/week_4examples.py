import math

#this is ai just to test my idea ill make the code myself for the assignment
# Step 1: Start with the first 10 known primes
known_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Step 2: Begin checking numbers starting after the 10th prime
candidate = known_primes[-1] + 1

# Step 3: Loop until we have 100 primes
while len(known_primes) < 100:
    is_prime = True
    limit = math.isqrt(candidate) + 1

    for prime in known_primes:
        if prime > limit:
            break
        if candidate % prime == 0:
            is_prime = False
            break

    if is_prime:
        known_primes.append(candidate)

    candidate += 1

# Step 4: Ask user for a number and check primality
number = int(input("Give a number: "))

if number <= known_primes[-1]:
    if number in known_primes:
        print("prime")
    else:
        for prime in known_primes:
            if number % prime == 0:
                print(f"not prime — divisible by {prime}")
                break
else:
    limit = math.isqrt(number) + 1
    for prime in known_primes:
        if prime > limit:
            break
        if number % prime == 0:
            print(f"not prime — divisible by {prime}")
            break
    else:
        print("prime")
