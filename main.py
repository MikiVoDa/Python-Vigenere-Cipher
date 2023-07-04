import tkinter as tk

#-------UI----------------------
# crearea ferestrei
window = tk.Tk()
window.title("Vigenere Cipher")
window.geometry("800x150")


# label-urile pentru intrebari si textbox-uri
lb_text = tk.Label(window, text="Text:")
lb_coded = tk.Label(window, text="Textul codat:")
lb_decoded = tk.Label(window, text="Textul decodat:")
lb_key = tk.Label(window, text="Cheie: ")


text = tk.Entry(window, width=40)
coded = tk.Entry(window, width=40)
decoded = tk.Entry(window, width=40)
key = tk.Entry(window, width=40)

#functie pentru a genera cheia
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return (key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return ("".join(key))

#functie pentru a cifra textul
def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return ("".join(cipher_text))

#functie pentru a decifra textul
def decipherText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return ("".join(orig_text))

#butonul de start va efectua si cifrarea/decifrarea textului
def start():
    coded.delete(0, 'end')
    decoded.delete(0, 'end')

    text_value = text.get().upper()
    key_value = (key.get()).upper()

    cipher_key = generateKey(text_value, key_value)
    cipher_text = cipherText(text_value, cipher_key)
    decipher_text = decipherText(text_value, cipher_key)


    coded.insert(0, f"{cipher_text}")
    decoded.insert(0, f"{decipher_text}")


# butonul de start
bt_start = tk.Button(window, text="      Start      ", command=start)


# adaugarea in pagina a elementelor
lb_text.grid(row=1, column=1, padx=10, pady=10)
text.grid(row=1, column=2, padx=10, pady=10)

lb_key.grid(row=2, column=1, padx=10, pady=10)
key.grid(row=2, column=2, padx=10, pady=10)

lb_coded.grid(row=1, column=3, padx=10, pady=10)
coded.grid(row=1, column=4, padx=10, pady=10)

lb_decoded.grid(row=2, column=3, padx=10, pady=10)
decoded.grid(row=2, column=4, padx=10, pady=10)

bt_start.grid(row=3, column=5, padx=10, pady=10)


window.mainloop()
