import math

# Read inputs
n, r = map(float, input().split())
n = int(n)
x1, y1 = map(float, input().split())

# Initialize variables
x_prev, y_prev = x1, y1
total_distance = 0

# Iterate through the points
for i in range(n - 1):
    # Read next point
    x, y = map(float, input().split())

    # Calculate distance between consecutive points
    dx = x - x_prev
    dy = y - y_prev
    total_distance += math.sqrt(dx ** 2 + dy ** 2)

    # Update previous point
    x_prev, y_prev = x, y

# Add distance from last point to the starting point
dx = x - x1
dy = y - y1
total_distance += math.sqrt(dx ** 2 + dy ** 2)

# Add circumference of the circle
total_distance += 2 * math.pi * r

# Output the total distance with 2 decimal places
print(round(total_distance, 2))