def caesar_shift(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char) - 65 + shift_amount) % 26) + 65) if char.isupper() else chr(((ord(char) - 97 + shift_amount) % 26) + 97)
            result += new_char
        else:
            result += char
    return result


# Decrypting by shifting back
print(caesar_shift("EOXH MHDQV", -3))  