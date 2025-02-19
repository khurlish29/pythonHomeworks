def invest(amount, rate, years):
    for i in range(1,years+1):
        amount += rate/100*amount
        print(f"year {i}: $ {amount:.2f}")

amount = float(input("Enter the initial amount:"))
rate = float(input("Enter an annual percentage:"))
years = int(input("Enter the number of years:"))

invest(amount,rate,years)