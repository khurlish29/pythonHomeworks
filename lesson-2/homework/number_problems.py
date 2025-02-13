#task_1
n = float(input("Enter float number: "))
print(f"{n:.2f}")

#task_2
nums = [int(input("Enter a number: " )) for i in range(3)]
print("Largest number: " + str(max(nums)))
print("Smallest number: " + str(min(nums)))

#task_3
km = float(input("Enter the value:"))
m = km*1000
cm = km*100000
print(f"{km} km is {m} meters and {cm} centimeters.")

#task_4
a = int(input("Enter first num:" ))
b = int(input("Enter second num:" ))
if (b!=0):
    print("Integer division: " + str(a//b))
print("Remainder: " + str(a%b))

#task_5
celsius = float(input("Enter the temperature in Celcius: " ))
fahrenheit = (celsius*9/5)+32
print(f"Temperature in Fahrenheit: {fahrenheit}" )

#task_6
n = int(input("Enter a number:"))
print(f"Last digit is: {n%10}")

#task_7
n = int(input("Enter a number:" ))
if (n%2==0):
    print("Number is even")
else:
    print("Number is odd")