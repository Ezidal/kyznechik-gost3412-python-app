from gost import *
import os

def mainRandom():
    full_key = os.urandom(32)
    key1 = list(full_key[:16])
    key2 = list(full_key[16:])

    blk = [0x99, 0x99, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF,
           0x00, 0x77, 0x66, 0x55, 0x44, 0x33, 0x22, 0x11]

    GOST_Kuz_Expand_Key(key1, key2)

    encrypted = GOST_Kuz_Encrypt(blk)
    print("Encrypted:", ''.join(f'{x:02X}' for x in encrypted))

    decrypted = GOST_Kuz_Decrypt(encrypted)
    print("Decrypted:", ''.join(f'{x:02X}' for x in decrypted))

if __name__ == "__main__":
       mainRandom()