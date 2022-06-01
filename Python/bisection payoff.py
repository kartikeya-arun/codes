balance=float(input("Enter balance :\t"))
annualInterestRate=float(input("Enter annualInterestRate :\t"))
mir=annualInterestRate/12
preBalance=balance
mlower=balance/12
mupper=(balance*(1+mir)**12)/12
pi=0.01
mmp=float(mlower+mupper)/2.0
while abs(0-preBalance)>=pi:
    preBalance=balance
    
    for i in range(12):
        preBalance=round(((preBalance-mmp)*(1+mir)),2)
    if preBalance>=0:
        mlower=mmp
    else:
        mupper=mmp
    mmp=mmp=(mlower+mupper)/2.0
print("lowest Monthly payment\n")
print("'"*50,"\n")
print(round(mmp,2))
