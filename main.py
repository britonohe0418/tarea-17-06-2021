class For:

    def __init__(self):
        pass


    def usoFor(self):
        nombre = "Daniel"
        dato = ["Daniel", 50, True]
        numeros = (2, 5.6, 4, 1)
        profesor = {"nombre": "Daniel", "edad": 50, "fac": "faci"}
        lista_notas = [(30, 40), [20, 40] ,(50, 40)]
        lista_estudiantes = [{"nombre": "Erick", "final": 70}, {"nombre": "Yady", "final": 60}, {"nombre": "Danny", "final": 90}]

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


use_of_for = For()
use_of_for.usoFor()
