#A program to predict the winner of the Wimbledon Finals
import random

#Set the count of wins for both
f = 0
c = 0

#Array containing both players
players = ["Federer","Cilic"]

#Count
x = 0

#Runs through 101 random simulations
while(x<101):
    prediction = random.choice(players)
    if prediction == "Federer":
        f = f+1
        x = x+1

    elif prediction == "Cilic":
        c = c+1
        x = x+1

#Prints the winner of more random matches
if c > f:
    print("The winner is Cilic!")

elif f > c:
    print("The winner is Federer!")




