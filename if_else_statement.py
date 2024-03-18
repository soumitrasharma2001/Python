# var1=6
# var2=int(input())
# if(var2>var1):
#     print("Greater")#When we enter in if condition then for every line of code we have to left some space as shown.
# elif var2==var1:
#     print("Equal")
# else:
#     print("Lesser")
#in functions
# list=[5,7,9]
# if 7 in list:
#     print("Number is in list")
# if 10 not in list:
#     print("Number is not in the list")
age=int(input())
if(age not in range(101)):
    print("Illogical value")
elif(age>18):
    print("You can drive")
elif(age==18):
    print("We can't decide we need to take your test.")
else:
    print("You can't drive")