square = lambda x : x*x

length= int(input("Enter the length of the list : "))
list_1 = []

for i in range(length):
    elements = int(input(f"Enter the {i+1} element of the list :  "))
    list_1.append(elements)


list_2 = list(map(square,list_1))

print("The original list is", list_1)
print("The square of the given list is", list_2)