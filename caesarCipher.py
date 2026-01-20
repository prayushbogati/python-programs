alphabets = [
  "A","B","C","D","E","F","G","H","I","J",
  "K","L","M","N","O","P","Q","R","S","T",
  "U","V","W","X","Y","Z"
]

# formulae
# encryption: c = (p + k) mod 26
# decryption: p = (c - k) mod 26


option = input("Encrypt or decrypt? (e/d): ").lower()

while option != "e" and option != "d":
    print("Invalid input! Go again.")
    option = input("Encrypt or decrypt? (e/d): ").lower()

if option == "e":
    plainText = input("enter text to encrypt: ").upper()
    key = int(input("Enter key: "))
    ciphertext = ""

    for letter in plainText:
        index = alphabets.index(letter)
        c = (index + key) % 26
        ciphertext = ciphertext + alphabets[c]
    print("Encrypted text is: " + ciphertext)

if option == "d":
    ciphertext = input("enter text to decrypt: ").upper()
    key = int(input("Enter key: "))
    plainText = ""
    
    for letter in ciphertext:
        index = alphabets.index(letter)
        p = (index - key) % 26
        plainText = plainText + alphabets[p]
    print("Decrypted text is: " + plainText)