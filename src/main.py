from tkinter import Tk, END
from gost import GOST_Kuz_Expand_Key, GOST_Kuz_Encrypt, GOST_Kuz_Decrypt
from gui import EncryptionApp

if __name__ == "__main__":
    root = Tk()
    app = EncryptionApp(root)
    root.mainloop()