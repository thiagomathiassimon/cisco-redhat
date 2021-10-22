def factorial(number):
   if (number < 2): 
      return number

   return number * factorial(number - 1 )

print('Ola Mundo!')

print("O fatorial de 5 é: ", factorial(5))
