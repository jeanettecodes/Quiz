print("Welcome to my quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")
score = 0

answer = input("What is the driest continent? ")
if answer.lower() == "antartica":
    print("Correct")
    score += 1 
else:
    print("Incorrect!")

answer = input("If a male donkey is a jack, what is the female called? ")
if answer.lower() == "jenny":
    print("Correct")
    score += 1 
else:
    print("Incorrect!")

answer = input("Who were high heels originally invented for? ")
if answer.lower() == "men":
    print("Correct")
    score += 1 
else:
    print("Incorrect!")

answer = input("What is the only fruit that has it's seeds on the outside? ")
if answer.lower() == "strawberry":
    print("Correct")
    score += 1 
else:
    print("Incorrect!")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%.")