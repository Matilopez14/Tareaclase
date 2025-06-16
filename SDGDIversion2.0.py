lista_productos=[]
#producto={"nombre":nombre,"cantidad":stock,precio:1500}




opcion="0"

"""
Agregar producto
Buscar producto
Actualizar cantidad/precio
Mostrar inventario completo
Eliminar producto
Salir
"""
def solicitarProducto():
    nombre=input("Ingrese el nombre del producto: ").lower()
    try:
        stock=int(input("Ingrese el stock del producto: "))
        precio=int(input("Ingrese el precio del producto: "))
        
        if stock<0 or precio <0:
            raise ValueError
            
        else:
            producto=[nombre,precio,stock]
            return producto

    except ValueError:
        print("Debe ingresar valores enteros positivos")
        

def buscarProducto(nombre):
    for producto in lista_productos:
        if producto["nombre"]==nombre:
            return producto
        else:
            print("No existe un producto con ese nombre")

    return None     

def guardarProducto(nombre,precio,stock):
   
   if buscarProducto(nombre)==None:
       producto={"nombre":nombre,"cantidad":stock,"precio":precio}
       lista_productos.append(producto)
       print("Se guardado correctamente el producto")

        
       

def actualizarProducto(nombre,nuevoPrecio,nuevoStock):
    productoEncontrado=buscarProducto(nombre)
    if buscarProducto!=None:
        indice=nombreProducto.index(nombre)
        productoEncontrado["cantidad"]=nuevoStock
        productoEncontrado["precio"]=nuevoPrecio
        lista_productos[indice]=productoEncontrado
        print("Producto actualizado con exito")
           
    else:
        print("No existe un producto con ese nombre")

def mostarInventarioCompleto():
    print("-"*60)
    if(len(lista_productos)==0):
        print("Aún no hay productos agregados")
        return
    else:

        for producto in lista_productos:
        
            print(f"Nombre: {producto["nombre"]} \t Precio: ${producto["precio"]} \t Stock: {producto["cantidad"]} unidades")
    
    print("-"*60)

def eliminarProducto(nombre):
    productoEncontrado=buscarProducto(nombre)
    if productoEncontrado!=None:
        lista_productos.remove(productoEncontrado)
        return True
    else:    
        return False



while opcion!="6":
    print("1.- Agregar producto")
    print("2.- Buscar producto")
    print("3.- Actualizar cantidad/precio")
    print("4.- Mostrar inventario completo")
    print("5.- Eliminar producto")
    print("6.- Salir")

    opcion=input("Ingrese la opción que desea(1-6): ")

    
    
    match opcion:

        case "1":
            nuevoProducto=solicitarProducto()#[nombre,precio,stock]
            if nuevoProducto != None:
                #guardarProducto(*nuevoProducto)
                guardarProducto(nuevoProducto[0],nuevoProducto[1],nuevoProducto[2])
        case "2":
            nombreProducto=input("Ingrese el nombre del producto a buscar: ").lower()
            productoEncontrado=buscarProducto(nombreProducto)
            if productoEncontrado!=None:
                print(f"Nombre: {productoEncontrado["nombre"]} \t Precio: ${productoEncontrado["precio"]} \t Stock: {productoEncontrado["cantidad"]} unidades")
        case "3":
            print("*Ingrese los datos del producto a actualizar*")
            nuevoProducto=solicitarProducto()#[nombre,precio,stock]
            if nuevoProducto != None:
                actualizarProducto(*nuevoProducto)
        case "4":
            mostarInventarioCompleto()
        case "5":
            nombreProducto=input("Ingrese el nombre del producto que desea eliminar"  )

            if eliminarProducto(nombreProducto)==True:
        case "6":
            #salir...
            pass        

