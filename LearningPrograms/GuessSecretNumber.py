secret_number = 10
guess_number = 0
count = 0
while(True):
    while(count < 3):
        guess_number = eval(input("Guess the number"))
        if(guess_number < secret_number):
            print("Enter number is less than the secret number")
        elif(guess_number > secret_number):
            print("Enter number is greater than the secret number")
        else:
            print("Your guess is RIGHT!!!")
            break
        count = count + 1
    if(count == 3):
        print("Resetting")
        secret_number = secret_number + 1
        count = 0
    else:
        break