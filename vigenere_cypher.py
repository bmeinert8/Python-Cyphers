text = 'Hello Zaira'
custome_key = 'python'

def vigenere_cypher(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_message = ''
    key_index = 0

    for letter in message.lower():
        # Append space to the message
        if letter == ' ':
            encrypted_message += letter
        else:
            # Find the right key character to encode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset abd the encrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(letter)
            new_index = (index + offset) % len(alphabet)
            encrypted_message += alphabet[new_index]
    return encrypted_message

encryption  = vigenere_cypher(text, custome_key)
print(encryption)