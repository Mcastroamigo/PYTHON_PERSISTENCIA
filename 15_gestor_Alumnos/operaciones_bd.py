import mysql.connector as con
def crear_conexion():
    return con.connect(host="localhost",
               user="root",
               password="root",
               port=3306,
               database="mundo")
    
def alta_alumnos(nombre, dni, curso):
    db = crear_conexion()
    cursor = db.cursor()

    sql_comprobar = "SELECT dni FROM alumnos WHERE dni = %s"
    cursor.execute(sql_comprobar, (dni,))

    resultado = cursor.fetchall()

    if len(resultado) > 0:
        print("El DNI ya existe")
    else:
        sql_insert = "INSERT INTO alumnos (nombre, dni, curso) VALUES (%s, %s, %s)"
       
        cursor.execute(sql_insert, (nombre, dni, curso))
        db.commit()
        print("Alumno añadido correctamente.")

    cursor.close()
    db.close()
        
        
        
def buscar_alumnos_curso(curso):
    db = crear_conexion()
    cursor = db.cursor()
    
    sql_buscar_curso="SELECT * FROM alumnos WHERE curso = &s"
    cursor.execute(sql_buscar_curso)  
    resultado=cursor.fetchall()
    db.close()
    
    
def buscar_alumnos_dni(dni):
    db = crear_conexion()
    cursor = db.cursor()
    
    sql_buscar_dni="SELECT * FROM alumnos WHERE dni = &s"
    cursor.execute(sql_buscar_dni)  
    resultado=cursor.fetchall()
    db.close()