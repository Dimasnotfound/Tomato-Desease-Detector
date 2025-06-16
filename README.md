# 🍅 Tomato Leaf Disease Detector

Website AI interaktif berbasis **deep learning** untuk mendeteksi penyakit daun tomat dari foto.  
Upload gambar daun tomat, dapatkan deteksi penyakit secara otomatis, lengkap dengan **penjelasan mudah dan saran penanganan** dalam bahasa Indonesia.

[![Made with Flask](https://img.shields.io/badge/Python-Flask-green?logo=flask)](https://flask.palletsprojects.com/)
[![Tailwind CSS](https://img.shields.io/badge/Styling-TailwindCSS-blue?logo=tailwindcss)](https://tailwindcss.com/)
![MIT License](https://img.shields.io/github/license/yourusername/tomato-leaf-disease-detector)

---

## 🚀 Fitur Utama

- **Deteksi otomatis 10 kelas penyakit daun tomat & sehat**
- **Akurasi tinggi** dengan ensemble 3 CNN
- **Penjelasan penyakit** & **saran solusi** dalam bahasa Indonesia
- **UI modern & responsif** (Tailwind CSS)
- Live **confidence (%)** setiap prediksi

---

## 🖼️ Demo

![Demo Website](https://placehold.co/600x320/png?text=Tomato+Leaf+Disease+Detector+Demo)

---

## 📦 Instalasi Cepat

1. **Clone repo ini:**
   ```bash
   git clone https://github.com/Dimasnotfound/Tomato-Desease-Detector.git
   cd tomato-leaf-disease-detector
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Siapkan model CNN di folder `models/`:**
   - `best_model_0.h5`
   - `best_model_1.h5`
   - `best_model_2.h5`
4. **Jalankan Flask:**
   ```bash
   python app.py
   ```
5. **Akses website:**  
   http://127.0.0.1:5000

---

## 📝 Struktur Folder

```
.
├── app.py
├── models/
│   ├── best_model_0.h5
│   ├── best_model_1.h5
│   └── best_model_2.h5
├── static/
│   └── uploads/
├── templates/
│   ├── index.html
│   └── result.html
└── README.md
```

---

## 🌱 Teknologi

- **Flask** — backend & API
- **TensorFlow/Keras** — deep learning inference
- **Tailwind CSS** — desain frontend responsif
- **Ensemble Learning** — prediksi lebih stabil dan akurat

---

## 📷 Contoh Penggunaan

1. Buka website.
2. Upload foto daun tomat.
3. Lihat hasil deteksi, confidence (%) model, penjelasan penyakit, dan saran perbaikan langsung!

---

## 👩‍🌾 Untuk Siapa?

- **Petani, pelajar, & masyarakat umum** yang ingin tahu kesehatan tanaman tomat secara mudah dan gratis.

---

## 📖 Lisensi

MIT License.  
Silakan gunakan, modifikasi, dan kontribusi untuk kebaikan petani Indonesia!

---

> **Dibuat dengan ❤️ untuk petani dan penggiat teknologi pertanian!**
