def reverse_no(n):
    reversed_no=0
    while n>0:
        remainder=n%10
        reversed_no=(reversed_no*10)+remainder
        n=n//10
    return reversed_no


number=int(input("Enter any number: "))
print(reverse_no(number))
