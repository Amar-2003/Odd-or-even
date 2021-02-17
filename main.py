import random
#instructions printout
with open('instructions.txt','r') as file:
    for line in file:
        print(line)
#toss
print("Time for Toss")
choice = input("Enter even or odd in small letter:")
if(choice != "even" and choice != "odd"):
    print("Enter either odd or even in small!!")
    exit(1)

try:
    tossnumber = int(input("Enter a number for toss:"))
except:
    print("Enter an integer!!")
    exit(1)
rantoss = int(random.randint(0,6))
print(f"Computer's chosen number is {rantoss}")
if ((tossnumber+rantoss)%2 == 0):
    if(choice == "even"):
        print("You won the toss")
        userwon = True
    else:
        print("Computer won the toss")
        userwon = False

else:
    if(choice == "odd"):
        print("You won the toss")
        userwon = True
    else:
        print("Computer won the toss")    
        userwon = False

if(userwon):
	inp = input("Enter your choice as Bowl or Bat in small:")
    
	if(inp == "bat"):
		userbat = True
	else:
		userbat = False
else:
	if(random.randint(0,1)):
		userbat = True
	else:
		userbat = False
if(userbat):
	print("You now take the role of Batsmen")
else:
	print("You now take the role of Bowler")
