arquetipo_personaje = {
    "Caballero": {
        "vida" : "",
        "defensa" : "",
        "ataque" : "",
        "alcance" : ""
    },
    "Guerrero": {
        "vida": 2,
        "defensa" : 2,
        "ataque" : 2,
        "alcance" : 2
    },
    "Arquero" : {
        "vida" : "",
        "defensa" : "",
        "ataque" : "",
        "alcance" : ""
    },
}

def modificacion_stats_caballero(caballero):
    caballero["vida"] = arquetipo_personaje["Guerrero"]["vida"] * 2
    caballero["defensa"] = arquetipo_personaje["Guerrero"]["defensa"] * 2
    caballero["ataque"] = int(arquetipo_personaje["Guerrero"]["ataque"]) // 2
    caballero["alcance"] = int(arquetipo_personaje["Guerrero"]["alcance"]) // 2

def modificacion_stats_arquero(arquero):
    arquero["vida"] = arquetipo_personaje["Guerrero"]["vida"]
    arquero["defensa"] = int(arquetipo_personaje["Guerrero"]["defensa"]) // 2
    arquero["ataque"] = arquetipo_personaje["Guerrero"]["ataque"]
    arquero["alcance"] = arquetipo_personaje["Guerrero"]["alcance"] * 2

def mostrar_pantalla():
    for rol, stats in arquetipo_personaje.items():
        print(f"Los stats del {rol} son: {stats}")

for key, value in arquetipo_personaje.items():
    match key:
        case "Caballero":
            modificacion_stats_caballero(value)
        case "Arquero":
            modificacion_stats_arquero(value)

mostrar_pantalla()


