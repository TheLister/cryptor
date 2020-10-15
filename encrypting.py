import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


# gather inputs
password_provided = input("Create a password: ") 
message = input("Enter your message: ")


password = password_provided.encode() #convert to type bytes
salt = b'p\xcckM\x15\xeb\xa6\xf9K\xe2l\xe7\xc49\xfe\xee'

kdf = PBKDF2HMAC( 
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)

key = base64.urlsafe_b64encode(kdf.derive(password))


# file = open('key.key', 'wb')
# file.write(key) #key is typebytes
# file.close()


encoded_message = message.encode()

fernet_object = Fernet(key)
encrypted_message = fernet_object.encrypt(encoded_message)

print('Using password "' + password_provided + '"' + ' to encrypt "' + message + '"')

print("the next line contains your key:")
print(key)

print("the next line contains your encrypted message:")
print(encrypted_message)    