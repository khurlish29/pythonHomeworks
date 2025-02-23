def check(func):
    def wrapper(a,b):
        if b==0:
            return "Denominator can't be zero"
        return func(a,b)
    return wrapper

@check
def div(a,b):
    return a/b

a,b = map(int,input("Enter the values: ").split())
print(div(a,b))