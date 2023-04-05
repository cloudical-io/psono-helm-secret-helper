#!/bin/python3
import nacl.encoding
from nacl.public import PrivateKey
import string
import secrets
import bcrypt

def main():
    uni = string.ascii_letters + string.digits
    box = PrivateKey.generate()
    private_key_hex = box.encode(encoder=nacl.encoding.HexEncoder)
    public_key_hex = box.public_key.encode(encoder=nacl.encoding.HexEncoder)

    with open('secrets.env', 'a') as f:

        SECRET_KEY = repr((''.join([secrets.choice(uni) for i in range(64)])).replace('\'', '"'))
        ACTIVATION_LINK_SECRET = repr((''.join([secrets.choice(uni) for i in range(64)])).replace('\'', '"'))
        DB_SECRET = repr((''.join([secrets.choice(uni) for i in range(64)])).replace('\'', '"'))
        EMAIL_SECRET_SALT = repr(str(bcrypt.gensalt().decode()))
        PRIVATE_KEY = repr(str(private_key_hex.decode()))
        PUBLIC_KEY = repr(str(public_key_hex.decode()))

        f.write(f'PSONO_SECRET_KEY={SECRET_KEY}\n')
        f.write(f'PSONO_ACTIVATION_LINK_SECRET={ACTIVATION_LINK_SECRET}\n')
        f.write(f'PSONO_DB_SECRET={DB_SECRET}\n')
        f.write(f'PSONO_EMAIL_SECRET_SALT={EMAIL_SECRET_SALT}\n')
        f.write(f'PSONO_PRIVATE_KEY={PRIVATE_KEY}\n')
        f.write(f'PSONO_PUBLIC_KEY={PUBLIC_KEY}\n')

if __name__ == '__main__':
    main()
