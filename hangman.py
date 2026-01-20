import random

myList = ["lion", "elephant", "hippopotamus", 'monkey', "dog"]
choiceList = []
display = ""
tries = 6
randomChoice = random.choice(myList)

# print(randomChoice) # hidden

blankSpace = ""
for i in range(len(randomChoice)):
    blankSpace += "_"
print(blankSpace)

print("Tries left: ", tries)
while display != randomChoice and tries > 0:
    choice = input("guess a letter: ").lower()
    choiceList.append(choice)
    for letter in randomChoice:
        if letter in choiceList:
            display += letter
        else:
            display += "_"
    print(display)
    if display == randomChoice:
        print("You win!")
        break
    display = ""
    if choice not in randomChoice:
        tries -= 1
        print("Try again!\nTries left: ", tries)
if tries == 0:
    print("You lose! Word was", randomChoice)