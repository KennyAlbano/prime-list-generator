i=0
n=10
primes=[2]
currentVal=3
while(len(primes)<n):
    if(currentVal%primes[i]==0):
        currentVal=currentVal+2
        i=0
    if(len(primes)==(i+1)):
        primes.append(currentVal)
    if(currentVal%primes[i]!=0):
        i+=1
print(primes)

#Prints the first n primes.
#only tests odd numbers because 2 is the only even prime

