len gets number of characters from string

parrot = "Norwegian Blue"

print len(parrot)
#outcome = 14

_____

lower makes letters in string all lowercase
parrot = "Norwegian Blue"

parrot2 = parrot.lower()

print(parrot2)
#outcome = norwegian blue

-------------
upper makes letters in string uppercase

parrot = "norwegian blue"

parrot2 = parrot.upper()

print(parrot2)

-----------------------------------
+ function adds together
print("hi " + "friend")
--------------------------
from datetime import datetime
now = datetime.now()

print("%s/%s/%s" % (now.month, now.day, now.year)) #the %s gets the string and replaces it
-------------------------------------
from datetime import datetime

now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day

print("The year is " + str(now.year))
print("The month is " + str(now.month))
print("Today is the "+ str(now.day) + "th") #prints our date
----------------------
#double equal signs means if something is equal to another thing or not
# one equal sign assigns a variable
