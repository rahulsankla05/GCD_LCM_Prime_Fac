# prime_factors.py
def prime_fac(n):
    prime=[]   # consider an blank list or array
    div=2     # //divisor initial value=2//
    while(div<=n):
        if n%div==0:  # n%2==0 run or consider +1 value of divisor
            n=n//div   # divide n/div 
            prime.append(div)   # append divisor value in prime list or array
        else:
            div+=1
    return prime
a=int(input("enter num:"))
print(prime_fac(a))
    
