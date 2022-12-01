# 0 IMPORTANTE
"""
REQUISITOS
1. tener instalado el pysqlite global o dentro de un proyecto

pip install pysqlite3 --> global

pipenv install pysqlite3 --> Esto es dentro de un proyecto si no sabe que es pipenv consultelo

2.Abrimos el proyecto en el visual studio
3.creamos el archivo main.py osea es este archivo o puede tambien llamarse main2
"""

# 1 Importamos el sqlite3
import sqlite3

# 2 Abrimos la base de datos
conn = sqlite3.connect('miaplicacion.db')

# 4 las bases de datos para mandarles comandos utilizan cosistas que se denominan cursores
# 4.1 Cursor: Es una variable que va contener uno datos en un momento determinado, si tengo multiples datos, el cursor ira iterando
# 5 Creamos el cursor:
cursor = conn.cursor()

# 7 Ejecutamos consultas
#rows = cursor.execute('SELECT * FROM users')

# 9 para tener solo un dato especifico
rows = cursor.execute('SELECT * FROM users WHERE username="maik"')

# 8 ver los resultados
for row in rows:
    print(row)


# 6 cerramos el cursor
cursor.close()
# 3 cerrar la conexion
conn.close()
