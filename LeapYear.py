# Amal Kariyawasam 12/05/2022
# Simple Leap Year Calculator using Python using If/elif Statements
#Logic: On every year that is evenly divisible by 4 **except** every year that is evenly divisible by 100 **unless** the year is also evenly divisible by 400

year = int(input("Which year do you want to check? "))
year_4=year%4
year_100=year%100
year_400=year%400

if year_4>0:
  print("Not a leap year")
elif year_100>0:
  print("Leap Year")
elif year_400==0:
  print("Leap year")
else:
  print("Not a leap year")
