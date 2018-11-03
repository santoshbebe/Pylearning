num = eval(input("Enter the number"))
multiplier = eval(input("Enter the multiplier"))
if not (num < 50 and num%multiplier ==0):
    print("the num ", num, "is a multiple of number", multiplier)
else:
    print("the num ", num, "is not a multiple of number", multiplier, "or the number is greater than 50")

