def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        print("No es posible la división en 0!!!")
        return None 
    else:
        return a / b

def evOperacion(operacion):
    while operacion not in ['+', '-', '*', 'x', '/','salir','n']:
        print("Operación no válida. Por favor ingrese otra operación.")
        operacion = input("Operación: ")
    return operacion

print("********************************************\n*************** Bienvenidx a ***************\n************** LA CALCULADORA **************\n***************  👁️  👄 👁️  💅 ***************\n********************************************\n\n")

a = float(input("Ingrese el primer valor: "))
print("\nIngresar el símbolo correspondiente a la operación deseada:\n+ Suma\n- Resta \n* o x Multiplicación\n/ División")
operacion = input('Operación: ')
operacion = evOperacion(operacion)

while True:
    try:    

        b = float(input("Ingrese el otro valor: "))

        if operacion == '+':
            resultado = suma(a, b)
        elif operacion == '-':
            resultado = resta(a, b)
        elif operacion in ['*', 'x']:
            resultado = multiplicacion(a, b)
        elif operacion == '/':
            resultado = division(a, b)

        print(f"\nRESULTADO: {resultado}\n")

        a = resultado
        operacion = input('Si desea salir, teclee "Salir".\nSi desea realizar una operación desde 0, ingrese n\n\nOperación:')
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

