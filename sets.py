# s_of_list=set([1,2,3,4,5])
# print(s_of_list)
# print(type(s_of_list))
s=set()
s.add(1)
s.add(2)#It will add only different values repeated values are not allowed
s1=s.union({2,3,4,5})#It creates a new set instead of modifying previous set
s2=s.intersection({2,4,5,6})

print(s.isdisjoint(s1))