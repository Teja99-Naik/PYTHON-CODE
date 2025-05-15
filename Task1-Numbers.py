
# 1. Format numbers using the format function
def format_args(a, b):
    result = "{} {}".format(a, b)
    print("Formatted Result:", result)

format_args(145, 'o')

# 2. Area of a circular pond and total water in it
radius = 84
pi = 3.14
area = pi * radius * radius
print("Area of the pond:", int(area))  # No decimal point

# Bonus: Water in pond
water_per_sq_meter = 1.4
total_water = int(area * water_per_sq_meter)
print("Total water in pond:", total_water)

# 3. Calculate speed in m/s
distance = 490
time_minutes = 7
time_seconds = time_minutes * 60
speed = int(distance / time_seconds)
print("Speed in meters/second:", speed)