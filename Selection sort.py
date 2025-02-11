list1=[56,2,1,78,6,0]
print("Unsorted list",list1)

for i in range(len(list1)-1):
    min_val=min(list1[i:])
    minvalidx=list1.index(min_val)
    list1[i],list1[minvalidx]=list1[minvalidx],list1[i]
    #
    print(list1)#to see each step

print("Sorted list in ascending order : ",list1)





for i in range(len(list1)-1):
    max_val=max(list1[i:])
    maxvalidx=list1.index(max_val)
    list1[i],list1[maxvalidx]=list1[maxvalidx],list1[i]
    #print(list1),to see each step

print("Sorted list in descending order : ",list1)

#for duplicate values
list2=[56,2,0,7,0,66,0,2]
print("Unsorted list",list2)

for i in range(len(list1)-1):
    min_val=min(list2[i:])
    minvalidx=list2.index(min_val,i)
    list2[i],list2[minvalidx]=list2[minvalidx],list2[i]
    #print(list1),to see each step

print("Sorted list in ascending order : ",list2)

#The Problem with Just list2.index(min_val)
#The .index() method returns only the first occurrence of a value.
#If there are duplicate values, it may return the wrong index.
#By using list2.index(min_val, i), we ensure that the search for min_val starts
#from index i, avoiding earlier occurrences that have already been placed correctly.
