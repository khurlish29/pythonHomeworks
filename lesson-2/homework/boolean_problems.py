#task_1
userName = input("Enter a username: ")
password = input("Enter a password: ")
print(userName!="" and password!="")

#task_2
n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
if (n1==n2):
    print("They are equal")

#task_3
n = int(input("Number:"))
if (n>=0 and n%2==0):
    print("Number is positive and even")

#task_4
a,b,c=input().split()
if (a!=b and b!=c and a!=c):
    print("they are different")

#task_5
str1=input("String 1: ")
str2 = input("String 2:")
if (len(str1)==len(str2)):
    print("they have the same length")

#task_6
n=int(input("Number:"))
if (n%3==0 and n%5==0):
    print("number is divisible by both 3 and 5")

#task_7
n1=int(input())
n2=int(input())
if (n1+n2>50):
    print("their sum is greater than 50")

#task_8
n=int(input())
if (n>=10 and n<=20):
    print("this number is in the range")
