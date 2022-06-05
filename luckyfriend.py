from logging import PlaceHolder
from tkinter import *
import random

root = Tk()
root.title("Luck friend Wheel")
root.geometry("400x400")
root.configure(background="purple")

entername = Entry(root)
nomes = []
resultado = Label(root, bg = "purple")
random_number_label = Label(root, bg = "purple")

def addfriend():
    nome_amigo = entername.get()
    nomes.append(nome_amigo)
    resultado["text"] = "Sua lista de amigos: " + str(nomes)

def amigo_aleatorio():
    length = len(nomes)
    indice = random.randint(0, length-1)
    random_number_label["text"] = str(indice)
    pessoa = nomes[indice]
    resultado["text"] = str(pessoa)

btn = Button(root)
btn = Button(root, text="Adicionar", command=addfriend)
btn.place(relx=0.5, rely=0.3, anchor=CENTER)

btn = Button(root)
btn = Button(root, text="Quem será o escolhido?", command=amigo_aleatorio)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

resultado.place(relx = 0.5, rely=0.7, anchor = CENTER)
random_number_label.place(relx = 0.5, rely=0.6, anchor = CENTER)
entername.place(relx=0.5, rely=0.2, anchor=CENTER)

root.mainloop()
