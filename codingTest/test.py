from collections import deque

# Example deque
i_deque = deque([1, 3, 5, 7, 9])

# Finding the maximum value
best = max(i_deque)

# Example if statement using 'best'
if best > 5:
    print(f"The maximum value {best} is greater than 5.")
else:
    print(f"The maximum value {best} is not greater than 5.")
