def encipher (text, key):
    return process(text, key, False)

def decipher (cipher, key):
    return process(cipher, key, True)

def rotate (rotor, position):
    new = (((ord(rotor) - ord("A")) + position) % 26)
    return chr(new + ord("A"))

def process (text, key, decipher):
    text = text.upper().replace(" ", "")
    key = key.upper()
    if (len(key) < 1):
        raise ValueError("key cannot be empty string")
    result = ""
    if not decipher:
        key += text
    for index in range(0, len(text)):
        if decipher:
            position = -ord(key[index % len(key)]) - ord("A")
            result += rotate(text[index], position)
            key += result[-1]
        else:
            position = ord(key[index]) - ord("A")
            result += rotate(text[index], position)
    return result

key = "1234"
key2 = "987654321"
#print encipher("Hello World!", key)
print decipher(encipher("Hello World", key), key)
print decipher(encipher("Hello World", key2), key2)