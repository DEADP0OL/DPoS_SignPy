from sys import version_info
from nacl import signing
from nacl import encoding
from binascii import hexlify
from hashlib import sha256

def sign_message(message,passphrase):
    priv_key = signing.SigningKey(sha256(str.encode(passphrase)).digest())
    signature = hexlify(priv_key.sign(str.encode(message))).decode()
    pub_key = priv_key.verify_key.encode(encoder=encoding.HexEncoder).decode()
    return(signature,pub_key)

if __name__ == '__main__':
    
    if version_info[0] < 3:
        print ('Python3 is required')
        raise SystemExit
    
    message = input("Enter Message: ")
    if (message is None) or (message == ''):
        raise SystemExit
            
    passphrase = input("Enter Passphrase: ")
    if (passphrase is None) or (passphrase == ''):
        raise SystemExit
    
    signature,pub_key = sign_message(message,passphrase)
    
    response = '-----BEGIN LISK SIGNED MESSAGE-----\n'
    response+='-----MESSAGE-----\n'
    response+=message+'\n'
    response+='-----PUBLIC KEY-----\n'
    response+=pub_key+'\n'
    response+='-----SIGNATURE-----\n'
    response+=signature+'\n'
    response+='-----END LISK SIGNED MESSAGE-----'
    
    print(response)