year = int(input("Please Enter Your Number : "))

leap_year = "This is a Leap Year" if year%4 == 0 and year%100 != 0 or year%400 == 0 else "This is not a Leap Year"

print(leap_year)
   