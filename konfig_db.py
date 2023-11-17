import mysql.connector

db_name = "gis_database"

def inisialisasi_db():
    host = "localhost"
    user = "root"
    password = ""
    sql_script_file = "gis_db.sql"

    db = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        )
    
    cursor = db.cursor()

    try:
        with open(sql_script_file, 'r') as file:
            sql_script = file.read()
        queries = [query.strip() for query in sql_script.split(';') if query.strip()]

        for query in queries:
            formatted_line = query.format(db_name=db_name) 
            cursor.execute(formatted_line)

    except mysql.connector.Error as err:
        print("Error: {}".format(err))

    finally:
        cursor.close()
        db.close()

def koneksi_db():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database=db_name
        )

        cursor = db.cursor(dictionary=True)

        db.commit()

        print("Koneksi sukses")
        return db, cursor
    except Exception as e:
        print(f"Error koneksi database: {e}")
        raise