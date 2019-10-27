from tkinter import *

#-----------------------VENTANA 1 = PRINCIPAL---------------------------

def funcion_v1():
    #----Configuración----
    v1 = Tk()
    v1.title("Presentación")
    v1.config(bg="beige")

    #----Declaración----
    v1_frame1 = Frame(v1)
    v1_boton1 = Button(v1_frame1, text="Avanzar", font=("footlight mt",12), command= lambda:[funcion_v2(),v1.withdraw()])
    # v1_imagen1 = PhotoImage(file="fisc.png")
    # v1_imagen2 = PhotoImage(file="utp.png")
    v1_label1 = Label(v1_frame1,text= """ Universidad Tecnológica de Panamá\n 
        Facultad de Ingeniería de Sistemas Computacionales\n
        Licenciatura en Ingeniería de Software\n
        Profesor: Ing. Samuel Jiménez
        
        SEMESTRE I
        2019""" ,fg="black", font=("footlight mt",14))
    # v1_label2 = Label(v1_frame1, image=utp)
    # v1_label3 = Label(v1_frame1, image=fisc)

    #----Renderizado----
    # v1_label3.grid(row=0, column=2,sticky="ne",padx=20)
    # v1_label2.grid(row=0, column=0,sticky="nw",padx=20)
    v1_label1.grid(row=2)
    v1_boton1.grid(row=1)
    v1_frame1.grid(padx=20, pady=20)
    v1.mainloop()

#----------------------VENTANA 2 = MENÚ-------------------------

def funcion_v2():
    #----Configuración----
    v2 = Toplevel()
    v2.title("Menú")
    v2.config(bg="beige")

    #----Declaración----
    v2_frame0 = Frame(v2)
    v2_frame1 = Frame(v2)
    v2_frame2 = Frame(v2)
    v2_imagen0 = PhotoImage(file= "")
    v2_imagen1 = PhotoImage(file= "./imagenes/Mapa_de_Bocas_del_Toro.png")
    v2_imagen2 = PhotoImage(file= "./imagenes/Mapa_de_Chiriqui.png")
    v2_imagen3 = PhotoImage(file= "./imagenes/Mapa_de_Cocle.png")
    v2_imagen4 = PhotoImage(file= "./imagenes/Mapa_de_Colon.png")
    v2_imagen5 = PhotoImage(file= "./imagenes/Mapa_de_Darien.png")
    v2_imagen6 = PhotoImage(file= "./imagenes/Mapa_de_Herrera.png")
    v2_imagen7 = PhotoImage(file= "./imagenes/Mapa_de_Los_Santos.png")
    v2_imagen8 = PhotoImage(file= "./imagenes/mapa-politico-panama2.png")
    v2_imagen9 = PhotoImage(file= "./imagenes/mapa-politico-panama1.png")
    v2_imagen10 = PhotoImage(file= "./imagenes/Mapa_de_Veraguas.png")
    v2_imagen11 = PhotoImage(file= "./imagenes/politico_embera.png")
    v2_imagen12 = PhotoImage(file= "./imagenes/Mapa_de_Guna_Yala.png")
    v2_imagen13 = PhotoImage(file= "./imagenes/Mapa_de_Ngobe_Bugle.png")
    v2_imagenes = [v2_imagen0, v2_imagen1,v2_imagen2,v2_imagen3,v2_imagen4,v2_imagen5,v2_imagen6,v2_imagen7,
                   v2_imagen8,v2_imagen9,v2_imagen10,v2_imagen11,v2_imagen12,v2_imagen13]
    v2_label1 = Label(v2_frame0, text="Selecione su opción de prefencia...",fg="black", font=("footlight mt",14))
    v2_label2 = Label(v2_frame1, text="Provincias", fg="black", font=("footlight mt", 14))
    v2_label3 = Label(v2_frame1, text="Comarcas", fg="black", font=("footlight mt", 14))
    v2_label4 = Label(v2_frame2, text= '',fg="black", font=("footlight mt",14))
    v2_label5 = Label(v2_frame2, text= '',fg="black", font=("footlight mt",12), wraplength = 200, justify=LEFT)
    v2_label6 = Label(v2_frame2, image= v2_imagen0, width=250)
    v2_label6.image = v2_imagen0
    eleccion1 = IntVar()
    v2_radiobutton1 = Radiobutton(v2_frame1,text="Bocas del Toro",variable= eleccion1,value=1)
    v2_radiobutton2 = Radiobutton(v2_frame1, text="Chiriquí", variable= eleccion1, value=2)
    v2_radiobutton3 = Radiobutton(v2_frame1, text="Coclé", variable= eleccion1, value=3)
    v2_radiobutton4 = Radiobutton(v2_frame1, text="Colón", variable= eleccion1, value=4)
    v2_radiobutton5 = Radiobutton(v2_frame1, text="Darién", variable= eleccion1, value=5)
    v2_radiobutton6 = Radiobutton(v2_frame1, text="Herrera", variable= eleccion1, value=6)
    v2_radiobutton7 = Radiobutton(v2_frame1, text="Los Santos", variable= eleccion1, value=7)
    v2_radiobutton8 = Radiobutton(v2_frame1, text="Panamá", variable= eleccion1, value=8)
    v2_radiobutton9 = Radiobutton(v2_frame1, text="Panamá Oeste", variable= eleccion1, value=9)
    v2_radiobutton10 = Radiobutton(v2_frame1, text="Veraguas", variable= eleccion1, value=10)
    v2_radiobutton11 = Radiobutton(v2_frame1, text="Emberá", variable= eleccion1, value=11)
    v2_radiobutton12 = Radiobutton(v2_frame1, text="Guna Yala", variable= eleccion1, value=12)
    v2_radiobutton13 = Radiobutton(v2_frame1, text="Ngabe-Buglé", variable= eleccion1, value=13)
    v2_boton1 = Button(v2_frame1,text = "Aceptar", font=("footlight mt", 14),command= lambda:[v2_label4.config(text= provincias[eleccion1.get()][0]),
                                                                                              v2_label5.config(text= provincias[eleccion1.get()][1]),
                                                                                              v2_label6.config(image= v2_imagenes[eleccion1.get()])])
    v2_boton2 = Button(v2_frame2, text="Lugares turísticos", font=("footlight mt", 14),command= funcion_v3)

    #----Renderizado----
    v2_label1.grid(row=0)
    v2_label2.grid(row=1)
    v2_radiobutton1.grid(row=2, sticky="w")
    v2_radiobutton2.grid(row=3, sticky="w")
    v2_radiobutton3.grid(row=4, sticky="w")
    v2_radiobutton4.grid(row=5, sticky="w")
    v2_radiobutton5.grid(row=6, sticky="w")
    v2_radiobutton6.grid(row=7, sticky="w")
    v2_radiobutton7.grid(row=8, sticky="w")
    v2_radiobutton8.grid(row=9, sticky="w")
    v2_radiobutton9.grid(row=10, sticky="w")
    v2_radiobutton10.grid(row=11, sticky="w")
    v2_label3.grid(row=12)
    v2_radiobutton11.grid(row=13, sticky="w")
    v2_radiobutton12.grid(row=14, sticky="w")
    v2_radiobutton13.grid(row=15, sticky="w")
    v2_boton1.grid(row=16)

    v2_label4.grid(row=1, columnspan=2)
    v2_label5.grid(row=3, rowspan= 6, column=0)
    v2_label6.grid(row=3, rowspan= 6, column=1)
    v2_boton2.grid(row=10, columnspan=2)
    v2_frame0.pack(side=TOP, padx=10, pady=10)
    v2_frame1.pack(side=LEFT, padx=30, pady=10)
    v2_frame2.pack(side=RIGHT, padx=30, pady=10)
    v2.mainloop

#----------------------VENTANA 3 = TURÍSTICOS-------------------------

def funcion_v3():
    #----Configuración----
    v3 = Toplevel()
    v3.title("Lugares turísticos")
    v3.config(bg="beige")

    #----Declaración----
    v3_frame1 = Frame(v3)
    v3_label1 = Label(v3_frame1, text="Selecione su lugar favorito...", fg="black",font=("footlight mt", 20))

    #----Renderizado----
    v3_frame1.grid(padx=20, pady=20)

#----------------------INFORMACIÓN-------------------------

provincias = {
    0: ['','',''],
    
    1: ["Bocas del Toro", """La provincia de Bocas se encuentra ubicada en el sector oeste de Panamá teniendo como
    límites al norte la provincia de Bocas del Toro y la comarca Ngäbe-Buglé, al oeste la provincia
    de Puntarenas (en la República de Costa Rica), al este la provincia de Veraguas y al sur el
    océano Pacífico"""],
    
    2: ["Chiriquí", """La provincia de Chiriquí se encuentra ubicada al norte la provincia de Bocas del Toro y
    la comarca Ngäbe-Buglé, al oeste la provincia de Puntarenas (en la República de Costa Rica),
    al este la provincia de Veraguas y al sur el océano Pacífico."""],

    3: ["Coclé", """La provincia de Coclé se encuentra ubicada al norte con la provincia de Colón, al este con la
    provincia de Panamá Oeste, al sur con la de Herrera y el golfo de Parita y al oeste
    con la de Veraguas."""],
    
    4: ["Colón", """La provincia de Colon se encuentra ubicada Limita al norte con el mar Caribe, al sur con las
    provincias de Panamá, Panamá Oeste y Coclé, al este con la Comarca de Guna Yala y al oeste
    con la provincia de Veraguas."""],
    
    5: ["Darién", """La provincia de Darién encuentra ubicada al norte con la provincia de Panamá y la
    comarca Guna Yala. Al sur limita con el océano Pacífico y la República de Colombia.
    Al este limita con la República de Colombia, y al oeste limita con el océano Pacífico
    y la provincia de Panamá."""],
    
    6: ["Herrera", """La provincia de Herrera se encuentra ubicada Limita al norte con las provincias de Veraguas
    y Coclé, al sur con la provincia de Los Santos, al este con el golfo de Parita y la
    provincia de Los Santos y al oeste con la provincia de Veraguas concretamente con
    el distrito de Mariato."""],
    
    7: ["Los Santos", """La provincia de Los Santos se encuentra ubicada al sureste de la península de
    Azuero. Las Tablas es su capital y localidad más poblada.
    Está compuesta por los distritos de Los Santos, Guararé, Las Tablas,
    Macaracas, Pedasí, Pocrí y Tonosí."""],

    8: ["Panamá", """La provincia de Panamá se encuentra ubicada al norte con la provincia de Colón y la Comarca
    Guna Yala, al sur con el océano Pacífico; al este con la provincia de Darién y la comarca
    Wargandí y al oeste con la provincia de Panamá Oeste."""],
    
    9: ["Panamá Oeste", """La provincia de Panamá Oeste se encuentra ubicada al norte con la provincia de Colón,
    al sur con el océano Pacífico; al este con la provincia de Panamá y al oeste con la
    provincia de Coclé."""],

    10: ["Veraguas", """La provincia de Veraguas se encuentra ubicada al norte con el Mar Caribe, al sur con el
    Océano Pacífico, al este con las provincias de Colón, Coclé, Herrera, Los Santos y
    al oeste con la provincia de Chiriquí y la Comarca Ngäbe-Buglé.
    Es la única provincia de Panamá que tiene costas en los
    océanos Atlántico y Pacífico."""],
    
    11: ["Emberá", """La provincia de Emberá-Wounaan abarca quinientas hectáreas y está dividida en cuarenta y
    dos comunidades con un total aproximado de nueve mil indígenas, Los emberás hablan
    el emberá y los wounaan el Wounaan meu. Emberá significa
    \'hombre bueno\' o \'buen amigo\'. El wounaan meu significa \'gente, personas o pueblo\'."""], 

    12: ["Guna Yala", """La provincia de Guna Yala se encuentra ubicada al norte con el mar Caribe, al sur con
    la provincia de Darién y la comarca Emberá Wounnan, al este con Colombia y al
    oeste con la provincia de Colón. """],
    
    13: ["Ngabe-Buglé", """La provincia de Ngåbe-Bugle se encuentra ubicada en la región occidental de Panamá.
    La comarca es atravesada de oeste a este por la Cordillera Central o Serranía de Tabasará,
    que separa dos regiones geográficas: la región atlántica o caribeña."""]
    }

#----------------------PROGRAMA PRINCIPAL-------------------------

funcion_v1()
