#remove vowels from the sentence
str1 = "This is a mad race"
# vowels = ['a','e','i','o','u']
vowels = "aeiou"
for idx in vowels:
   if idx in str1:
       str1 = str1.replace(idx,'')
print(str1)
# print(str1.count(vowels[0]))
# str2 = str1.replace(vowels[0],'')
# str2 = str2.replace(vowels[1],'')
# str2 = str2.replace(vowels[2],'')
# str2 = str2.replace(vowels[3],'')
# str2 = str2.replace(vowels[4],'')
# print(str2)
