known_primes = [2]
candidate = known_primes[-1] + 1

number = 600851475143
if number >= 2:
    while candidate < number:
        is_prime = False
        candidate_limit = math.sqrt(candidate)
        for prime in known_primes:
            if prime > candidate_limit:
                is_prime = True
                break
            if candidate % prime == 0:
                break

        if is_prime:
            known_primes.append(candidate)

        candidate += 1
    return(known_primes)
else:
    known_primes = []
    return("None")

number = int(input("give number"))
make_prime_list(number)

for i in reversed(known_primes):
    if number % i == 0:
        print(i)
        break
