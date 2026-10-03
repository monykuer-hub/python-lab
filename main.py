from util import square, is_even

user_input = float(input("Enter the number: "))

num_squared = square(user_input) 
is_number_even = is_even(user_input)

print(f"The square of {user_input} is {num_squared}")

print(f"The number is even: {is_number_even}")
