print("Please think of a number between 0 and 100!")
hi = str("h")
lo = str("l")
corr = str("c")
low = 0
high = 100
guess =(high + low)/2
print ("Is your secret number " + str(guess) + "?")
x = (raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
while x != corr:
    if x == hi:
        high = guess
        guess =(high + low)/2
        print ("Is your secret number " + str(guess) + "?")
        x = (raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
    elif x == lo:
        low = guess
        guess =(high + low)/2
        print ("Is your secret number " + str(guess) + "?")
        x = (raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
    else:
        print ("Sorry, i did not understand your input")
        print ("Is your secret number " + str(guess) + "?")
        x = (raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
print ("Game over. Your secret number is: " +str(guess))
