#i'm a bad kid  because i used ai to make my assignment 1 more efficient and less repetitive but it functions the same
def how_many_coins(coin_name: str) -> int:
    while True:
        try:
            return int(input(f"How many {coin_name} do you have?: "))
        except ValueError:
            print("That is not a whole digit!")

def main() -> None:
    username = input("Please give your name: ").capitalize()

    coin_names = ["pennies", "nickels", "dimes", "quarters"]
    coin_values = [1, 5, 10, 25]
    coin_counts = []

    for name in coin_names:
        coin_counts.append(how_many_coins(name))

    total_cents = sum(count * value for count, value in zip(coin_counts, coin_values))
    change = total_cents / 100

    print(f"Hello {username}, you have ${change:.2f} in change.")

if __name__ == "__main__":
    main()
