# Initial list
numbers = [3, 1, 4, 1, 5, 9, 2]


# Predictions


# numbers[0]    # Should return 3 (first element)
# numbers[-1]   # Should return 2 (last element)
# numbers[3]    # Should return 1 (fourth element, index 3)
# numbers[:-1]  # Should return [3, 1, 4, 1, 5, 9] (all except the last element)
# numbers[3:4]  # Should return [1] (slice from index 3 up to, but not including, index 4)
# 5 in numbers  # Should return True (5 is in the list)
# 7 in numbers  # Should return False (7 is not in the list)
# "3" in numbers # Should return False ("3" is a string, but the list has integer 3)
# numbers + [6, 5, 3]  # Should return [3, 1, 4, 1, 5, 9, 2, 6, 5, 3] (concatenating lists)


# Verifying predictions
print(numbers[0])      # Output: 3
print(numbers[-1])     # Output: 2
print(numbers[3])      # Output: 1
print(numbers[:-1])    # Output: [3, 1, 4, 1, 5, 9]
print(numbers[3:4])    # Output: [1]
print(5 in numbers)    # Output: True
print(7 in numbers)    # Output: False
print("3" in numbers)  # Output: False
print(numbers + [6, 5, 3])  # Output: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]


# Modifications


# Change the first element to "ten"
numbers[0] = "ten"


# Change the last element to 1
numbers[-1] = 1


# Print all elements except the first two
print(numbers[2:])


# Check if 9 is in the list
print(9 in numbers)

