import random
#instructions printout
with open('instructions.txt','r') as file:
    for line in file:
        print(line)
#toss
print("Time for Toss")
choice = input("Enter even or odd in small letter:")
tossnumber = int(input("Enter a number for toss:"))
rantoss = int(random.randint(0,1)
if((tossnumber + rantoss)%2 == 0):
    if(choice = "even"):
        print("You won the toss")
        #To do
    else:
        print("Computer won the toss")
        #to do

else:
    if(choice == "odd"):
        print("You won the toss")
        #To do
    else:
        print("Computer won the toss")    
        #To do