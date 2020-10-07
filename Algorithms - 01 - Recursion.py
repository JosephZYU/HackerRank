def fact(n):

  # Define base case n is 1
  if n == 1:
    return 1

  # Define recursive case n != 1
  # Loop while N > 1, keep multiplying that product n and 
  # decrementing (gradually decrease) that product

  else:
    return n*fact(n-1)
    
# Define function of  fibonacci sequence
def fs(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fs(n-1) + fs(n-2)
    
# We can actually write if, elif, else statement in 1 line

# Define function of  fibonacci sequence
def fs(n):
  if n == 0: return 0
  elif n == 1: return 1
  else: return fs(n-1) + fs(n-2)
  
A = []

for n in range(11):
  print(fs(n))
  A.append(fs(n))

print(A)

# 🧐 the trick about recursion is to place your func inside your func!
# It may seem counter-intuition at first, try to get use to it

def collatz(n):

  # Define base case
  if n == 1:
    return 0

  # If n is even number, repeat this process on n/2
  elif n % 2 == 0:
    return 1 + cc(n/2)

  # 👀 The FINAL condition should be else to be comprehensive
  # DO NOT Place elif in the end
  else:
    return 1 + cc(3*n + 1)

  # If n is odd number, repeat this process on 3n + 1
  # elif n % 2 == 0:
  #   return 1 + cc(3*n + 1)

"""
def collatz(n):
  if n == 1:
    return 0

  elif n % 2 == 0:
    return 1 + cc(n/2)

  else:
    return 1 + cc(3*n + 1)
"""

def collatz(n):
  if n == 1:
    return 0
  elif n % 2 == 0:
    return 1 + collatz(n/2)
  else:
    return 1 + collatz(3*n + 1)
    
for i in A[3:]:
  print(collatz(i))
  
def collatz_jyu(n):
  if n == 1:
    return 0
  elif n % 2 == 0:
    n = 1 + collatz(n/2)
    return n
  else:
    n = 1 + collatz(3*n + 1)
    return n  
