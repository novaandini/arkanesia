from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import sys
import os

# Load model & tokenizer
model_path = os.path.abspath("models/chatbot_bert_model")  # Ganti jika model disimpan di folder lain
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

# Mapping label index ke nama intent
label_mapping = {
    0: "aktivitas",
    1: "budget",
    2: "cuaca",
    3: "detail_wisata",
    4: "kuliner",
    5: "lokasi_wisata",
    6: "penginapan",
    7: "transportasi",
    8: "uncategorized",
    9: "wisata_alam",
    10: "wisata_bahari",
    11: "wisata_budaya",
    12: "wisata_edukasi",
    13: "wisata_rekreasi",
    14: "wisata_sejarah",
}

def predict_intent(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=1)
    predicted_label = torch.argmax(probs, dim=1).item()
    intent = label_mapping.get(predicted_label, "unknown")
    confidence = probs[0][predicted_label].item()
    return intent, confidence

if __name__ == "__main__":
    # Kalau dipanggil dari terminal
    if len(sys.argv) > 1:
        input_text = " ".join(sys.argv[1:])
        intent, confidence = predict_intent(input_text)
        print(f"Intent: {intent} (confidence: {confidence:.2f})")
    else:
        print("Masukkan teks sebagai argumen.")
