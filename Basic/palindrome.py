def palindrome(n):
    num=n
    result=0
    while n>0:
        last_digit=n%10
        result=(result*10)+last_digit
        n=n//10
    return num==result
n=int(input("Enter a number:"))
print(palindrome(n))