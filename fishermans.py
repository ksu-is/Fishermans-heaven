# work in progress
# This is where the code will be 
# Enter your name and if you would like to use the fishing gps or not
# After that you will press 'find' if you woild like it to generate a radnom fish to find
# If not you will exit the app by pressing 'exit'
# When ypu generate the fish information it will show location and bait of the fish
import random
import time

fishing = True
a = b = c = d = e = f = 0 #define multiple variables as same thing
print ("---------------------------------")
print ("          Fishing GPS            ")
print ("---------------------------------")
time.sleep(1)
name = input("Welcome to the fishing GPS! \nEnter your name: ")
answer = input("Enter 'yes' or 'no' if you like to use the fishing app " + name + ": ")
if answer.lower() == "no":
    fishing == False
while fishing == True:    
    time.sleep(1)
    answer = input("Type 'find' and hit enter to start the fish gps, if not type 'exit' to quit: ")
    if answer == "exit":
        fishing = False
        er = float(g / (a + b + c + d + e + f))
        print("------------------------------------")
        print("Thank you for using the fishing GPS!")
        print("These were the fish that were generated:", "\n- Freshwater fish: ", str(a), "catfish, ", str(b), "bass ", "\n- Saltwater fish: ", str(c), "shark, ", str(d), "redfish", str(e), "barracuda, ", str(f), "brim, ")
    else:
        t = random.randrange(1, 9)
        if t == 1:
            a += 1
            print("The GPS came up with a catfish!")
            print("This fish is located in freshwater")
            print("bait to use: chicken liver, dough balls, and hotdogs")
        elif t == 2:
            b += 1
            print("The GPS came up with a bass!")
            print("This fish is located in freshwater")
            print("bait to use: artificial lures or worms")
        elif t == 3:
            c += 1
            print("The GPS came up with a shark!")
            print("This fish is located in saltwater")
            print("bait to use: dead or live fish")
        elif t == 4:
            d += 1
            print("The GPS came up with a redfish!")
            print("This fish is located in saltwater")
            print("bait to use: small pieces of octopus")
        elif t== 5:
            e += 1
            print("The GPS came up with a barracuda!")
            print("This fish is located in saltwater")
            print("bait to use: cigar fish")
        elif t== 6:
            f += 1
            print("The GPS came up with a brim!")
            print("This fish is located in freshwater")
            print("bait to use: bread or worm")
        elif t >= 7:
            g += 1
            print("There has been an error in the GPS") 