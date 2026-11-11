# Knowledge Base: IntelliTrac GPS Tracker VT-51 E-Seal

> **Sumber**: Katalog resmi "VT-51 E-Seal Catalogue 2026.11.03" (3 halaman) dan halaman produk
> https://intellitrac.co.id/products/vt-51e-seal (diambil 11 November 2026). Spesifikasi teknis di
> kedua sumber identik. Bagian "Peruntukan" dan "Integrasi API" hanya ada di halaman web.

---

## Ringkasan Produk

- **Kategori**: Segel elektronik (*e-seal*) dengan GPS tracking 4G, untuk mengamankan dan memantau pintu kargo, kontainer, dan aset bergerak.
- **Tagline**: "Ultimate Cargo Protection", "Track Smarter, Secure Better", "Pantau Akurat, Segel Aman, Kargo Terlindungi".
- **Cara kerja singkat**: tali baja (lock hook) dikaitkan ke pintu kargo/kontainer, lalu unit mengunci otomatis. Segel hanya bisa dibuka lewat perintah jarak jauh (SMS atau aplikasi Android/iOS) atau kunci RFID yang sudah terotorisasi. Setiap upaya perusakan dikirim sebagai peringatan ke sistem.
- **Sumber daya**: baterai internal isi ulang 10.000 mAh, tidak mengambil daya dari kendaraan.
- **Slogan halaman web**: "Smart Lock, Smart Track, Ultimate Cargo Protection!"

## Peruntukan (Kebutuhan Keamanan Aset Bergerak)

| Segmen | Kegunaan |
|---|---|
| Truk Kontainer (Trailer) | Mengamankan pintu peti kemas selama perjalanan lintas kota, antar pulau, maupun rute internasional |
| Truk Box (Wing Box/CDE/CDD) | Mengamankan kargo bernilai tinggi dari risiko pencurian saat di jalan, tempat istirahat, maupun gudang transit |
| Truk Tangki (BBM/CPO/Bahan Kimia) | Mencegah pengurasan ilegal atau pencurian muatan cair (susut muatan) dengan menyegel katup tangki |
| Kendaraan Logistik Farmasi (Cold Chain) | Menyegel pintu boks pendingin agar tidak ada akses tidak sah yang dapat merusak kualitas suhu kargo |
| Kereta Api Barang (Freight Train) | Mengamankan gerbong kargo tertutup yang membawa barang bernilai tinggi atau bahan pokok dalam jumlah besar |
| Bea Cukai & Otoritas Pelabuhan (Customs) | Segel keamanan untuk memastikan kontainer impor/ekspor tidak dibuka secara ilegal sebelum pemeriksaan bea cukai |

## Integrasi API

VT-51 E-Seal dapat diintegrasikan dengan:
- **SPIONAM** (Kementerian Perhubungan)
- **SILACAK** (Kementerian Lingkungan Hidup dan Kehutanan), lihat juga `silacak_klhk.md`
- **Aplikasi internal perusahaan customer**

---

## Fitur Utama (Key Features)

- **Smart GPS Tracking**: melacak pergerakan aset secara akurat dengan kombinasi 4G dan GNSS (GPS + BeiDou + GLONASS).
- **Dual Access Control**: segel bisa dibuka jarak jauh via SMS/aplikasi, atau langsung di lokasi dengan kunci RFID.
- **Dual SIM Connectivity**: dua slot SIM dengan pemilihan jaringan otomatis di area minim sinyal.
- **Smart Security Alerts**: peringatan instan ke sistem saat terdeteksi upaya perusakan, misalnya tali dipotong atau sandi salah.
- **Smart Auto-Lock**: segel mengunci otomatis begitu tali baja dimasukkan ke posisinya.
- **FOTA Remote Update**: pembaruan firmware perangkat secara nirkabel dari jarak jauh.

## Fitur Lainnya (More Features)

- Polygon Geofence
- Lock/Unlock Audit Trail (riwayat buka/kunci segel)
- Shock Resistant
- Authorized Access Control
- Automatic Power Saving
- 2 RFID Keys Included (2 kunci RFID sudah termasuk dalam paket)
- Cover Open Detection (deteksi penutup unit dibuka)
- Fast & Accurate Positioning
- Bluetooth (opsional)

## Keunggulan

- **Keamanan Berlapis**: notifikasi peringatan instan ke sistem jika ada upaya perusakan.
- **Operasional Bebas Hambatan**: kunci RFID memudahkan bongkar muat secara aman meski tanpa jaringan seluler.
- **Daya Tahan Ekstra**: tahan air IP67, tali baja tahan tarik 200 kg, suhu kerja -20°C hingga +80°C.
- **Efisiensi Baterai & Pemeliharaan**: baterai mendukung operasi hingga 140 jam pada mode pelaporan real-time, ditambah update firmware jarak jauh (FOTA).

Versi halaman web memakai nama manfaat berbeda untuk poin yang sama:
- **Perlindungan Kargo Maksimal**: meningkatkan keamanan logistik dan mencegah risiko pencurian dengan keamanan berlapis.
- **Visibilitas End-to-End**: pemantauan penuh pergerakan aset dengan pelacakan lokasi presisi, dari titik keberangkatan hingga tujuan akhir.
- **Kendali Akses Fleksibel**: buka segel jarak jauh dengan kata sandi via SMS/aplikasi, atau kunci RFID terotorisasi saat bongkar muat di area tanpa sinyal.
- **Efisiensi Operasional**: mengurangi biaya perawatan dengan baterai hingga 140 jam (mode real-time) dan FOTA.

---

## Cara Kerja

1. **Mode Standby**: dalam keadaan normal tanpa gangguan, perangkat tidur dan bangun berkala (default 30 menit). Pemindaian RFID, getaran, penutup dibuka, atau tali dimasukkan/dicabut membangunkan perangkat selama sekitar 10 menit, dan selama itu data lokasi dikirim setiap 30 detik (default).
2. **Penguncian**: perangkat mengunci otomatis setelah kedua ujung tali pengait dimasukkan. Buzzer berbunyi sekali (tali terdeteksi), motor bekerja, lalu buzzer berbunyi dua kali (terkunci berhasil).
3. **Membuka Jarak Jauh**: kirim perintah lewat SMS atau aplikasi IntelliTrac (web, Android/iOS) melalui tombol unlock pada fitur *send command* unit VT-51. Buzzer berbunyi 3 detik tanda tali sudah bisa ditarik. Jika tali tidak ditarik dalam 10 detik, buzzer berbunyi hingga 60 detik. Jika tetap dibiarkan, perangkat terkunci kembali.
4. **Membuka dengan RFID** (cara normal sehari-hari): pindai kunci RFID ke perangkat. Jika sah, buzzer berbunyi sekali, motor berputar, lalu buzzer berbunyi dua kali tanda tali siap ditarik. Jika RFID tidak sah, buzzer berbunyi terus selama 3 detik dan peringatan dikirim ke platform.

---

## Spesifikasi Teknis

| Item | Spesifikasi |
|---|---|
| Ukuran | 195 mm x 114 mm x 37 mm |
| Berat | 833 g (termasuk unit utama dan tali pengait) |
| Material | Engineering plastic |
| Jaringan seluler | 4G LTE Cat1 industrial IoT module |
| Band frekuensi | 4G LTE-FDD: B1/B3/B5/B8; 4G LTE-TDD: B34/B38/B39/B40/B41 |
| Modul GSM | Quectel M25, EC200 series, atau EC25 series |
| SIM Card | Dual SIM Card (Micro) |
| GNSS | GPS + BeiDou + GLONASS, chipset AT6558R, 32 channel |
| Cold start / Hot start | ≤32 detik / ≤1 detik |
| Sensitivitas | Cold start capture -148 dBm, tracking -165 dBm |
| Akurasi posisi | <2,5 m (CEP50) |
| Antena | Antena internal untuk sinyal GSM dan penerimaan sinyal satelit GNSS |
| Mode transmisi data | TCP (jaringan seluler) atau SMS |
| Memori | 16 MB (flash memory buffer) |
| Baterai | Isi ulang 10.000 mAh, tipe 18650 Lithium |
| Tegangan & arus kerja | 3,7 Vdc, 40-200 mA |
| Durasi kerja | Mode real-time: 140 jam |
| Pengisian daya | DC 5V, 2A, konektor 5521 |
| Sensor gerak | 3D acceleration sensor (G-sensor) |
| Lock hook | Stainless steel, tahan tarik 200 kg |
| Indikator LED | 4 LED (Communication, Location, Low power, Charge) |
| Tahan air | IP67 |
| Suhu kerja | -20°C s/d +80°C |
| Suhu penyimpanan | -40°C s/d +80°C |
| Kelembapan | 5% s/d 99% |
| Bluetooth | BLE 4.2, 2,4 GHz (FHSS), opsional |
| RFID | 125 kHz, tag tipe ID Card |

---

> **Catatan untuk Mintel**: VT-51 E-Seal adalah **segel elektronik untuk pintu kargo/kontainer**, bukan GPS tracker kendaraan. Perangkat ini bertenaga baterai sendiri dan tidak tersambung ke kelistrikan kendaraan, jadi JANGAN mengaitkannya dengan fitur kendaraan seperti Engine Cut-Off, deteksi ignition/mesin, hourmeter, OBD-II CAN800, sensor suhu, atau perilaku mengemudi (HA/HB). Kalau customer butuh pelacakan kendaraannya sekaligus, sampaikan bahwa VT-51 bisa dipadukan dengan GPS tracker kendaraan (VT-45 Lite/VT-45) dan arahkan ke Sales Executive untuk konfigurasinya.
>
> Soal **SMS**: di VT-51, SMS dipakai sebagai salah satu cara mengirim perintah buka segel dan sebagai mode transmisi data perangkat. Ini TIDAK mengubah ketentuan bahwa SMS bukan kanal notifikasi alert platform IntelliTrac. Peringatan perusakan VT-51 dikirim "ke sistem/platform", jadi JANGAN menjanjikan peringatan perusakan dikirim lewat SMS ke HP customer.
>
> Soal **satelit**: frasa "Satellite detection" pada antena artinya penerimaan sinyal satelit GNSS untuk menghitung posisi, BUKAN komunikasi data via satelit. Pengiriman data VT-51 tetap lewat jaringan seluler (TCP) atau SMS. Saat tidak ada sinyal seluler, data disimpan di flash memory buffer 16 MB, dan segel tetap bisa dibuka di lokasi dengan kunci RFID.
>
> Soal **baterai**: angka resmi hanya **140 jam pada mode real-time**. Katalog tidak menyebut berapa lama baterai bertahan pada mode standby, jadi JANGAN menebak durasinya (misal "berminggu-minggu"). Cukup sampaikan bahwa mode standby dan Automatic Power Saving dirancang untuk menghemat baterai, lalu arahkan ke Sales Executive untuk estimasi sesuai pola pengiriman customer.
>
> Soal **cara membuka segel**: cara normal sehari-hari adalah menempelkan kartu RFID terotorisasi langsung ke perangkat di lokasi. Buka jarak jauh adalah opsi tambahan. Aplikasi yang dipakai untuk buka jarak jauh adalah **aplikasi IntelliTrac yang sama** (web dan mobile) yang dipakai untuk GPS tracker lain, bukan aplikasi terpisah. Di aplikasi itu setiap GPS tampil sebagai satu device/kendaraan, dan untuk unit VT-51 disediakan fungsi *send command* berupa tombol unlock gembok. Tombol ini diaktifkan per unit oleh tim IntelliTrac sebagai bagian dari prosedur standar saat aktivasi VT-51, jadi customer tidak perlu mengajukan permintaan khusus. Jadi customer yang sudah memakai IntelliTrac untuk armadanya bisa memantau dan membuka segel VT-51 dari aplikasi yang sama.
>
> Soal **peruntukan**: untuk truk tangki, VT-51 menyegel **katup tangki** agar tidak dibuka diam-diam, bukan mengukur isi/volume cairan (IntelliTrac tidak punya fuel/level sensor fisik, lihat `catalogue_2026.md`). Untuk cold chain farmasi, VT-51 hanya menyegel pintu boks; pemantauan suhunya tetap butuh VT-45 + Sensor Suhu. Untuk bea cukai, sampaikan sebatas kegunaan yang tertulis (memastikan kontainer tidak dibuka sebelum pemeriksaan). JANGAN menyatakan VT-51 sudah tersertifikasi, disetujui, atau diwajibkan oleh Direktorat Jenderal Bea dan Cukai maupun otoritas pelabuhan, karena status itu tidak tercantum di sumber mana pun.
>
> Soal **integrasi API**: SPIONAM dan SILACAK tercantum sebagai integrasi yang didukung, tapi detail teknis, persyaratan, dan biayanya tidak ada di knowledge base. Arahkan ke Sales Executive untuk peninjauan.
>
> Hal yang **tidak tercantum** di katalog maupun halaman web dan statusnya TIDAK DIKETAHUI (jangan dikarang, arahkan ke Sales Executive): kegunaan spesifik fitur Bluetooth opsional, harga unit dan biaya kunci RFID tambahan, masa garansi VT-51, serta dukungan jaringan 2G (meski salah satu opsi modul GSM-nya Quectel M25, jangan menyebut VT-51 punya fallback 2G).
