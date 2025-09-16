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
        return("None")

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
    if number <= 0:
        return []

    known_primes = make_prime_list(max(2, number * number))  # ✅ ensures input is at least 2
    prime_count = []

    for prime in known_primes:
        if len(prime_count) < number:
            prime_count.append(prime)
        else:
            break

    return prime_count

def main() -> None:
    print("Welcome to my calculator.")
    while True:
        while True:
            option = input("If you would like to determine even or odd, press 1 \nIf you would like to count the digits, press 2 \nIf you would like a list of primes up to your number, press 3 \nIf you would like to determine whether your number is a prime, press 4 \nIf you would like to find the prime after or including your number, press 5 \nIf you would like that amount of primes press 6 \n")
            if option == "1" or option == "2" or option == "3" or option == "4" or option == "5" or option == "6" or option == "":
                break
            else:
                print("Not a valid option!")
        if option == "":
            break
        while True:
            try:
                number = int(input("Give a number please for your operation: "))
                break
            except ValueError:
                print("Not a valid number!")
        if option == "1":
            print(odd_or_even(number))
        if option == "2":
            print(count_the_digits(number))
        if option == "3":
            print(is_prime(number))
        if option == "4":
            print(next_prime(number))
        if option == "5":
            print(make_prime_list(number))
        if option == "6":
            print(this_many_primes(number))

if __name__ == "__main__":
    main()