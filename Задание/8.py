def sdvig(text, shift=3):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(shifted_char)
        else:
            result.append(char)
    return ''.join(result)

text = input()
sdvtext = sdvig(text)
print(f"Исходная строка: {text}")
print(f"Зашифрованная строка: {sdvtext}")