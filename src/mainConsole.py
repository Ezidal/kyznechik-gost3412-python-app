from gost import *

def mainStdIn():
    import binascii

    def input_hex_block(prompt: str) -> List[int]:
        while True:
            try:
                hex_str = input(prompt).strip().replace(' ', '')
                if len(hex_str) != 32 and len(hex_str) != 0:
                    raise ValueError("Нужно ввести ровно 16 байт (32 hex-символа)")
                return list(binascii.unhexlify(hex_str))
            except Exception as e:
                print("Ошибка:", e)
    full_key_ex = os.urandom(32)
    key1ex = list(full_key_ex[:16])
    key2ex = list(full_key_ex[16:])
    print("Введите ключ (32 hex-символа = 16 байт) — первая половина (key1)")
    print("Пример ключа:", ''.join(f'{x:02X}' for x in key1ex))
    print("Если хотите использовать пример ключа, просто нажмите Enter.")
    print("Если хотите ввести свой ключ, введите его целиком.")
    key1 = input_hex_block("key1: ")
    if not key1:
        key1 = key1ex
    print("key1:", ''.join(f'{x:02X}' for x in key1))
    print("*------------------------------------------------*")


    print("Введите ключ (32 hex-символа = 16 байт) — вторая половина (key2):")
    print("Пример ключа:", ''.join(f'{x:02X}' for x in key2ex))
    print("Если хотите использовать пример ключа, просто нажмите Enter.")
    print("Если хотите ввести свой ключ, введите его целиком.")
  
    key2 = input_hex_block("key2: ")
    if not key2:
        key2 = key2ex
    print("key2:", ''.join(f'{x:02X}' for x in key2))
    print("*------------------------------------------------*")
   
    
    print("Введите блок для шифрования (32 hex-символа = 16 байт):")
    print
    blk = input_hex_block("Блок: ")
    GOST_Kuz_Expand_Key(key1, key2)

    encrypted = GOST_Kuz_Encrypt(blk)
    print("Encrypted:", ''.join(f'{x:02X}' for x in encrypted))

    decrypted = GOST_Kuz_Decrypt(encrypted)
    print("Decrypted:", ''.join(f'{x:02X}' for x in decrypted))

if __name__ == "__main__":
       mainStdIn()