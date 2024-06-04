Q1

# Number of rows for the pattern
rows = 5

# Loop to iterate over each row
for i in range(1, rows + 1):
    # Loop to print stars for each row
    for j in range(1, i + 1):
        print("*", end="")
    print()

# Loop to iterate over each row in reverse order
for i in range(rows - 1, 0, -1):
    # Loop to print stars for each row in reverse order
    for j in range(1, i + 1):
        print("*", end="")
    print()

Q2

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Loop through the list using a range starting from index 1 (the second element)
# with a step of 2 to access only the odd-indexed elements
for i in range(1, len(my_list), 2):
    print(my_list[i])

Q3

x = [23, 'Python', 23.98]
types_list = []

for item in x:
    types_list.append(type(item))

print(x)
print(types_list)

Q4

def unique_list(input_list):
    unique_items = []
    for item in input_list:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items

# Sample List
sample_list = [1, 2, 3, 3, 3, 3, 4, 5]

# Get unique list
unique_result = unique_list(sample_list)

print("Sample List:", sample_list)
print("Unique List:", unique_result)

Q5

def count_case_characters(input_string):
    upper_count = 0
    lower_count = 0
    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

# Input string
input_string = 'The quick Brow Fox'

# Calculate counts
upper_count, lower_count = count_case_characters(input_string)

# Print results
print("Input String:", input_string)
print("No. of Upper-case characters:", upper_count)
print("No. of Lower-case Characters:", lower_count)

