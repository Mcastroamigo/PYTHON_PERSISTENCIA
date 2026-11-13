
import mysql.connector as con



def crear_conexion():
    return con.connect(
        host="localhost",
        user="root",
        password="root",
        port=3306,
        database="universidad"
    )



def alta_alumnos(nombre, dni, curso, email, nota):

    db = crear_conexion()
    cursor = db.cursor()

    try:

        sql_comprobar = "SELECT dni FROM alumnos WHERE dni = %s"
        cursor.execute(sql_comprobar, (dni,))

        resultado = cursor.fetchone()

        if resultado:
            return False

    
        sql_insert = """
        INSERT INTO alumnos (nombre, dni, curso, email, nota)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(sql_insert, (nombre, dni, curso, email, nota))

        db.commit()

        return True

    except con.IntegrityError:
        return False

    finally:
        cursor.close()
        db.close()


def buscar_alumnos_curso(curso):

    db = crear_conexion()
    cursor = db.cursor(dictionary=True)

    sql = "SELECT * FROM alumnos WHERE curso = %s"

    cursor.execute(sql, (curso,))

    resultado = cursor.fetchall()

    cursor.close()
    db.close()

    return resultado




def buscar_alumnos_dni(dni):

    db = crear_conexion()
    cursor = db.cursor(dictionary=True)

    sql = "SELECT * FROM alumnos WHERE dni = %s"

    cursor.execute(sql, (dni,))

    resultado = cursor.fetchone()

    cursor.close()
    db.close()

    return resultado




def eliminar_alumno(dni):

    db = crear_conexion()
    cursor = db.cursor()

    sql = "DELETE FROM alumnos WHERE dni = %s"

    cursor.execute(sql, (dni,))

    db.commit()

    resultado = cursor.rowcount

    cursor.close()
    db.close()

    return resultado > 0




def cursos():

    db = crear_conexion()
    cursor = db.cursor(dictionary=True)

    sql = "SELECT DISTINCT curso FROM alumnos"

    cursor.execute(sql)

    resultado = cursor.fetchall()
import mysql.connector as con
def crear_conexion():
    return con.connect(host="localhost",
               user="root",
               password="root",
               port=3306,
               database="universidad")
    
def buscar_alumno(dni):
    sql="select * from alumnos where dni=%s"
    db=crear_conexion()
    cursor=db.cursor(dictionary=True)
    cursor.execute(sql,(dni,))
    resultado= cursor.fetchone() #Devuelve el alumno con ese dni. Si no existe devuelve None
    db.close()
    return resultado
def buscar_alumnos_curso(curso):
    sql="select * from alumnos where curso=%s"
    db=crear_conexion()
    cursor=db.cursor(dictionary=True)
    cursor.execute(sql,(curso,))
    resultado=cursor.fetchall()
    db.close()
    return resultado
def alta_alumno(dni,nombre,email,curso,nota):
    sql="insert alumnos(dni,nombre,email,curso,nota) values(%s,%s,%s,%s,%s)"
    db=crear_conexion()
    cursor=db.cursor()
    cursor.execute(sql,(dni,nombre,email,curso,nota))
    db.commit()
    db.close()
def eliminar_alumno(dni):
    sql="delete from alumnos where dni=%s"
    db=crear_conexion()
    cursor=db.cursor()
    cursor.execute(sql,(dni,))  
    db.commit()
    db.close()  
def cursos():
    sql="select distinct(curso) from alumnos"
    db=crear_conexion()
    cursor=db.cursor(dictionary=True)
    cursor.execute(sql)
    resultado=cursor.fetchall() #[{"curso":"Python","curso":"Java"}]
    resultado=[c["curso"] for c in resultado]
    db.close()
    return resultado    
def actualizar(dni,nombre,email,curso,nota):
    sql="update alumnos set nombre=%s, email=%s, curso=%s, nota=%s where dni=%s"
    db=crear_conexion()
    cursor=db.cursor()
    cursor.execute(sql,(nombre,email,curso,nota,dni))
    db.commit()
    db.close() 
    resultado = [c["curso"] for c in resultado]

    cursor.close()
    db.close()

    return resultado

def actualizar(dni,nombre,email,curso,nota):
    sql="update alumnos set nombre=%s, email=%s curso=%s, nota=%s where dni=%s"
    db=crear_conexion()
    cursor=db.cursor()
    cursor.execute(sql,(nombre,email,curso,nota,dni))
    db.commit()
    db.close()