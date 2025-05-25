from gost import GOST_Kuz_Expand_Key, GOST_Kuz_Encrypt, GOST_Kuz_Decrypt
import os
from tkinter import *

class EncryptionApp:
    def __init__(self, master):
        self.master = master
        master.title("GOST Encryption")

        self.label_key1 = Label(master, text="Key 1 (32 hex characters = 16 bytes):")
        self.label_key1.pack()
        self.entry_key1 = Entry(master, width=50)
        self.entry_key1.pack()

        self.label_key2 = Label(master, text="Key 2 (32 hex characters = 16 bytes):")
        self.label_key2.pack()
        self.entry_key2 = Entry(master, width=50)
        self.entry_key2.pack()

        self.label_block = Label(master, text="Block:")
        self.label_block.pack()
        self.entry_block = Entry(master, width=50)
        self.entry_block.pack()

        self.random_key_button = Button(master, text="Random key", command=self.generate_random_key)
        self.random_key_button.pack()

        self.random_value_button = Button(master, text="Random value", command=self.generate_random_value)
        self.random_value_button.pack()

        self.encrypt_button = Button(master, text="Encrypt", command=self.encrypt_data)
        self.encrypt_button.pack()

        self.decrypt_button = Button(master, text="Decrypt", command=self.decrypt_data)
        self.decrypt_button.pack()

        self.result_text = Text(master, height=10, width=50)
        self.result_text.pack()

        self.scrollbar = Scrollbar(master, command=self.result_text.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.result_text.config(yscrollcommand=self.scrollbar.set)

    def generate_random_key(self):
        random_key1 = os.urandom(16).hex()
        random_key2 = os.urandom(16).hex()
        self.entry_key1.delete(0, END)
        self.entry_key1.insert(0, random_key1)
        self.entry_key2.delete(0, END)
        self.entry_key2.insert(0, random_key2)

    def generate_random_value(self):
        random_value = os.urandom(16).hex()
        self.entry_block.delete(0, END)
        self.entry_block.insert(0, random_value)

    def encrypt_data(self):
        key1_hex = self.entry_key1.get().strip()
        key2_hex = self.entry_key2.get().strip()
        block_str = self.entry_block.get().strip()

        encrypted = []
        if len(key1_hex) != 32 or len(key2_hex) != 32:
            self.result_text.delete(1.0, END)
            self.result_text.insert(END, "Error: All inputs must be 32 hex characters.")
            return
        
        block_hex = block_str.encode('utf-8').hex()
        print(len(block_hex))
        print(block_hex)
        print("*******")
        if len(block_hex) != 32:
            if len(block_hex) < 32:
                block_hex += '0' * (32 - len(block_hex))
                key1 = list(bytes.fromhex(key1_hex))
                key2 = list(bytes.fromhex(key2_hex))
                block = list(bytes.fromhex(block_hex))

                GOST_Kuz_Expand_Key(key1, key2)
                encrypted = GOST_Kuz_Encrypt(block)

                self.result_text.delete(1.0, END)
                self.result_text.insert(END, f"Encrypted: {''.join(f'{x:02X}' for x in encrypted)}\n")
            elif len(block_hex) > 32:
                list_block_hex = []
                while block_hex != "":
                    if len(block_hex) > 32:
                        list_block_hex.append(block_hex[:32])
                        block_hex = block_hex[32:]   
                    else:
                        list_block_hex.append(block_hex)
                        block_hex = ""
                        list_block_hex[len(list_block_hex) - 1] += '0' * (32 - len(list_block_hex[len(list_block_hex) - 1]))
                for i, j in enumerate(list_block_hex):
                    if len(list_block_hex[i]) != 32:
                        self.result_text.delete(1.0, END)
                        self.result_text.insert(END, "Error: Block must be 32 hex characters.")
                        return
                    else:
                        key1 = list(bytes.fromhex(key1_hex))
                        key2 = list(bytes.fromhex(key2_hex))
                        block = list(bytes.fromhex(j))

                        GOST_Kuz_Expand_Key(key1, key2)
                        encrypted += GOST_Kuz_Encrypt(block)
                self.result_text.delete(1.0, END)
                self.result_text.insert(END, f"Encrypted: {''.join(f'{x:02X}' for x in encrypted)}\n")
            return


        key1 = list(bytes.fromhex(key1_hex))
        key2 = list(bytes.fromhex(key2_hex))
        block = list(bytes.fromhex(block_hex))

        GOST_Kuz_Expand_Key(key1, key2)
        encrypted = GOST_Kuz_Encrypt(block)

        self.result_text.delete(1.0, END)
        self.result_text.insert(END, f"Encrypted: {''.join(f'{x:02X}' for x in encrypted)}\n")
        
    def decrypt_data(self):
        decrypted_str = ""
        key1_hex = self.entry_key1.get().strip()
        key2_hex = self.entry_key2.get().strip()
        # block_hex = self.entry_block.get().strip()
        block_hex =self.result_text.get("1.0", END).strip()
        block_hex = block_hex.replace("Encrypted: ", "").replace("Decrypted: ", "").replace("\n", "").replace(" ", "")
        print("decrypt:", block_hex)
        if len(key1_hex) != 32 or len(key2_hex) != 32:
            self.result_text.delete(1.0, END)
            self.result_text.insert(END, "Error: All inputs must be 32 hex characters.")
            return

        if len(block_hex) > 32:
            list_block_hex = []
            while block_hex != "":
                if len(block_hex) > 32:
                    list_block_hex.append(block_hex[:32])
                    block_hex = block_hex[32:]   
                else:
                    list_block_hex.append(block_hex)
                    block_hex = ""
            for i, j in enumerate(list_block_hex):
                if len(list_block_hex[i]) != 32:
                    self.result_text.delete(1.0, END)
                    self.result_text.insert(END, "Error: Block must be 32 hex characters.")
                    return
                else:
                    key1 = list(bytes.fromhex(key1_hex))
                    key2 = list(bytes.fromhex(key2_hex))
                    block = list(bytes.fromhex(j))

                    GOST_Kuz_Expand_Key(key1, key2)
                    decrypted_hex = GOST_Kuz_Decrypt(block)
                    decrypted = ''.join(f'{x:02X}' for x in decrypted_hex)
                    decrypted_str += bytes.fromhex(decrypted).decode("utf-8")
            self.result_text.delete(1.0, END)
            self.result_text.insert(END, f"Decrypted: {decrypted_str}\n")
            return

        key1 = list(bytes.fromhex(key1_hex))
        key2 = list(bytes.fromhex(key2_hex))
        block = list(bytes.fromhex(block_hex))

        GOST_Kuz_Expand_Key(key1, key2)
        decrypted_hex = GOST_Kuz_Decrypt(block)
        decrypted = ''.join(f'{x:02X}' for x in decrypted_hex)
        decrypted = bytes.fromhex(decrypted).decode("utf-8")


        self.result_text.delete(1.0, END)
        self.result_text.insert(END, f"Decrypted: {decrypted}\n")

if __name__ == "__main__":
    root = Tk()
    app = EncryptionApp(root)
    root.mainloop()