from config import APP_NAME, PROMPT_NAME, PROMPT_NUMBER
from utils import celsius_to_fahrenheit, greet, is_even, square


def main():
    print(f"Welcome to {APP_NAME}!")
    name = input(PROMPT_NAME)
    number = int(input(PROMPT_NUMBER))
    parity = "even" if is_even(number) else "odd"

    print(greet(name))
    print(f"Square: {square(number)}")
    print(f"The number is {parity}.")
    print(f"Fahrenheit: {celsius_to_fahrenheit(number)}")


if __name__ == "__main__":
    main()
