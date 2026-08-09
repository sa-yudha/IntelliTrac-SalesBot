# 🛰️ IntelliTrac SalesBot

> **Final Project - Course: LLM-Based Tools and Gemini API Integration for Data Scientists**  
> 🌐 **Live Demo Web App**: [https://intellitrac-salesbot.streamlit.app/](https://intellitrac-salesbot.streamlit.app/)
>
> *Organized by Hacktiv8 & Supported by Google.org / AVPN*

---

## 📌 Overview

**IntelliTrac SalesBot** adalah aplikasi chatbot AI pre-sales berbasis web yang dirancang untuk PT Intimap (IntelliTrac Indonesia). Chatbot ini berfungsi sebagai asisten konsultasi pintar bagi calon pelanggan yang tertarik dengan produk pelacak kendaraan (GPS Tracker), AI Dashcam (ADAS & DMS), serta sistem manajemen armada (Fleet Management System).

Chatbot ini diberi nama **"Mintel"**, yang diprogram untuk memberikan rekomendasi produk sesuai jenis armada bisnis calon customer (truk logistik, truk reefer pendingin, truk semen, bus, hingga kendaraan operasional kantor), menjelaskan spesifikasi teknis, serta mengarahkan calon customer ke Sales Executive resmi saat membutuhkan penawaran harga resmi (Sales Handoff).

---

## ✨ Fitur Utama

- 🧠 **Powered by Google Gemini AI**: Memanfaatkan model LLM **Gemini 3.5 Flash-Lite** (dipadukan dengan sistem *multi-model fallback*: **Gemini 3.1 Flash-Lite**, **Gemini 3.6 Flash**, **Gemini 3.5 Flash**) untuk pemrosesan bahasa alami (NLP) yang cepat, hemat, dan akurat.
- 📚 **Integrated Knowledge Base**: Dilengkapi konteks dokumen resmi PT Intimap, Katalog Produk 2026, serta Matriks Spesifikasi & Fitur Perangkat (VT-45 Lite, VT-45, JC261, JC450, OBD-II CAN800, dll.).
- 🤝 **Sales Handoff Card**: Secara otomatis menampilkan kartu kontak Sales Representative (WhatsApp & Email) ketika calon customer menanyakan penawaran harga resmi atau berniat melakukan pembelian.
- 🔍 **Fast Product Match (Sidebar)**: Widget rekomendasi cepat berdasarkan pilihan jenis armada calon pelanggan.
- 💡 **Quick Prompt Chips**: Pilihan pertanyaan populer untuk memudahkan interaksi awal calon customer.
- 🎨 **Modern & Responsive UI**: Antarmuka web interaktif menggunakan Streamlit dengan tema warna khas IntelliTrac (Navy Blue & Orange).

---

## 🏗️ Struktur Proyek

```
Final_Project_IntelliTrac_SalesBot/
│
├── app.py                  # Aplikasi utama Streamlit (UI & Gemini API Handler)
├── requirements.txt        # Daftar dependensi Python
├── .env.example            # Template konfigurasi API Key Google Gemini
├── .gitignore              # Mengabaikan file sensitif (.env)
├── README.md               # Dokumentasi lengkap proyek
│
└── knowledge/              # Knowledge Base Dokumen Perusahaan & Produk
    ├── company_profile.md  # Profil PT Intimap & IntelliTrac Indonesia
    ├── catalogue_2026.md   # Deskripsi & spesifikasi katalog produk 2026
    └── product_features.md # Tabel matriks perbandingan fitur & perangkat
```

---

## 🚀 Cara Menjalankan Aplikasi Secara Lokal

### 1. Prasyarat
- Python 3.10 atau versi yang lebih baru.
- Google Gemini API Key (bisa didapatkan secara gratis di [Google AI Studio](https://aistudio.google.com/)).

### 2. Kloning Repositori & Install Dependensi
```bash
git clone https://github.com/USERNAME/IntelliTrac-SalesBot.git
cd IntelliTrac-SalesBot

# Install dependensi
pip install -r requirements.txt
```

### 3. Konfigurasi Environment Variables
Buat file `.env` di direktori utama dan tambahkan API Key Anda:
```env
GOOGLE_API_KEY=AIzaSy...
```
*(Catatan: Jika `.env` tidak diisi, Anda juga dapat memasukkan API Key secara langsung melalui form di sidebar aplikasi).*

### 4. Jalankan Aplikasi Streamlit
```bash
streamlit run app.py
```
Aplikasi akan secara otomatis terbuka di browser pada alamat `http://localhost:8501`.

---

## 📋 Informasi Submisi Final Project (Hacktiv8)

- **Nama Project**: IntelliTrac SalesBot
- **Target Pengguna**: Calon customer dari IntelliTrac GPS Tracker & Fleet Management Systems
- **Manfaat Chatbot**: Memberikan edukasi produk, kualifikasi kebutuhan armada, dan konsultasi pre-sales sebelum di-handoff ke sales person resmi dari tim IntelliTrac.

---

## 📄 Lisensi & Hak Cipta
© 2026 PT Intimap / IntelliTrac Indonesia & Yudha. Dikembangkan untuk Hacktiv8 Final Project.
