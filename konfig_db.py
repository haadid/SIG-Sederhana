import mysql.connector

db_name = "gis_database"

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