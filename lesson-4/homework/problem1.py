list1 = list(map(int, input("Enter the elements of the first list: ").split()))
list2 = list(map(int, input("Enter the elements of the second list: ").split()))
output = []
for i in list1:
    if i not in list2:
        output.append(i)
for i in list2:
    if i not in list1:
        output.append(i)
print(output)
