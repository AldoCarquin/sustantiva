def suma (a, b):
    return a + b

def resta (a, b):
    return a - b

def multiplicacion (a, b):
    return a * b

def division (a, b):
    if b == 0:
        print("No es posible la división en 0!!!")
    else:
        return a / b
    
def evaluar(a,b):
            if operacion == "+":
                print(f"RESULTADO: {suma(a,b)}")
                a = suma(a,b)
            elif operacion == "-":
                print(f"RESULTADO: {resta(a,b)}")
                a = resta(a,b)
            elif operacion == "*" or operacion == "x":
                print(f"RESULTADO: {multiplicacion(a,b)}")
                a = multiplicacion(a,b)
            elif operacion == "/":
                print(f"RESULTADO: {division(a,b)}")
                a = division(a,b)
            else:
                print("Símbolo no valido.")

def evOperacion (operacion):
    while operacion != "+" and operacion != "-" and operacion != "*" and operacion != "x" and operacion != "/":
        print("Operación no válida. Por favor ingrese otra operación.")
        operacion=str(input("Operación:"))

c = (evaluar)

print("********************************************\n*************** Bienvenidx a ***************\n************** LA CALCULADORA **************\n***************  👁️  👄 👁️  💅 ***************\n********************************************\n\n")

print("ATENCION")

a = input("Primero ingrese el PRIMER valor:")

print("AHORA ingresar el símbolo correspondiente a la operación deseada:\n+ Suma\n- Resta \n* o x Multiplicación\n/ división")
        

while True:
    operacion = (input("Operación:"))
    evOperacion(operacion)
    b = input("Ahora ingrese el OTRO valor:")        
    c = evaluar(a, b)
    a = c

        
        

        






