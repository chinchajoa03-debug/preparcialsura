#Llamando las funciones
import random

from funcionUno import ingresar_usuario
from funcionDos import crear_listado
from funcionTres import clasificar_prenda

ingresar_usuario("prueba@gmail.com", "1234", "jeanc", 8, "la mazea")
prenda = {
        "id":random.randint(1,100),
        "tipo":random.choice(["camisa", "pantalon", "falda", "zapatos"]),
        "marca":random.choice(["nike", "adidas", "puma", "reebok"]),
        "precio":random.choice([25000, 30000, 70000, 42000]),
        "estado":random.choice(["nuevo", "usado", "reparado"])
    }
crear_listado(10,prenda)

clasificar_prenda("REGULAR")