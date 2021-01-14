from cryptography.fernet import Fernet

key = Fernet.generate_key()

crypter = Fernet(key)

password = crypter.encrypt(b'EncryptionFirst')
decrypter = crypter.decrypt(password)

print("Your password: " + str(decrypter,'utf8'))
print("\n Encryption of that password: ")
print(str(password,'utf8'))