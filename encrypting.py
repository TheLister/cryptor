from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)

file = open('key.key', 'wb')
file.write(key) #key is type bytes
file.close()
