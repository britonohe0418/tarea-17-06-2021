class For:

    def __init__(self):
        pass


    def usoFor(self):
        nombre = "Daniel"
        dato = ["Daniel", 50, True]
        numeros = (2, 5.6, 4, 1)
        profesor = {"nombre": "Daniel", "edad": 50, "fac": "faci"}

        # for i in range(5):
        #     print("i: {}".format(i))
    
        # for i in range(2, 10):
        #     print("i: {}".format(i))
    
        # for i in range(4, 10, 2):
        #     print("i:{}".format(i), end=" ")

        # for i in range(12, 3, -3):
        #     print("i:{}".format(i), end=" ")
    
        # longitud = len(dato)
        # print(dato[0])
        # print(dato[1])
        # print(dato[2])
        # print("")
        # j = 0
        # while j < longitud:
        #     print("While:{}".format(j), dato[j], end=" ")
        #     j += 1
        # print("")
        # for i in range(longitud-1, -1, -1):
        #     print("For:{}".format(i), dato[i], end=" ")
    
        # for i, dato in enumerate(numeros):
        #     print("For:", i, dato)
    
        # for dato in numeros:
        #     print("Dato:", dato)
    
        # for dato in ['H', 'o', 'l', 'a', 'que', 'tal']:
        #     print("Dato:", dato)

        # print("Diccionario de notas.")
        # for llave, valor in profesor.items():
        #     print(llave + ":" + str(valor), end=" ")

        # for estudiante in lista_estudiantes:
        #     for llave, valor in estudiante.items():
        #         print(llave + ":" + str(valor), end="  ")

        # lista_de_notas = [(30, 40), [20, 40] ,(50, 40)]
        # acum = 0
        # longi = 0
        # for notas in lista_de_notas:
        #     parcial = 0
        #     print("" + str(notas), end=" ")
        #     for nota in notas:
        #         longi += 1
        #         acum += nota
        #         parcial += nota
        #     promedio_parcial = parcial/len(notas)
        #     print("Notas Parciales:{}, Promedio Parcial:{}".format(parcial, promedio_parcial))
        # promedio = (acum/longi)
        # print("Total notas:{} - #Notas:{}, Promedio:{}".format(acum, longi, promedio))

        # lista_estudiantes = [{"nombre": "Erick", "final": 70}, {"nombre": "Yady", "final": 60}, {"nombre": "Danny", "final": 90}]
        # acum = 0
        # cont = 0
        # for estudiantes in lista_estudiantes:
        #     print(estudiantes)
        #     for llave, valor in estudiantes.items():
        #         print(str(llave) + ":" + str(valor), end="")
        #         if llave == "final": acum += valor
        #         print("")
        #     cont += 1
        # print(acum/cont)

        # oracion = "Hola como estas"
        # vocales = []
        # for carro in oracion:
        #     if carro in ('a', 'e', 'i', 'o', 'u'):
        #         vocales.append(carro)
        # print(vocales)
        print([carro for carro in "Hola como estas" if carro in ('a', 'e', 'i', 'o', 'u')])


use_of_for = For()
use_of_for.usoFor()
