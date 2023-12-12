from util import install_dependencies

install_dependencies()

import tkinter as tk
from tkinter import messagebox, Label
from coordenadas import info
from Calculador_Distancia import calcular_distancia
from PIL import ImageTk, Image

partida = None
llegada = None

_, lugares = info()

nombres_a_ids = {lugares[id_lugar]["nombre"]: id_lugar for id_lugar in lugares}

def obtener_seleccion():
    global partida, llegada
    indices = listbox.curselection()
    if len(indices) == 2:
        partida = nombres_a_ids[listbox.get(indices[0])]
        llegada = nombres_a_ids[listbox.get(indices[1])]
        messagebox.showinfo(
            title="Ítems seleccionados",
            message=f"Partida: {lugares[partida]['nombre']}, Llegada: {lugares[llegada]['nombre']}"
        )
        calcular_distancia(partida, llegada)
    else:
        messagebox.showinfo(
            title="Error",
            message="Por favor, selecciona dos lugares."
        )

def limitar_seleccion(event):
    indices = listbox.curselection()
    if len(indices) > 2:
        listbox.selection_clear(indices[2:])

ventana = tk.Tk()
ventana.geometry("400x300")
ventana.title("Lista en Tk")

def background(ventana):
    bg_image_path = ("./resources/background.png")
    bg_image = Image.open(bg_image_path).resize((1280, 720))
    ventana.bg = ImageTk.PhotoImage(bg_image)
    Label(ventana, image=ventana.bg).place(x=0, y=0, relwidth=1, relheight=1)

background(ventana)
listbox = tk.Listbox(ventana, selectmode=tk.MULTIPLE)
listbox.bind('<<ListboxSelect>>', limitar_seleccion)

for id_lugar in lugares:
    listbox.insert(tk.END, lugares[id_lugar]["nombre"]) 
listbox.pack()

boton_obtener_seleccion = tk.Button(
    text="Obtener selección",
    command=obtener_seleccion
)
boton_obtener_seleccion.pack()

ventana.mainloop()