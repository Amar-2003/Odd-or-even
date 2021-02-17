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
score1 = 0
score2 = 0
#play1
while(True):
    try:
        r = int(input("Enter Your run in range of 0 to 6 inclusive:"))
    except:
        print("Enter an integer between 0 and 6")
    n = int(random.randint(0,6))
    print(n)
    if(userbat):
        if(r == n):
            print("You are out :(",end="   ")
            print(f"Your run now is {score1}")
            break
        else:
            score1 += r
            print(f"Your run now is {score1}")
    else:
        if(r == n):
            print("Computer is out :),Nice bowling",end="   ")
            print(f"Computer's run now is {score2}")
            break
        else:
            score2 += n
            print(f"computer's run now is {score2}")
    
