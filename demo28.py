"""
Mã hóa và giải mã Caesar Cipher: 
Viết hai hàm để mã hóa và giải mã một chuỗi sử dụng phương pháp mã hóa Caesar Cipher với một khóa cho trước.
"""

def caesar_cipher_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            encrypted += char
    return encrypted

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

text = input("Nhập văn bản để mã hóa: ")
shift = int(input("Nhập khóa mã hóa (số nguyên): "))
encrypted_text = caesar_cipher_encrypt(text, shift)
print("Văn bản đã mã hóa:", encrypted_text)
print("Văn bản đã giải mã:", caesar_cipher_decrypt(encrypted_text, shift))
