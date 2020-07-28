def run():
    nombres = ["juana", "carlos", "juxy", "hernesto", "ana", "cristiancito", "cacique", "jorge","chavez", "pepe"]
    nombres_positivos = []


    def calculo_vocales():
        for i in nombres:
            for letras in i:
                diccionario = {
                "a" : operacion_por_vocal(i, "a"),
                "e" : operacion_por_vocal(i, "e"),
                "i" : operacion_por_vocal(i, "i"),
                "o" : operacion_por_vocal(i, "o"),
                "u" : operacion_por_vocal(i, "u")
                }

            if sum(diccionario.values()) == 2:
                print(diccionario, i, "_____", "\033[1;32m"+"POSITIVO" + "\033[0;m" + " >>>> tiene 2 vocales")
                nombres_positivos.append(i)
            else:
                print(diccionario, i, "_____" , "\033[1;31m" + "NEGATIVO" + "\033[0;m")
        
        print("""
        Depurando ... 
        
        nombres con 2 vocales: 
         """)
        
        for i in nombres_positivos:
            print(i)


    def operacion_por_vocal(nombre, vocal): 
        cuenta = 0
        for letra in nombre:
            if letra == vocal:
                cuenta += 1
        return cuenta
    calculo_vocales()


if __name__ == "__main__":
    run()