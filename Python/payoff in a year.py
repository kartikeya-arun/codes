balance=float(input("Enter balance :\t"))
annualInterestRate=float(input("Enter annualInterestRate :\t"))
mir=annualInterestRate/12
mmp=0
preBalance=balance
while balance>0:
    mmp+=10
    balance=preBalance
    for i in range(12):
        mub=balance-mmp
        balance=mub+mir*mub       
print("lowest Monthly payment\n")
print("'"*50,"\n")
print(mmp)
