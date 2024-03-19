text = 'Hello Zaira'
shift = 3

def caesar_cypher(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_message = ''

    for letter in message.lower():
        if letter == ' ':
            encrypted_message += letter
        else:
            index = alphabet.find(letter)
            new_index = (index + offset) % len(alphabet)
            encrypted_message += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_message)

caesar_cypher(text, shift)

caesar_cypher('hello world', 13)