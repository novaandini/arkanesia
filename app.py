from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from geopy.distance import geodesic
from dotenv import load_dotenv
# from sklearn.metrics.pairwise import cosine_similarity
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)

class Tour(db.Model):
    __tablename__ = 'tour'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(191), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(191), nullable=False)
    image = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=True)
    prices = db.Column(db.Float, nullable=False)
    district = db.Column(db.String(191), nullable=True)
    province = db.Column(db.String(191), nullable=True)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    createdAt = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    updatedAt = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<Tour {self.name}>'

@app.route('/recommendation', methods=['POST'])
def recommendation():
    data = request.get_json()
    user_loc = (data['latitude'], data['longitude'])

    tours = Tour.query.all()
    hasil = []

    for tour in tours:
        lokasi_wisata = (tour.latitude, tour.longitude)
        jarak = round(geodesic(user_loc, lokasi_wisata).kilometers, 2)
        hasil.append({
            'id': tour.id,
            'name': tour.name,
            'date': tour.date,
            'location': tour.location,
            'image': tour.image,
            'description': tour.description,
            'link': tour.link,
            'prices': tour.prices,
            'disrict': tour.disrict,
            'province': tour.province,
            'latitude': tour.latitude,
            'longitude': tour.longitude,
            'createdAt': tour.createdAt,
            'updatedAt': tour.updatedAt,
            'jarak': jarak
        })

    hasil = sorted(hasil, key=lambda x: x['jarak'])[:5]  # Ambil 5 terdekat
    return jsonify(hasil)

# def calculate_similarity(user_interest, item_categories):
#     all_categories = list(set(user_interest + item_categories))
#     user_vector = [1 if cat in user_interest else 0 for cat in all_categories]
#     item_vector = [1 if cat in item_categories else 0 for cat in all_categories]
    
#     return cosine_similarity([user_vector], [item_vector])[0][0]

# @app.route('/minat', methods=['POST'])
# def minat():
#     data = request.get_json()
#     interests = (data['interest'])
#     session['user_interest'] = interests

#     tours = Tour.query.all()
#     recommendations = []
#     for tour in tours:
#         similarity = calculate_similarity(interests, tour.name)
#         if similarity > 0:
#             recommendations.append({
#                 'id': tour.id,
#                 'name': tour.name,
#                 'location': tour.location,
#                 'similarity': similarity
#             })

#     hasil = sorted(recommendations, key=lambda x: x['similarity'], reverse=True)[:5]
#     return jsonify(hasil)

if __name__ == '__main__':
    app.run(debug=True)
