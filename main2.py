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
# 10.2.2 importamos el getpass
import getpass

# 10 Hacer un sistema de verficacion de usuario y contraseña
# 10.2 creamos la funcion main


def main():
    username = input("Nombre de usuario: ")
    password = getpass.getpass("Contraseña: ")

    if verifica_credenciales(username, password):
        print("Login correcto")
    else:
        print("Login incorrecto")

# 12.2 creamos la funcion main2


def main2():
    crear_usuario(5, "marta", "ma123")

# 10.1 crear la funcion verifica_credenciales


def verifica_credenciales(username, password):
    # 10.1.1 conectarse una base de dato sqlite3
    conn = sqlite3.connect('miaplicacion.db')
    # 10.1.3 para trabajar con datos debemos crear un cursor
    cursor = conn.cursor()

    # 10.1.5 realizamos la query o consulta
    query = f"SELECT id FROM users WHERE username='{username}' AND password='{password}'"
    print("Query a ejecutar: ", query)

    # 10.1.6 el rows
    rows = cursor.execute(query)
    # 10.1.6.1 el metodo fetchone solamente me va a devolver un elemento
    data = rows.fetchone()
    print("data es: ", type(data))
    # 10.1.4 cerramos el cursor
    cursor.close()
    # 10.1.2 cerramos la conexion
    conn.close()

    # 10.1.7
    if data == None:
        return False
    return True

# 12 Creamos una funcion para crear un usuario o ingresar datos a la tabla


def crear_usuario(identificador, usuario, clave):
    # 12.1 copiamos el contenido de la funcion de verifica_credenciales
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()
    # 12.1.1 solo cambiamos el query
    # 12.1.1.1 primera forma de ingresar
    #query = f"INSERT INTO users (id, username, password) VALUES('{identificador}', '{usuario}', '{clave}')"
    #rows = cursor.execute(query)

    # 12.1.1.2 segunda forma de ingresar
    query = '''INSERT INTO users (id, username, password) VALUES(?, ?, ?)'''
    rows = cursor.execute(query, (identificador, usuario, clave))

    # 12.1.2
    print(type(rows))
    # 12.1.3 ponemos la funcion commit
    conn.commit()

    cursor.close()
    conn.close()


# 10.2.1
if __name__ == '__main__':
    main2()

# 11 comenteamos todo lo de abajo
# -----------------------------------------------------
# 2 Abrimos la base de datos
#conn = sqlite3.connect('miaplicacion.db')

# 4 las bases de datos para mandarles comandos utilizan cosistas que se denominan cursores
# 4.1 Cursor: Es una variable que va contener uno datos en un momento determinado, si tengo multiples datos, el cursor ira iterando
# 5 Creamos el cursor:
#cursor = conn.cursor()

# 7 Ejecutamos consultas
#rows = cursor.execute('SELECT * FROM users')

# 9 para tener solo un dato especifico
#rows = cursor.execute('SELECT * FROM users WHERE username="maik"')

# 8 ver los resultados
# for row in rows:
#    print(row)


# 6 cerramos el cursor
# cursor.close()
# 3 cerrar la conexion
# conn.close()

# --------------------------------------
