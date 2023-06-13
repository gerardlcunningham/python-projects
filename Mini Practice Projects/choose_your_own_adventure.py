print("Welcome to Choose Your Adventure game!")
name = input("What is your adventurer name? ")
print("Welcome, brave adventurer " + name + "!")

begin_adventure = input("Would you like to begin your adventure? (yes/no)? ").lower()

if begin_adventure == "yes":
    print("Okay, brave adventurer, let's begin!")

else:
    print("Goodbye adventurer!")
    quit()

