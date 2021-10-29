def factorial(number):
   if (number < 2): 
      return number

   return number * factorial(number - 1 )

'''
https://projecteuler.net/problem=10
Summation of primes
Show HTML problem content 
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
def summationOfPrimes(numOfPrimes):
   sumOfPrimes = 0
   numOfPrimes = numOfPrimes - 1

   while (numOfPrimes > 1): 
     if ( isPrime( numOfPrimes )): 
        sumOfPrimes = sumOfPrimes + numOfPrimes

     numOfPrimes = numOfPrimes - 1

   return sumOfPrimes

def isPrime(number): 
   divisor = 2

   while ( divisor < number): 
      if (number % divisor == 0):
         return False

      divisor = divisor + 1

   return True

print("O fatorial de 5 é: ", factorial(5))

number = 200
print("A soma dos primos menores que ", number, "é ", summationOfPrimes(number))
