dictionary={
"Set":"It is a collection of well defined objects.",
"Program":"It is a set of instructions given to a computer to make it perform a particular task.",
"Computer":"It is an electronic device which takes an input from the user do some processing and gives some output",
"CPU":"CPU is the brain of the computer",
"RAM":"RAM is the storage area where we store those data which is currently use by CPU"}
print("Enter the word")
inp=input()
if inp in dictionary.keys():
    print(dictionary[inp])
else:
    print("Word is not available")