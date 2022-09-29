def prime_checker(number):
  if number > -3 and number < 3:
    #numbers -2, -1, 0, 1, 2 are not prime
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
