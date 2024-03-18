list_of_students=["Soham","Sonu","Soujanya","Soumitra","Sourabh","Swarnim","Sparsh"]
#print(list_of_students[0])
#Below these function will change the original list
# list_of_students.sort()
# list_of_students.reverse()
numbers=[1,2,3,4,56,1]
print(numbers[0:5])#here it prints upto 56
print(numbers[:])#value at left side of ':' is zero and value of right side is the length of list
print(numbers[1:])#it will skip the value at zeroth index and print remaining values
print(numbers[::])#here value of 1st parameter is zero and value of 2nd parameter is length of list and 3rd is 1
numbers.append(67)
numbers.insert(2,58)
numbers.insert(5,58)
numbers.remove(58)
numbers.remove(58)
numbers.pop()
#Tuples
# tp=(1,2,3)
# #tp[1]=4 this will throw an error because tp is a tuple and tuples are immutable
# print(tp)
# a=1 
# b=8
# #swapping two variables
# a,b=b,a
# print(a,b)
#numbers.clear()
numbers.extend(list_of_students)
print(numbers.index(3))