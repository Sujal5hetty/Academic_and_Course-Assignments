def duplicate_char(string):
    frequency={}
    for char in string:
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char]=1

    sorted_frequency=sorted(frequency.items(),key=lambda x: x[1],reverse=True)
    duplicates={}
    for item in sorted_frequency:
        if item[1]>1:
            duplicates[item[0]]=item[1]
    print("The duplicate characters are : \n")
    for key,value in duplicates.items():
        print(key,":","{:02}".format(value),end='   ')

IS=input("Enter a string: ")
duplicate_char(IS)
