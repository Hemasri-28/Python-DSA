def extraction(n):
    while n>0:
        last_digit=n%10
        print(last_digit)
        n=n//10
n=int(input("Enter a number:"))
extraction(n)