import math


# FUNCIONES 
def suma(a, b):
    resultado = (a + b)
    return resultado

def resta(a, b):
    resultado = (a - b)
    return resultado

def multiplicacion(a, b):
    resultado = (a * b)
    return resultado

def division(a, b):
    if b == 0:
        print('No es posible la división en 0!!!')
        return None
    else:
        resultado = a / b
        return resultado
    
def potencia(a, b):
    resultado = (a ** b)
    return resultado

# FUNCIONES SOLAS

def raiz(a):
    resultado = math.sqrt(a) 
    return resultado

def rad(a):
    resultado = math.radians(a)
    return resultado

def sin(a):
    resultado = math.sin(a)
    return resultado 

def cos(a):
    resultado = math.cos(a)
    return resultado

def tan(a):
    if a == 90 or a == 270:
        print('El resultado es infinito (Tangente de 90º o 270º).\nEl valor ingresado volverá a 0.')
        resultado = 0
    else:
        resultado = math.tan(a)
    return resultado

def lognat(a):
    resultado = math.log(a)
    return resultado

def log10(a):
    resultado = math.log10(a)
    return resultado

def f(a):
    resultado = math.factorial(a)
    return resultado

# FUNCION EVALUADORA
def evOperacion(operacion):
    while operacion not in ['+', '-', '*', 'x', '/','raiz', 'rad', 'sin', 'cos', 'tan', 'lognat', 'log10', 'f', 's','n']:
        print('Operación no válida. Por favor ingrese otra operación.')
        operacion = input('Operación: ')
    return operacion

# MENU 
def menu(operacion,a, resultado):
    if operacion in ['raiz', 'rad', 'sin', 'cos', 'tan', 'lognat', 'log10', 'f']:
        match operacion:
            case 'raiz':
                resultado = raiz(a)
                return resultado
            case 'rad':
                resultado = rad(a)
                return resultado
            case 'sin':
                resultado = sin(a)
                return resultado
            case 'cos':
                resultado = cos(a)
                return resultado
            case 'tan':
                resultado = tan(a)
                return resultado
            case 'lognat':
                resultado = lognat(a)
                return resultado
            case 'log10':
                resultado = log10(a)
                return resultado
            case 'f':
                resultado = f(a)
                return resultado
    else:
        b = float(input("Ingrese el otro valor: "))
        match operacion:
            case '+':
                resultado = suma(a,b)
                return resultado
            case '-':
                resultado = resta(a,b)
                return resultado
            case '*':
                resultado = multiplicacion(a,b)
                return resultado
            case 'x':
                resultado = multiplicacion(a,b)
                return resultado
            case '/':
                resultado = division(a,b)
                return resultado

def main():
    print('********************************************\n*************** Bienvenidx a ***************\n************** LA CALCULADORA **************\n***************  👁️  👄 👁️  💅 ***************\n********************************************\n\n')
    while True:
        try:
            a = int(input('Ingrese el primer valor: '))
            print('\nIngresar el símbolo correspondiente a la operación deseada:\n\n-   +    Suma\n-   -    Resta \n- * o x  Multiplicación\n-   /    División\n-   p    Potencia\n-  raiz  Raiz cuadrada\n-  rad   Grados a radianes\n-  sin   Seno\n-  cos   Coseno\n-  tan   Tangente\n- lognat Logaritmo natural\n- log10  Logaritmo con base 10\n-   f    Factorial\n-   s    PARA SALIR')
            operacion = input('Operación: ')
            operacion = evOperacion(operacion)
            while operacion != 's':
                resultado = menu(operacion, a, 0)
                print(f'\n**** El resultado es {resultado} ***\n')
                a = resultado
                operacion = input('Si desea salir, teclee "s".\nSi desea realizar una operación desde 0, ingrese n\n\nContinuar con una operación:')
                operacion = evOperacion(operacion)
                if operacion == "s":
                    print('Saliendo de\n********************************************\n************** LA CALCULADORA **************\n***************  👁️  👄 👁️  💅 ***************\n********************************************')
                    break
                elif operacion== 'n':
                    a = float(input("Ingrese el primer valor: "))
                    operacion = input('Operación: ', )
                    operacion = evOperacion(operacion)
        except ValueError:
            print('Valor ingresado invalido.')
        break





if __name__ == "__main__":
    main()