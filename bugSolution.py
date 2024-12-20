def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    return sum(numeric_numbers) / len(numeric_numbers)

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_mixed_list = [1, 2, 'a', 4, 5]
average_mixed = calculate_average(my_mixed_list)
print(f"The average of a mixed list is: {average_mixed}")

my_list_with_strings = ['a','b','c']
average_string = calculate_average(my_list_with_strings)
print(f"The average of a list with only string is: {average_string}"