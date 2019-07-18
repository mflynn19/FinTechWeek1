import sympy

# (1) Write a program that prints the numbers from 1 to 100, except: if it's a multiple of 3, it prints "fizz" instead, and if it's a multiple of 5 it prints "buzz" instead.  And for multiples of both 3 and 5, it prints "fizzbuzz."  (This is also a great improv game when done in person, going around the circle.) 
def fizzBuzz():
    for i in range(1, 100):
        if (i % 3 == 0):
            print("fizz")
        elif (i % 5 == 0):
            print("buzz")
        elif (i % 3 == 0 and i % 5 == 0):
            print("fizzbuzz")
        else:
            print(i)

# (1a) EXTRA SUPER CHALLENGE VERSION: make the program print "fizz" for numbers that contain the digit 3 (and the same for buzz and digit 5, and fizzbuzz for both digits 3 and 5).  
def fizzBuzz2():
    for i in range(0, 100):
        if (3 in i):
            print("fizz")
        elif (5 in i):
            print("buzz")
        elif (3 in i and 5 in i):
            print("fizzbuzz")
        else:
            print(i)
            
# (2) Write a program to calculate the nth Fibonacci number.
def fibbo(num):
    if (int(num) <= 1):
        return(num)
    else:
        return(fibbo(int(num)- 1) + fibbo(int(num) - 2))
    #since you want the nth you need to -1 to get the actual value and -2 to get the previous value

print(fibbo(10))

# (3) Write a program to print the nth row of Pascal's Triangle.


# (4) Write a program that finds all the prime numbers less than a given number n.
def primes(n):
    return list(sympy.primerange(0, n))
print (primes(10))

# EXTRA CHALLENGE VERSION: How efficiently can you make this program run?  
# (5) Write a square root calculator.

