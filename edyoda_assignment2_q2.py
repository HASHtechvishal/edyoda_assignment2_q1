#q2--Write a Python program to print a dictionary whose keys should be the alphabet from a-z and 
#the value should be corresponding ASCII values


new_dict = {}
 
for i in range(97, 97 + 26):
    new_dict[chr(i)] = i
 
print(new_dict)
