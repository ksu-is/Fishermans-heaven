# work in progress
# This is where the code will be 
# Enter the name of the fish you would like to catch
import random
import time

fishing = True
a = b = c = d = e = 0 #define multiple variables as same thing
print ("---------------------------------")
print ("          Fishing GPS            ")
print ("---------------------------------")
time.sleep(1)
name = input("What is the name of the fish you would like to catch? ")
answer = input("Are you going to fish today for the, " + name + "?")
if answer.lower() == "no":
    fishing == False
while fishing == True:    
    time.sleep(1)
    answer = input("go fish or exit app? ")
    if answer == "exit app":
        fishing = False
        er = float(e / (a + b + c + d))
        print("------------------------------------")
        print("Thank you for using the fishing GPS!")
        print("You caught:", str(a), "catfish, ", str(b), "bass, ", str(c), "shark, ", str(d), "redfish. \nEfficiency Rate: ", str(er), ".")
    else:
        t = random.randrange(1, 7)
        if t == 1:
            a += 1
            print("You caught a catfish!")
            print("This fish is located in freshwater")
            print("bait to use: chicken liver, dough balls, and hotdogs")
        elif t == 2:
            b += 1
            print("You caught a bass!")
            print("This fish is located in freshwater")
            print("bait to use: artificial lures or worms")
        elif t == 3:
            c += 1
            print("You caught a shark!")
            print("This fish is located in saltwater")
            print("bait to use: dead or live fish")
        elif t == 4:
            d += 1
            print("You caught a redfish!")
            print("This fish is located in saltwater")
            print("bait to use: small pieces of octopus")
        elif t >= 5:
            e += 1
            print("You caught nothing!")