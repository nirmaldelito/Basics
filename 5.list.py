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


def dul(list):

    if len(list) == (len(set(list))):
        return False
    else:
        return False


ans = dul(list)
print(ans)

#d. What would the output look like for you program for the following
array = [12, 71, 92, 56, 121, 33, 89, 47, 25, 64, 100, 103, 2, 19, 96]


def candy(x):
    if x in array:
        print("yes")
    else:
        print("no")


candy(47)
candy(99)
