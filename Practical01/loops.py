"""
Task a
"""
# # Count in 10s from 0 to 100
# for i in range(0, 101, 10):
#     print(i, end=' ')
# print()  # To move to the next line


"""
Task b
"""
# # Count down from 20 to 1
# for i in range(20, 0, -1):
#     print(i, end=' ')
# print()  # To move to the next line


"""
Part c
"""
# Print n stars on one line
# n = int(input("Enter the number of stars: "))
# for i in range(n):
#     print('*', end='')
# print()  # To move to the next line


"""
Part d
"""
# Print n lines of increasing stars
n = int(input("Enter the number of stars: "))
for i in range(1, n + 1):
   print('*' * i)  # Print i stars on the i-th line
