import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play = input("play blackjack game? (y/n) ").lower()

def generateRandomCard():
    index = random.choice(cards)
    return cards[index]

def generateTotal(cards):
    total = 0
    for card in cards:
        total += card
    return total

def runHit(userTotal):
    userCardList.append(generateRandomCard())
    userTotal += userCardList[len(userCardList) - 1]
    print(userCardList, f"Total: {userTotal}")
    if userTotal > 21:
        print("You lose!")
        exit()


if play == "y":

    while True:
        userCardList = []
        dealerCardList = []
        
        userCardList.append(generateRandomCard())
        userCardList.append(generateRandomCard())

        dealerCardList.append(generateRandomCard())
        print(dealerCardList, f"Dealer Total: {dealerCardList[0]}")
        dealerCardList.append(generateRandomCard())
        
        userTotal = generateTotal(userCardList)
        dealerTotal = generateTotal(dealerCardList)

        print(userCardList, f"User Total: {userTotal}")

        while True:
            gameOver = False
            hitOrStand = input("Hit or stand: ").lower()

            if hitOrStand == "hit" or hitOrStand == "h":
                runHit(userTotal)

            elif hitOrStand == "stand" or hitOrStand == "s":
                while True:
                    if dealerTotal < 15: # this make it bit difficult as bot tries to make the total greater than 14
                        dealerCardList.append(generateRandomCard())
                        dealerTotal = generateTotal(dealerCardList)
                        if dealerTotal > 21:
                            print(f"Dealer total: {dealerTotal}. You win!")
                            gameOver = True
                            break
                    if userTotal > dealerTotal:
                        print("You win!")
                        gameOver = True
                        break
                    if userTotal == dealerTotal:
                        print("Game drawn!")
                        gameOver = True
                        break
                    if userTotal < dealerTotal:
                        print("You lose!")
                        gameOver = True
                        break
                if gameOver:
                    print(f"{userCardList} User Total: {userTotal}\n{dealerCardList} Dealer Total: {dealerTotal}")
                    break

            else:
                print("type correct input")

        newGame = input("Play again? (y/n) ")
        if newGame == "n":
            print("Thanks for playing!")
            break

else:
    exit()
