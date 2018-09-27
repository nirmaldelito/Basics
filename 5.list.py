list = [12,23,34,45,56,67]
#a. Find if a number ‘x’ is in the array or not.
#b. Print the position of the number ‘x’


def find(x):
    if x in list:
        print("yes")
        print(list.index(x))
    else:
        print("no")

#c. Print true/false for the following question - “does it contain any duplicate elements?”


if len(list) == (len(set(list))):
    print("false,the list contains no duplicates")
else:
    print("True,the list contains duplicates")
#d. What would the output look like for you program for the following
array = [12, 71, 92, 56, 121, 33, 89, 47, 25, 64, 100, 103, 2, 19, 96]
x = 47
output("yes")
x = 99
output("no")
