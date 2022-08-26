# lcm_Gcd.py
n1=int(input("enter number1:"))
n2=int(input("enter number2: "))
orgn1=n1    # to store original num 1
orgn2=n2    # to store original num 2

while(n1%n2!=0):   # start a loop till 0 as remainder
	rem=int(n1%n2)   # remainder = n1%n2
	n1=n2           # now divisor become divident
	n2=rem       # now remainder become divisor

gcd=n2     # greatest common factor will be n2=divisor of both numbers
lcm=((orgn1*orgn2)//gcd)  
print("gcd of given numbers:",gcd)
print("lcm of given numbers is:",lcm)