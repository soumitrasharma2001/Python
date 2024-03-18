str="I am a programmer"
# print(str[0])
# print(str[7:16])#here 7 is including and 16 is excluding it is string slicing
# print(len(str))
# print(str[0:56])#it will print full string
# print(str[0:5:2])#it will skip every single characters
# print(str[0:])#it will print entire string
# print(str[:]) #it will print entire string
# print(str[::]) #it will print entire string
# print(str[:5])#it will print from zeroth index to 3th index
#print the reverse string 
# print(str[::-1])#it will invert entire string
# print(str[::-2])#first it will invert the entire string and removes every second character
print(str.isalnum())
print(str.isalpha())
print(str.endswith("programmer"))
print(str.count("b"))
print(str.capitalize())#it will capitalize first character of the string
print(str.find("a"))
print(str.lower())#it will lower the every character inside the string
print(str.upper())#it will upper the every character inside the string
print(str.replace("I am","He is"))