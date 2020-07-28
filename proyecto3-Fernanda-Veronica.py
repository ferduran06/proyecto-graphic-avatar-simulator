from tkinter import *
import os
from tkinter import messagebox as MessageBox

path = 'C:/Users/hp/Documents/GitHub/proyecto-graphic-avatar-simulator/AVATARS'
files = os.listdir(path)


class Vestuario:
    def __init__(self):
        self.vestuario = {
            "accesorios": ["Lentes", "Reloj", "Brazalete", "Cadena", "Aretes","Sombrero", "Ninguno"],
            "ropa": ["Formal", "Casual", "Deportivo", "Baño", "Etiqueta"],
            "calzado": ["Botas", "Tenis", "Zapatilla", "Mocasines",  "Pantuflas",
                        "Tacones"]}  # Attributes assigned

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

class Rostro:
    def __init__(self):
        self.rostro = ["Redondo", "Alargado", "Corazón", "Cuadrado", "Ovalado", "Rectangular"]  # Attributes assigned

    def set(self, rostro):
        self.rostro = rostro

    def getRostro(self):
        return self.rostro

    def getRostroIndice(self, indice):
        return self.rostro[indice]

class Piel:
    def __init__(self):
        self.piel = ["Negra", "Marrón", "Morena", "Clara", "Blanca"]  # Attributes assigned

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

class Ojos:
    def __init__(self):
        self.ojos = ["Almendrados", "Separados", "Redondos", "Caídos", "Saltones", "Juntos", "Profundos",
                     "Asiático"]  # Attributes assigned

    def setFormaOjos(self, formaOjos):
        self.ojos = formaOjos  # Assign value in the dictionary in the eye shape position

    def getFormaOjoa(self):  # Get that gets the eye shape in X position
        return self.ojos

    def getOjosIndice(self, indice):
        return self.ojos[indice]

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
    ventana.mainloop()  # para que la ventana no se cierre la ventana

def ingresar(v,e1,e2, nombre,contrasenna):

    if nombre == "fer" and contrasenna =="123":

        ventana_ingresar = Toplevel()
        ventana_ingresar.config(background="pink")
        ventana_ingresar.title("Administrator")
        ventana_ingresar.geometry("500x400")

        Label(ventana_ingresar, bg="pink", text="Graphic Avatar Simulator", font="Time, 20").pack(padx=20,pady=40)
        saludo = ("Welcome " + nombre)
        Label(ventana_ingresar,bg = "pink", text=saludo,font="Arial, 15").pack()
        Button(ventana_ingresar, text="Create Avatar",command = lambda:createAvatar(ventana_ingresar),font="Arial, 11").pack(padx=10, pady=20)
        Button(ventana_ingresar, text="Dress up Avatar",command = lambda:dressingAvatar(ventana_ingresar),font="Arial, 11").pack(padx=10, pady=20)
        v.withdraw()

    elif nombre == "Vero" and contrasenna == "1234":

        ventana_ingresar = Toplevel()
        ventana_ingresar.config(background="pink")
        ventana_ingresar.title("Analyst")
        ventana_ingresar.geometry("500x400")

        Label(ventana_ingresar, bg="pink", text="Graphic Avatar Simulator", font="Time, 20").pack(padx=20,pady=40)
        saludo = ("Welcome " + nombre)
        Label(ventana_ingresar, bg="pink", text=saludo, font="Arial, 15").pack()
        Button(ventana_ingresar, text="Report 1", command= lambda:mostrar_Consulta1(ventana_ingresar),font="Arial, 11").pack(padx=10, pady=20)
        Button(ventana_ingresar, text="Report 2", command= lambda:mostrar_Consulta2(ventana_ingresar),font="Arial, 11").pack(padx=10, pady=20)
        v.withdraw()
    else:
        MessageBox.showerror("Error","INVALID DATA. TRY AGAIN")

    def regresar():
        ventana_ingresar.destroy()
        v.deiconify()

    Button(ventana_ingresar, text="Exit",font="Arial,11", command=lambda: regresar()).pack(padx=0, pady=20)
    v.wait_window(ventana_ingresar)

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
    Button(ventana_create, command =lambda :registerFace(ventana,cedula,cedula.get()),text="Next",font="Arial, 11").pack(padx=10,pady=20)

    ventana_create.mainloop()

def registerFace(v,c,cedula):
    ventana_face = Toplevel()
    ventana_face.config(bg = "pink")
    ventana_face.title("Create Avatar")
    ventana_face.geometry("500x500")

    selected = IntVar()
    creaciontxt(cedula)

    haces = Rostro()
    c = 0

    Label(ventana_face, bg="pink", text="Graphic Avatar Simulator", font="Time, 20").pack(padx=20, pady=40)
    Label(ventana_face, bg="pink", text="FACE SHAPES AVATAR", font="Arial, 15").pack()
    Label(ventana_face, bg="pink", text="FACE ", font="Arial, 14").pack(padx=10, pady=10)
    Label(ventana_face, bg="pink", text="Select an option ", font="Arial, 13").pack(padx=10, pady=10)

    for i in haces.getRostro():
        Radiobutton(ventana_face,bg="pink",text=i,variable=selected,value=c,font="Arial, 12").pack()
        c += 1
    Button(ventana_face, command =lambda :registerSkin(ventana_face,cedula,selected.get()),text="Next",font="Arial, 11").pack(padx=10,pady=20)
    ventana_face.mainloop()


def registerSkin(ventana,cedula,faces):
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

    Button(ventana_skin, command=lambda: registerHair(ventana_skin, cedula, faces,selected.get()), text="Next",
           font="Arial, 11").pack(padx=10, pady=20)
    ventana_skin.mainloop()

def registerHair(ventana,cedula,faces,skin):

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
    Button(ventana_hair, command=lambda: registerEyes(ventana_hair, cedula, faces, skin,selected.get()), text="Next",
           font="Arial, 11").pack(padx=10, pady=20)
    ventana_hair.mainloop()


def registerEyes(ventana,cedula,faces,skin,hair):

    eyes = Ojos()
    c = 0

    selected = IntVar()

    ventana_eyes = Toplevel()
    ventana_eyes.config(bg = "pink")
    ventana_eyes.title("Create Avatar")
    ventana_eyes.geometry("600x600")

    Label(ventana_eyes, bg="pink", text="Graphic Avatar Simulator", font="Time, 20").pack(padx=20, pady=40)
    Label(ventana_eyes, bg="pink", text="EYE SHAPE AVATAR", font="Arial, 15").pack()
    Label(ventana_eyes, bg="pink", text="SHAPE ", font="Arial, 14").pack(padx=10, pady=10)
    Label(ventana_eyes, bg="pink", text="Select an option ", font="Arial, 13").pack(padx=10, pady=10)
    for i in eyes.getFormaOjoa():
        Radiobutton(ventana_eyes,bg="pink",text=i,variable=selected,value=c,font="Arial, 12").pack()
        c += 1
    Button(ventana_eyes, command=lambda: registerGender(ventana_eyes, cedula, faces,skin,hair, selected.get()), text="Next",
           font="Arial, 11").pack(padx=10, pady=20)
    ventana_eyes.mainloop()


def registerGender(ventana,cedula,faces,skin,hair,eyes):

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
    Button(ventana_gender, command=lambda: mostrarInfor(ventana_gender, cedula, faces, skin, hair,eyes, selected.get()),
           text="Next",
           font="Arial, 11").pack(padx=10, pady=20)
    ventana_gender.mainloop()

def validarId(c,cedula):
    id = str(cedula)+'.txt'
    for txt in files:
        if id == txt:
            MessageBox.showerror("Error", "THIS ID IS NOT REGISTERED")

def mostrarRostro(faces):

    rostros = Rostro()
    return rostros.getRostroIndice(faces)

def mostrarColor(skin):

    piel = Piel()
    return piel.getPielIndice(skin)

def mostrarCabello(hair):

    cabello = Cabello()
    return cabello.getTexturaIndice(hair)

def mostrarOjos(eyes):

    ojos = Ojos()
    return ojos.getOjosIndice(eyes)

def mostrarGenero(gender):

    genero = Genero()
    return genero.getgeneros(gender)

def guardarDatos(cedula,gender,faces,skin,hair,eyes):
    nombreTxt = str(cedula)+".txt"
    archivo = open(nombreTxt,"w")
    archivo.write("INFORMATION AVATAR" + '\n')
    archivo.write("Genero " + str(gender) + '\n')
    archivo.write("Rostro "+ str(faces) + '\n')
    archivo.write("Color Piel " + str(skin) + '\n')
    archivo.write("Pelo "+ str(hair) + '\n')
    archivo.write("Ojos "+ str(eyes) + '\n')
    archivo.close()

def mostrarInfor(ventana,cedula,faces,skin,hair,eyes,gender):

    ventana_gender = Toplevel()
    ventana_gender.config(bg = "pink")
    ventana_gender.title("Create Avatar")
    ventana_gender.geometry("600x650")

    face = mostrarRostro(faces)
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

    Label(ventana_gender, bg="pink", text="YOUR SHAPE OF FACE ", font='Arial, 13').pack(padx=10, pady=10)
    Label(ventana_gender, bg="pink", text=face, font="Arial, 12").pack()

    Label(ventana_gender, bg="pink", text="YOUR SKIN COLOR", font='Arial, 13').pack(padx=10, pady=10)
    Label(ventana_gender, bg="pink", text=skins, font="Arial, 12").pack()

    Label(ventana_gender, bg="pink", text="YOUR SKIN COLOR", font='Arial, 13').pack(padx=10, pady=10)
    Label(ventana_gender, bg="pink", text=skins, font="Arial, 12").pack()

    Label(ventana_gender, bg="pink", text="YOUR HAIR TEXTURE", font='Arial, 13').pack(padx=10, pady=10)
    Label(ventana_gender, bg="pink", text=hairs, font="Arial, 12").pack()

    Label(ventana_gender, bg="pink", text="YOUR EYE SHAPE", font='Arial, 13').pack(padx=10, pady=10)
    Label(ventana_gender, bg="pink", text=eye, font="Arial, 12").pack()

    guardarDatos(cedula,gender,faces,skin,hair,eyes)

    Button(ventana_gender, text="Exit",font="Arial,11", command=lambda: ventanaPrincipal() ).pack(padx=0, pady=20)


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

    Button(ventana_create, command =lambda :dressOutfit(ventana,cedula,cedula.get()),text="Next",font="Arial, 11").pack(padx=10,pady=20)

    ventana_create.mainloop()


def dressOutfit(ventana,c,cedula):
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
    ventana_outfit.mainloop()


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
    ventana.withdraw()

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
    Button(ventana_shoes, text="Next", command=lambda:mostrarOutfit(ventana,cedula,outfit,accesorios,selected.get()), font="Arial, 11").pack(padx=10,pady=20)
    ventana.withdraw()

def mostrarOutfits(outfit):

    ropa = Vestuario()
    return ropa.getRopas(outfit)

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
    Button(ventana_outfit, text="Exit", font="Arial,11", command=lambda: ventanaPrincipal()).pack(padx=0, pady=20)
    ventana_outfit.mainloop()

def guardarOutfit(cedula, outfit, accesorios,shoes):
    nombreTxt = str(cedula) + ".txt"
    archivo = open(nombreTxt, "a")
    archivo.write("INFORMATION AVATAR" + '\n')
    archivo.write("Atuendo " + str(outfit) + '\n')
    archivo.write("Accesorio " + str(accesorios) + '\n')
    archivo.write("Zapatos " + str(shoes) + '\n')
    archivo.close()

def mostrar_Consulta1(ventana):
    ventana_consulta1 = Toplevel()
    ventana_consulta1.config(bg="pink")
    ventana_consulta1.title("Create Avatar")
    ventana_consulta1.geometry("400x400")
    Label(ventana_consulta1, bg="pink",text="Graphic Avatar Simulator",font="Time, 20").pack(padx=20,pady=40)
    Label(ventana_consulta1, bg="pink", text="REPORT 1", font="Arial, 15").pack()

    Button(ventana_consulta1, text="Consulta Genero", font= "Arial 11", command=lambda: ventanaPrincipal()).pack(padx=0, pady=20)
    ventana_consulta1.mainloop()

def mostrar_Consulta2(ventana):
    ventana_consulta2 = Toplevel()
    ventana_consulta2.config(bg="pink")
    ventana_consulta2.title("Create Avatar")
    ventana_consulta2.geometry("400x400")
    Label(ventana_consulta2, bg="pink",text="Graphic Avatar Simulator",font="Time, 20").pack(padx=20,pady=40)
    Label(ventana_consulta2, bg="pink", text="REPORT 2", font="Arial, 15").pack()

    Button(ventana_consulta2, text="Consulta Cabello", font= "Arial 11", command=lambda: ventanaPrincipal()).pack(padx=0, pady=20)
    ventana_consulta2.mainloop()

def Consulta_1(carpeta,indice,comp):
    resultados=[]
    with os.scandir(carpeta) as ficheros:
        for fichero in ficheros:
            archi = open(fichero)
            lineas = archi.readlines()

            if lineas[indice] == comp:
                resultados.append(fichero.name)
            archi.close()
    return resultados

a= Consulta_1("C:/Users/hp/Documents/GitHub/proyecto-graphic-avatar-simulator/AVATARS",2,"Rostro 3\n")
cont=0
for i in a:
    archivo= open("C:/Users/hp/Documents/GitHub/proyecto-graphic-avatar-simulator/AVATARS/"+a[cont])
    lineas= archivo.readlines()
    cont+=1
    print(lineas)

def Consulta_2(carpeta,indice,comp):
    resultados=[]
    with os.scandir(carpeta) as ficheros:
        for fichero in ficheros:
            archi = open(fichero)
            lineas = archi.readlines()

            if lineas[indice] == comp:
                resultados.append(fichero.name)
            archi.close()
    return resultados

a= Consulta_2("C:/Users/hp/Documents/GitHub/proyecto-graphic-avatar-simulator/AVATARS",2,"Rostro 4\n")
cont=0
for i in a:
    archivo= open("C:/Users/hp/Documents/GitHub/proyecto-graphic-avatar-simulator/AVATARS/"+a[cont])
    lineas= archivo.readlines()
    cont+=1
    print(lineas)
def main():
    ventanaPrincipal()

main()
