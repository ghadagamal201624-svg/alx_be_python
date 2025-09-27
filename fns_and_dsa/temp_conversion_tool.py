FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius
def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit
def main():
    print ("Temperature Conversion Tool")
temp_input = input("enter the temperature to convert:")
temprature = float(temp_input)
unit = input("is this in Celsius or Fahrenheit? (C/F):").strip().upper()
if unit == "C":
    converted = convert_to_fahrenheit(temprature)
    print(f"{temprature}°C is {converted:.2f}°F")
elif unit == "F":
    converted = convert_to_celsius(temprature)
    print(f"{temprature}°F is {converted:.2f}°C")
else:
    print("Error: Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
if __name__ == "__main__":
    main()    