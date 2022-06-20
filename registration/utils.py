'''
    client side encryption decryption method 
'''
import uuid

from SaveText_web.settings import SECRET_ENCRYPT_KEY


print(SECRET_ENCRYPT_KEY)

def genrateKey():
    key = uuid.uuid4().hex[:15]
    value = encrypt(key,SECRET_ENCRYPT_KEY)
    return value

def decrypt(msg,key):
    key = decrypt_key(key,SECRET_ENCRYPT_KEY)
    ord_vlaue = 0
    for i in range(0,len(key)):
        ord_vlaue+=ord(key[i])
    key_iteration_value = ord_vlaue%len(key)
    print(ord_vlaue)
    print(key_iteration_value)
    decrypted_msg = ""
    for i in range(0,len(msg)):
        decrypted_msg += chr(ord(msg[i])-key_iteration_value)
    return decrypted_msg


def encrypt(msg,key):
    key = decrypt_key(key,SECRET_ENCRYPT_KEY)
    ord_vlaue = 0
    for i in range(0,len(key)):
        ord_vlaue+=ord(key[i])
    key_iteration_value = ord_vlaue%len(key)
    print(ord_vlaue)
    print(key_iteration_value)
    encrypted_msg = ""
    for i in range(0,len(msg)):
        encrypted_msg += chr(ord(msg[i])+key_iteration_value)
    return encrypted_msg

def decrypt_key(msg,key):
    ord_vlaue = 0
    for i in range(0,len(key)):
        ord_vlaue+=ord(key[i])
    key_iteration_value = ord_vlaue%len(key)
    print(ord_vlaue)
    print(key_iteration_value)
    decrypted_msg = ""
    for i in range(0,len(msg)):
        decrypted_msg += chr(ord(msg[i])-key_iteration_value)
    return decrypted_msg