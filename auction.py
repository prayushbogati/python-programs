# auction using dictionary

print("****AUCTION*****")

buyers = {} 

while True:
    buyer = input("Enter buyer's name: ").capitalize()
    while True:
        try:
            bid = int(input("Enter bid amount: "))
            break
        except:
            print("Enter a valid bid!")

    buyers[buyer] = bid

    while True:
        isAll = input("Are there other buyers? (y/n): ").lower()
        if isAll == "yes" or isAll == "y":
            break
        print("Enter y or n !")

    if isAll == "n" or isAll == "no":
        break

hBid = 0
for key in buyers:
    if buyers[key] > hBid:
        hBid = buyers[key]
        winner = key
print(f"The winner is {winner} with the bid of {hBid}!")
