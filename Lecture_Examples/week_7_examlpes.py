def main() -> None:
    a: bool = True
    b: bool = False
    c: bool = False

    result: str = "1" if not a else ("2" if not b else("3" if not c else "4"))
    print(result)
if __name__ == "__main__":
    main()