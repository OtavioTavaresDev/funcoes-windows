from tkinter import *
from tkinter import ttk
import pyautogui as pa


def printscreen():
    pa.press("printscreen")

def windows():
    pa.press("winright")

def aumentarVL():
    pa.press("volumeup")

def diminuirVL():
    pa.press("volumedown")

janela = Tk()
janela.geometry("500x500")
bmvdo = ttk.Label(janela, text="Funções do Windows."). grid(column=3, row=0)
prnt = ttk.Button(janela, command=printscreen, text="Print Screen.").grid(column=2, row=6)
wndows = ttk.Button(janela, command=windows, text="windows.").grid(column=5, row=6)
diminuir_volume = ttk.Button(janela, command=diminuirVL, text="Diminuir o volume do áduio.").grid(column=2, row=8)
aumentar_volume = ttk.Button(janela, command=aumentarVL, text="Aumentar o volume do áudio.").grid(column=5, row=8)

janela.mainloop()