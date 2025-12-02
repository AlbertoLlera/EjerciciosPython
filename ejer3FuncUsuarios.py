usuarios_activos = []

def crear_usuario(nombre, email, activo = True):
    if activo:
        usuarios_activos.append([nombre, email, activo])



usuarios = [
    ["Ana", "ana@email.com", True],
    ["Carlos", "carlos@email.com", False],
    ["Maria", "maria@email.com", True]
]

for usuario in usuarios:
    crear_usuario(nombre = usuario[0], email = usuario[1], activo = usuario[2])

for activos in usuarios_activos:
    print(f"El usuario {activos[0]}, con email {activos[1]} está activo")