age = input("Are You a Cigarette Addict Older Than 75 Years Old ? (yes/no) ").title().strip().lower()
chronic = input("Do You Have a Severe Chronic Disease ? (yes/no) ").title().strip().lower()
immune = input("Is Your Immune System Too Weak ? (yes/no) ").title().strip().lower()

if age == "yes" :
  age = True
elif age == "no" :
  age = False

if chronic == "yes" :
  chronic = True
elif chronic == "no" :
  chronic = False

if immune == "yes" :
  immune = True
elif immune == "no" :
    immune == False

if age or chronic or immune == "yes" :
    print("You are in risky group")
elif age or chronic or immune == "no" :
    print("You are not in risky group")
else :
    print("Wrong answer ! Run again")
 
    