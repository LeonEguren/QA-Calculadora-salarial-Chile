import os
import pyodbc
from dotenv import load_dotenv

# from tests.Chile.test_candidato_CL import experiencia_CL
load_dotenv()
Url_Calculadora_test_Cl = os.getenv("Url_Calculadora_test_Cl")
nombre_candidato_nuevo = os.getenv("nombre_candidato_nuevo")
nombre_candidato_registrado = os.getenv("nombre_candidato_registrado")
correo_candidato_nuevo_CL = os.getenv("correo_candidato_nuevo_CL")
correo_candidato_registrado_CL = os.getenv("correo_candidato_registrado_CL")
especialidad_CL = os.getenv("especialidad_CL")
posicion_CL = os.getenv("posicion_CL")
localidad_RM_CL = os.getenv("localidad_RM_CL")
localidad_ZonaSur_CL = os.getenv("localidad_ZonaSur_CL")
experiencia_CL = os.getenv("experiencia_CL")
buzon_correo = os.getenv("buzon_correo")
salario_a_ingresar = os.getenv("salario_a_ingresar")


# Función para conectarse a la base de datos de SQL Server
def connect_to_sql_server_CL():
    server = os.getenv('DB_SERVER_CL')
    database = os.getenv('DB_DATABASE_CL')
    user = os.getenv('DB_USER_CL')
    password = os.getenv('DB_PASS_CL')

    try:
        connection = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={user};'
            f'PWD={password};'
            'Trusted_Connection=no;'
        )
        print("Conexión exitosa a la base de datos SQL Server")
        return connection
    except Exception as error:
        print("Error al conectar a la base de datos SQL Server:", error)
        return None

# Función para ejecutar una consulta
def execute_query(connection, query, select=True):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        if select:
            result = cursor.fetchall()
            return result
        else:
            connection.commit()  # Confirmar la transacción
            return True
    except Exception as error:
        print("Error al ejecutar la consulta:", error)
        return None

# Función para eliminar un registro basado en el correo
def eliminar_registro_CL(mail: str) -> bool:
    conn = connect_to_sql_server_CL()
    if conn:
        delete_query = f"DELETE FROM users WHERE email = '{mail}'"
        print("Ejecutando query:", delete_query)

        # Ejecutar la eliminación sin verificar si el registro existe
        result = execute_query(conn, delete_query, select=False)
        if result:
            print(f'Registro con correo {mail} eliminado con éxito.')
            return True
        else:
            print(f'No se pudo eliminar el registro con correo {mail}.')
            return False
    else:
        print("No se pudo conectar a la base de datos.")
        return False

def obtener_rango_minimo_CL():
    connection = connect_to_sql_server_CL()
    if connection:
        try:
            cursor = connection.cursor()
            # Consulta SQL usando parámetros para evitar inyección SQL
            query = """
            SELECT rangoMinimo 
            FROM CSRNG 
            WHERE especialidad = ? 
              AND puesto = ? 
              AND escala = ? 
              AND region = ?
            """
            # Ejecuta la consulta con los valores correspondientes
            cursor.execute(query, (especialidad_CL, posicion_CL, experiencia_CL, localidad_RM_CL))
            result = cursor.fetchone()  # Obtener el primer resultado

            if result:
                rango_minimo = result[0]  # Asumiendo que 'rangoMinimo' está en la primera columna
                return float(rango_minimo)  # Convertir a float
            else:
                print("No se encontraron resultados para la consulta.")
                return None
        except Exception as error:
            print("Error al ejecutar la consulta:", error)
            return None
        finally:
            connection.close()  # Cerrar la conexión
    else:
        print("No se pudo conectar a la base de datos.")
        return None

def obtener_fecha_CL():
    connection = connect_to_sql_server_CL()
    if connection:
        try:
            cursor = connection.cursor()
            # Consulta SQL usando parámetros para evitar inyección SQL
            query = """
            SELECT rangoMinimo 
            FROM CSRNG 
            WHERE especialidad = ? 
              AND puesto = ? 
              AND escala = ? 
              AND region = ?
            """
            # Ejecuta la consulta con los valores correspondientes
            cursor.execute(query, (especialidad_CL, posicion_CL, experiencia_CL, localidad_RM_CL))
            result = cursor.fetchone()  # Obtener el primer resultado

            if result:
                fecha_creacion = result[0]  # Asumiendo que 'fechaCreacion' está en la primera columna
                return fecha_creacion.year  # Devolver solo el año
            else:
                print("No se encontraron resultados para la consulta.")
                return None
        except Exception as error:
            print("Error al ejecutar la consulta:", error)
            return None
        finally:
            connection.close()  # Asegurar que la conexión se cierra
    else:
        print("No se pudo conectar a la base de datos.")
        return None
