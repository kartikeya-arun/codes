previous_balance = balance
monthly_interest_rate = annualInterestRate/12.0
minMonthlyPayment = 0

while(balance >= 0):
    minMonthlyPayment += 10
    balance = previous_balance
    #Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    monthlyUnpaidBalance = 0

    for month in range(1,13):
        #Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
        monthlyUnpaidBalance = balance - minMonthlyPayment
        #Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
        balance = monthlyUnpaidBalance + (monthly_interest_rate * monthlyUnpaidBalance)

print(minMonthlyPayment)
