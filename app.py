from flask import Flask, render_template, request, redirect, url_for
from routes import *

app = Flask(__name__)

@app.route('/')
def index():
    success, lokasi_markers = get_semua_lokasi()
    return render_template('index.html', success=success, lokasi_markers=lokasi_markers)

@app.route('/tambah_lokasi', methods=['POST'])
def tambah_lokasi_route():
    nama = request.form['lokasi']
    latitude = float(request.form['lat'])
    longitude = float(request.form['long'])
    
    success, message = tambah_lokasi(nama, latitude, longitude)

    print(message)

    return redirect(url_for('index'))

@app.route('/edit_lokasi/<int:lokasi_id>')
def edit_lokasi(lokasi_id):
    success, lokasi = get_lokasi_by_id(lokasi_id)
    return render_template('edit.html', success=success, lokasi=lokasi)

@app.route('/update_lokasi/<int:lokasi_id>', methods=['POST'])
def update_lokasi_route(lokasi_id):
    nama = request.form['lokasi']
    latitude = float(request.form['lat'])
    longitude = float(request.form['long'])

    success, message = update_lokasi(lokasi_id, nama, latitude, longitude)

    print(message)

    return redirect(url_for('index'))

@app.route('/hapus_lokasi/<int:lokasi_id>')
def hapus_lokasi_route(lokasi_id):
    success, message = hapus_lokasi(lokasi_id)

    print(message)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
