# One way to compare algorithms is by timing them. Their example is below:

import time

def sumOfN2(n):
   start = time.time()

   theSum = 0
   for i in range(1,n+1):
      theSum = theSum + i

   end = time.time()

   return theSum,end-start

# The time module obviously has to be imported and the function executed in the REPL:

>>>for i in range(5):
       print("Sum is %d required %10.7f seconds"%sumOfN2(10000)) # This will execute the code.
      
# you can then use this to test various different approaches to solving the problem. This shows that our above loop is not very efficient.

def sumOfN3(n):
   return (n*(n+1))/2

print(sumOfN3(10))

# if we do the same here

>>>for i in range(5):
       print("Sum is %d required %10.7f seconds"%sumOfN3(10000)) # We can see that this is far quicker to execute!
      
# in fact this does not scale even as the numbers are increased. This is therefore a better algorithm.
