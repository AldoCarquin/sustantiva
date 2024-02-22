import math
resultado = ''
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        print('No es posible la división en 0!!!')
        return None 
    else:
        return a / b
    
def potencia(a, b):
    return a**b


def evOperacion(operacion):
    while operacion not in ['+', '-', '*', 'x', '/','r', 'rad', 'sin', 'cos', 'tan', 'lognat', 'log10', 'f', 'salir','n']:
        print('Operación no válida. Por favor ingrese otra operación.')
        operacion = input('Operación: ')
    return operacion

print('********************************************\n*************** Bienvenidx a ***************\n************** LA CALCULADORA **************\n***************  👁️  👄 👁️  💅 ***************\n********************************************\n\n')

a = float(input('Ingrese el primer valor: '))
print('\nIngresar el símbolo correspondiente a la operación deseada:\n\n-   +    Suma\n-   -    Resta \n- * o x  Multiplicación\n-   /    División\n-   p    Potencia\n-   r    Raiz cuadrada\n-  rad   Grados a radianes\n-  sin   Seno\n-  cos   Coseno\n-  tan   Tangente\n- lognat Logaritmo natural\n- log10  Logaritmo con base 10\n-   f    Factorial\n')
operacion = input('Operación: ')
operacion = evOperacion(operacion)

while True:
    try:    
        if operacion in ["r", "rad", "sin", "cos", "tan", "lognat", "log10", "f"]:
            if operacion == "r":
                resultado = math.sqrt(a)
            elif operacion == "rad":
                resultado = math.radians(a)
            elif operacion == "sin":
                resultado = math.sin(a)
            elif operacion == "cos":
                resultado = math.cos(a)
            elif operacion == "tan":
                if a == 90 or a == 270:
                    print('El resultado es Infinito (Tangente de 90º o 270º).\nEl valor ingresado volverá a 0.')
                    resultado = 0
                else:
                    resultado = math.tan(a)
            elif operacion == "lognat":
                resultado = math.log(a)
            elif operacion == "log10":
                resultado = math.log10(a)
            elif operacion == "f":
                resultado = math.factorial(a)

            print(f'Resultado: {resultado}\n')
        else:
            b = float(input("Ingrese el otro valor: "))

            if operacion == '+':
                resultado = suma(a, b)
            elif operacion == '-':
                resultado = resta(a, b)
            elif operacion in ['*', 'x']:
                resultado = multiplicacion(a, b)
            elif operacion == '/':
                resultado = division(a, b)
            elif operacion == "p":
                resultado = potencia(a, b)

            print(f"\nRESULTADO: {resultado}\n")

        a = resultado
        operacion = input('Si desea salir, teclee "Salir".\nSi desea realizar una operación desde 0, ingrese n\n\nContinuar con una operación:')
        operacion = evOperacion(operacion)
        if operacion == "salir":
            print('Saliendo de\n********************************************\n************** LA CALCULADORA **************\n***************  👁️  👄 👁️  💅 ***************\n********************************************')
            break
        elif operacion== 'n':
            a = float(input("Ingrese el primer valor: "))
            operacion = input('Operación: ', )
            operacion = evOperacion(operacion)
        
    except ValueError:
        print("Valor ingresado no valido. Reintente.")