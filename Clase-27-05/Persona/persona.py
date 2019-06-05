from persona import Persona

per1 = Persona("Carlos", "Lopez")
per2 = Persona("Mario", "Rodriguez")

print("Listado de nombres:")
print(per1.nombre)
print(per2.nombre)

print("\nListado de apellidos:")
print(per1.apellido)
print(per2.nombre)

'''
Aca usamos el set para cambiar el nombre y lo testeamos con un print
per1.nombre = "Jorge"
print(per1.nombre)
'''