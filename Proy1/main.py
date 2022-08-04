nombre = "Hilario"
print("Tu nombre es " + nombre)

number = 12
print(number)
print(type(number))

number_2 = 5.6
print(type(number_2))

suma = 89 + 123.09 #conversión implícita
print("La suma es " + str(suma))
print(type(suma))

str_uno = "1"
print(4 + int(str_uno)) #conversion explícita (yo indico por código)

num1 = 7.5
print(int(num1))

num2 = 4
print(float(num2))

#formateo de cadenas
name = "Hilario"
lastname = "Medina"
age = 37
print("Tu nombre es {} {}, y tienes {} años".format(name, lastname, age))
#v3.6 python cadenas literales
print(f"Tu nombre es {name} {lastname} y tienes {age} años")

#operadores matemáticos
x = 4
y = 8
z = 9
print(f"La suma de {x} + {y} = {x + y}")
print(f"La resta de {z} - {x} = {z - x}")
print(f"La multiplicación de {x} * {y} = {x * y}")
print(f"La división de {z} / {x} = {z / x}")
print(f"La división al piso de {z} // {x} = {z // x}") #quita los decimales
print(f"El resto de {z} % {x} = {z % x}")
print(f"La potencia de {y} ** {x} = {y ** x}")
print(f"La raíz cuadra de {z} = {z **0.5}")
print("")
#redondeo
resultado = 90/7
print(resultado)
print(round(resultado))
print(round(resultado, 2))

num1 = round(13/2,0)
print(num1)
print(type(num1))
