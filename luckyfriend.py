from tkinter import *
import random

root = Tk()
root.title("Luck friend Wheel")
root.geometry("400x400")
root.configure(background="purple")

nomes = ['Louise', 'Thomas', 'Mingau', 'Matheus', 'Luiza']
resultado = Label(root, bg = "purple")

def indice_aleatorio():
    indice = random.randint(0,4)
    pessoa = nomes[indice]
    resultado["text"] = pessoa

btn = Button(root)
btn = Button(root, text="Quem será?", command=indice_aleatorio)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)

resultado.place(relx = 0.5, rely=0.6, anchor = CENTER)

root.mainloop()
