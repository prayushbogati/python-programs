import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play = input("play blackjack game? (y/n) ").lower()

def generateRandomCard():
    index = random.choice(cards)
    return cards[index]

def generateCardsSum(cards):
    total = 0
    for card in cards:
        total += card
    return total

if play == "y":

    userCardList = []
    dealerCardList = []
    
    userCardList.append(generateRandomCard())
    userCardList.append(generateRandomCard())

    dealerCardList.append(generateRandomCard())
    dealerCardList.append(generateRandomCard())
    
    userTotal = generateCardsSum(userCardList)
    dealerTotal = generateCardsSum(dealerCardList)

    print(userCardList, f"Total: {userTotal}")


    while True:
        hitOrStand = input("Hit or stand: ").lower()

        if hitOrStand == "hit" or hitOrStand == "h":
            userCardList.append(generateRandomCard())
            userTotal += userCardList[len(userCardList) - 1]
            print(userCardList, f"Total: {userTotal}")
            if userTotal > 21:
                print("You lose!")
                break

        elif hitOrStand == "stand" or hitOrStand == "s":
            print(f"User Total: {userTotal}\nDealer Total: {dealerTotal}")
            if userTotal > dealerTotal and userTotal <= 21:
                print("You win!")
            elif userTotal == dealerTotal:
                print("Draw!")
            else:
                print("You lose!")

            break

        else:
            print("type correct input")

else:
    exit()