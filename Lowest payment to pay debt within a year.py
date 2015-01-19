balance = float(raw_input("Your balance today: " ))
annualInterestRate = float(raw_input("Annual Interest Rate: " ))
monthlyInterestRate = annualInterestRate / 12
low = (balance / 12)
high = (balance * (1 + monthlyInterestRate)**12) / 12.0
payment = (high+low)/2
remain = balance
epsilon = 0.001
while (remain >= epsilon):
    payment = (high+low)/2
    for i in range (12):
        Balance1 = remain-payment
        monthInterest = Balance1*(annualInterestRate/12)
        remain = Balance1+monthInterest
    if (remain < 0): 
        high = payment
        remain = balance
    elif (remain > epsilon):
        low = payment
        remain = balance
print "Lowest Payment: %.2f" % (payment)
