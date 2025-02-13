#task_1
name = input("Enter your name: ")
birtYear = int(input("Enter your year of birth: "))
age = 2025-birtYear
print(f"{name}, you are {age} years old!")

#task_2
txt = "LMaasleitbtui"
print("Car names: ", txt[1::2], txt[0::2])

#task_3
str = input("Enter a string:")
print(len(str))
print(str.upper())
print(str.lower())

#task_4
str = input("Enter a string:")
if str==str[::-1]:
    print("String is palindrome")
else:
    print("String is not palindrome")

#task_5
str = input("Enter a string:").lower()
vowels = "aeiou"
v=sum(str.count(v) for v in vowels)
c=len(str)-v
print(f"Number of vowels is {v}, and consonants is {c}")

#task_6
str1 = input("Enter first string: ")
str2 = input("Enter second string:" )
if (str2 in str1):
    print("first string contains the second ")
else:
    print("first string doesnt contain the second")

#task_7
s = input("Input sentence: ")
r = input("Replace:")
w = input("With:")
sep = s.split()
for i in range(len(sep)):
    if sep[i]==r:
        sep[i]=w
print("Output: " + " ".join(sep))

#task_8
s = input("Enter a string: " )
print(s[0],s[-1])

#task_9
s = input("Enter a string:")
print(s[::-1])

#task_10
s = input("Enter a sentence: ")
print(len(s.split()))

#task_11
str = input("Enter a string:")
digits = "01234556789"
count = 0
for c in str:
    for d in digits:
        if c==d:
            count+=1
if count>0:
    print("String contains digits")
else:
    print("String doesnt contain digits")

#task_12
str = input("Enter words:" ).split()
print(",".join(str))

#task_13
str = input("Enter a string: " )
print(str.replace(" ",""))

#task_14
str1 = input("Enter first string:")
str2 = input("Enter second string:")
if (str1==str2):
    print("They are equal")
else:
    print("They are not equal")

#task_15
str = input("Input: ")
sep = str.split()
acr = ""
for c in sep:
    acr +=c[0].upper()
print(acr)

#task_16
str = input("Enter a string:")
char = input("Enter a character:")
print(str.replace(char,""))

#task_17
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
newStr = ""
for char in string:
    if char in vowels:
        newStr += "*"
    else:
        newStr += char
print(newStr)

#task_18
str = input("Input:")
print("Starts with: " + str.split()[0])
print("Ends with: " + str.split()[-1])
