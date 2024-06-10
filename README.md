# 🔥 FINAL PROJECT TEKNOLOGI KOMPUTASI AWAN 2024🔥

## A. Cakupan Capaian Pembelajaran Mata Kuliah (CPMK)
1. Mampu memahami dan menerapkan berbagai servis pada layanan awan.
2. Mampu merancang dan mengaplikasikan teknologi komputasi awan.


## B. Constraint Final Project
1. FP ini dikerjakan secara berkelompok **maksimal 4-5 orang**
2. Linkungan cloud yang digunakan (pilih salah satu)
    - `Google Cloud Platform (Credit 300$)`
        * Boleh memanfaatkan semua fitur yang ada
        * Harga sesuai dengan yang disediakan Provider
    - `Digital Ocean (Credit 200$)`
        * Boleh memanfaatkan semua fitur yang ada
        * Harga sesuai dengan yang disediakan Provider
    - `Microsoft Azure (Credit 100$)`
        * Boleh memanfaatkan semua fitur yang ada
        * Harga sesuai dengan pricing calculator Azure
    - `Local Vritual Machine (VirtualBox/Vagrant) sebagai alternatif simulasi cloud.`
        * Apabila membuat lebih dari 1 VM, maka VM harus dibuat **minimal** dari 2 Komputer / Host yang berbeda
        * Hanya boleh membuat VM dengan spesifikasi sebagai berikut

            | No | Tipe   | CPU   | Memory | Harga / bulan |
            |----|--------|-------|--------|---------------|
            | 1  | vm1    | 1vCPU | 512 MB | 4 US$         |
            | 2  | vm2    | 1vCPU | 1 GB   | 6 US$         |
            | 3  | vm3    | 1vCPU | 2 GB   | 12 US$        |
            | 4  | vm4    | 2vCPU | 2 GB   | 18 US$        |
            | 5  | vm5    | 2vCPU | 4 GB   | 24 US$        |
            | 6  | vm6    | 4vCPU | 8 GB   | 48 US$        |


## C. Permasalahan

Anda adalah seorang lulusan Teknologi Informasi, sebagai ahli IT, salah satu kemampuan yang harus dimiliki adalah **Keampuan merancang, membangun, mengelola aplikasi berbasis komputer menggunakan layanan awan untuk memenuhi kebutuhan organisasi.**

Pada suatu saat anda mendapatkan project untuk mendeploy sebuah aplikasi Sentiment Analysis dengan komponen Backend menggunakan python: [sentiment-analysis.py](/Resources/BE/sentiment-analysis.py) dengan spesifikasi sebagai berikut

## Endpoints:



1. **Analyze Text**
   - **Endpoint:** `POST /analyze`
   - **Description:** This endpoint accepts a text input and returns the sentiment score of the text.
   - **Request:**
     ```json
     {
        "text": "Your text here"
     }
     ```
    - **Response:**
      ```json
      {
        "sentiment": <sentiment_score>
      }
      ```

2. **Retrieve History**
   - **Endpoint:** `GET /history`
   - **Description:** This endpoint retrieves the history of previously analyzed texts along with their sentiment scores.
   - **Response:**
     ```json
     {
      {
        "text": "Your previous text here",
        "sentiment": <sentiment_score>
      },
      ...
     }
     ```
---

Kemudian juga disediakan sebuah Frontend sederhana menggunakan [index.html](/Resources/FE/index.html) dan [styles.css](/Resources/FE/styles.css) dengan tampilan antarmuka sebagai berikut

![alt text](image.png)

Kemudian anda diminta untuk mendesain arsitektur cloud yang sesuai dengan kebutuhan aplikasi tersebut. Apabila dana maksimal yang diberikan adalah **1 juta rupiah per bulan (65 US$)**
konfigurasi cloud terbaik seperti apa yang bisa dibuat?

## D. Output Final Project dan Penilaian
1. Buatlah rancangan arsitektur cloud nya beserta harga yang diperlukan (20%) **(dipresentasikan saat diskusi minggu 15)**
2. Lakukan instalasi / implementasi rancangan cloud dan aplikasi, pastikan setiap endpoint aplikasi dapat berjalan (20%)
3. Lakukan load testing menggunakan Locust ([Locustfile](/Resources/Test/locustfile.py)) untuk endpoint Get Order dan Create new Order dengan parameter pengujian sebagai berikut (35%)
    1. Locust harus dijalankan dengan Komputer / Host yang berbeda dari Aplikasi
    2. Berapakah **jumlah Request per seconds (RPS)** maksimum yang dapat ditangani oleh server dengan durasi waktu load testing 60 detik? (tingkat failure harus 0%)
    3. Berapa **jumlah peak concurrency** maksimum yang dapat ditangani oleh server dengan **spawn rate 50** dan durasi waktu load testing 60 detik? (tingkat failure harus 0%)
    4. Berapa **jumlah peak concurrency** maksimum yang dapat ditangani oleh server dengan **spawn rate 100** dan durasi waktu load testing 60 detik? (tingkat failure harus %)
    5. Berapa **jumlah peak concurrency** maksimum yang dapat ditangani oleh server dengan **spawn rate 200** dan durasi waktu load testing 60 detik? (tingkat failure harus 0%)
    6. Berapa **jumlah peak concurrency** maksimum yang dapat ditangani oleh server dengan **spawn rate 500** dan durasi waktu load testing 60 detik? (tingkat failure harus 0%)
4. Buatlah dokumentasi laporan dalam github (markdown) dengan konten sebagai berikut: (25%)
    1. Introduction, jelaskan permasalahan (bisa mereferensi ke soal ini)
    2. Gambar desain rancangan arsitektur komputasi awan (dapat menggunakan https://app.diagrams.net/) dan Tabel harga spesifikasi dan Harga VM
    3. Tuliskan langkah langkah implementasi dan konfigurasi teknologinya (Load balancing, instalasi app.py, instalasi mongodb, dll) disertai screenshot lebih bagus 
    4. Hasil Pengujian endpoint setiap API (dapat menggunakan Postman) dan tampilan Antarmuka Aplikasi
    5. Hasil Pengujian dan analisis Loadtesting menggunakan Locust 
    6. Kesimpulan dan saran.

## X. Tips and trick
1. Implementasikan dengan spesifikasi paling kecil terlebih dahulu, coba cari kofigurasi optimal untuk memaksimalkan kerja processor dan memory, kemudian lakukan scale out untuk mendapatkan hasil Load testing terbaik.
2. Manfaatkan semua yang sudah dipelajari dalam kelas dan praktikum komputasi awan (Load balancing, provisioning, dll)
3. Good Luck :fist:
