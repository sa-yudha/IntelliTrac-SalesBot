# Knowledge Base: FAQ (Frequently Asked Questions) & Solusi Teknis IntelliTrac

Dokumen ini berisi panduan jawaban cepat untuk pertanyaan-pertanyaan spesifik dan keraguan teknis yang sering diajukan oleh calon pelanggan.

---

## 1. Kondisi Blank Spot / Sinyal Terputus (Kombinasi GSM & GPS)

### Pertanyaan:
*"Bagaimana jika kendaraan masuk ke area blank spot (seperti perkebunan pedalaman, area tambang terpencil, atau basement gedung) yang tidak ada sinyal internet/GSM? Apakah pelacakan akan terputus dan datanya hilang?"*

### Panduan Jawaban untuk Mintel:
1. **Ada Dua Jenis Sinyal yang Berperan Berbeda, Jelaskan Bedanya Dulu**:
   - **Sinyal GPS** (dari satelit): dipakai perangkat untuk menghitung posisi/koordinat kendaraan.
   - **Sinyal GSM/seluler** (dari BTS provider, misal Telkomsel): dipakai perangkat untuk mengirim data (event & posisi) ke server IntelliTrac.
   - Kedua sinyal ini bisa hilang secara independen satu sama lain, sehingga hasilnya berbeda-beda tergantung kombinasi yang terjadi. JANGAN menjawab dengan satu jawaban generik untuk semua kondisi "blank spot", karena efeknya berbeda tergantung kombinasi di bawah.
2. **Empat Kombinasi Sinyal dan Efeknya**:

   | Sinyal GSM | Sinyal GPS | Efek Saat Terjadi | Saat Kedua Sinyal Kembali |
   |---|---|---|---|
   | Tidak ada | Tidak ada | Perangkat **tidak mengirim** event data maupun posisi sama sekali | Langsung lompat ke posisi terbaru, **tanpa** ada data/posisi lampau yang dikirim (karena tidak ada yang bisa dibuffer; GPS-nya sendiri tidak dapat sinyal, jadi tidak ada koordinat yang bisa disimpan) |
   | Ada | Tidak ada | Perangkat **tetap mengirim event data** (mesin nyala, pintu buka, overspeeding, dll) secara real-time, tapi **tanpa** update posisi | Langsung lompat ke posisi terbaru, **tanpa** mengirim posisi lampau |
   | Tidak ada | Ada | Perangkat **tidak mengirim** event data maupun posisi secara real-time (karena tidak ada jaringan untuk mengirim), tapi tetap merekamnya ke memori internal (*buffer memory*) | **Secara bertahap** (gradual, bukan sekaligus) mengirim seluruh event data dan posisi yang sempat terekam offline |
   | Ada | Ada | Kondisi normal: perangkat selalu mengirim event data dengan posisi ter-update secara real-time | Tidak relevan, kondisi sudah normal |

3. **Contoh Skenario Nyata per Kombinasi** (bantu customer mengenali kombinasi mana yang relevan dengan operasional mereka):
   - **GSM tidak ada, GPS ada**: perkebunan pedalaman, tambang terpencil, jalur laut/hutan yang tidak terjangkau menara BTS provider mana pun, namun langit terbuka sehingga GPS tetap dapat sinyal satelit. Contoh: melewati gurun atau pendaki naik gunung.
   - **GSM ada, GPS tidak ada**: wilayah tertutup atau terhalang bangunan tinggi, namun masih terdapat sinyal BTS provider di sekitar.
   - **GSM tidak ada, GPS tidak ada**: basement gedung bertingkat, terowongan panjang, atau garasi bawah tanah, di mana baik sinyal satelit maupun sinyal BTS provider sama-sama terhalang struktur bangunan.
4. **Tegaskan Secara Proaktif bahwa Notifikasi Event Tetap Aman pada Kombinasi "GSM Ada, GPS Tidak Ada"**:
   - Ini poin yang paling penting untuk menenangkan calon customer, dan sering ditanyakan secara tidak langsung, misalnya: *"Kalau pintu box dibuka pas kendaraan di parkiran bawah tanah, apa saya masih kebagian notifikasinya?"*
   - JANGAN menjawab kabur seperti "data yang dikirim tidak menyertakan posisi" tanpa menyebut nasib event data-nya, karena itu bisa membuat customer khawatir seolah notifikasi kejadiannya juga hilang.
   - **Tegaskan dengan jelas dan proaktif**: notifikasi/event data (mesin nyala, pintu box dibuka, overspeeding, dll) **tetap terkirim secara real-time**, jadi customer tidak perlu khawatir kehilangan notifikasi kejadian penting. Yang tertunda **hanya** update posisi/koordinatnya sampai GPS dapat sinyal kembali, bukan notifikasi kejadiannya.
5. **JANGAN Menjanjikan Riwayat "Utuh 100%" atau "Tanpa Ada Data yang Terlewat" Secara Mutlak**:
   - Klaim itu **hanya** berlaku untuk kombinasi "GSM tidak ada, GPS ada" (baris ketiga tabel di atas), dan bahkan itu pun tetap dibatasi kapasitas buffer memory internal (data terlama berpotensi tertimpa kalau durasi offline sangat lama).
   - Untuk kombinasi "GSM tidak ada, GPS tidak ada" maupun "GSM ada, GPS tidak ada", secara desain **tidak ada data/posisi lampau yang di-backfill** begitu sinyal kembali, karena perangkat tidak bisa membuffer koordinat yang memang tidak pernah berhasil dihitung.
6. **Arahkan ke Sales Executive** untuk armada yang rutin beroperasi di area dengan pola sinyal seperti ini, agar kapasitas buffer dan konfigurasi pelaporan dapat ditinjau/disesuaikan.

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

---

## 6. Interval Pengiriman Data GPS (Real-Time vs Sleep Mode)

### Pertanyaan:
*"Berapa detik/menit sekali GPS Tracker IntelliTrac mengirim update posisi? Apakah update-nya terus-menerus tiap detik?"*

### Panduan Jawaban untuk Mintel:
1. **Saat Mesin Menyala (IGN-ON) - Mode Real-Time**:
   - Perangkat mengirim update posisi berdasarkan **mana yang lebih dulu terpenuhi** dari tiga kondisi berikut (bukan cuma satu kondisi tunggal):
     - **Interval waktu**: setiap 15 detik.
     - **Perubahan arah (heading/angle)**: setiap kali arah kendaraan berubah 15 derajat.
     - **Event triggered**: begitu ada kejadian tertentu, misalnya mesin dinyalakan, pintu box dibuka, atau terjadi overspeeding.
   - Jelaskan kombinasi ketiganya secara utuh ke customer. JANGAN hanya menyebut "setiap 15 detik" saja, karena itu memberi kesan sistem kurang responsif terhadap perubahan arah mendadak atau kejadian penting yang sebenarnya langsung terdeteksi.
2. **Saat Mesin Mati (IGN-OFF) - Sleep Mode**:
   - Perangkat masuk ke mode sleep dan mengirim update posisi setiap **1 jam sekali** untuk menghemat konsumsi daya baterai cadangan internal.
   - Angka 1 jam ini konsisten dengan penjelasan di `faq_website.md` (Q15, "Apakah Kendaraan dalam Kondisi Mesin Mati Tetap Terlacak?").
3. **Interval Dapat Dikonfigurasi**: sampaikan bahwa interval real-time maupun sleep di atas adalah pengaturan default, bukan batasan mutlak. Untuk kebutuhan armada khusus (misal butuh update lebih rapat), arahkan ke Sales Executive untuk penyesuaian konfigurasi.
