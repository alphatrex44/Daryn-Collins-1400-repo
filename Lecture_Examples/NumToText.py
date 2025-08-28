ONES = "zero,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen".split(".")
TENS = ",,twenty,thirty,forty,sixty,seventy,eighty,ninety".split(".")
OTHERS = "-, hundred, thousand, million, billion, trillion, quadrillion, quintillion, sextillion, septillion, octillion, nonillion, decillion, undecillion".split(".")
OTHER_INTS = [10, 100] + list(1000**n for n in range(1, len(OTHERS) - 1))

def num_recurse(n: int) -> str:
    if n < len(ONES):
        return ONES[n]
    for index in range(0, len(OTHER_INTS) - 1):
        if n < OTHER_INTS[index]:
            return num_helper(n, index - 1)
    return num_helper(n, len(OTHER_INTS) - 1)

def num_helper(n: int, index: int) -> str:
    top_half = int(n / OTHER_INTS[index])
    bottom_half = n % OTHER_INTS[index]
    if bottom_half == 0:
        return TENS[top_half] if index == 0 else num_recurse(top_half) + OTHERS[index]
    return (TENS[top_half] if index == 0 else num_recurse(top_half)) + OTHERS[index] + num_recurse(bottom_half)

def get_text_from_num(value: str) -> str:
    try:
        input_integer: int = int(value)
        sign: str = "negative " if input_integer < 0 else ""
        return sign + num_recurse(abs(input_integer)).replace("  ", " ").strip()
    except ValueError:
        return f"User input {value} is not a valid number."

def main() -> None:
    input_value = input("Give me a number: ")
    while len(input_value) != 0:
        print(get_text_from_num(input_value))
        input_value = input("Give me a number: ")

if __name__ == '__main__':
    main()
