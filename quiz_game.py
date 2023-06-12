print("Welcome to my computer quiz!")

playing = input("Do you want to play a game? ").lower()
    
if playing != "yes":
    quit()
    
print("Okay! Let's play!")
score = 0

answer = input("What is the color of an apple? ").lower()
if answer == "red":
    print("You are correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the color of a banana? ").lower()
if answer == "yellow":
    print("You are correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the color of a watermelon? ").lower()
if answer == "green":
    print("You are correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the color of blueberries? ").lower()
if answer == "blue":
    print("You are correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions corrrect!")
print("You got " + str((score/4) * 100) + "% corrrect!")
    

