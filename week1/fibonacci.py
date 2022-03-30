def Fibonacci(n):
  nterms = int(input("Enter a number for Fib: ")) + 1
 
  n1, n2 = 0, 1
  count = 0
  

  if nterms <= 0:
     print("Please enter a positive integer")

  elif nterms == 1:
     print("Fibonacci sequence upto",nterms,":")
     print(n1)

  else:
     print("Fibonacci sequence:")
     while count < nterms:
         print(n1)
         nth = n1 + n2
        
         n1 = n2
         n2 = nth
         count += 1


def fibtester():
    Test = 1
  
    if Test < 0:
        print("Sorry, Fib does not exist for negative numbers")
    else:
        print( Fibonacci(Test))

