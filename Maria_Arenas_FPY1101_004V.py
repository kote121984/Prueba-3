import json
import datetime

pizzas={
    "cuatro quesos":{"pequeña":6000,"mediana":9000,"familiar":12000},
    "hawaiana":{"pequeña":6000,"mediana":9000,"familiar":12000},
    "napolitana":{"pequeña":5500,"mediana":8500,"familiar":11000},
    "pepperoni":{"pequeña": 7000, "mediana":10000,"familia":13000}
}

ventas=[]
def menu_inicio():
    print(".::::Pizzas DuocUC::::.")
    print("1.Registrar una venta")
    print("2.Mostrar todas las ventas.")
    print("3.Buscar ventas por cliente.")
    print("4.Guardar las ventas en un archivo.")
    print("5.Cargar las ventas desde un archivo.")
    print("6.Generar Boleta")
    print("7.Salir del programa.")

def registrar_ventas():
        cliente=input("Ingrese nombre del cliente: ")
        pizza=input("¿Que tipo de pizza desea?:\ncuatro quesos\nhawaiana\nnapolitana\npepperoni: \n")
        tamaño=input("¿Que tamaño desea?: \npequeña\nmediana\nfamiliar\n: ")
        cantidad=int(input("¿cuantas pizzas desea?: "))

        if pizza in pizzas and tamaño in pizzas[pizza]:
              precio =pizzas[pizza][tamaño]*cantidad
        else:
              print("Tipo de Pizza o tamaño no valido")  
              return
         
        tipo=input("¿Ingrese el tipo de usuario?: \nestudiante diurno\nestudiante vespertino\nadministrativo\n: ")
        descuento=0.0

        if tipo=="estudiante diurno":
              descuento=0.15
        elif tipo=="estudiante vespertino":
              descuento=0.20
        elif tipo=="administrativo":
              descuento=0.10
        else:
              print("Tipo de usuario no valido")
              return
        descuento_total=precio*descuento
        precio_final=precio-descuento_total

        venta= {
              "cliente":cliente,
              "tipo de pizza":pizza,
              "tamaño de la pizza":tamaño,
              "cantidad":cantidad,
              "total a pagar":precio_final,
              "fecha y hora":datetime.datetime.now().strftime("%y-%m-%d %h:%m")
        }                           
        
        ventas.append(venta)
        print("venta registrada Exitosamente")

def mostrar_ventas():
    if ventas:
        for idx, venta in enumerate(ventas, start=1):
            print(f"\nventa {idx}: ")
            print(f"Cliente      : {venta['cliente']}")
            print(f"Tipo de pizza: {venta['tipo de pizza']}")
            print(f"Tamaño       : {venta['tamaño de la pizza']}")
            print(f"Cantidad     : {venta['cantidad']}")
            print(f"Precio final : ${venta['total a pagar']:.2f}")
            print(f"Fecha y hora : {venta['fecha y hora']}")
    else:
         print("No hay ventas  resgistradas")
def buscar_clientes():
    buscar=input("Ingrese el nombre del Cliente: ")
    cliente_encontrado=False
    for venta in ventas:
        if venta["cliente"].lower()==buscar.lower():    
            print(f"\nCliente: {venta['cliente']}")
            print("-------------------------------------------")
            print(f"Tipo de pizza :     {venta['tipo de pizza']}")
            print(f"Tamaño        :     {venta['tamaño de la pizza']}")
            print(f"Cantidad      :     {venta['cantidad']}")
            print(f"Fecha y hora  : {venta['fecha y hora']}")
            print("-------------------------------------------")
            cliente_encontrado=True
            break
    if not cliente_encontrado:
            print(f"Cliente {buscar} no tiene ningun pedido realizado.")

def guardar_venta():
    with open('ventas.json', 'w') as archivo:
        json.dump(ventas, archivo)
    print('ventas guardadas con exito.')

def cargar_ventas():
    global ventas
    try:
        with open('ventas.json', 'r') as archivo:
            ventas= json.load(archivo)
        print('ventas cargadas en archivo ventas')
    except FileNotFoundError:
        print('no se encontro el archivo ventas')    

def generar_boleta():
    boleta=input("Ingrese el nombre del Cliente: ")
    cliente_encontrado=False
    for venta in ventas:
        if venta["cliente"].lower()==boleta.lower():    
            print("\n------------ Boleta de Venta ------------")
            print(f"Fecha y hora: {venta['fecha y hora']}")
            print(f"Cliente: {venta['cliente']}")
            print("-------------------------------------------")
            print(f"Tipo de pizza:     {venta['tipo de pizza']}")
            print(f"Tamaño       :     {venta['tamaño de la pizza']}")
            print(f"Cantidad     :     {venta['cantidad']}")
            print(f"Precio final :    ${venta['total a pagar']:.2f}")
            print("-------------------------------------------")
            cliente_encontrado=True
            break
    if not cliente_encontrado:
            print(f"Cliente {boleta} no tiene ningun pedido realizado.")
        
     
while True:
    menu_inicio()
    opcion = input("\tOPC: ")

    if opcion == '1':
        registrar_ventas()

    elif opcion == '2':
        mostrar_ventas()

    elif opcion == '3':
        buscar_clientes()  

    elif opcion == '4':
        guardar_venta()

    elif opcion == '5':
        cargar_ventas()

    elif opcion == '6':
        generar_boleta()

    elif opcion == '7':
        print("Saliendo del Programa.....") 
        break          
    else:
         print("Seleccione una opcion valida")