from tkinter import *

# Função para calcular a conversão da temperatura
# C = (F - 32) * 5/9

def calcular():
    F = float(textbox1.get())
    C = (F-32) * 5/9
    final.set(str(round(C,1)) + " graus Celsius")

# Interface Gráfica
root = Tk()
root.title("Conversor de Temperatura")
root.geometry("250x225")
root.configure(bg="azure")  # Cor de fundo azul-claro
final = StringVar()

# Cálculos e Informações da conversão da temperatura
label1=Label(root,text="Graus Fahrenheit: ", bg="azure", font=("Arial", 15))
textbox1=Entry(root, font=("Arial", 15))
button1=Button(root,text="Calcular", command=calcular, bg="blueviolet", fg="mintcream", font=("Arial", 15, "bold"))
label_resultado=Label(root, textvariable=final, bg="azure", fg="blueviolet", font=("Arial", 15, "bold"))

#layout
label1.grid()
textbox1.grid()
button1.grid()
label_resultado.grid()

root.mainloop()
