#1)
# Ask the user to enter height and weight
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate BMI using the formula
bmi = weight / (height ** 2)

# Determine the category based on BMI value
if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")
    
    
    
    
    #2)
    # List of cities grouped by country
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# Ask the user to enter a city name
city = input("Enter a city name: ")

# Check which country the city belongs to
if city in australia:
    print(f"{city} is in Australia")
elif city in uae:
    print(f"{city} is in UAE")
elif city in india:
    print(f"{city} is in India")
else:
    print(f"Sorry, I don't know which country {city} belongs to.")
    
    
    
    #3)
    # Define city lists for each country again
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# Ask the user to enter two cities
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

# Check if both cities are in the same country
if city1 in india and city2 in india:
    print("Both cities are in India")
elif city1 in uae and city2 in uae:
    print("Both cities are in UAE")
elif city1 in australia and city2 in australia:
    print("Both cities are in Australia")
else:
    print("They don't belong to the same country")