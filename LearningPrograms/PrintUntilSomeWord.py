str1 = "Attending Python Class on Saturday"
str_to_remove = "on"
#Output = "Attending Python Class Saturday"
l1 = str1.split(' ')
print(l1)
str11 = ""
if (str_to_remove in l1):
    print("Found the str to remove in sentence")
    for idx in l1:
        if(idx != str_to_remove):
            str11 = str11 + idx + " "
        else:
            break
            # continue
    print(str11)
else:
    print(str1)

