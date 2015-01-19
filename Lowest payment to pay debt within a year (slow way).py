balance = float(raw_input("Your balance today: " ))
annualInterestRate = float(raw_input("Annual Interest Rate: " ))
payment = 0
monthlyInterestRate = annualInterestRate /12
balance1 = balance
month = 0

while balance1 > 0:
    payment += 10
    balance1 = balance

    for month in range(12):
        balance1 -= payment
        balance1 += monthlyInterestRate * balance1
        month += 1
print " Lowest Payment:", payment
