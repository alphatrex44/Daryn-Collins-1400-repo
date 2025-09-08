import math




def odd_or_even(number: int) -> str:
    if  number % 2 == 0:
        return("Even")
    else:
        return("Odd")

def count_the_digits(number: int) -> int:
    independent_number = abs(number)
    return len(str((independent_number)))

def make_prime_list(number: int) -> list:
    known_primes = [2]
    candidate = known_primes[-1]+1
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
        return(known_primes)

def is_prime(number: int) -> bool:
    known_primes = make_prime_list(number)
    if number >= 2:
        for prime in known_primes:
            if number % prime == 0:
                return(False)
        return(True)
    else:
        return(False)
def next_prime(number: int) -> int:
    known_primes = make_prime_list(number)
    independent_number = number
    if number >= 2:
        while True:
            is_number_prime = True
            for prime in known_primes:
                if independent_number % prime == 0:
                    is_number_prime = False
                    break

            if is_number_prime:
                return independent_number
            independent_number += 1
        else:
            return 2

def this_many_primes(number: int) -> list:
    known_primes = make_prime_list(number*number)
    prime_count = []
    if number >= 2:
        for prime in known_primes:
            if len(prime_count) < number:
                prime_count.append(prime)
            else:
                return prime_count
    else:
        return None
def main() -> None:
    while True:
        try:
            number = int(input("Give a number please: "))
            break
        except ValueError:
            print("Not a valid number!")
    print(odd_or_even(number))
    print(count_the_digits(number))
    print(is_prime(number))
    print(next_prime(number))
    print(make_prime_list(number))
    print(this_many_primes(number))
if __name__ == "__main__":
    main()