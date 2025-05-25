from tkinter import Tk, Label, Entry, Button, Text, Scrollbar, END
from gost import GOST_Kuz_Expand_Key, GOST_Kuz_Encrypt, GOST_Kuz_Decrypt

def encrypt_data():
    key1 = entry_key1.get().strip()
    key2 = entry_key2.get().strip()
    block = entry_block.get().strip()

    if len(key1) != 32 or len(key2) != 32 or len(block) != 32:
        text_output.delete(1.0, END)
        text_output.insert(END, "Ошибка: Все вводимые данные должны быть 32 hex-символа (16 байт).")
        return

    key1_bytes = list(bytes.fromhex(key1))
    key2_bytes = list(bytes.fromhex(key2))
    block_bytes = list(bytes.fromhex(block))

    GOST_Kuz_Expand_Key(key1_bytes, key2_bytes)
    encrypted = GOST_Kuz_Encrypt(block_bytes)
    decrypted = GOST_Kuz_Decrypt(encrypted)

    text_output.delete(1.0, END)
    text_output.insert(END, f"Encrypted: {''.join(f'{x:02X}' for x in encrypted)}\n")
    text_output.insert(END, f"Decrypted: {''.join(f'{x:02X}' for x in decrypted)}\n")

app = Tk()
app.title("Kuznechik Encryption App")

label_key1 = Label(app, text="Введите ключ 1 (32 hex-символа):")
label_key1.pack()

entry_key1 = Entry(app, width=50)
entry_key1.pack()

label_key2 = Label(app, text="Введите ключ 2 (32 hex-символа):")
label_key2.pack()

entry_key2 = Entry(app, width=50)
entry_key2.pack()

label_block = Label(app, text="Введите блок для шифрования (32 hex-символа):")
label_block.pack()

entry_block = Entry(app, width=50)
entry_block.pack()

button_encrypt = Button(app, text="Зашифровать", command=encrypt_data)
button_encrypt.pack()

text_output = Text(app, height=10, width=50)
text_output.pack()

scrollbar = Scrollbar(app, command=text_output.yview)
scrollbar.pack(side='right', fill='y')
text_output.config(yscrollcommand=scrollbar.set)

app.mainloop()