#Dictionary in python is nothing but a key value pairs.
d1={}
d2={"45":"Soujanya","46":"Soumitra","47":"Soumya","48":{"Soumitra":"Web","Soujanya":"AI","Sonu":"Data Science"}}
#print(d2["48"]["Soumitra"])
#updating the current dictionary
print(d2.get("45"))
d2["49"]="Sourabh"
d2.update({"50":"Sourav"})
#deleting data from dictionary
d3=d2# note d3 and d2 both are pointers that points to same dictionary so if you made changes in d3 it will affect the d2
d3=d2.copy()
del d3["45"]
print(d2)
#printing keys and items
print(d2.items())
print(d2.keys())