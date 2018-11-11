l1 = [1,2,3,'a','b',3.14,6,'c']
int_list = []
str_list = []
float_list = []
main_list = []
for idx in l1:
    if(isinstance(idx, int)):
        int_list.append(idx)
    elif(isinstance(idx,str)):
        str_list.append(idx)
    elif(isinstance(idx,float)):
        float_list.append(idx)
main_list.extend(int_list)
main_list.extend(str_list)
main_list.extend(float_list)
print(main_list)