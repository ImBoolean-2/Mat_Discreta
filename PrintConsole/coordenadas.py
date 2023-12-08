def info():
    aristas = {
            "1": {"4": 0.1, "6": 10.5},
            "2": {"7": 3.5, "3": 5.9,"6": 5.9, "4": 3.2},
            "3": {"2": 5.9, "10": 5.9, "11": 13.3},
            "4": {"1": 0.1, "7": 1.5},
            "5": {"6": 1.5, "9": 30.0},  
            "6": {"5": 1.5, "1": 10.5, "2": 5.9},
            "7": {"2": 3.5, "4": 1.5, "10": 1.5},
            "8": {"10": 45.0, "11": 45.0, "9": 45.0},
            "9": {"5": 30.0, "8": 45.0},
            "10": {"8": 45.0, "3": 5.9, "11": 13.3},
            "11": {"8": 45.0, "3": 13.3, "10": 13.3}
        }

    lugares = {
            "1": {"nombre": "Plaza mayor de lima", "latitud": 12.0459754, "longitud": 77.0307660},
            "2": {"nombre": "Circuito magico de las aguas", "latitud": 12.0703313, "longitud": 77.0361421},
            "3": {"nombre": "Parque de las leyendas", "latitud": 12.0685787, "longitud": 77.0892947},
            "4": {"nombre": "Catedral de lima", "latitud": 12.0467484, "longitud": 77.0345755},
            "5": {"nombre": "Puente de los suspiros", "latitud": 12.1491583, "longitud": 77.0231006},
            "6": {"nombre": "Parque 7 de junio", "latitud": 12.1208236, "longitud": 77.0297885},
            "7": {"nombre": "Museo de arte de lima-mali", "latitud": 12.0604452, "longitud": 77.0395717},
            "8": {"nombre": "Castillo chancay", "latitud": 11.5741923, "longitud": 77.2741650},
            "9": {"nombre": "Pachacamac", "latitud": 12.1504446, "longitud": 76.8735087},
            "10": {"nombre": "Parque del amor", "latitud": 11.8780339, "longitud": 77.1691546},
            "11": {"nombre": "Fortaleza del real felipe", "latitud": 12.0625086, "longitud": 77.1513723}
        }
    return aristas, lugares