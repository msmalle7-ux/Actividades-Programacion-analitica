# Ejercicios practica 3

# %% 1. Definir una función 
#Complete la palabra clave que define una función.

def saludar():
    print("Hola")
saludar()

# %% 2. Llamar a la función 
#Complete la línea que ejecuta la función ya definida.

def bienvenida():
    print("Bienvenido al curso")
bienvenida()


# %% 3. Predice el orden de ejecución 
#Sin ejecutar, determine en qué orden aparecen los mensajes.
def uno():
    print("A")
print("B")
uno()
print("C")

#imprime en el siguiente orden: B, A, C 
# Python lee uno() la graba en memoria pero no la ejecuta inmediatamente

# %% 4. Corrige el orden 
#El programa falla porque la función se llama antes de existir. Reescriba el bloque completo
#en el orden correcto.
def saludar(nombre):
        print("Hola,", nombre)
saludar("Ana")

# %% 5. Función con un parámetro 
#Complete el parámetro que recibe la función.

def saludar(nombre):
    print("Hola,", nombre)
saludar("Ana")

# %% 6. Función con dos parámetros 
#Complete los parámetros necesarios para calcular el área.

def area(base, altura):
    return base * altura
print(area(3, 4))

# %% 7. Completa la llamada 
#Complete los argumentos para obtener exactamente el resultado indicado.

def area(base, altura):
    return base * altura
print(area(5, 5.0)) # 25.0

# %% 8. Reutilizar la misma función 
#Llame tres veces a la misma función con precios distintos.
def con_iva(precio):
    return precio * 1.19
print(con_iva(100))
print(con_iva(50))
print(con_iva(200))

# %% 9. Parámetro o argumento 
#Observe la definición y la llamada, y distinga cada uno de los dos nombres.

def doble(n):
    return n * 2
resultado = doble(5)

# %% 10. Argumentos por posición 
#Complete la llamada para que se imprima: Ana 20 Bogota

def perfil(nombre, edad, ciudad):
    print(nombre, edad, ciudad)
perfil("Ana", 20,"Bogotá")



# %% 11. Argumentos por nombre 
#Complete los nombres de los parámetros para que el orden deje de importar.

def perfil(nombre, edad, ciudad):
    print(nombre, edad, ciudad)
perfil(edad =20, nombre ="Ana", ciudad ="Bogota")

# %% 12. Valor por defecto 
#Complete el valor por defecto del parámetro saludo.

def saludar(nombre, saludo= "Hola"):
    print(saludo, nombre)
saludar("Ana")

# %% 13. Reemplazar el valor por defecto 
#Complete el argumento que sustituye al saludo por defecto.

def saludar(nombre, saludo="Buen día"):
    print(saludo, nombre)
saludar("Luis", "Buenos días")

# %% 14. Orden de los parámetros 
#El siguiente encabezado produce un error. Reescriba la definición completa de forma
#correcta.

def registrar(producto, cantidad=1): # debe ir primero producto, luego cantidad
    print(producto, cantidad)

# %% 15. Una lista como argumento 
#Complete el recorrido para sumar todos los precios recibidos.

def total(precios):
    suma = 0
    for p in precios:
        suma = suma + p
    return suma
print(total([1200, 950, 3400]))

# %% 16. Devolver un valor 
#Complete la palabra clave que entrega el resultado.

def doble(n):
    return n * 2
print(doble(5))

# %% 17. Usar el valor devuelto 
#Complete la llamada para guardar el resultado y operar con él.

def doble(n):
    return n * 2
resultado = doble(6)
print(resultado + 1)

# %% 18. Función sin return 
#Sin ejecutar, determine qué imprimen las dos últimas líneas.
# Al ejecutar, imprime HOla Ana

def saludo(nombre):
    print("Hola,", nombre)
x = saludo("Ana")
print(x)

# %% 19. print o return 
#La suma falla. Corrija la función para que el resultado pueda seguir usándose y escriba la
# versión corregida.

def doble(n):
    resultado = n * 2
    return resultado    

total = doble(5) + 3
print (total)

# %% 20. return dentro de una condición 
#Complete la instrucción que devuelve el segundo resultado.

def signo(n):
    if n < 0:
        return "negativo"
    return "positivo"
print(signo(-4))
print(signo(7))

# %% 21. return termina la función 
#Sin ejecutar, determine qué se imprime y qué línea nunca se ejecuta.

def prueba(n):
    if n > 0:
        return "positivo"
    print("linea intermedia") # Esta es la linea que nunca se ejecuta
    return "otro"
print(prueba(5))

# %% 22. Devolver dos valores 
#Complete la función para que entregue el mínimo y el máximo.

def resumen(valores):
    return min(valores), max(valores)
menor, mayor = resumen([8, 3, 10, 5])
print(menor, mayor)

# %% Encadenar funciones 
#Complete la llamada interna para calcular el precio con IVA redondeado.
def con_iva(p):
    return p * 1.19
def redondear(valor):
    return round(valor, 2)
print(redondear(con_iva(1200)))

# %% 24. Variable local y global 
#Sin ejecutar, determine qué imprime cada una de las dos llamadas.

mensaje = "global"
def prueba():
    mensaje = "local"
    print(mensaje)
prueba()
print(mensaje)

# %% 25. Evitar las variables globales 
# Reescriba la función para que reciba el IVA como parámetro y no dependa de una variable
# externa.


def con_iva(precio, iva = 0.19):
    return precio * (1 + iva)

    
# %% 26. No modificar el original 
#Complete la función para que devuelva una lista nueva sin alterar la que recibe.

def agregar(lista, elemento):
    nueva = lista + [elemento]
    return nueva
datos = [1, 2]
print(agregar(datos,3))
print(datos)

# %% 27. Función que recibe una lista 
#Complete la función que calcula el promedio de una lista de notas.
def promedio(notas):
    total = 0
    for n in notas:
        total = total + n
    return total / len(notas)
print(promedio([3.5, 4.2, 2.8]))

# %% 28.Función que recibe un diccionario 
# Complete las claves para mostrar el nombre y la nota del estudiante.

def describir(alumno):
    print(alumno["nombre"], alumno["nota"])
describir({"nombre": "Laura", "nota": 4.6})

# %% 29. Función que devuelve una lista 
#Complete el método que agrega elementos y el valor que se devuelve.

def aprobados(estudiantes):
    resultado = []
    for e in estudiantes:
        if e["nota"] >= 3.0:
            resultado.append(e["nombre"])
    return resultado
datos = [{"nombre": "Ana", "nota": 4.2},
{"nombre": "Luis", "nota": 2.8}]
print(aprobados(datos))

# %% 30. Reporte de notas con funciones AVANZADO
#Complete el programa que calcula el promedio de un estudiante, decide si aprueba y
#muestra el reporte usando tres funciones.

def promedio(notas):
    total = 0
    for n in notas:
        total = total + n
    return total / len(notas)
def aprueba(prom, minimo= 3.0):
    return prom >= minimo
def reporte(nombre, notas):
    prom = promedio(notas)
    print(nombre, round(prom, 2))
    if aprueba(prom):
        print("Aprobado")
    else:
        print("No aprobado")
reporte("Laura", [3.5, 4.2, 2.8])

# %%
