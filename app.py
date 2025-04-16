from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from geopy.distance import geodesic
from dotenv import load_dotenv
from utils.preprocessing import cleaningText
from utils.preprocessing import casefoldingText
from utils.preprocessing import stemmingText
from utils.preprocessing import fix_slangwords
# from transformers import AutoModelForSequenceClassification
from sentence_transformers import SentenceTransformer, util
# from transformers import AutoTokenizer
from flask_cors import CORS
from sklearn.metrics.pairwise import cosine_similarity
import torch
import re
import pandas as pd
import os
# import gdown
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(ngram_range=(1,2), max_features=5000)
model = SentenceTransformer('distiluse-base-multilingual-cased')

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)
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
            'district': tour.district,
            'province': tour.province,
            'latitude': tour.latitude,
            'longitude': tour.longitude,
            'createdAt': tour.createdAt,
            'updatedAt': tour.updatedAt,
            'jarak': jarak
        })

    hasil = sorted(hasil, key=lambda x: x['jarak'])[:5]  # Ambil 5 terdekat
    return jsonify(hasil)

def load_cleaned_tour():
    with app.app_context():
        wisata_df = Tour.query.all()

        # Buat dataframe dari hasil query
        wisata_cleaned_df = pd.DataFrame([{
            'id': w.id,
            'name': w.name,
            'date': w.date,
            'location': w.location,
            'image': w.image,
            'description': w.description,
            'link': w.link,
            'prices': w.prices,
            'district': w.district,
            'province': w.province,
            'latitude': w.latitude,
            'longitude': w.longitude,
            'createdAt': w.createdAt,
            'updatedAt': w.updatedAt,
        } for w in wisata_df])

        # Daftar kolom yang perlu dibersihkan
        text_columns = ['name', 'location', 'description', 'district', 'province']

        # Bersihin teks
        for col in text_columns:
            wisata_cleaned_df[col] = wisata_cleaned_df[col].apply(cleaningText).apply(casefoldingText)

        # Stemming khusus description
        wisata_cleaned_df['description'] = wisata_cleaned_df['description'].apply(stemmingText)

        # Gabungkan semua kolom jadi satu string
        wisata_cleaned_df['combined'] = wisata_cleaned_df.apply(
            lambda row: ' '.join([row[col] for col in ['name', 'district', 'province', 'location', 'description']]),
            axis=1
        )

        return wisata_cleaned_df

wisata_cleaned_df = load_cleaned_tour()
embeddings = model.encode(wisata_cleaned_df['combined'].tolist(), convert_to_tensor=True)

def rekomendasi_wisata(question, top_k=3):
    with app.app_context():
        original_question = question.lower()

        all_provinces = wisata_cleaned_df['province'].str.lower().unique()

        lokasi_filter = None
        for prov in all_provinces:
            if prov in original_question:
                lokasi_filter = prov
                break

        question = cleaningText(question)
        question = casefoldingText(question)
        question = stemmingText(question)
        query_embedding = model.encode(question, convert_to_tensor=True)
        
        # Saat ada filter lokasi
        if lokasi_filter:
            mask = wisata_cleaned_df['province'].str.lower().str.contains(lokasi_filter)
            df_filtered = wisata_cleaned_df[mask]
            embeddings_filtered = embeddings[mask.values]  # <- filter embedding juga
        else:
            df_filtered = wisata_cleaned_df
            embeddings_filtered = embeddings

        # Reset index
        df_filtered = df_filtered.reset_index(drop=True)
        embeddings_filtered = embeddings_filtered.cpu()  # kalau tensor di GPU

        # Cosine similarity terhadap embedding hasil filter
        cos_scores = util.pytorch_cos_sim(query_embedding, embeddings_filtered)[0]
        top_results = cos_scores.topk(k=top_k)

        # Ambil hasil
        recommendations = []
        for score, idx in zip(top_results[0], top_results[1]):
            idx = idx.item()
            wisata_id = df_filtered.iloc[idx]['id']

            # Query ke database berdasarkan id asli
            wisata = Tour.query.get(wisata_id)

            # Pastikan wisata-nya ketemu
            if wisata:
                recommendations.append({
                    'id'         : wisata.id,
                    'name'       : wisata.name,
                    'district'   : wisata.district,
                    'province'   : wisata.province,
                    'location'   : wisata.location,
                    'description': wisata.description,
                })

        return recommendations, lokasi_filter

chatbot_url = "https://raw.githubusercontent.com/novaandini/arkanesia/refs/heads/main/data/chatbot.csv"
chatbot_df = pd.read_csv(chatbot_url)

# ID file dari Google Drive
# file_id = '1ci-vc5GTWdkHewbLgMuRydx77FwM-Sof'
# # Output path
# output_path = 'models/chatbot_bert_model/model.safetensors'

# # Cek apakah file udah ada
# if not os.path.exists(output_path):
#     # Bikin folder kalau belum ada
#     os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
#     url = f'https://drive.google.com/uc?id={file_id}'
#     gdown.download(url, output_path, quiet=False)
#     print("Model downloaded successfully!")
# else:
#     print("Model already exists.")


# chatbot_model = AutoModelForSequenceClassification.from_pretrained("./models/chatbot_bert_model")
# chatbot_tokenizer = AutoTokenizer.from_pretrained("./models/chatbot_bert_model")

with open('./models/chatbot_sklearn_model/text_model.pkl', 'rb') as model_file:
    chatbot_model = pickle.load(model_file)  # Ini model Sklearn

with open('./models/chatbot_sklearn_model/vectorizer.pkl', 'rb') as f:
    chatbot_tokenizer = pickle.load(f)

label_mapping = {
    0: "aktivitas", 1: "budget", 2: "cuaca", 3: "detail_wisata",
    4: "kuliner", 5: "lokasi_wisata", 6: "penginapan", 7: "transportasi",
    8: "uncategorized", 9: "wisata_alam", 10: "wisata_bahari", 11: "wisata_budaya",
    12: "wisata_edukasi", 13: "wisata_rekreasi", 14: "wisata_sejarah"
}

def preprocess(text):
    cleaned_text = cleaningText(text)
    cleaned_text = casefoldingText(cleaned_text)
    cleaned_text = fix_slangwords(cleaned_text)
    cleaned_text = stemmingText(cleaned_text)
    return cleaned_text

def predict(text):
    cleaned_text = preprocess(text)

    # Text classification
    # inputs = chatbot_tokenizer(cleaned_text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    # with torch.no_grad():
    #     outputs = chatbot_model(**inputs)
    # probs = torch.nn.functional.softmax(outputs.logits, dim=1)
    # label = torch.argmax(probs, dim=1).item()
    # confidence = probs[0][label].item()

    vector = chatbot_tokenizer.transform([cleaned_text])
    prediction = chatbot_model.predict(vector)
    intent = prediction[0]

    # Ambil rekomendasi wisata
    recommendations, lokasi_filter = rekomendasi_wisata(text)

    # Pilih jawaban template sesuai intent
    # answer = chatbot_df[chatbot_df['Intent'] == label_mapping[label]].sample(n=1).iloc[0]['Jawaban']
    answer = chatbot_df[chatbot_df['Intent'] == intent].sample(n=1).iloc[0]['Jawaban']

    placeholders = re.findall(r"\[rekomendasi_(\d+)\]", answer)
    final_answer = answer

    # Cek dan ganti [nama_daerah]
    if "[nama_daerah]" in final_answer:
        if lokasi_filter is None:
            final_answer = final_answer.replace("[nama_daerah]", "Indonesia")
        else:
            final_answer = final_answer.replace("[nama_daerah]", lokasi_filter)

    # Ganti placeholder rekomendasi
    for ph in placeholders:
        idx = int(ph) - 1  # karena rekomendasi_1 = recommendation[0]
        if idx < len(recommendations):
            final_answer = final_answer.replace(f"[rekomendasi_{ph}]", recommendations[idx]['name'])
        else:
            final_answer = final_answer.replace(f"[rekomendasi_{ph}]", "-")

    data = []
    for rec in recommendations:
        data.append({
            'id': int(rec['id']),
            'name': rec['name'],
            'district': rec['district'],
            'province': rec['province'],
            'location': rec['location'],
            'description': rec['description'],
        })

    result = {
        'answer': final_answer,
        # 'score': confidence,
        'intent': intent,
        # 'intent': label_mapping[label],
        'result': data
    }
    return result

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    question = data.get('question')
    
    if not question:
        return jsonify({'error': 'question wajib diisi!'}), 400
    
    result = predict(question)
    return jsonify(result)

def calculate_similarity(user_interest, item_categories):
    all_categories = list(set(user_interest + item_categories))
    user_vector = [1 if cat in user_interest else 0 for cat in all_categories]
    item_vector = [1 if cat in item_categories else 0 for cat in all_categories]
    
    return cosine_similarity([user_vector], [item_vector])[0][0]

@app.route('/interest', methods=['POST'])
@app.route('/interest', methods=['POST'])
def interest():
    data = request.get_json()

    if isinstance(data, dict):
        data = [data]

    df = pd.DataFrame(data)

    interests = (df['name'].str.cat(df[['district', 'province', 'location', 'description']], sep=' ')).str.lower()
    interests_text = ' '.join(interests)
    cleaned_text = preprocess(interests_text)

    session['user_interest'] = cleaned_text

    tours_cleaned = load_cleaned_tour()

    ids = tours_cleaned['id'].tolist()
    tour_details = Tour.query.filter(Tour.id.in_(ids)).all()
    tour_dict = {tour.id: tour for tour in tour_details}

    recommendations = []

    for _, tour in tours_cleaned.iterrows():
        similarity = calculate_similarity(cleaned_text.split(), tour['combined'].split())
        if similarity > 0:
            tour_detail = tour_dict.get(tour['id'])
            if tour_detail:
                recommendations.append({
                    'id': tour_detail.id,
                    'name': tour_detail.name,
                    'date': tour_detail.date,
                    'location': tour_detail.location,
                    'image': tour_detail.image,
                    'description': tour_detail.description,
                    'link': tour_detail.link,
                    'prices': tour_detail.prices,
                    'district': tour_detail.district,
                    'province': tour_detail.province,
                    'latitude': tour_detail.latitude,
                    'longitude': tour_detail.longitude,
                    'createdAt': tour_detail.createdAt,
                    'updatedAt': tour_detail.updatedAt,
                    'similarity': similarity
                })

    hasil = sorted(recommendations, key=lambda x: x['similarity'], reverse=True)[:5]
    return jsonify(hasil)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))