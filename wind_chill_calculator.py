# Wind Chill Calculator
# Calculates wind chill for wind speeds 5 to 60 mph at a user-specified temperature

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9/5 + 32

def calculate_wind_chill(temp_f, speed):
    """Calculate wind chill in Fahrenheit for given temp and wind speed."""
    return 35.74 + 0.6215 * temp_f - 35.75 * (speed ** 0.16) + 0.4275 * temp_f * (speed ** 0.16)

# Get user input
temp = float(input("What is the temperature? "))
unit = input("Fahrenheit or Celsius (F/C)? ").strip().upper()

if unit == "C": 
    temp_f = celsius_to_fahrenheit(temp)
else:
    temp_f = temp

for speed in range(5, 65, 5):
    wind_chill = calculate_wind_chill(temp_f, speed)
    print(f"At temperature {temp_f:.1f}F, and wind speed {speed} mph, the windchill is: {wind_chill:.2f}F")
