# Universidad del Valle de Guatemala
# MM2015 - Matemática Discreta
# Proyecto Corto 2 - Teoría de Números
# Maria Isabel Solano Bonilla - 20504
# Desc: El siguiente programa presenta un programa con 3 funciones las cuales permiten determinar si un número es primo,
#       utilizar el teorema fundamental del álgebra y el algoritmo de eclides. Para ello es necesario en el menú
#       seleccionar la función que se desea utilizar en ingresar los datos que se le requieren


import math

# Funciones a utilizar...

# Números Primos
def Primo(n):
    Resultado = 0 # 0 si es primo, o el factor d
    
    for x in range(2,int(math.sqrt(n))+1):
        
        for y in range (2,int(n)):
            if (n - y*x) == 0:
                #x es un múltiplo
                Resultado = x
    
    return Resultado

# Teorema Algoritmo de Euclides
def Euclides(a, b):
    Resultado = 0 # mcd(a,b)
    Residuo = -1
    while Residuo != 0:
        temp = int(a/b)
        Resultado = b
        Residuo = a-temp*b
        
        a = b
        b = Residuo
      
    return Resultado


# Inicio del loop del programa ...

Loop = True
while Loop:
    try:
        print("\n¿Qué función desea utilizar?\n1)Sacar números primos\n2)Teorema Fundamental de la aritmética\n3)Algoritmo de Euclides\n4)Salir del programa")
        Menu = int(input("Ingrese el número de la función que desea utilizar: "))
        
        # Números primos
        if Menu == 1:
            print ()
            ver = True #verificador
            while ver:
                #pedirle al usuario que ingrese el número
                n = int(input("Ingrese el número que desea determinar si es primo o compuesto: "))
                
                if n > 1:
                    # Se puede avanzar
                    ver = False
                else:
                    # Se repite el loop hasta que el usuario ingrese un número válido
                    print ("El número debe ser entero positivo mayor que 1. Intente nuevamente")
                
            #se puede utilizar la función correspondiente
            r = Primo(n)
            if r == 0:
                print ("Es primo")
            else:
                print (f"Es compuesto, un divisor es: ",r)
        
        # Teorema fundamental del álgebra
        elif Menu == 2:
            print ()
            n = 0
            ver = True #verificador
            while ver:
                #pedirle al usuario que ingrese el número
                n = int(input("Ingrese el número que verificar: "))
                
                if n > 1:
                    # Se puede avanzar
                    ver = False
                else:
                    # Se repite el loop hasta que el usuario ingrese un número válido
                    print ("El número debe ser entero positivo mayor que 1. Intente nuevamente")
            
            #Se puede continuar con el cálculo
                    
            #verificar si es primo
            if Primo(n) == 0:
                print ("Ya es un número primo")
                
            else:
                #SE busca la factorización
                
                #Se buscan todos los primos menores al número
                primos = [] #crear un array vacío
                for x in range (2,n):
                    if Primo(x) == 0:
                        #Agregar en el array
                        primos.append(x)
                
                #Se verifica si los primos son factores
                factores = []
                while n>1:
                    for x in primos:
                        m = int(n/x)
                        #print(f"resultado primo",m)
                        if (n-m*x) == 0:
                            #print(f"factor primo",x)
                            factores.append(x)
                            n = m
                            #print(f"nueva n",n)
                #se sale del while y se imprime el resultado
                print(factores)
                
        
        # Algoritmo de Euclides
        elif Menu == 3:
            print ()
            a = 0
            ver = True #verificador
            while ver:
                #pedirle al usuario que ingrese el número
                a = int(input("Ingrese el primer número: "))
                
                if a > 0:
                    # Se puede avanzar
                    ver = False
                else:
                    # Se repite el loop hasta que el usuario ingrese un número válido
                    print ("El número debe ser entero positivo. Intente nuevamente")
            b = 0
            ver = True #verificador
            while ver:
                #pedirle al usuario que ingrese el número
                b = int(input("Ingrese el primer segundo (debe ser menor que el primero): "))
                
                if b > 0 and b < a:
                    # Se puede avanzar
                    ver = False
                else:
                    # Se repite el loop hasta que el usuario ingrese un número válido
                    print ("El número debe ser entero positivo. Intente nuevamente")
                    
            #ya se pueden usar los factores
            print (f"El máximo común divisor es: ",Euclides(a,b))


        
        #Salir del programa
        elif Menu == 4:
            print("\nGracias por utilizar el programa")
            Loop = False
            
        elif Menu == 100:
            #fucnión secreta, obtener el código de acceso para el exámen
            print ()
            
        else:
            print("La opción ingresada no es válida")
            
    except ValueError:
        print ('El valor ingresado no es válido')
        
    