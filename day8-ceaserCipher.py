alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("type 'encode' to encrypt and 'decode' to decrypt: ").lower()
text = input("Enter the text: ").lower()
key = int(input("Enter the key: "))


def caeser(text, key, direction):
    
    newText = ""
    for char in text:
        if char in alphabets:
            index = alphabets.index(char)
            if direction == "encode":
                index += key
            elif direction == "decode":
                index -= key
            index = index % 26
            newText += alphabets[index]
        else:
            newText += char
    print(f"The {direction}d text is {newText}")

while True:
    
    caeser(text, key, direction)
    again = input("Do you want to go again? 'yes' or 'no': ").lower()
    if again == "yes":
        direction = input("type 'encod' to encrypt and 'decode' to decrypt: ").lower()
        text = input("Enter the text: ").lower()
        key = int(input("Enter the key: "))
        caeser(text, key, direction)
    else:
        print("Thank you")
        break
