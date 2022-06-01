balance=float(input("Enter balance :\t"))
annualInterestRate=float(input("Enter annualInterestRate :\t"))
updatedBalance = balance
monthlyInterestRate = (annualInterestRate) / 12
epsilon = 0.01

lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate)**12) / 12
ans = (upperBound + lowerBound)/2.0

while abs(0 - updatedBalance) >= epsilon:
    
    updatedBalance = balance
    
    for i in range(0, 12):
        updatedBalance = round(((updatedBalance - ans) * (1 + monthlyInterestRate)), 2)
    if  updatedBalance >= 0:
        lowerBound = ans
    else:
        upperBound = ans
    ans = (upperBound + lowerBound)/2.0

print("Lowest Payment: " + str(round(ans, 2)))

    
