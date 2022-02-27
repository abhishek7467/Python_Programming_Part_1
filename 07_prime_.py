num = int(input("Enter the num:\n"))
prime=True
for i in range(2,num):
    if(num%i==0):
        prime =False
        break
if prime:
    print("this no. is prime")
else:
    print("this no.is not prime")    