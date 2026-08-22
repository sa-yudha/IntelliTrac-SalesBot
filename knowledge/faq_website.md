# Knowledge Base: FAQ Publik Website IntelliTrac

> **Sumber**: https://intellitrac.co.id/faqs - diambil 15 Agustus 2026 (16 FAQ, 2 kategori).
> **Status dokumen**: versi terkoreksi. Sebagian jawaban telah direvisi dari teks asli
> website karena mengandung kekeliruan teknis, klaim berlebihan, atau kontradiksi dengan
> katalog produk. Rincian setiap perubahan beserta teks aslinya ada di
> `docs/FAQ_Website_Revision_Report.md`.
> **Catatan sinkronisasi**: bila halaman website sudah diperbarui mengikuti laporan revisi,
> lakukan scrape ulang dan samakan kembali dokumen ini.

---

# BAGIAN 1: Pertanyaan Umum Tentang GPS Tracker

## Q1. Apa Itu GPS Tracker?

GPS Tracker adalah perangkat yang memanfaatkan sinyal satelit untuk menentukan posisi, lalu mengirim data posisi, pergerakan, dan status kendaraan ke server lewat jaringan seluler.

Selain kendaraan, alat ini juga dipakai untuk memantau aset bergerak dan personel di lapangan, dan hasilnya bisa dipantau real-time lewat web dashboard maupun aplikasi mobile.

---

## Q2. Mengapa GPS Tracker Penting?

GPS Tracker penting untuk manajemen armada, meningkatkan keselamatan pengemudi, dan memaksimalkan produktivitas kendaraan.

Manfaatnya terasa langsung di operasional sehari-hari: pengelola armada bisa tahu posisi dan status seluruh kendaraan setiap saat, mendeteksi pergerakan yang mencurigakan atau upaya pencurian, menekan pemborosan BBM akibat idling berlebihan, memantau perilaku mengemudi berisiko seperti akselerasi atau pengereman mendadak dan overspeed, sampai memantau kelelahan pengemudi. Riwayat perjalanan dan laporan performa yang terekam juga jadi dasar evaluasi armada ke depannya.

---

## Q3. Bagaimana Cara Kerja GPS Tracker?

Sistem ini melibatkan lima komponen: GPS Tracker, satelit GPS, jaringan seluler, server, dan perangkat pengguna.

Perangkat menerima sinyal dari satelit GPS yang berisi data waktu presisi dan posisi orbit satelit (*ephemeris*), bukan koordinat kendaraan. Dengan sinyal dari minimal 4 satelit, perangkat menghitung sendiri koordinat lintang, bujur, dan ketinggiannya lewat metode trilaterasi. Komunikasi dengan satelit ini satu arah: perangkat hanya menerima, tidak pernah mengirim apa pun ke satelit.

Setelah posisi dihitung, perangkat mengirim koordinat itu beserta data status kendaraan (mesin, kecepatan, sensor) ke server IntelliTrac lewat jaringan seluler 4G LTE (tipe tertentu seperti VT-45 punya fallback ke 2G/GSM). Server kemudian memproses data tersebut dan menampilkannya lewat web browser, aplikasi desktop, maupun aplikasi smartphone.

> **Catatan untuk Mintel**: jangan menyatakan bahwa "satelit mengirimkan sinyal kembali ke perangkat" atau bahwa "satelit mengirimkan koordinat". GPS bersifat pasif/satu arah dan koordinat dihitung oleh perangkat. Calon customer dari sektor tambang dan logistik sering memiliki tim teknis yang paham hal ini.

---

## Q4. Apakah GPS Tracker Dapat Bekerja di Area yang Tidak Ada Sinyal Seluler?

Bisa. Perangkat IntelliTrac dilengkapi memori internal (*buffer memory*) yang tetap merekam riwayat perjalanan meski tidak ada koneksi seluler.

Saat kendaraan masuk ke area tanpa sinyal seluler, perangkat tetap menerima sinyal satelit GPS dan terus mencatat titik koordinat, status mesin, kecepatan, serta data sensor ke memori internal. Begitu sinyal seluler kembali, seluruh rekaman offline itu otomatis terunggah ke server, sehingga riwayat perjalanan dan laporan armada tetap lengkap, selama kapasitas memori internal masih cukup menampung durasi offline tersebut.

Ada satu hal yang perlu dibedakan di sini: kondisi di atas hanya berlaku untuk area tanpa sinyal seluler. Di basement, terowongan, atau gudang tertutup, yang hilang justru sinyal GPS-nya sendiri, jadi posisi memang tidak bisa dihitung sampai kendaraan kembali ke area terbuka.

| Kondisi | Sinyal GPS | Sinyal Seluler | Hasil |
|---|---|---|---|
| Perkebunan pedalaman, tambang terpencil, jalur laut/hutan | Ada | Tidak ada | Posisi tetap terekam ke memori internal, lalu tersinkron otomatis |
| Basement, terowongan, gudang tertutup, garasi bertingkat | Tidak ada | Tidak ada | Posisi tidak bisa dihitung selama di dalam; perekaman berlanjut saat kembali ke area terbuka |

> **Catatan untuk Mintel**: jangan menjanjikan riwayat "utuh 100%" atau "tanpa ada data yang terlewat" tanpa syarat, karena buffer memory kapasitasnya terbatas - kalau kendaraan offline sangat lama, data terlama berpotensi tertimpa. Jangan juga memakai basement sebagai contoh blank spot, karena di sana sinyal GPS-nya ikut terhalang. Untuk armada yang rutin beroperasi di area tanpa sinyal dalam durasi panjang, arahkan ke Sales Executive supaya kapasitas buffer dan konfigurasi intervalnya bisa disesuaikan.

---

## Q5. Apakah GPS Tracker Bisa Untuk Semua Jenis Kendaraan?

Bisa. GPS Tracker IntelliTrac dipakai di alat berat, bus, truk, mobil penumpang, van ekspedisi, sampai sepeda motor - cocok untuk sektor pertambangan, logistik, konstruksi, agrikultur, transportasi umum, pengelolaan sampah, rantai dingin (*cold chain*), maupun kendaraan pribadi.

Pemilihan tipenya biasanya menyesuaikan kebutuhan armada:

| Jenis kendaraan / kebutuhan | Rekomendasi |
|---|---|
| Mobil operasional, motor, van ekspedisi | VT-45 Lite |
| Truk reefer, truk mixer, alat berat, bus antarkota (butuh multi-sensor) | VT-45 |
| Armada yang perlu pengawasan pengemudi & jalan (AI dashcam) | JC261 (2 kamera) |
| Truk kargo besar, bus, truk tambang (butuh banyak titik kamera) | JC450 (hingga 5 kamera) |

Semua tipe di atas sudah dilengkapi live tracking 24 jam dan engine cut-off/immobilizer. Spesifikasi lengkapnya ada di `catalogue_2026.md` dan `product_features.md`.

---

## Q6. Berapa Harga GPS Tracker?

Harga bervariasi tergantung tipe perangkat, fitur yang dibutuhkan, dan jumlah unit armada. Paket *tracking only* lebih ekonomis untuk kebutuhan pelacakan dasar, sementara paket premium menawarkan fitur kustom seperti AI dashcam, multi-sensor, atau integrasi ERP. Untuk perusahaan dengan armada besar, tersedia juga opsi sewa.

> **Catatan untuk Mintel**: harga final selalu disusun Sales Executive berdasarkan tipe perangkat, jumlah unit armada, fitur yang dipilih, dan skema langganan, lalu dituangkan dalam Surat Penawaran resmi. Karena itu angka pastinya tidak tersedia di luar dokumen tersebut. Saat calon customer menanyakan biaya, jelaskan komponen apa saja yang memengaruhi harga, lalu tawarkan untuk menghubungkan ke Sales Executive IntelliTrac agar mendapatkan *Official Quotation / Surat Penawaran* resmi.

---

## Q7. Apakah GPS Tracker IntelliTrac Bergaransi?

Ya. Perangkat GPS Tracker IntelliTrac bergaransi 1 (satu) tahun, dan sensor bergaransi 1 (satu) tahun.

Garansi ini berlaku selama kerusakan bukan disebabkan oleh masuknya air melebihi batas ketahanan rating IP perangkat (misalnya perendaman) atau kelalaian penggunaan, perangkat tidak dimodifikasi atau dibongkar sendiri oleh customer di luar teknisi resmi IntelliTrac, dan kerusakan bukan akibat faktor eksternal di luar pemakaian normal seperti kecelakaan, kebakaran, atau lonjakan tegangan ekstrem.

> **Catatan untuk Mintel**: garansi mengikuti batas rating IP masing-masing perangkat. VT-45 ber-rating IP65 (tahan debu dan cipratan air) dan kamera CE04 pada JC450 ber-rating IP67 (waterproof), jadi paparan air dalam batas rating tersebut termasuk pemakaian normal. Yang berada di luar cakupan garansi adalah kerusakan akibat air melebihi batas rating perangkat, misalnya perendaman. Untuk klaim garansi spesifik, arahkan ke tim Support/Service resmi.

---

## Q8. Apakah GPS Tracker IntelliTrac Legal?

Ya, legal. Perangkat dan layanan IntelliTrac sudah memenuhi ketentuan regulasi yang berlaku di Indonesia: bersertifikasi Postel (SDPPI) untuk alat dan perangkat telekomunikasi, terdaftar sebagai Penyelenggara Sistem Elektronik (PSE) di Kementerian Komunikasi dan Digital (Komdigi), dan PT Intimap sendiri tersertifikasi ISO 9001:2015 oleh lembaga sertifikasi yang terakreditasi KAN (Komite Akreditasi Nasional). Server dan data center-nya pun berlokasi di Indonesia.

PT Intimap adalah penyedia dan mitra resmi solusi IntelliTrac GPS di Indonesia, di bawah naungan Virtual Map (Australia) Pty Ltd.

> **Catatan untuk Mintel**: gunakan istilah resmi berikut secara persis. Nama kementeriannya adalah Kementerian Komunikasi dan Digital (Komdigi), sebelumnya bernama Kominfo hingga Oktober 2024. Untuk PSE, gunakan frasa "terdaftar sebagai PSE", karena PSE berbentuk pendaftaran. Untuk ISO, gunakan frasa "PT Intimap tersertifikasi ISO 9001:2015 oleh lembaga sertifikasi yang terakreditasi KAN", karena KAN memberi akreditasi kepada lembaga sertifikasi. Sebutkan setiap sertifikasi dan pendaftaran secara spesifik satu per satu. Bila customer meminta salinan dokumen legalitas, arahkan ke Sales Executive.

---

## Q9. Apakah Ada Biaya Pemasangan dan Maintenance?

Untuk lokasi yang masuk area layanan kantor pusat dan cabang IntelliTrac, biaya pemasangan dan maintenance sudah termasuk dalam paket layanan, jadi tidak ada biaya tambahan. Untuk lokasi di luar area layanan tersebut, bisa berlaku biaya perjalanan dan akomodasi teknisi yang dihitung berdasarkan jarak dan kondisi lokasi.

Kantor layanan saat ini ada di Jakarta (Head Office) dan Surabaya (Branch Office) - alamat lengkapnya ada di `company_profile.md`.

> **Catatan untuk Mintel**: sampaikan bahwa pemasangan dan maintenance sudah termasuk dalam paket layanan untuk lokasi di dalam area layanan kantor pusat dan cabang. Untuk lokasi di luar area tersebut, cakupan layanan dan kemungkinan biaya perjalanan teknisi dihitung menurut jarak dan kondisi lokasi, sehingga perlu dikonfirmasi Sales Executive. Ketentuan juga dapat berbeda antara skema langganan dan pembelian putus, serta untuk kondisi di luar pemakaian normal (lihat Q7). Untuk lokasi di luar Jabodetabek dan Surabaya, arahkan ke Sales untuk pengecekan cakupan layanan.

---

## Q10. Bagaimana Cara Pembelian GPS Tracker?

Pembelian bisa dilakukan lewat kanal resmi berikut:

- **Telepon / WhatsApp**: +62 811-845-6789 atau +62 811-1130-6717
- **Telepon Head Office (Jakarta)**: (021) 6325 999
- **Telepon Branch Office (Surabaya)**: (031) 870 8082
- **Email Sales**: sales@intellitrac.co.id
- **Website resmi**: www.intellitrac.co.id
- **Media sosial resmi IntelliTrac Indonesia**

Alurnya biasanya dimulai dari konsultasi kebutuhan armada bersama Sales Executive, dilanjutkan penyusunan *Official Quotation*, sampai penjadwalan pemasangan oleh teknisi resmi.

> **Catatan untuk Mintel**: ini adalah titik *sales handoff* utama. Tawarkan secara proaktif untuk menghubungkan calon customer ke WhatsApp atau Email Tim Sales. Untuk skema uji coba (Trial Gratis), lihat panduan di `faq.md`.

---

# BAGIAN 2: Pertanyaan Tentang Fitur GPS Tracker

## Q11. Apa Itu Live Tracking?

Live Tracking adalah fitur yang memungkinkan pengguna memantau lokasi kendaraan secara real-time melalui peta digital, baik dari web dashboard maupun aplikasi mobile.

Selain titik lokasi, informasi yang ditampilkan mencakup status mesin (ON/OFF), kecepatan, arah pergerakan, dan data sensor yang terpasang. Interval pembaruan datanya bisa dikonfigurasi sesuai kebutuhan armada.

---

## Q12. Apa Itu Geofence?

Geofence (*geographical fence*) adalah batas virtual geografis yang digambar di peta digital untuk menandai area tertentu, misalnya area gudang, lokasi tambang, wilayah operasional, atau titik pengiriman.

Sistem akan mengirim notifikasi otomatis ketika kendaraan masuk ke dalam atau keluar dari area tersebut. Fitur ini penting untuk pengawasan kendaraan, pembatasan wilayah operasional, verifikasi kedatangan di titik tujuan, serta deteksi penyimpangan rute.

---

## Q13. Apakah Fitur Engine Cut-Off (Immobilizer) itu Aman?

Aman. Fitur Engine Cut-Off IntelliTrac bekerja sebagai immobilizer, artinya hanya memutus fungsi starter kendaraan, bukan mematikan mesin yang sedang berjalan.

Kalau fitur ini diaktifkan saat kendaraan sedang melaju, mesin tidak akan mati mendadak, karena perintahnya bekerja di sistem starter, bukan di mesin itu sendiri, sehingga tidak membahayakan pengemudi maupun pengguna jalan lain. Begitu kendaraan berhenti dan mesin dimatikan oleh pengemudi, kendaraan baru tidak bisa distarter lagi sampai fitur ini dinonaktifkan dari aplikasi - memberi proteksi ekstra dari pencurian tanpa risiko kecelakaan akibat mesin mati saat berkendara.

Fitur ini tersedia di seluruh lini produk: VT-45 Lite, VT-45, JC261, dan JC450.

> **Catatan untuk Mintel**: ini klaim keselamatan, jadi presisinya penting. Gunakan istilah "Engine Cut-Off / Immobilizer (pemutus starter)" saat menjelaskan fitur ini. Bila customer menyebutnya dengan istilah umum di pasaran seperti "Matikan Mesin Jarak Jauh", jelaskan bahwa cara kerjanya adalah memutus fungsi starter, bukan mematikan mesin yang sedang berjalan. Kalau customer bertanya apakah mesin bisa dimatikan saat kendaraan sedang melaju, jawabannya tidak, dan justru itulah yang membuat fitur ini aman. Jangan pernah menjanjikan kemampuan mematikan mesin yang sedang berjalan.

---

## Q14. Apakah Tersedia Aplikasi Mobile Android dan iOS?

Ya. IntelliTrac menyediakan aplikasi mobile untuk Android dan iOS, selain web dashboard dan aplikasi desktop. Android bisa diunduh di [Google Play Store](https://play.google.com/store/apps/details?id=com.intimap.mobile.hawk), dan iOS tersedia untuk perangkat iPhone/iPad.

Lewat aplikasi mobile, pengguna bisa melakukan live tracking, mengatur geofence, melihat playback perjalanan, menerima notifikasi, mengakses laporan performa, sampai menjalankan Driver Pre-Start Checklist (P2H).

---

## Q15. Apakah Kendaraan dalam Kondisi Mesin Mati Tetap Terlacak?

Ya. Kendaraan dalam kondisi mesin OFF tetap mengirimkan data lokasi GPS ke server. Secara default, pengiriman datanya dilakukan setiap 1 jam sekali untuk menghemat konsumsi daya, tapi interval ini bisa dikonfigurasi sesuai kebutuhan armada.

> **Catatan untuk Mintel**: sampaikan angka 1 jam ini sebagai pengaturan default, bukan batasan mutlak. Kalau customer butuh interval berbeda saat kendaraan parkir (misalnya untuk armada bernilai tinggi atau kendaraan yang lama tidak beroperasi), arahkan ke Sales Executive untuk penyesuaian konfigurasi. Satu hal lagi, saat suplai daya kendaraan terputus, perangkat beralih ke baterai cadangan internal yang kapasitasnya terbatas (160-300 mAh tergantung tipe). Untuk rincian lengkap interval saat mesin menyala (kombinasi 15 detik / perubahan heading 15 derajat / event triggered), lihat `faq.md` bagian Interval Pengiriman Data.

---

## Q16. Berapa Lama Data Disimpan di Server?

Lama penyimpanannya beda-beda tergantung jenis datanya:

| Jenis data | Lokasi penyimpanan | Retensi |
|---|---|---|
| Data telemetri & GPS (riwayat posisi, kecepatan, status mesin, data sensor, laporan) | Server IntelliTrac | 6 bulan terakhir |
| Rekaman video dashcam (JC261 / JC450) | microSD di dalam perangkat (hingga 256GB pada JC261, hingga 512GB pada JC450) | Bergantung kapasitas kartu & jumlah kamera aktif; berlaku sistem *loop recording* (rekaman terlama tertimpa otomatis) |
| Klip video event (auto-capture saat insiden, pengereman mendadak, alarm) | Terunggah ke server | Sesuai kebijakan paket berlangganan |

> **Catatan untuk Mintel**: jangan jawab "6 bulan" untuk pertanyaan soal rekaman video dashcam. Retensi 6 bulan itu cuma berlaku untuk data telemetri/GPS. Video utuh tersimpan lokal di microSD dengan sistem loop recording, jadi durasinya tergantung kapasitas kartu dan jumlah channel kamera yang aktif. Untuk kebutuhan retensi video jangka panjang atau arsip khusus, arahkan ke Sales Executive.
