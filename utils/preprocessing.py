import re
import string
import nltk
import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
nltk.download('stopwords') # Untuk stopwords
# from transformers import AutoTokenizer
# from datasets import Dataset
# from datasets import DatasetDict
import requests


factory = StemmerFactory()
stemmer = factory.create_stemmer()
# tokenizer = AutoTokenizer.from_pretrained("indobenchmark/indobert-base-p1")

def cleaningText(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)
    text = re.sub(r'#[A-Za-z0-9]+', '', text)
    text = re.sub(r'RT[\s]', '', text)
    text = re.sub(r"http\S+", '', text)
    text = re.sub(r'\b\d+\b', '', text)
    text = re.sub(r'[^\w\s]', '', text)

    text = text.replace('\n', ' ')
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.strip(' ')
    return text

def casefoldingText(text):
    text = text.lower()
    return text

slangwords = {
    "@": "di", "abis": "habis", "wtb": "beli", "masi": "masih", "wts": "jual", "wtt": "tukar", "bgt": "sangat",  
    "maks": "maksimal", "ngga": "tidak", "gk": "tidak", "ga": "tidak", "uda": "sudah", "udah": "sudah", "udh": "sudah",  
    "jga": "juga", "jg": "juga", "lemot": "lambat", "pake": "pakai", "kl": "kalau", "klo": "kalau", "dpt": "dapat",  
    "kpd": "kepada", "jd": "jadi", "tokped": "tokopedia", "yg": "yang", "knp": "kenapa", "jls": "jelas", "tdk": "tidak",  
    "sy": "saya", "gw": "saya", "gue": "saya", "loe": "kamu", "lu": "kamu", "elo": "kamu", "trs": "terus", "td": "tadi",  
    "skrg": "sekarang", "sbnrnya": "sebenarnya", "bs": "bisa", "gmn": "gimana", "kmrn": "kemarin", "btw": "ngomong-ngomong",  
    "tp": "tapi", "trm": "terima", "dgn": "dengan", "sm": "sama", "smpe": "sampai", "ampun": "tidak sanggup", "pdhl": "padahal",  
    "bnyk": "banyak", "plis": "tolong", "brp": "berapa", "dr": "dari", "tdr": "tidur", "dmn": "dimana", "spt": "seperti",  
    "cm": "cuma", "tggu": "tunggu", "cb": "coba", "blm": "belum", "swt": "kesal", "mlh": "malah", "msh": "masih", "bkn": "bukan",  
    "bt": "kesal", "d": "di", "aj": "aja", "mnrt": "menurut", "ok": "oke", "mnt": "minta", "org": "orang", "bgs": "bagus",  
    "krn": "karena", "hrus": "harus", "sdh": "sudah", "smw": "semua", "trmksh": "terima kasih", "brngkt": "berangkat",  
    "stlh": "setelah", "sblm": "sebelum", "gak": "tidak", "sampe": "sampai", "banget": "sangat", "bngt": "sangat", "gaada": "tanpa", "jd": "jadi", "jdi": "jadi", "kalo": "kalau", "bagu": "bagus",
}

def load_slangwords():
    url = "https://raw.githubusercontent.com/louisowen6/NLP_bahasa_resources/master/combined_slang_words.txt"
    response = requests.get(url)
    slang_dict = json.loads(response.text)
    return slang_dict

slang_dict = load_slangwords()

def fix_slangwords(text, slang_dict=slang_dict, casefold=True):
    merged_slang = slangwords.copy()
    merged_slang.update(slang_dict)  # Prioritaskan dari URL jika ada yang sama

    words = text.split()
    fixed_words = []

    for word in words:
        key = word.lower() if casefold else word
        if key in merged_slang:
            fixed_words.append(merged_slang[key])
        else:
            fixed_words.append(word)

    return ' '.join(fixed_words)

def stemmingText(text):
    return stemmer.stem(text)

def tokenizingText(text):
    text = word_tokenize(text)
    return text

def filteringText(text): # Menghapus stopwords dalam teks

    listStopwords = set(stopwords.words('indonesian'))
    listStopwords1 = set(stopwords.words('english'))
    listStopwords.update(listStopwords1)
    listStopwords.update(['yaa','nya','na','sih','ku',"di","ya","gaa","loh","kah","woi","woii","woy","dong","kok","ny","eh","nyaa","nih","Aah", "aja"])
    filtered = []
    for txt in text:
        if txt not in listStopwords:
            filtered.append(txt)
    text = filtered
    return text

def toSentence(list_words): # Mengubah daftar kata menjadi kalimat
    sentence = ' '.join(word for word in list_words)
    return sentence

# Tokenisasi
# def tokenize(batch):
#     tokenized = tokenizer(batch['question'], padding=True, truncation=True)
#     tokenized["labels"] = batch["label"]
#     return tokenized
