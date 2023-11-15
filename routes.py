from konfig_db import koneksi_db

def tambah_lokasi(nama, latitude, longitude):
    try:
        db, cursor = koneksi_db()
        cursor.execute("INSERT INTO lokasi (nama, latitude, longitude) VALUES (%s, %s, %s)", (nama, latitude, longitude))
        db.commit()
        return True, "Data berhasil ditambahkan"
    except Exception as e:
        return False, f"Error tambah data: {e}"

def get_semua_lokasi():
    try:
        db, cursor = koneksi_db()
        cursor.execute("SELECT * FROM lokasi")
        lokasi_markers = cursor.fetchall()
        return True, lokasi_markers
    except Exception as e:
        return False, f"Error ambil data: {e}"

def get_lokasi_by_id(lokasi_id):
    try:
        db, cursor = koneksi_db()
        cursor.execute("SELECT * FROM lokasi WHERE id=%s", (lokasi_id,))
        lokasi = cursor.fetchone()
        return True, lokasi
    except Exception as e:
        return False, f"Error ambil data: {e}"

def update_lokasi(lokasi_id, nama, latitude, longitude):
    try:
        db, cursor = koneksi_db()
        cursor.execute("UPDATE lokasi SET nama=%s, latitude=%s, longitude=%s WHERE id=%s", (nama, latitude, longitude, lokasi_id))
        db.commit()
        return True, "Data berhasil diupdate"
    except Exception as e:
        return False, f"Error update data: {e}"

def hapus_lokasi(lokasi_id):
    try:
        db, cursor = koneksi_db()
        cursor.execute("DELETE FROM lokasi WHERE id=%s", (lokasi_id,))
        db.commit()
        return True, "Data berhasil dihapus"
    except Exception as e:
        return False, f"Error hapus data: {e}"
