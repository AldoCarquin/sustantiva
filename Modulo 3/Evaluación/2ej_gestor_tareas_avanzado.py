import datetime

tareas=[]
tareasRealizadas=[]


print('***************************************\n****Bienvenidx al gestor de tareas*****\n***************************************')

while True:

    try:
        print('\n***************************************\nIngrese una de las siguientes opciones para continuar:\n1.- Ver tareas\n2.- Agregar tarea\n3.- Completar tarea\n4.- Borrar tarea\n5.- Ver tareas realizadas.\n6.- Exportar archivo TXT con las listas.\n7.- Salir\n***************************************\n')
        opcion=int(input('Opción:'))

        # OPCION 1 VER TAREAS
        if opcion == 1:
            lenTareas=len(tareas)
            if lenTareas == 0:
                print(f'La lista de tareas actuales está vacia.')
                input("Presiona Enter para continuar...")
            else:
                number=1
                for n in tareas:
                    print(f'{number}.- {n}')
                    number+=1
                input("Presiona Enter para continuar...")
                
        # OPCION 2 AGREGAR TAREA
        elif opcion == 2:
            tarea=input('Ingrese una tarea para agregar:')
            if tarea== "":
                print('Tarea no valida. Reintente.')
            else:
                tareas.append(tarea)
                print(f'Tarea "{tarea}" ingresada con éxito.')
                input("Presiona Enter para continuar...")
            
            
            
        # OPCION 3 COMPLETAR TAREA
        elif opcion == 3:
             
            # SI NO HAY TAREAS EN EL SISTEMA:
            if len(tareas) == 0:
                print('No hay tareas ingresadas.')
                input("Presiona Enter para continuar...")
                
            # SI HAY TAREAS EN EL SISTEMA
            else:
                number=1
                
                print('Las tareas actuales son las siguientes:')
                for n in tareas:
                    print(f'{number}.- {n}')
                    number+=1
            
                try:
                    completada=int(input('Ingresa número de tarea completada:'))-1
                    traspaso=tareas[completada]
                    tareas.pop(completada)
                    tareasRealizadas.append(traspaso)
                    print(f'Tarea {traspaso} modificada satisfactoriamente.')
                    input("Presiona Enter para continuar...")
                    
                    
                except ValueError:
                    print('Valor ingresado no valido. Ingrese por favor un número de la lista.')
     
            
        # OPCION 4 BORRAR TAREA 
        elif opcion==4:
            if len(tareas) == 0:
                print('No hay tareas pendientes para borrar.')
                input("Presiona Enter para continuar...")
            else:
                print('Las tareas actuales son las siguientes:')
                number=1
                for n in tareas:
                    print(f'{number}.- {n}')
                    number+=1
                try:
                    borrar=int(input('Ingresa número de la tarea a eliminar:'))-1
                    eliminada = tareas[borrar]
                    tareas.pop(borrar)
                    print(f'Tarea "{eliminada}" eliminada satisfactoriamente.')
                    input("Presiona Enter para continuar...")
                                      
                except ValueError:
                    print('Valor ingresado no valido. Ingrese por favor un número de la lista.')    
            
        # OPCION 5 TAREAS REALIZADAS
        elif opcion==5:
            if len(tareasRealizadas) == 0:
                print('No hay tareas realizadas.')
                input("Presiona Enter para continuar...")
            else:
                print('Las tareas realizadas son las siguientes:')
                number=1
                for n in tareasRealizadas:
                    print(f'{number}.- {n}')
                    number+=1
                input("Presiona Enter para continuar...")
            
        # OPCION 6 GUARDAR DATOS
        elif opcion == 6:
            print("Opción 6")
            momento = datetime.datetime.now()
            nombreArchivo = momento.strftime("%H-%M-%S_%d-%m-%y.txt")
            
            # Abrir el archivo en modo escritura y escribir en él
            with open(nombreArchivo, "w") as archivo:
                archivo.write("\n******************************************\nTareas pendientes:\n")
                if len(tareas) == 0:
                    archivo.write("No hay tareas pendientes :(\n")
                else:
                    number=1
                    for tarea in tareas:
                        archivo.write(f"{number}.- {tarea}\n")
                        number += 1
                
                archivo.write("\n******************************************\nTareas completadas:\n")
                if len(tareasRealizadas) == 0:
                    archivo.write("No hay tareas realizadas :(\n")
                else:
                    number=1
                    for tareaHecha in tareasRealizadas:
                        archivo.write(f"{number}.- {tareaHecha}\n")
                        number += 1
            
            print("Archivo creado:", nombreArchivo)
            
        
        # OPCION 7 SALIR
        elif opcion==7:
            print('Muchas gracias.')
            break
        
        # EXCEPCIONES
        else:
            print('Menú no valido. Por favor vuelve a ingresar un número del 1 al 6.')
    except ValueError:
        print('Valor invalido. Por favor ingrese un valor numérico del 1 al 6')
    