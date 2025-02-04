list1=[0,23,12,3,22]
print("Unsorted list: " ,list1)
for j in range(len(list1)-1):
    for i in range(len(list1)-1-j):
        if list1[i]>list1[i+1]:
         list1[i],list1[i+1]=list1[i+1],list1[i]
         print(list1)
        else:
            print(list1)
    print()


print("Sorted list in ascending order:",list1)

list2=[3,34,234,5,2,43]
print("Unsorted list: " ,list2)
for j in range(len(list2)-1):
    for i in range(len(list2)-1):
        if list2[i]<list2[i+1]:
         list2[i],list2[i+1]=list2[i+1],list2[i]


print("Sorted list in descending order:",list2)
