from time import pthread_getcpuclockid
year = 2022
 
if (year % 4 == 0 & year % 100 != 0) | (year % 400 == 0):
    print("leap year")
else:
    print("not a leap year")