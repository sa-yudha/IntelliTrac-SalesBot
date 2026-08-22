# Knowledge Base: FAQ (Frequently Asked Questions) & Solusi Teknis IntelliTrac

Dokumen ini berisi panduan jawaban cepat untuk pertanyaan-pertanyaan spesifik dan keraguan teknis yang sering diajukan oleh calon pelanggan.

---

## 1. Kondisi Blank Spot (Area Tanpa Sinyal GSM / Luar Jangkauan Seluler)

### Pertanyaan:
*"Bagaimana jika kendaraan masuk ke area blank spot (seperti perkebunan pedalaman, area tambang terpencil, atau basement gedung) yang tidak ada sinyal internet/GSM? Apakah pelacakan akan terputus dan datanya hilang?"*

### Panduan Jawaban untuk Mintel:
1. **Penyimpanan Data Offline (Internal Buffer Memory / Blackbox Offline)**:
   - Perangkat GPS Tracker IntelliTrac dilengkapi dengan memori internal cerdas (buffer memory).
   - Ketika kendaraan berada di area *blank spot* tanpa koneksi internet, perangkat akan **tetap merekam semua titik koordinat lintasan, status mesin, kecepatan, dan data sensor (seperti sensor suhu atau pintu)** ke dalam memori lokal perangkat secara akurat.
2. **Sinkronisasi Otomatis (Auto Data Upload)**:
   - Begitu kendaraan keluar dari area blank spot dan kembali menangkap sinyal seluler (4G LTE), perangkat akan **secara otomatis mengunggah seluruh riwayat rekaman offline tersebut ke server pusat IntelliTrac**.
3. **Hasil untuk Pengguna**:
   - Riwayat perjalanan (*replay history*) dan laporan armada pengguna akan tetap utuh 100%, tanpa ada rute atau riwayat sensor yang terputus atau hilang.

---

## 2. Skema Uji Coba / Trial Gratis

### Pertanyaan:
*"Perusahaan kami memiliki armada dalam jumlah banyak dan ingin mencoba dulu 1 atau beberapa unit untuk melihat performa dan sistemnya (Trial Gratis), apakah diperbolehkan dan bagaimana mekanismenya?"*

### Panduan Jawaban untuk Mintel:
1. **Mendukung Program Trial Gratis**:
   - IntelliTrac sangat terbuka dan mendukung program **Trial Gratis** (uji coba unit) khusus untuk calon pelanggan korporat (B2B) dan pengelola armada komersial.
   - Gunakan istilah **"Trial Gratis"**, bukan "POC" atau "Proof of Concept", saat berkomunikasi dengan calon customer.
2. **Mekanisme Pengajuan Trial**:
   - Calon customer dapat mendiskusikan kebutuhan armada, jumlah unit, dan fitur yang ingin diuji coba (misal: Live Tracking, AI Dashcam, atau Sensor Suhu) langsung bersama tim Sales Executive resmi.
   - Tim Sales akan menyiapkan skema penawaran resmi serta jadwal pemasangan unit uji coba oleh teknisi.
3. **Arahkan ke Sales Handoff**:
   - Berikan respon yang antusias dan tawarkan untuk langsung menghubungkan calon customer ke WhatsApp atau Email Tim Sales IntelliTrac untuk proses registrasi program Trial.

---

## 3. Contoh Kendaraan yang Kompatibel dengan Modul OBD-II CAN800

### Pertanyaan:
*"Kendaraan/truk kami merek [X], apakah modul OBD-II CAN800 (yang dipasangkan dengan VT-45) sudah pasti kompatibel untuk membaca data ECU-nya?"*

### Panduan Jawaban untuk Mintel:
1. **Contoh Kendaraan yang Sudah Terkonfirmasi Kompatibel**:
   - Dongfeng dCi 465
   - Shacman X3000
   - Shacman F3000
   - Hongyan Kingkan 430
   - FAW 350HP
   - Motor Sights MS700
2. **Jika Merek/Tipe Kendaraan Customer Tidak Ada di Daftar Ini**:
   - JANGAN menjawab bahwa kendaraan tersebut otomatis tidak kompatibel maupun otomatis kompatibel. Kompatibilitas OBD-II CAN800 bergantung pada protokol ECU spesifik tiap merek dan tahun produksi kendaraan.
   - Sampaikan bahwa daftar di atas adalah contoh kendaraan yang sudah terkonfirmasi, dan arahkan calon customer untuk mengonfirmasi tipe/tahun kendaraannya langsung ke tim Sales Executive atau teknisi IntelliTrac agar kompatibilitasnya dapat dipastikan sebelum pemasangan.

---

## 4. Instalasi Plug and Play (PnP) Tanpa Pemotongan Kabel

### Pertanyaan:
*"Mau pasang OBD yang PnP (Plug and Play), tanpa ada pemotongan/pemasangan kabel-kabel, apakah ada?"*

### Panduan Jawaban untuk Mintel:
1. **Bagian yang Benar-Benar Plug and Play**:
   - Modul OBD-II CAN800 memang tinggal dicolokkan langsung ke port OBD-II kendaraan (umumnya di bawah kemudi/dasbor), tanpa pemotongan kabel untuk modul ini sendiri.
2. **Bagian yang TIDAK Plug and Play (Wajib Disampaikan, Jangan Disembunyikan)**:
   - CAN800 tetap harus disambungkan lewat kabel ke unit GPS Tracker VT-45.
   - VT-45 sendiri membutuhkan pemasangan/instalasi terpisah oleh teknisi resmi, bukan sekadar dicolok tanpa pemasangan apa pun.
3. **JANGAN Menjawab "Tentu Saja Ada" atau Menjanjikan Instalasi Sepenuhnya Tanpa Kabel/Pemasangan**:
   - IntelliTrac saat ini tidak menjual unit GPS Tracker yang sepenuhnya plug and play berdiri sendiri.
   - Jelaskan dengan jujur: hanya koneksi CAN800 ke port OBD-II yang plug and play, sedangkan VT-45 tetap dipasang oleh teknisi resmi IntelliTrac.
4. **Arahkan ke Sales/Teknisi**:
   - Untuk detail proses pemasangan, estimasi waktu instalasi, dan penjadwalan teknisi, arahkan calon customer ke Sales Executive atau tim teknisi IntelliTrac.

---

## 5. Pencatatan Hourmeter (HM) pada VT-45

### Pertanyaan:
*"Apa device VT-45 bisa simpan hourmeter?"*

### Panduan Jawaban untuk Mintel:
1. **Ya, IntelliTrac Dapat Menyajikan Data Hourmeter**, tapi mekanismenya bukan berupa data mentah yang tersimpan/dihitung di dalam perangkat VT-45 itu sendiri. Jelaskan mekanisme sebenarnya sebagai berikut:
   - VT-45 mengirim data secara periodik ke server dalam bentuk titik-titik posisi (setiap titik = satu waktu + koordinat + status kendaraan saat itu).
   - Setiap titik data itu menyertakan status **ignition ON/OFF** (mesin menyala/mati) dan, jika sensor Auxiliary/PTO terpasang, status **aux/PTO aktif/tidak aktif**.
   - **Server IntelliTrac** yang mengakumulasi durasi status "ON"/"aktif" dari rangkaian titik-titik data tersebut menjadi total Hourmeter (jam kerja mesin atau jam kerja fungsi PTO), lalu menampilkannya di dashboard/laporan.
2. **JANGAN Menjelaskan Seolah VT-45 Punya Register/Counter Hourmeter Internal** yang bisa dibaca langsung dari dalam perangkat. Hourmeter adalah hasil kalkulasi/akumulasi di sisi server berdasarkan status per titik data, bukan angka yang disimpan mentah di dalam VT-45.
3. **Dua Sumber Hourmeter yang Bisa Dijelaskan ke Customer**:
   - Hourmeter mesin, berdasarkan status ignition ON/OFF (fitur bawaan, tanpa sensor tambahan).
   - Hourmeter fungsi alat berat (misal PTO hidrolik), berdasarkan status sensor Auxiliary/PTO (butuh sensor tambahan, lihat `catalogue_2026.md` bagian Sensor & Aksesori).
4. **Arahkan ke Sales/Teknisi** untuk kebutuhan format laporan Hourmeter yang spesifik atau kombinasi sensor tambahan yang dibutuhkan.
