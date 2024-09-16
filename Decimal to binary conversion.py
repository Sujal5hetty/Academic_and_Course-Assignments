def decimal_to_binary(n):
    integer_part=int(n)
    fractional_part=n-integer_part

    binary_integer_part=bin(integer_part).replace("0b","")

    

    binary_fractional_part=""
    while fractional_part:
        fractional_part*=2
        if fractional_part>=1:
            binary_fractional_part+="1"
            fractional_part-=1
        else:
            binary_fractional_part+="0"

        #to limit no of digits upto precision of 10
        if len(binary_fractional_part)>10:
            break

    
    if binary_fractional_part:
        return f" {binary_integer_part}.{binary_fractional_part}"
    else:
        return binary_integer_part
    


decimal_no=float(input("Enter a decimal no: "))

binary_no=decimal_to_binary(decimal_no)

print(f" The binary representation of {decimal_no} is {binary_no}")
