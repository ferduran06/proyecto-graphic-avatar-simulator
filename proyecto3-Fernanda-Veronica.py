from tkinter import *
import os
from PIL import Image, ImageTk

from tkinter import messagebox as MessageBox

path = 'C:/Users/hp/Documents/GitHub/proyecto-graphic-avatar-simulator/AVATARS/'
files = os.listdir(path)

class Vestuario:
    def __init__(self):
        self.vestuario = {"accesorios": ["Lentes", "Reloj", "Gorra", "Sombrero", "Ninguno"],
                            "ropa": ["Formal", "Casual", "Deportivo", "Bikini"],
            "calzado": ["Tenis", "Zapatilla", "Pantuflas","Tacones"]}  # Attributes assigned

    def setAccesorios(self, accesorios):  # Assign value in the dictionary in the accessories position
        self.vestuario["accesorios"] = accesorios

    def setRopa(self, ropa):  # Assign value in dictionary at outfit position
        self.vestuario["ropa"] = ropa

    def setCalzado(self, calzado):  # Assign value in the dictionary in the shoe position
        self.vestuario["calzado"] = calzado

    def getAccesorios(self):  # Get that gets the accesory in X position
        return self.vestuario["accesorios"]

    def getAccesorio(self, indice):
        return self.vestuario["accesorios"][indice]

    def getRopas(self, indice):
        return self.vestuario["ropa"][indice]

    def getCalzados(self, indice):
        return self.vestuario["calzado"][indice]

    def getRopa(self):  # Get that gets the outfit in X position
        return self.vestuario["ropa"]

    def getCalzado(self):  # Get that gets the shoe in X position
        return self.vestuario["calzado"]


class Piel:
    def __init__(self):
        self.piel = ["Negra","Morena","Piel", "Blanca"]  # Attributes assigned

    def set(self, piel):
        self.piel = piel

    def getPiel(self):
        return self.piel

    def getPielIndice(self, indice):
        return self.piel[indice]

class Cabello:
    def __init__(self):
        self.cabello = ["Lacio", "Ondulado", "Rizado"]  # Attributes assigned

    def set(self, cabello):
        self.cabello = cabello

    def getTextura(self):
        return self.cabello

    def getTexturaIndice(self, indice):
        return self.cabello[indice]

class ColorCabello:
    def __init__(self):
        self.ColorCabello = ["Negro", "Castaño", "Rubia"]  # Attributes assigned

    def setColorCabello(self, colorCabello):
        self.ColorCabello = colorCabello  # Assign value in the dictionary in the eye shape position

    def getColorCabello(self):  # Get that gets the eye shape in X position
        return self.ColorCabello

    def getColorCabelloIndice(self, indice):
        return self.ColorCabello[indice]

class Genero:
    def __init__(self):
        self.genero = ["Femenino", "Masculino"]  # Attributes assigned

    def set(self, genero):
        self.genero = genero

    def getGenero(self):
        return self.genero

    def getgeneros(self, indice):
        return self.genero[indice]

def ventanaPrincipal():
    ventana = Tk()  # ventana padre
    ventana.config(background="pink")
    ventana.title("Graphic avatar simulator")
    ventana.geometry("600x400")  # el tamaño

    # direccion = PhotoImage(file="avion.png")  # dirección de la imagen
    # imagen = Label(ventana, image=direccion).place(x=0, y=0)  # .place(x,y) uno le dice en qué posición lo quiere

    #TITULO
    label1 = Label(ventana, background="pink", text="Welcome Graphic Avatar Simulator", font="Time, 20").pack(padx=20,pady=40)  #.pack() lo centra

    #DIGITAR EL USUARIO
    Label(ventana, background="pink",text="User", font="Arial, 15").pack(padx=5, pady=5)  # .pack() lo centra
    entry_nombre_usuario = Entry(ventana, font="Arial, 12")
    entry_nombre_usuario.pack(padx=5, pady=5)

    #DIGITAR LA CONTRASEÑA
    Label(ventana, background="pink", text="Password", font="Arial, 15").pack(padx=5, pady=5)  # .pack() lo centra
    entry_contraseña = Entry(ventana, show="*", font="Arial, 12")
    entry_contraseña.pack(padx=5, pady=5)


    Button(ventana, text="LOGIN",command = lambda:ingresar(ventana,entry_nombre_usuario,entry_contraseña,entry_nombre_usuario.get(),entry_contraseña.get()),font="Arial, 13").pack(padx=5, pady=10)
    Button(ventana, text="EXIT", font="Arial, 11").pack(padx=0, pady=0)
    ventana.mainloop()

def admin(v,nombre):
    ventana_ingresar = Toplevel()
    ventana_ingresar.config(background="pink")
    ventana_ingresar.title("Administrator")
    ventana_ingresar.geometry("500x400")

    Label(ventana_ingresar, bg="pink", text="Graphic Avatar Simulator", font="Time, 20").pack(padx=20, pady=40)
    saludo = ("Welcome " + nombre)

    Label(ventana_ingresar, bg="pink", text=saludo, font="Arial, 15").pack()
    Button(ventana_ingresar, text="Create Avatar", command=lambda: createAvatar(ventana_ingresar),
           font="Arial, 11").pack(padx=10, pady=20)

    Button(ventana_ingresar, text="Dress up Avatar", command=lambda: dressingAvatar(ventana_ingresar),
           font="Arial, 11").pack(padx=10, pady=20)

    def regresar():
        ventana_ingresar.destroy()
        v.deiconify()

    Button(ventana_ingresar, text="Exit", font="Arial,11", command=lambda: regresar()).pack(padx=0, pady=20)
    v.withdraw()

def analista(v,nombre):
    ventana_ingresar = Toplevel()
    ventana_ingresar.config(background="pink")
    ventana_ingresar.title("Analyst")
    ventana_ingresar.geometry("500x400")

    Label(ventana_ingresar, bg="pink", text="Graphic Avatar Simulator", font="Time, 20").pack(padx=20,pady=40)
    saludo = ("Welcome " + nombre)

    Label(ventana_ingresar, bg="pink", text=saludo, font="Arial, 15").pack()
    Button(ventana_ingresar, text="Report 1: GENDER", command= lambda:mostrar_Consulta1(ventana_ingresar,nombre),font="Arial, 11").pack(padx=10, pady=20)
    Button(ventana_ingresar, text="Report 2: SKIN", command= lambda:mostrar_Consulta2(ventana_ingresar,nombre),font="Arial, 11").pack(padx=10, pady=20)

    def regresar():
        ventana_ingresar.destroy()
        v.deiconify()

    Button(ventana_ingresar, text="Exit", font="Arial,11", command=lambda: regresar()).pack(padx=0, pady=20)
    v.withdraw()


def ingresar(v,e1,e2, nombre,contrasenna):

    if nombre == "fer" and contrasenna =="123":
        admin(v,nombre)

    elif nombre == "Vero" and contrasenna == "1234":
        analista(v,nombre)

    else:
        MessageBox.showerror("Error", "INVALID DATA. TRY AGAIN")

def creaciontxt(id):
    archi = open(str(id)+'.txt', 'w')
    archi.close()

def createAvatar(ventana):
    ventana_create = Toplevel()
    ventana_create.config(bg = "pink")
    ventana_create.title("Create Avatar")
    ventana_create.geometry("400x400")

    Label(ventana_create, bg="pink", text="Graphic Avatar Simulator", font="Time, 20").pack(padx=20, pady=40)
    Label(ventana_create, bg="pink", text="CREATE AVATAR", font="Arial, 15").pack()
    Label(ventana_create, bg="pink", text="Enter your ID to be previously registered ", font="Arial, 14").pack(padx=10,
                                                                                                               pady=10)
    cedula = Entry(ventana_create, font="Arial, 13")
    cedula.pack(padx=10, pady=10)
    Button(ventana_create, command =lambda :registerSkin(ventana,cedula,cedula.get()),text="Next",font="Arial, 11").pack(padx=10,pady=20)

    ventana.withdraw()

def registerSkin(ventana,c,cedula):
    skin = Piel()
    c = 0
    selected = IntVar()

    ventana_skin = Toplevel()
    ventana_skin.config(bg = "pink")
    ventana_skin.title("Create Avatar")
    ventana_skin.geometry("500x500")

    Label(ventana_skin, bg="pink", text="Graphic Avatar Simulator", font="Time, 20").pack(padx=20, pady=40)
    Label(ventana_skin, bg="pink", text="SKIN COLORS AVATAR", font="Arial, 15").pack()
    Label(ventana_skin, bg="pink", text="COLORS ", font="Arial, 14").pack(padx=10, pady=10)
    Label(ventana_skin, bg="pink", text="Select an option ", font="Arial, 13").pack(padx=10, pady=10)

    for i in skin.getPiel():
        Radiobutton(ventana_skin,bg="pink",text=i,variable=selected,value=c,font="Arial, 12").pack()
        c += 1

    Button(ventana_skin, command=lambda: registerHair(ventana_skin, cedula, selected.get()), text="Next",
           font="Arial, 11").pack(padx=10, pady=20)
    ventana.destroy()

def registerHair(ventana,cedula,skin):

    hair = Cabello()
    c = 0

    selected = IntVar()
    ventana_hair = Toplevel()
    ventana_hair.config(bg = "pink")
    ventana_hair.title("Create Avatar")
    ventana_hair.geometry("500x500")
    Label(ventana_hair, bg="pink", text="Graphic Avatar Simulator", font="Time, 20").pack(padx=20, pady=40)
    Label(ventana_hair, bg="pink", text="HAIR TEXTURE AVATAR", font="Arial, 15").pack()
    Label(ventana_hair, bg="pink", text="TEXTURE ", font="Arial, 14").pack(padx=10, pady=10)
    Label(ventana_hair, bg="pink", text="Select an option ", font="Arial, 13").pack(padx=10, pady=10)
    for i in hair.getTextura():
        Radiobutton(ventana_hair,bg="pink",text=i,variable=selected,value=c,font="Arial, 12").pack()
        c += 1
    Button(ventana_hair, command=lambda: registerEyes(ventana_hair, cedula, skin,selected.get()), text="Next",
           font="Arial, 11").pack(padx=10, pady=20)
    ventana.destroy()


def registerEyes(ventana,cedula,skin,hair):

    colorHair = ColorCabello()
    c = 0

    selected = IntVar()

    ventana_hairs = Toplevel()
    ventana_hairs.config(bg = "pink")
    ventana_hairs.title("Create Avatar")
    ventana_hairs.geometry("600x600")

    Label(ventana_hairs, bg="pink", text="Graphic Avatar Simulator", font="Time, 20").pack(padx=20, pady=40)
    Label(ventana_hairs, bg="pink", text="EYE SHAPE AVATAR", font="Arial, 15").pack()
    Label(ventana_hairs, bg="pink", text="SHAPE ", font="Arial, 14").pack(padx=10, pady=10)
    Label(ventana_hairs, bg="pink", text="Select an option ", font="Arial, 13").pack(padx=10, pady=10)
    for i in colorHair.getColorCabello():
        Radiobutton(ventana_hairs,bg="pink",text=i,variable=selected,value=c,font="Arial, 12").pack()
        c += 1
    Button(ventana_hairs, command=lambda: registerGender(ventana_hairs, cedula,skin,hair, selected.get()), text="Next",
           font="Arial, 11").pack(padx=10, pady=20)
    ventana.destroy()

def registerGender(ventana,cedula,skin,hair,eyes):

    gender = Genero()
    c = 0
    selected = IntVar()

    ventana_gender = Toplevel()
    ventana_gender.config(bg = "pink")
    ventana_gender.title("Create Avatar")
    ventana_gender.geometry("500x500")
    Label(ventana_gender, bg="pink", text="Graphic Avatar Simulator", font="Time, 20").pack(padx=20, pady=40)
    Label(ventana_gender, bg="pink", text="EYE SHAPE AVATAR", font="Arial, 15").pack()
    Label(ventana_gender, bg="pink", text="SHAPE ", font="Arial, 14").pack(padx=10, pady=10)
    Label(ventana_gender, bg="pink", text="Select an option ", font="Arial, 13").pack(padx=10, pady=10)
    for i in gender.getGenero():
        Radiobutton(ventana_gender,bg="pink",text=i,variable=selected,value=c,font="Arial, 12").pack()
        c += 1
    Button(ventana_gender, command=lambda: mostrarInfor(ventana_gender, cedula, skin, hair,eyes, selected.get()),
           text="Next",
           font="Arial, 11").pack(padx=10, pady=20)

    ventana.destroy()

def validarId(v,c,cedula):
    id = str(cedula)+'.txt'
    with os.scandir(path) as ficheros:
        for fichero in ficheros:
            if id  == fichero.name:
                dressOutfit(v,cedula)
            elif fichero== "":
                MessageBox.showerror("Error", "THIS ID IS NOT REGISTERED")

def mostrarColor(skin):

    piel = Piel()
    return piel.getPielIndice(skin)

def mostrarCabello(hair):

    cabello = Cabello()
    return cabello.getTexturaIndice(hair)

def mostrarOjos(hairs):

    colorHairs = ColorCabello()
    return colorHairs.getColorCabelloIndice(hairs)

def mostrarGenero(gender):

    genero = Genero()
    return genero.getgeneros(gender)

def guardarDatos(cedula,gender,skin,hair,eyes):
    nombreTxt = str(cedula)+".txt"
    archivo = open("AVATARS/"+nombreTxt,"w")
    archivo.write("INFORMATION AVATAR" + '\n')
    archivo.write("Genero " + str(gender) + '\n')
    archivo.write("Color Piel " + str(skin) + '\n')
    archivo.write("Pelo "+ str(hair) + '\n')
    archivo.write("Color Pelo "+ str(eyes) + '\n')
    archivo.close()

def mostrarInfor(ventana,cedula,skin,hair,eyes,gender):

    ventana_gender = Toplevel()
    ventana_gender.config(bg = "pink")
    ventana_gender.title("Create Avatar")
    ventana_gender.geometry("600x650")

    skins = mostrarColor(skin)
    hairs = mostrarCabello(hair)
    eye = mostrarOjos(eyes)
    genders = mostrarGenero(gender)

    Label(ventana_gender, bg="pink", text="Graphic Avatar Simulator", font="Time, 20").pack(padx=20, pady=30)
    Label(ventana_gender, bg="pink", text="SHOW INFORMATION", font="Arial, 15").pack()

    Label(ventana_gender, bg="pink", text="ID ", font='Arial, 13').pack(padx=10, pady=10)
    Label(ventana_gender, bg="pink", text=cedula, font="Arial, 12").pack()

    Label(ventana_gender, bg="pink", text="ITS GENDER", font='Arial, 13').pack(padx=10, pady=10)
    Label(ventana_gender, bg="pink", text=genders, font="Arial, 12").pack()

    Label(ventana_gender, bg="pink", text="YOUR SKIN COLOR", font='Arial, 13').pack(padx=10, pady=10)
    Label(ventana_gender, bg="pink", text=skins, font="Arial, 12").pack()

    Label(ventana_gender, bg="pink", text="YOUR SKIN COLOR", font='Arial, 13').pack(padx=10, pady=10)
    Label(ventana_gender, bg="pink", text=skins, font="Arial, 12").pack()

    Label(ventana_gender, bg="pink", text="YOUR HAIR TEXTURE", font='Arial, 13').pack(padx=10, pady=10)
    Label(ventana_gender, bg="pink", text=hairs, font="Arial, 12").pack()

    Label(ventana_gender, bg="pink", text="YOUR EYE SHAPE", font='Arial, 13').pack(padx=10, pady=10)
    Label(ventana_gender, bg="pink", text=eye, font="Arial, 12").pack()

    guardarDatos(cedula,gender,skin,hair,eyes)

    Button(ventana_gender, text="Exit",font="Arial,11", command=lambda: admin(ventana_gender,cedula) ).pack(padx=0, pady=20)

    ventana.destroy()

def dressingAvatar(ventana):

    ventana_create = Toplevel()
    ventana_create.config(bg = "pink")
    ventana_create.title("Create Avatar")
    ventana_create.geometry("400x400")

    Label(ventana_create, bg="pink", text="Graphic Avatar Simulator", font="Time, 20").pack(padx=20, pady=40)
    Label(ventana_create, bg="pink", text="AVATAR OF DRESSING", font="Arial, 15").pack()
    Label(ventana_create, bg="pink", text="Enter your ID to choose your outfit", font="Arial, 14").pack(padx=10,
                                                                                                               pady=10)
    cedula = Entry(ventana_create, font="Arial, 13")
    cedula.pack(padx=10, pady=10)

    Button(ventana_create, command =lambda:validarId(ventana_create,cedula,cedula.get()),text="Next",font="Arial, 11").pack(padx=10,pady=20)
    ventana.destroy()

def dressOutfit(v,cedula):

    vestuarios = Vestuario()
    c = 0
    selected = IntVar()

    ventana_outfit = Toplevel()
    ventana_outfit.config(bg = "pink")
    ventana_outfit.title("Create Avatar")
    ventana_outfit.geometry("600x600")
    Label(ventana_outfit, bg="pink", text="Graphic Avatar Simulator", font="Time, 20").pack(padx=20, pady=40)
    Label(ventana_outfit, bg="pink", text="DRESS UP AVATAR", font="Arial, 15").pack()
    Label(ventana_outfit, bg="pink", text="Outfit ", font="Arial, 14").pack(padx=10, pady=10)
    Label(ventana_outfit, bg="pink", text="Select an option ", font="Arial, 13").pack(padx=10, pady=10)

    for i in vestuarios.getRopa():
        Radiobutton(ventana_outfit,bg="pink",text=i,variable=selected,value=c,font="Arial, 12").pack()
        c += 1

    Button(ventana_outfit,command=lambda: dressAccesory(ventana_outfit,cedula,selected.get()),text="Next",
           font="Arial, 11").pack(padx=10, pady=20)
    v.destroy()


def dressAccesory(ventana,cedula,outfit):
    vestuarios = Vestuario()
    c = 0
    selected = IntVar()

    ventana_accesory = Toplevel()
    ventana_accesory.config(bg="pink")
    ventana_accesory.title("Create Avatar")
    ventana_accesory.geometry("600x600")

    Label(ventana_accesory, bg="pink", text="Graphic Avatar Simulator", font="Time, 20").pack(padx=20, pady=40)
    Label(ventana_accesory, bg="pink", text="DRESS UP AVATAR", font="Arial, 15").pack()
    Label(ventana_accesory, bg="pink", text="Accessories ", font="Arial, 14").pack(padx=10, pady=10)
    Label(ventana_accesory, bg="pink", text="Select an option ", font="Arial, 13").pack(padx=10, pady=10)
    for i in vestuarios.getAccesorios():
        Radiobutton(ventana_accesory,bg="pink",text=i,variable=selected,value=c,font="Arial, 12").pack()
        c += 1
    Button(ventana_accesory, text="Next",command=lambda:dressShoes(ventana_accesory,cedula,outfit,selected.get()), font="Arial, 11").pack(padx=10,
                                                                                                             pady=20)
    ventana.destroy()

def dressShoes(ventana,cedula,outfit,accesorios):
    vestuarios = Vestuario()
    c = 0
    selected = IntVar()

    ventana_shoes = Toplevel()
    ventana_shoes.config(bg="pink")
    ventana_shoes.title("Create Avatar")
    ventana_shoes.geometry("600x600")
    Label(ventana_shoes, bg="pink", text="Graphic Avatar Simulator", font="Time, 20").pack(padx=20, pady=40)
    Label(ventana_shoes, bg="pink", text="DRESS UP AVATAR", font="Arial, 15").pack()
    Label(ventana_shoes, bg="pink", text="Shoes ", font="Arial, 14").pack(padx=10, pady=10)
    Label(ventana_shoes, bg="pink", text="Select an option ", font="Arial, 13").pack(padx=10, pady=10)
    for i in vestuarios.getCalzado():
        Radiobutton(ventana_shoes,bg="pink",text=i,variable=selected,value=c,font="Arial, 12").pack()
        c += 1
    Button(ventana_shoes, text="AVATAR INFORMATION", command=lambda:mostrarOutfit(ventana,cedula,outfit,accesorios,selected.get()), font="Arial, 11").pack(padx=10,pady=20)
    Button(ventana_shoes, text="CHECK YOUR AVATAR",
           command=lambda: mostrarAvatar(ventana, cedula, outfit, accesorios, selected.get()), font="Arial, 11").pack(
        padx=10, pady=20)

    ventana.destroy()

def mostrarOutfits(outfit):

    ropa = Vestuario()
    return ropa.getRopas(outfit)

def mostrarAvatar(ventana,cedula,outif,accesorios,zapatos):
    ventana_avatar = Toplevel()
    ventana_avatar.config(bg="pink")
    ventana_avatar.title("Create Avatar")
    ventana_avatar.geometry("600x600")
    Label(ventana_avatar, bg="pink", text="Graphic Avatar Simulator", font="Time, 20").pack(padx=00, pady=10)
    Label(ventana_avatar, bg="pink", text="THIS IS YOUR AVATAR", font="Arial, 15").pack()

    guardarOutfit(cedula,outif,accesorios,zapatos)

    id = str(cedula) + '.txt'
    with os.scandir(path) as ficheros:
        for fichero in ficheros:
            if id == fichero.name:
                    archi = open(fichero)
                    lineas = archi.readlines()

                    if lineas[1] == 'Genero 0\n' and lineas[2] == 'Color Piel 3\n' and lineas[4] == 'Color Pelo 2\n'\
                                    and lineas[6] == 'Atuendo 0\n':

                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/01.png'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="107", height="357")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 0\n' and lineas[2] == 'Color Piel 2\n' and lineas[4] == 'Color Pelo 2\n'\
                                    and lineas[6] == 'Atuendo 0\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/02.png'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="108", height="365")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 0\n' and lineas[2] == 'Color Piel 1\n' and lineas[4] == 'Color Pelo 0\n'\
                                    and lineas[6] == 'Atuendo 0\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/03.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="110", height="367")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 0\n' and lineas[2] == 'Color Piel 0\n' and lineas[4] == 'Color Pelo 0\n' \
                            and lineas[6] == 'Atuendo 0\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/04.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="106", height="366")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 0\n' and lineas[2] == 'Color Piel 3\n' and lineas[4] == 'Color Pelo 2\n' \
                            and lineas[6] == 'Atuendo 3\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/05.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="107", height="360")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 0\n' and lineas[2] == 'Color Piel 2\n' and lineas[4] == 'Color Pelo 2\n' \
                            and lineas[6] == 'Atuendo 3\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/06.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="106", height="364")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 0\n' and lineas[2] == 'Color Piel 1\n' and lineas[4] == 'Color Pelo 0\n' \
                            and lineas[6] == 'Atuendo 3\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/07.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="106", height="364")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 0\n' and lineas[2] == 'Color Piel 0\n' and lineas[4] == 'Color Pelo 0\n' \
                            and lineas[6] == 'Atuendo 4\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/08.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="105", height="363")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 0\n' and lineas[2] == 'Color Piel 3\n' and lineas[4] == 'Color Pelo 2\n' \
                            and lineas[6] == 'Atuendo 1\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/09.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="102", height="369")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 0\n' and lineas[2] == 'Color Piel 2\n' and lineas[4] == 'Color Pelo 2\n' \
                            and lineas[6] == 'Atuendo 1\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/10.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="106", height="366")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 0\n' and lineas[2] == 'Color Piel 1\n' and lineas[4] == 'Color Pelo 0\n' \
                            and lineas[6] == 'Atuendo 1\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/11.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="107", height="362")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 0\n' and lineas[2] == 'Color Piel 0\n' and lineas[4] == 'Color Pelo 0\n' \
                            and lineas[6] == 'Atuendo 1\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/12.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="107", height="365")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 0\n' and lineas[2] == 'Color Piel 3\n' and lineas[4] == 'Color Pelo 2\n' \
                            and lineas[6] == 'Atuendo 3\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/13.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="107", height="360")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 0\n' and lineas[2] == 'Color Piel 2\n' and lineas[4] == 'Color Pelo 2\n' \
                            and lineas[6] == 'Atuendo 3\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/14.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="104", height="362")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 0\n' and lineas[2] == 'Color Piel 1\n' and lineas[4] == 'Color Pelo 0\n' \
                            and lineas[6] == 'Atuendo 3\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/15.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="106", height="366")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 0\n' and lineas[2] == 'Color Piel 0\n' and lineas[4] == 'Color Pelo 0\n' \
                            and lineas[6] == 'Atuendo 3\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/16.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="109", height="363")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 1\n' and lineas[2] == 'Color Piel 1\n' and lineas[4] == 'Color Pelo 2\n' \
                            and lineas[6] == 'Atuendo 0\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/17.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="173", height="366")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 1\n' and lineas[2] == 'Color Piel 2\n' and lineas[4] == 'Color Pelo 1\n' \
                            and lineas[6] == 'Atuendo 0\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/18.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="175", height="365")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 1\n' and lineas[2] == 'Color Piel 1\n' and lineas[4] == 'Color Pelo 0\n' \
                            and lineas[6] == 'Atuendo 0\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/19.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="173", height="364")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 1\n' and lineas[2] == 'Color Piel 0\n' and lineas[4] == 'Color Pelo 0\n' \
                            and lineas[6] == 'Atuendo 0\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/20.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="170", height="366")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 1\n' and lineas[2] == 'Color Piel 1\n' and lineas[4] == 'Color Pelo 2\n' \
                            and lineas[6] == 'Atuendo 2\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/21.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="173", height="349")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 1\n' and lineas[2] == 'Color Piel 2\n' and lineas[4] == 'Color Pelo 1\n' \
                            and lineas[6] == 'Atuendo 2\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/22.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="171", height="350")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 1\n' and lineas[2] == 'Color Piel 1\n' and lineas[4] == 'Color Pelo 0\n' \
                            and lineas[6] == 'Atuendo 2\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/23.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="171", height="360")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 1\n' and lineas[2] == 'Color Piel 1\n' and lineas[4] == 'Color Pelo 0\n' \
                            and lineas[6] == 'Atuendo 2\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/24.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="167", height="347")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 1\n' and lineas[2] == 'Color Piel 1\n' and lineas[4] == 'Color Pelo 2\n' \
                            and lineas[6] == 'Atuendo 1\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/25.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="172", height="359")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 1\n' and lineas[2] == 'Color Piel 2\n' and lineas[4] == 'Color Pelo 1\n' \
                            and lineas[6] == 'Atuendo 1\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/26.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="171", height="360")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 1\n' and lineas[2] == 'Color Piel 1\n' and lineas[4] == 'Color Pelo 0\n' \
                            and lineas[6] == 'Atuendo 1\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/27.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="175", height="354")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 1\n' and lineas[2] == 'Color Piel 0\n' and lineas[4] == 'Color Pelo 0\n' \
                            and lineas[6] == 'Atuendo 1\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/28.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="170", height="358")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 1\n' and lineas[2] == 'Color Piel 1\n' and lineas[4] == 'Color Pelo 2\n' \
                            and lineas[6] == 'Atuendo 3\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/29.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="173", height="366")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 1\n' and lineas[2] == 'Color Piel 2\n' and lineas[4] == 'Color Pelo 1\n' \
                            and lineas[6] == 'Atuendo 3\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/30.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="173", height="366")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 1\n' and lineas[2] == 'Color Piel 1\n' and lineas[4] == 'Color Pelo 0\n' \
                            and lineas[6] == 'Atuendo 3\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/31.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="173", height="366")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    elif lineas[1] == 'Genero 1\n' and lineas[2] == 'Color Piel 0\n' and lineas[4] == 'Color Pelo 0\n' \
                            and lineas[6] == 'Atuendo 3\n':
                        img_niñas = ImageTk.PhotoImage(Image.open('OUTFITS/32.PNG'))
                        panel_hombre = Label(ventana_avatar, image=img_niñas, width="165", height="359")
                        panel_hombre.photo = img_niñas
                        panel_hombre.place(x="220", y="150")

                    archi.close()

        def regresar():
            ventana_avatar.destroy()
            ventana.deiconify()
        ventana.destroy()
        Button(ventana_avatar, text="Exit", font="Arial,11", command=lambda: regresar()).pack(padx=0, pady=20)

def mostrarAccesorios(accesorio):

    ropa = Vestuario()

    return ropa.getAccesorio(accesorio)

def mostrarZapatos(shoe):

    ropa = Vestuario()
    return ropa.getCalzados(shoe)


def mostrarOutfit(ventana,cedula,outfit,accesorios,shoes):
    ventana_outfit = Toplevel()
    ventana_outfit.config(bg = "pink")
    ventana_outfit.title("Create Avatar")
    ventana_outfit.geometry("600x600")

    outfits = mostrarOutfits(outfit)
    accesorio = mostrarAccesorios(accesorios)
    shoe = mostrarZapatos(shoes)

    Label(ventana_outfit, bg="pink", text="Graphic Avatar Simulator", font="Time, 20").pack(padx=20, pady=40)
    Label(ventana_outfit, bg="pink", text="SHOW OUTFIT", font="Arial, 15").pack()

    Label(ventana_outfit, bg="pink", text="Outfit ", font="Arial, 14").pack(padx=10, pady=10)
    Label(ventana_outfit, bg="pink", text=outfits, font="Arial, 12").pack()

    Label(ventana_outfit, bg="pink", text="YOUR ACCESSORY", font='Arial, 13').pack(padx=10, pady=10)
    Label(ventana_outfit, bg="pink", text=accesorio, font="Arial, 12").pack()

    Label(ventana_outfit, bg="pink", text="YOUR SHOES", font='Arial, 13').pack(padx=10, pady=10)
    Label(ventana_outfit, bg="pink", text= shoe, font="Arial, 12").pack()

    guardarOutfit(cedula, outfit, accesorios,shoes)
    Button(ventana_outfit, text="Exit", font="Arial,11", command=lambda: admin(ventana,cedula)).pack(padx=0, pady=20)

    ventana.destroy()

def guardarOutfit(cedula, outfit, accesorios,shoes):
    nombreTxt = str(cedula) + ".txt"
    archivo = open("AVATARS/"+nombreTxt,"a")
    archivo.write("INFORMATION AVATAR" + '\n')
    archivo.write("Atuendo " + str(outfit) + '\n')
    archivo.write("Accesorio " + str(accesorios) + '\n')
    archivo.write("Zapatos " + str(shoes) + '\n')
    archivo.close()

def mostrar_Consulta1(ventana,cedula):
    ventana_consulta1 = Toplevel()
    ventana_consulta1.config(bg="pink")
    ventana_consulta1.title("Report")
    ventana_consulta1.geometry("400x400")
    Label(ventana_consulta1, bg="pink",text="Graphic Avatar Simulator",font="Time, 20").pack(padx=20,pady=40)
    Label(ventana_consulta1, bg="pink", text="REPORT 1", font="Arial, 15").pack()
    Label(ventana_consulta1, bg="pink", text="AVATARS WITH FEMALE GENDER", font="Arial, 15").pack()

    cont = 0
    with os.scandir(path) as ficheros:
        for fichero in ficheros:
            archi = open(fichero)
            lineas = archi.readlines()
            if lineas[1] == 'Genero 0\n':

                cont += 1



        Label(ventana_consulta1,bg="pink",text=cont, font="Arial, 15").pack()

    ventana.destroy()

def mostrar_Consulta2(ventana,cedula):
    ventana_consulta2 = Toplevel()
    ventana_consulta2.config(bg="pink")
    ventana_consulta2.title("Report")
    ventana_consulta2.geometry("400x400")
    Label(ventana_consulta2, bg="pink",text="Graphic Avatar Simulator",font="Time, 20").pack(padx=20,pady=40)
    Label(ventana_consulta2, bg="pink", text="REPORT 2", font="Arial, 15").pack()

    Label(ventana_consulta2, bg="pink", text="AVATAR WITH BLACK SKIN", font="Arial, 15").pack()
    cont = 0
    with os.scandir(path) as ficheros:
        for fichero in ficheros:
            archi = open(fichero)
            lineas = archi.readlines()
            if lineas[2] == 'Color Piel 0\n':

                cont += 1



        Label(ventana_consulta2,bg="pink",text=cont, font="Arial, 15").pack()

    ventana.destroy()

def Consulta_1(indice,comp):
    carpeta = 'C:/Users/hp/Documents/GitHub/proyecto-graphic-avatar-simulator/AVATARS/'
    resultados=[]
    with os.scandir(carpeta) as ficheros:
        for fichero in ficheros:
            archi = open(fichero)
            lineas = archi.readlines()

            if lineas[indice] == comp:
                resultados.append(fichero.name)

            archi.close()

    return resultados

a= Consulta_1(1,"Genero 0\n")


def Consulta_2(indice,comp):
    carpeta = 'C:/Users/hp/Documents/GitHub/proyecto-graphic-avatar-simulator/AVATARS/'
    resultados = []
    with os.scandir(carpeta) as ficheros:
        for fichero in ficheros:
            archi = open(fichero)
            lineas = archi.readlines()

            if lineas[indice] == comp:
                resultados.append(fichero.name)

            archi.close()

    return resultados
b = Consulta_1(2, "Color Piel 0\n")

def main():
    ventanaPrincipal()

main()







