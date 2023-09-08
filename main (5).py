# write a program that determines whether year entered by user is a leap year or not using if-elif- else statement.

def print_leap_year(year):
    if(year % 4==0):
        print(year,"is a leap year")
    else:
        print(year," is not a leap year")
year=int(input("enter the  year"))
print_leap_year(year)