#n!=1*2*3*4.....*n
''''a=int(input("enter no. for find factorial:\n"))
product=1
n=a
for i in range(n):
    product=product*(i+1)
print(product)    

#n!=1*2*3*4.....*n'''
'''def factorial_te(n):

    
    product=1
    
    for i in range(n):
        product=product*(i+1)
    return product
'''
def factorial_re(n):
    
    if n==0 or n==0:
        return 1
    return n*factorial_re(n-1)
#f=factorial_te(5)
f=factorial_re(4)
print(f)            
