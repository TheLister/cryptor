import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet



# Gather Inputs
# encrypted_message_provided = input("Paste your encrypted message: ")
# key_provided = input("Paste your key: ")



# password = password_provided.encode() #convert to type bytes
# salt = b'p\xcckM\x15\xeb\xa6\xf9K\xe2l\xe7\xc49\xfe\xee'
# print(salt)

# kdf = PBKDF2HMAC( 
#     algorithm=hashes.SHA256(),
#     length=32,
#     salt=salt,
#     iterations=100000,
#     backend=default_backend()
# )

# key = base64.urlsafe_b64encode(kdf.derive(password))
# print(key)


# encrypted_message = "my secret message"
# print(message)
# encoded_message = message.encode()

password_provided = input("Paste your key: ")
password = password_provided.encode() #convert to type byte

encrypted_message_provided = input("Paste your encrypted message ")
encrypted_message = encrypted_message_provided.encode()



fernet_token = Fernet(password)
decrypted_message = fernet_token.decrypt(encrypted_message)
decrypted_message_str = decrypted_message.decode("utf-8")


print("decrypted message:")
print(decrypted_message_str)
