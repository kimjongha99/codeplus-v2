n = int(input())
buildings = input().split()  # For example: "6 9 5 7 4"
result = []

for i in range(len(buildings)):
    # Check the buildings to the left of the current building
    left_buildings = buildings[:i]
    index = 0  # Default value if no taller building is found

    # Iterate in reverse to find the first taller building
    for j in range(i - 1, -1, -1):
        if buildings[j] > buildings[i]:
            index = j + 1  # Adding 1 because indices are 0-based
            break

    result.append(index)

# Output the result
print(result)