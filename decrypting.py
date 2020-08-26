from cryptography.fernet import Fernet

file = open('key.key','rb')
key = file.read() #key is type bytes
file.close()

print(key)