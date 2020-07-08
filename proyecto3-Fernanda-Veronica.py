from tkinter import *

class Vestuario:
    def __init__(self):
        self.vestuario = {
            "accesorios": ["Lentes", "Reloj", "Brazalete", "Piercing", "Cadena", "Aretes", "Anillo", "Cintorón",
                           "Sombrero", "Ninguno"],
            "ropa": ["Formal", "Informal", "Casual", "Deportivo", "Baño", "Etiqueta", "Invierno", "Trabajo",
                     "Uniforme"],
            "calzado": ["Botas", "Tenis", "Zapatilla", "Sandalias", "Mocasines", "Náuticos", "Pantuflas",
                        "Tacones"]}  # Attributes assigned

    def setAccesorios(self, accesorios):  # Assign value in the dictionary in the accessories position
        self.vestuario["accesorios"] = accesorios

    def setRopa(self, ropa):  # Assign value in dictionary at outfit position
        self.vestuario["ropa"] = ropa

    def setCalzado(self, calzado):  # Assign value in the dictionary in the shoe position
        self.vestuario["calzado"] = calzado

    def getLenAccesorios(self):  # Get which one gets the length from the list in accessory position
        return len(self.vestuario["accesorios"])

    def getAccesorios(self):  # Get that gets the accesory in X position
        return self.vestuario["accesorios"]

    def getLenRopa(self):  # Get which gets the length of the list in the outfit position
        return len(self.vestuario["ropa"])

    def getAccesorio(self, indice):
        return self.vestuario["accesorios"][indice[0]]

    def getRopas(self, indice):
        return self.vestuario["ropa"][indice]

    def getCalzados(self, indice):
        return self.vestuario["calzado"][indice]

    def getLenRopa(self):
        return len(self.vestuario["ropa"])

    def getRopa(self):  # Get that gets the outfit in X position
        return self.vestuario["ropa"]

    def getLenCalzado(self):  # Get which one gets the length from the list in the shoe position
        return len(self.vestuario["calzado"])

    def getCalzado(self):  # Get that gets the shoe in X position
        return self.vestuario["calzado"]

    def getAccesorio(self, indice):
        return self.vestuario["accesorios"][indice[0]]

    def getRopas(self, indice):
        return self.vestuario["ropa"][indice]  # Gets the value in the dictionary in the outfit key at x position

    def getCalzados(self, indice):
        return self.vestuario["calzado"][indice]  # Gets the value in the dictionary in the shoe key at x position


def createAvatar(ventana):

    ventana_create = Toplevel()
    ventana_create.config(bg = "pink")
    ventana_create.title("Create Avatar")
    ventana_create.geometry("500x400")
    label1 = Label(ventana_create, bg="pink", text="Graphic Avatar Simulator", font="Time, 20").pack(padx=20, pady=40)
    label3 = Label(ventana_create, bg="pink", text="CREATE AVATAR", font="Arial, 15").pack()
    ventana.withdraw()

def ingresar(v,e1,e2, nombre,contrasenna):

    if nombre == "fer" and contrasenna =="123":

        ventana_ingresar = Toplevel()
        ventana_ingresar.config(background="pink")
        ventana_ingresar.title("Administrator")
        ventana_ingresar.geometry("500x400")
        label1 = Label(ventana_ingresar, bg="pink", text="Graphic Avatar Simulator", font="Time, 20").pack(padx=20,pady=40)
        saludo = ("Welcome " + nombre)
        label3 = Label(ventana_ingresar,bg = "pink", text=saludo,font="Arial, 15").pack()
        Button(ventana_ingresar, text="Create Avatar",command = lambda:createAvatar(ventana_ingresar),font="Arial, 11").pack(padx=10, pady=20)
        Button(ventana_ingresar, text="Dress up Avatar", font="Arial, 11").pack(padx=10, pady=20)
        v.withdraw()

    else:
        ventana_ingresar = Toplevel()
        ventana_ingresar.config(background="pink")
        ventana_ingresar.title("Analyst")
        ventana_ingresar.geometry("500x400")
        label1 = Label(ventana_ingresar, bg="pink", text="Graphic Avatar Simulator", font="Time, 20").pack(padx=20,pady=40)
        saludo = ("Welcome " + nombre)
        label3 = Label(ventana_ingresar, bg="pink", text=saludo, font="Arial, 15").pack()
        Button(ventana_ingresar, text="Report 1", font="Arial, 11").pack(padx=10, pady=20)
        Button(ventana_ingresar, text="Report 2", font="Arial, 11").pack(padx=10, pady=20)
        v.withdraw()

    def regresar():
        ventana_ingresar.destroy()
        v.deiconify()

    boton_destruir = Button(ventana_ingresar, text="Exit",font="Arial,11", command=lambda: regresar()).pack(padx=0, pady=20)
    v.wait_window(ventana_ingresar)

def ventanaPrincipal():
    ventana = Tk()  # ventana padre
    ventana.config(background="pink")
    ventana.title("Graphic avatar simulator")
    ventana.geometry("600x400")  # el tamaño

    # direccion = PhotoImage(file="avion.png")  # dirección de la imagen
    # imagen = Label(ventana, image=direccion).place(x=0, y=0)  # .place(x,y) uno le dice en qué posición lo quiere

    #TITULO
    label1 = Label(ventana, bg="pink", text="Welcome Graphic Avatar Simulator", font="Time, 20").pack(padx=20,pady=40)  #.pack() lo centra

    #DIGITAR EL USUARIO
    label2 = Label(ventana, bg="pink",text="User", font="Arial, 15").pack(padx=5, pady=5)  # .pack() lo centra
    entry_nombre_usuario = Entry(ventana, font="Arial, 12")
    entry_nombre_usuario.pack(padx=5, pady=5)

    #DIGITAR LA CONTRASEÑA
    label3 = Label(ventana, bg="pink", text="Password", font="Arial, 15").pack(padx=5, pady=5)  # .pack() lo centra
    entry_contraseña = Entry(ventana, show="*", font="Arial, 12")
    entry_contraseña.pack(padx=5, pady=5)


    Button(ventana, text="LOGIN",command = lambda:ingresar(ventana,entry_nombre_usuario,entry_contraseña,entry_nombre_usuario.get(),entry_contraseña.get()),font="Arial, 13").pack(padx=5, pady=10)
    Button(ventana, text="EXIT", font="Arial, 11").pack(padx=0, pady=0)
    ventana.mainloop()  # para que la ventana no se cierre la ventana


def main():
    ventanaPrincipal()


main()
