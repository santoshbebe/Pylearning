def take_input():
    var1 = eval(input("Guess the number"))
    return var1


def compare_guess_number(guess_number, secret_number):
    if (guess_number < secret_number):
        print("Enter number is less than the secret number")
        return False
    elif (guess_number > secret_number):
        print("Enter number is greater than the secret number")
        return False
    else:
        print("Your guess is RIGHT!!!")
        return True


def reset_secret_number(secret_number):
    return secret_number + 1


def main():
    secret_number = 10
    guess_number = 0
    count = 0
    while(True):
        while(count < 3):
            guess_number = take_input()
            flag = compare_guess_number(guess_number,secret_number)
            if(flag):
                break
            count = count + 1
        if(count == 3):
            print("Resetting")
            secret_number = reset_secret_number(secret_number)
            count = 0
        else:
            break

main()