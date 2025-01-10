FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
 
def convert_to_celsius(fahrenheit):
        fahrenheit = float(temp_value)
        celsius_value = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        return f'{celsius_value}°C'

def convert_to_fahrenheit(celsius):
        celsius = float(temp_value)
        fahrenheit_value = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
        return f'{fahrenheit_value}°F'




temp_value = input("Enter the temperature to convert: ")
temp_mesurment =input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
temp_value = float(temp_value)
    
if temp_mesurment == "F":
    result = convert_to_celsius(temp_value)
    print(f"{temp_value}°F is {result}")
elif temp_mesurment == "C":
    result = convert_to_fahrenheit(temp_value)
    print(f"{temp_value}°C is {result}")
else:
    print("Invalid temperature. Please enter a numeric value.")