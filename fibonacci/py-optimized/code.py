import sys

def fibonacci(n):
  if (n == 0):
    return 0
  if (n == 1):
    return 1
  return fibonacci(n-1) + fibonacci(n-2)

def main():
    u = int(sys.argv[1])
    fib0 = 0
    fib1 = 1
    r = 1
    for i in range(2, u):
      fib = fib0 + fib1
      r += fib
      fib0 = fib1
      fib1 = fib
    print(r)

main()
