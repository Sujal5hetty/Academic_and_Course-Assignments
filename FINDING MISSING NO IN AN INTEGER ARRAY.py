def find_missing(arr):
    n=100
    expected_sum=n*(n+1)//2
    actual_sum=sum(arr)
    missing_no=expected_sum-actual_sum
    return missing_no
arr=list(range(0,101))
arr.remove(43)
print(find_missing(arr))
