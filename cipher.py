# add your code here
alphabets = 'abcdefghijklmnopqrstuvwxyz'
def final_words(original_words, shift=5):
    def shifted_letter(char):
        if char in alphabets:
            char_num = ord(char) - 97
            char = chr((char_num + shift) % 26 + 97 )
        return char
    return ''.join(shifted_letter(char) for char in original_words)
original_words = input('Please enter a senctence: ')
print('The encrypted sentence is:', final_words(original_words, shift=5))