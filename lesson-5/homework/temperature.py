def convert_cel_to_far(celsius):
    return (celsius*9/5+32)
def convert_far_to_cel(fahrenheit):
    return (fahrenheit-32)*5/9
fahrenheit = float(input("Enter a temperature in degrees F: "))
print(f"{fahrenheit} degrees F = {convert_far_to_cel(fahrenheit):.2f} degrees C")

celsius = float(input("Enter a temperature in degrees C: "))
print(f"{celsius} degrees C = {convert_cel_to_far(celsius):.2f} degrees F")
