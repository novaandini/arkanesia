import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

import numpy as np

# Contoh dataset (pertanyaan chatbot)
texts = ["Apa tempat wisata di Bali?", "Apa tempat wisata di Jakarta?", "Wisata murah di Surabaya"]
labels = [0, 1, 2]  # Label kategori destinasi

# Tokenisasi teks
tokenizer = Tokenizer(num_words=5000, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
padded_sequences = pad_sequences(sequences, maxlen=10, padding="post")
padded_sequences = np.array(padded_sequences, dtype=np.float32)
labels = np.array(labels, dtype=np.float32)  # Jika labels berupa angka


# Buat model LSTM untuk NLP
model = keras.Sequential([
    Embedding(input_dim=5000, output_dim=16, input_length=10),
    LSTM(32),
    Dense(16, activation='relu'),
    Dense(3, activation='softmax')  # 3 kategori (Bali, Jakarta, Surabaya)
])

# Compile & train model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(padded_sequences, labels, epochs=50)

repeat = 1
# Prediksi contoh baru
while (repeat == 1): 
    new_text = input("Kamu: ")
    new_seq = tokenizer.texts_to_sequences(new_text)
    new_pad = pad_sequences(new_seq, maxlen=10, padding="post")

    pred = model.predict(new_pad)
    print("Kategori Prediksi:", pred.argmax())
