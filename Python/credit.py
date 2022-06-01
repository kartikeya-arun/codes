def remBalance(balance,annualInterestRate,monthlyPaymentRate):
    mir=annualInterestRate/12
    for i in range(12):
        mmp=monthlyPaymentRate*balance
        mub=balance-mmp
        balance=mub+mir*mub
        print("Month",i+1,"remaining Balance:",round(balance,2))
    return round(balance,2)
#
balance=float(input("Enter balance :\t"))
annualInterestRate=float(input("Enter annualInterestRate :\t"))
monthlyPaymentRate=float(input("Enter monthlyPaymentRate :\t"))
print(remBalance(balance,annualInterestRate,monthlyPaymentRate))
