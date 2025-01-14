def calculate_average(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if not numbers:
        return 0
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("List elements must be numbers.")
    return sum(numbers) / len(numbers)

#Example Usage
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

# Example of error handling
try:
    bad_input = [1,2,"a",4]
    average_bad = calculate_average(bad_input)
    print(f"The average is {average_bad}")
except ValueError as e:
    print(f"Error: {e}")

try:
    bad_input = 123
    average_bad = calculate_average(bad_input)
    print(f"The average is {average_bad}")
except TypeError as e:
    print(f"Error: {e}")
