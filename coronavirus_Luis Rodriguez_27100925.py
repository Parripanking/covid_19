#LUIS JOSE RODRIGUEZ RODRIGUEZ
#CI: 27.100.925

añoActual= 2020
"""---------------------------------------------CLASE LISTA DE PERSONAS---------------------------------------"""
class listaPersonas:
    def __init__(self):
        self.lp = []

    def agregar_persona(self,  persona):
        self.lp.append(persona)  

    def mostrar_Personas(self):
        i=1
        for persona in self.lp:            
            persona.mostrar(i)
            i=i+1
      
         
"""------------------------------------------CLASE PERSONA---------------------------------------------------"""
class Persona:
    def __init__(self, nom, ape, ident, fecha, paisA, gen):
        self.nombre = nom
        self.apellido = ape
        #self.id = ident
        self.fecha_n= fecha
        self.pais= paisA
        self.genero = gen
        self.estatus= "SOSPECHOSO"     #posibles estatus: sospechoso, activo, descartado, recuperado, fallecido.  

    def edad(self):
        return añoActual - self.fecha_n[2]

    def mostrar(self,numeroindice):
        print(
            str(numeroindice)+".["+ self.estatus + "] " + self.nombre +" "+ self.apellido+" "+ str(self.edad()) +" años "+"("+str (self.fecha_n[0])+"-"+str (self.fecha_n[1])+"-"+str(self.fecha_n[2])+") "+ self.pais+" "+self.genero
            )

    def mostrar_detalles_ESTATUS(self, numeroindice):
        print("ESTATUS:["+self.estatus+"] "+ self.esUN())
        print("Nombre: "+self.nombre) 
        print("Apellido: "+self.apellido)
        print("genero: "+self.genero)
        print("Fecha de nacimiento: "+str (self.fecha_n[0])+"-"+str(self.fecha_n[1])+"-"+str(self.fecha_n[2]))
        print("Pais: "+ self.pais)
        
    def cambiarEstatus(self):
        terminar = False
        opcion = 0    
        while not terminar: 
            terminar = True           
            print ("1. Sospechoso")
            print ("2. Activo")
            print ("3. Inactivo")
            print ("4. Recuperado")
            print ("5. Fallecido") 

            opcion = pedirNumeroEntero()

            if opcion == 1:
                self.estatus="SOSPECHOSO"
            elif opcion == 2:
                self.estatus="ACTIVO"
            elif opcion == 3:
                self.estatus="INACTIVO"
            elif opcion == 4:
                self.estatus="RECUPERADO"
            elif opcion == 5:
                self.estatus="FALLECIDO"
            else:
                terminar= False
                print ("la opcion ingresada no es valida, ingrese un numero entre 1 y 5")

    def esUN(self): #menor adulto anciano
        es=""
        if (self.edad()<18):
            es="menor"
        elif (self.edad()>18 and self.edad()<60):
            es="adulto"
        elif (self.edad()>60):
            es="anciano"         
        return es   
"""----------------------------------------OPCIONES DEL MENU-------------------------------------------"""

def registrar_persona(lista):  #REGISTRAR PERSONAS
    print("\n"+"INGRESAR UN CASO")
    try:
        nom= str(input("ingrese el nombre: "))
        ape= str(input("ingrese el apellido: ")) 
        ident= str(input("ingrese su id: "))
        print ("ingrese su dia de nacimiento( Dia-mes-Año):")
        fechaD= int(input("(ejemplo:  31) Dia:"))
        fechaM= int(input("(ejemplo:  12) mes:"))
        FechaA= int(input("(ejemplo:2020) Dia:")) 

        fecha = (fechaD,fechaM,FechaA)    #guarda en una tupla la fecha

        paisA= str(input("ingrese su pais: "))
        terminar = False
        opcion = 0    
        while not terminar: 
            terminar = True 
            gen= str(input("ingrese su genero: "))          
            print ("1. masculino")
            print ("2. femenino")

            opcion = pedirNumeroEntero()

            if opcion == 1:
                gen ="masculino"
            elif opcion == 2:
                gen ="femenino"
            else:
                terminar= False
                print ("la opcion ingresada no es valida")

        nueva= Persona(nom,ape,ident,fecha,paisA,gen)
        lista.agregar_persona(nueva)
    except ValueError:
        print("ha ocurrido un error intente nuevamente")
        registrar_persona(lista)    
    return lista

def contar_por_genero(lista,estatus,genero):
    cont= 0
    for persona in lista:
        if(persona.estatus==estatus and persona.genero==genero):
            cont= cont + 1
    return cont

def contar_por_edad(lista,estatus,edad):
    cont=0
    for persona in lista:
        if(persona.estatus== estatus and persona.esUN()==edad):
            cont=cont+1
    return cont

def modificarEstatus(lista,i):
    regresar = False
    opcion = 0    
    while not regresar:
        print("")
        lista.lp[i].mostrar_detalles_ESTATUS(i)
        print("")
        print ("1. modificar estatus")
        print ("2. regresar") 
        opcion = pedirNumeroEntero()
        if opcion == 1:
            lista.lp[i].cambiarEstatus()
            print ("completado con exito")
            regresar = True

        elif opcion == 2:
            regresar = True        
        else:
            print ("la opcion ingresada no es valida")


def estatus(lista):
    regresar = False
    opcion = 0    
    while not regresar:
        print ("\n"+"ESTATUS A NIVEL MUNDIAL")
        lista.mostrar_Personas()

        if(len(lista.lp)>0): #si hay casos que mostrar
            
            print ("\n"+"Nota:")
            print ("ingrese el numero de caso para ver mas detalles o modificar el estatus de una persona")
            print ("-1. para regresar")  

            opcion = pedirNumeroEntero()
 
            if opcion == -1:
                regresar =True
            else:
                if (opcion<=len(lista.lp) and opcion > 0): 
                    modificarEstatus(lista,opcion -1)
                else:
                    print("El numero ingresado no pertenece a ningun caso") 
        else:
            print("actualmente no se han ingresado casos al sistema intente mas tarde")
            regresar=True # entonces regresa al menu anterior                   

def Mostrar_estadisticas(lista): # num de casos sospechosos, confirmados, descartados, recuperados, fallecidos(filtrado por genero y edad)   
    regresar = False
    opcion = 0 
    while not regresar:
        print ("\n"+"CONTADOR DE CASOS")
        print ("1. Filtrar por genero")
        print ("2. Filtrar por edades")
        print ("3. regresar")
        opcion = pedirNumeroEntero()
        if opcion == 1: #filtrar por genero
            print ("\n"+"CASOS FEMENINOS: ")
            #casos sospechosos en mujeres
            print ("-sospechosos: "+ str(contar_por_genero(lista,"SOSPECHOSO","femenino")))
            #casos activos en mujeres
            print ("-confirmados: "+ str(contar_por_genero(lista,"ACTIVO","femenino")))
            #casos descartados en mujeres
            print ("-descartados: "+ str(contar_por_genero(lista,"INACTIVO","femenino")))
            #casos recuperados en mujeres
            print ("-recuperados: "+ str(contar_por_genero(lista,"RECUPERADO","femenino")))            
            #casos fallecidos en mujeres
            print ("-fallecidos: "+ str(contar_por_genero(lista,"FALLECIDO","femenino"))) 

            print ("CASOS MASCULINOS: ")
            #casos sospechosos en hombres
            print ("-sospechosos: "+ str(contar_por_genero(lista,"SOSPECHOSO","masculino")))
            #casos activos en hombres
            print ("-confirmados: "+ str(contar_por_genero(lista,"ACTIVO","masculino")))
            #casos descartados en hombres
            print ("-descartados: "+ str(contar_por_genero(lista,"INACTIVO","masculino")))
            #casos recuperados en hombres
            print ("-recuperados: "+ str(contar_por_genero(lista,"RECUPERADO","masculino")))            
            #casos fallecidos en hombres
            print ("-fallecidos: "+ str(contar_por_genero(lista,"FALLECIDO","masculino"))) 
   
        elif opcion == 2:
            print ("\n"+"CASOS EN MENORES DE EDAD:")
            #casos sospechosos en menores
            print ("-sospechosos: "+ str(contar_por_edad(lista,"SOSPECHOSO","menor")))
            #casos activos en menores
            print ("-confirmados: "+ str(contar_por_edad(lista,"ACTIVO","menor")))
            #casos descartados en menores
            print ("-descartados: "+ str(contar_por_edad(lista,"INACTIVO","menor")))
            #casos recuperados en menores
            print ("-recuperados: "+ str(contar_por_edad(lista,"RECUPERADO","menor")))            
            #casos fallecidos en menores
            print ("-fallecidos: "+ str(contar_por_edad(lista,"FALLECIDO","menor"))) 

            print ("CASOS EN ADULTOS:")   
            #casos sospechosos en adultos
            print ("-sospechosos: "+ str(contar_por_edad(lista,"SOSPECHOSO","adulto")))
            #casos activos en adultos
            print ("-confirmados: "+ str(contar_por_edad(lista,"ACTIVO","adulto")))
            #casos descartados en adultos
            print ("-descartados: "+ str(contar_por_edad(lista,"INACTIVO","adulto")))
            #casos recuperados en adultos
            print ("-recuperados: "+ str(contar_por_edad(lista,"RECUPERADO","adulto")))            
            #casos fallecidos en adultos
            print ("-fallecidos: "+ str(contar_por_edad(lista,"FALLECIDO","adulto")))

            print ("CASOS EN ANCIANOS:")   
            #casos sospechosos en adultos
            print ("-sospechosos: "+ str(contar_por_edad(lista,"SOSPECHOSO","anciano")))
            #casos activos en adultos
            print ("-confirmados: "+ str(contar_por_edad(lista,"ACTIVO","anciano")))
            #casos descartados en adultos
            print ("-descartados: "+ str(contar_por_edad(lista,"INACTIVO","anciano")))
            #casos recuperados en adultos
            print ("-recuperados: "+ str(contar_por_edad(lista,"RECUPERADO","anciano")))            
            #casos fallecidos en adultos
            print ("-fallecidos: "+ str(contar_por_edad(lista,"FALLECIDO","anciano")))

        elif opcion == 3:
            regresar = True
        else:            
            print ("la opcion ingresada no es valida, ingrese un numero entre 1 y 3")   

"""----------------------------------------------MENU--------------------------------------------------"""
def pedirNumeroEntero():  #confirma que el numero ingresado sea valido (como un entero)
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("ingrese una opcion: "))
            correcto=True
        except ValueError:
            print('Error: debe ingresar un numero entero')
    return num

if __name__ == "__main__":    #EL MAIN CONTIENE EL MENU PRINCIPAL
    lista= listaPersonas()

    salir = False
    opcion = 0    
    while not salir:
        print ("\n"+":: SISTEMA DE CONTROL DE CASOS DE COVID-19")
        print ("1. Registrar caso")
        print ("2. Estatus de pacientes")
        print ("3. Contador de casos a nivel mundial")
        print ("4. Salir")   
 
        opcion = pedirNumeroEntero()
 
        if opcion == 1:
            registrar_persona(lista)
        elif opcion == 2:
            estatus(lista)
        elif opcion == 3:
            Mostrar_estadisticas(lista.lp)
        elif opcion == 4:
            salir = True
        else:
            print ("la opcion ingresada no es valida, ingrese un numero entre 1 y 3")

    pass