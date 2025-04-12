from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from geopy.distance import geodesic

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/arkanesia'
db = SQLAlchemy(app)

class Wisata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(100))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

@app.route('/rekomendasi', methods=['POST'])
def rekomendasi():
    data = request.get_json()
    user_loc = (data['latitude'], data['longitude'])

    tempat_wisata = Wisata.query.all()
    hasil = []

    for tempat in tempat_wisata:
        lokasi_wisata = (tempat.latitude, tempat.longitude)
        jarak = geodesic(user_loc, lokasi_wisata).kilometers
        hasil.append({
            'name': tempat.name,
            'address': tempat.address,
            'jarak': jarak
        })

    hasil = sorted(hasil, key=lambda x: x['jarak'])[:5]  # Ambil 5 terdekat
    return jsonify(hasil)

if __name__ == '__main__':
    app.run(debug=True)
