balance = float(raw_input("Your balance today: " ))
annualInterestRate = float(raw_input("Annual Interest Rate: " ))
monthlyPaymentRate = float(raw_input("Your monthly payment rate (as a fraction of your debt): " ))

month = 0
totalpaid = 0
round(totalpaid, 2)
minimumpayment = 0
round(minimumpayment, 2)
for int in range(12):
    if month != 12:
        month += 1
        print ("Month: " + str(month))
        minimumpayment = balance * monthlyPaymentRate
        balance = balance - minimumpayment
        print ("Minimum monthly payment: " + str(minimumpayment))
        balance = balance * (1 + (annualInterestRate/12))
        print ("Remaining balance: " + str(balance))
        totalpaid += minimumpayment
print ("Total paid: " + str(totalpaid))
print ("Remaining balance: " + str(balance))
