import random
#instructions printout
with open('instructions.txt','r') as file:
    for line in file:
        print(line)
#toss
print("Time for Toss")
choice = input("Enter e for even and o odd in small letter:")
if(choice != "e" and choice != "o"):
    print("Enter either o or e in small!!")
    exit(1)

try:
    tossnumber = int(input("Enter a number for toss:"))
except:
    print("Enter an integer!!")
    exit(1)
rantoss = int(random.randint(0,6))
print(f"Computer's chosen number is {rantoss}")
if ((tossnumber+rantoss)%2 == 0):
    if(choice == "e"):
        print("You won the toss")
        userwon = True
    else:
        print("Computer won the toss")
        userwon = False

else:
    if(choice == "o"):
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
score1 = 0 #user's score
score2 = 0 # computer's score
print("Play 1 started, All the Best :)")
#play1
while(True):
    try:
        r = int(input("Enter Your run in range of 0 to 6 inclusive:"))
    except:
        print("Enter an integer between 0 and 6")
    n = int(random.randint(0,6))
    print(f"Computer chose {n}")
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
#play 2
print("Play 2 started")
while(True):
    try:
        r = int(input("Enter Your run in range of 0 to 6 inclusive:"))
    except:
        print("Enter an integer between 0 and 6")
    n = int(random.randint(0,6))
    print(f"Computer chose {n}")
    print(n)
    if not (userbat):
        if(r == n):
            print("You are out :(",end="   ")
            print(f"Your run now is {score1}")
            break
        else:
            score1 += r
            print(f"Your run now is {score1}",end="  ")
            if(score1 > score2):
                break
            print(f"Runs for you to win is {score2 - score1} ")
            
    else:
        if(r == n):
            print("Computer is out :),Nice bowling",end="   ")
            print(f"Computer's run now is {score2}")
            break
        else:
            score2 += n
            print(f"computer's run now is {score2}", end="  ")
            if(score2 > score1):
                break
            print(f"runs remaining for computer to win is {score1 - score2}")

if(score1 > score2):
        print(f"You won by {score1 - score2} runs")
else:
        print(f"Computer won by {score2 - score1} runs ")

    
