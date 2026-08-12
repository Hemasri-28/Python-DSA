def armstrong(n):
    num=n
    nod=len(str(n))
    total=0
    while n>0:
        last_digit=n%10
        total=total+(last_digit**nod)
        n=n//10
    return num==total
n=int(input("Enter a number:"))
print(armstrong(n))