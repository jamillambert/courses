while True:
    year = input("Enter the year to check if it is a leap year (x to exit): ")
    if year == 'x':
        break
    if (int(year) % 4 == 0 & int(year) % 100 != 0) | (int(year) % 400 == 0):
        print(f'{year} is a leap year')
    else:
        print(f'{year} is not a leap year')
