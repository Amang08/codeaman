triple = lambda x : x*3


length = int(input("Enter the length of the list: "))
list_1 = []

for i in range(length):
    elements = int(input("enter the elements of the list: "))
    list_1.append(elements)


list_2 = list(map(triple,list_1))


print("original list is", list_1)
print("Triple of given list is", list_2)