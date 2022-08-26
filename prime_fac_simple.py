# prime_fac_simple.py

n=int(input("num:"))
div=2
# //prime fac using while loop//
while(div<=n):
	if n%div==0:
		n=n//div
		print(div,end=" ")
	else:
		div+=1


# prime fac using "for" loop:   
'''
n=int(input("num_value:"))     
for div in range(2,n+1):
    if n%div==0:
        n=n//div
        print(div,end=" ")
    else:
        div+=1
'''