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
answer = input("Is the fish freshwater or saltwater? ")
if answer.lower() == "freshwater":
    fishing == False
while fishing == True:    
    time.sleep(1)
    answer = input("Does it have a large mouth? ")
    if answer == "yes":
        fishing = False
        er = float(e / (a + b + c + d))
        print("--------------------------------")
        print("       You caught a bass!       ")
        print("You caught:", str(a), "cod, ", str(b), "salmon, ", str(c), "shark, ", str(d), "wildfish. \nEfficiency Rate: ", str(er), ".")
    else:
        t = random.randrange(1, 7)
        if t == 1:
            a += 1
            print("You caught a cod!")
        elif t == 2:
            b += 1
            print("You caught a salmon!")
        elif t == 3:
            c += 1
            print("You caught a shark!")
        elif t == 4:
            d += 1
            print("You caught a wildfish!")
        elif t >= 5:
            e += 1
            print("You caught nothing!")