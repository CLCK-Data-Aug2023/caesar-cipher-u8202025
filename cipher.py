# add your code here
def encrypt(sentence):
    encrypted_sentence = ""
    for char in sentence:
        if char.isalpha():
            # Encrypt only alphabetic characters
            offset = 13  # You can choose a different offset for encryption
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + offset) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + offset) % 26 + ord('A'))
            encrypted_sentence += encrypted_char
        else:
            # Keep non-alphabetic characters unchanged
            encrypted_sentence += char
    return encrypted_sentence

# Get user input
user_input = input("Please enter a sentence: ")

# Encrypt the sentence
encrypted_sentence = encrypt(user_input)

# Display the result
print("The encrypted sentence is:", encrypted_sentence)
