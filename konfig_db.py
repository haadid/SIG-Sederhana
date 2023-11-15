import mysql.connector

def koneksi_db():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="gis_database"
        )

        cursor = db.cursor(dictionary=True)

        db.commit()

        print("Koneksi sukses")
        return db, cursor
    except Exception as e:
        print(f"Error koneksi database: {e}")
        raise