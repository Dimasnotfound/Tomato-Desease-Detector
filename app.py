import os
import numpy as np
from flask import Flask, render_template, request, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# SETTINGS
MODEL_PATHS = [
    "models/best_model_0.h5",
    "models/best_model_1.h5",
    "models/best_model_2.h5",
]
CLASS_LABELS = [
    "Tomato_Bacterial_spot",
    "Tomato_Early_blight",
    "Tomato_Late_blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_leaf_spot",
    "Tomato_Spider_mites_Two_spotted_spider_mite",
    "Tomato__Target_Spot",
    "Tomato__Tomato_YellowLeaf__Curl_Virus",
    "Tomato__Tomato_mosaic_virus",
    "Tomato_healthy",
]
TARGET_SIZE = (64, 64)
MODEL_ACCURACY = 0.95

LABEL_TRANSLATE = {
    "Tomato_Bacterial_spot": {
        "id": "Bercak Bakteri",
        "desc": "Daun tomat terkena bercak bakteri, biasanya muncul bercak coklat kehitaman.",
        "tips": "Singkirkan daun terinfeksi, hindari penyiraman dari atas, gunakan pestisida bakterisida jika perlu.",
    },
    "Tomato_Early_blight": {
        "id": "Hawar Dini",
        "desc": "Gejala berupa bercak coklat bulat di daun bawah.",
        "tips": "Buang daun sakit, rotasi tanaman, gunakan fungisida bila parah.",
    },
    "Tomato_Late_blight": {
        "id": "Hawar Daun Akhir",
        "desc": "Daun dan buah jadi kecoklatan/berair, cepat menyebar.",
        "tips": "Segera buang bagian terinfeksi, hindari kelembaban tinggi, gunakan fungisida sistemik.",
    },
    "Tomato_Leaf_Mold": {
        "id": "Jamur Daun",
        "desc": "Daun berubah kuning dan terdapat bercak jamur di bawah daun.",
        "tips": "Jaga ventilasi, jangan terlalu rapat menanam, semprot fungisida.",
    },
    "Tomato_Septoria_leaf_spot": {
        "id": "Bercak Septoria",
        "desc": "Bercak kecil bulat abu-abu dikelilingi coklat pada daun tua.",
        "tips": "Buang daun sakit, hindari daun basah lama, gunakan fungisida.",
    },
    "Tomato_Spider_mites_Two_spotted_spider_mite": {
        "id": "Tungau Merah",
        "desc": "Daun tomat tampak kuning dan terdapat jaring halus.",
        "tips": "Semprot air ke bawah daun, gunakan insektisida alami (misal neem oil).",
    },
    "Tomato__Target_Spot": {
        "id": "Bercak Target",
        "desc": "Bercak bulat dengan lingkaran seperti target.",
        "tips": "Buang daun/buah sakit, jaga kebersihan kebun.",
    },
    "Tomato__Tomato_YellowLeaf__Curl_Virus": {
        "id": "Virus Keriting Daun Kuning",
        "desc": "Daun menguning, keriting, tanaman kerdil.",
        "tips": "Cabut tanaman terinfeksi berat, kendalikan vektor (kutu putih), gunakan benih tahan virus.",
    },
    "Tomato__Tomato_mosaic_virus": {
        "id": "Virus Mosaik",
        "desc": "Daun belang-belang kuning-hijau, pertumbuhan lambat.",
        "tips": "Hancurkan tanaman sakit, jangan pegang tanaman sehat setelah menyentuh yang sakit.",
    },
    "Tomato_healthy": {
        "id": "Sehat",
        "desc": "Daun tomat sehat!",
        "tips": "Pertahankan perawatan seperti biasa, perhatikan tanda penyakit.",
    },
}


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"

# Load models only once
models = [load_model(path) for path in MODEL_PATHS]


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", accuracy=MODEL_ACCURACY)


@app.route("/detect", methods=["POST"])
def detect():
    file = request.files["file"]
    if not file or file.filename == "":
        return redirect(url_for("index"))

    filename = file.filename
    save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(save_path)

    # Load & preprocess
    img = image.load_img(save_path, target_size=TARGET_SIZE)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # Ensemble: average probability (confidence)
    all_probs = [m.predict(img_array)[0] for m in models]  # (n_models, n_classes)
    avg_prob = np.mean(all_probs, axis=0)
    voted_pred = np.argmax(avg_prob)
    confidence = float(avg_prob[voted_pred]) * 100  # as percentage

    prediction = CLASS_LABELS[voted_pred]
    label_info = LABEL_TRANSLATE.get(prediction, {})
    nama_id = label_info.get("id", prediction)
    deskripsi = label_info.get("desc", "-")
    tips = label_info.get("tips", "-")

    return render_template(
        "result.html",
        filename=filename,
        prediction=nama_id,
        deskripsi=deskripsi,
        tips=tips,
        accuracy=MODEL_ACCURACY,
        confidence=confidence,
    )


if __name__ == "__main__":
    os.makedirs("static/uploads", exist_ok=True)
    app.run(debug=True)
