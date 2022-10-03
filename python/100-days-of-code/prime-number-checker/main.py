def prime_checker(number):
  if number < 3:
    # Numbers 0, 1, 2 are not prime and negative numbers are either by definition 
    # not prime or prime if the positive number is prime, 
    # therefore only positive numbers need to be checked
    print("It's not a prime number.")
    return
  for i in range(2, number-1):
    if number % i == 0:
      print("It's not a prime number.")
      return
  print("It's a prime number.")

while True:
  try:
    n = int(input("\nEnter number to check if it is a prime number (x to exit): "))
    prime_checker(number=n)
  except:
    break
