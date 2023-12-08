# 🔥 FINAL PROJECT (FP) TEKNOLOGI KOMPUTASI AWAN 🔥

## A. Cakupan Capaian Pembelajaran Mata Kuliah (CPMK)
1. Mampu memahami dan menerapkan berbagai servis pada layanan awan.
2. Mampu merancang dan mengaplikasikan teknologi komputasi awan.


## B. Constraint Final Project
1. FP ini dikerjakan secara berkelompok (mengikuti kelompok presentasi)
2. Linkungan cloud yang digunakan (pilih salah satu)
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

Anda adalah seorang lulusan Teknologi Informasi, sebagai ahli IT, salah satu kemampuan yang harus dimiliki adalah **Keampuan merancang, membangun, mengelola aplikasi berbasis komputer menggunakan layanan awan untuk memenuhi kebutuhan organisasi.**(menurut kurikulum IT ITS 2023 😙) 

Pada suatu saat teman anda ingin mengajak anda memulai bisnis di bidang digital marketing, anda diberikan sebuah aplikasi berbasis API File: [app.py](/app.py) dengan spesifikasi sebagai berikut

## Endpoints:

1. **Get All Orders**
   - **Endpoint:** `GET /orders`
   - **Description:** Retrieve a list of all orders.
   - **Response:**
     ```json
     {
       "orders": [
         {"_id": "order_id_1", "product": "Product1", "quantity": 5, "customer_name": "John Doe", "customer_address": "123 Main St"},
         {"_id": "order_id_2", "product": "Product2", "quantity": 3, "customer_name": "Jane Smith", "customer_address": "456 Oak St"},
         // ...
       ]
     }
     ```

2. **Get a Specific Order by ID**
   - **Endpoint:** `GET /orders/<order_id>`
   - **Description:** Retrieve details of a specific order by its ID.
   - **Response:**
     ```json
     {
       "order": {"_id": "order_id", "product": "ProductX", "quantity": 8, "customer_name": "Alice Johnson", "customer_address": "789 Elm St"}
     }
     ```

3. **Create a New Order**
   - **Endpoint:** `POST /orders`
   - **Description:** Create a new order.
   - **Request:**
     ```json
     {
       "product": "ProductY",
       "quantity": 2,
       "customer_name": "Bob Anderson",
       "customer_address": "101 Pine St"
     }
     ```
   - **Response:**
     ```json
     {
       "message": "Order created successfully",
       "order": {"_id": "new_order_id", "product": "ProductY", "quantity": 2, "customer_name": "Bob Anderson", "customer_address": "101 Pine St"}
     }
     ```

4. **Update an Order by ID**
   - **Endpoint:** `PUT /orders/<order_id>`
   - **Description:** Update an existing order by its ID.
   - **Request:**
     ```json
     {
       "quantity": 10,
       "customer_address": "Updated Address"
     }
     ```
   - **Response:**
     ```json
     {
       "message": "Order updated successfully",
       "order": {"_id": "order_id", "product": "Updated Product", "quantity": 10, "customer_name": "Existing Name", "customer_address": "Updated Address"}
     }
     ```

5. **Delete an Order by ID**
   - **Endpoint:** `DELETE /orders/<order_id>`
   - **Description:** Delete an existing order by its ID.
   - **Response:**
     ```json
     {
       "message": "Order deleted successfully"
     }
     ```

    ### MongoDB Configuration:

    - **Database:** `orders_db`
    - **Connection URI:** `mongodb://localhost:27017/orders_db`

---

Kemudian anda diminta untuk mendesain arsitektur cloud yang sesuai dengan kebutuhan aplikasi tersebut. Apabila dana maksimal yang diberikan adalah **1 juta rupiah per bulan (65 US$)**
konfigurasi cloud terbaik seperti apa yang bisa dibuat?

## D. Output Final Project dan Penilaian
1. Buatlah rancangan arsitektur cloud nya beserta harga yang diperlukan (20%) **(dipresentasikan saat diskusi minggu 15)**
2. Lakukan instalasi / implementasi rancangan cloud dan aplikasi, pastikan setiap endpoint aplikasi dapat berjalan (30%)
3. Lakukan load testing menggunakan Locust ([Locustfile](/locustfile.py)) untuk endpoint Get Order dan Create new Order dengan parameter pengujian sebagai berikut (30%)
    1. Locust harus dijalankan dengan Komputer / Host yang berbeda dari Aplikasi
    2. Berapakah **jumlah Request per seconds (RPS)** maksimum yang dapat ditangani oleh server dengan durasi waktu load testing 60 detik? (tingkat failure harus 0%)
    3. Berapa **jumlah peak concurrency** maksimum yang dapat ditangani oleh server dengan **spawn rate 25** dan durasi waktu load testing 60 detik? (tingkat failure harus 0%)
    4. Berapa **jumlah peak concurrency** maksimum yang dapat ditangani oleh server dengan **spawn rate 50** dan durasi waktu load testing 60 detik? (tingkat failure harus %)
    5. Berapa **jumlah peak concurrency** maksimum yang dapat ditangani oleh server dengan **spawn rate 10**0 dan durasi waktu load testing 60 detik? (tingkat failure harus 0%)
4. Buatlah dokumentasi laporan dalam github (markdown) dengan konten sebagai berikut: (20%)
    1. Introduction, jelaskan permasalahan (bisa mereferensi ke soal ini)
    2. Gambar desain rancangan arsitektur komputasi awan (dapat menggunakan https://app.diagrams.net/) dan Tabel harga spesifikasi dan Harga VM
    3. Tuliskan langkah langkah implementasi dan konfigurasi teknologinya (Load balancing, instalasi app.py, instalasi mongodb, dll) disertai screenshot lebih bagus 
    4. Hasil Pengujian endpoint setiap API (dapat menggunakan Postman)
    5. Hasil Pengujian dan analisis Loadtesting menggunakan Locust 
    6. Kesimpulan dan saran.

## X. Tips and trick
1. Implementasikan dengan spesifikasi paling kecil terlebih dahulu, coba cari kofigurasi optimal untuk memaksimalkan kerja processor dan memory, kemudian lakukan scale out untuk mendapatkan hasil Load testing terbaik.
2. Manfaatkan semua yang sudah dipelajari dalam kelas dan praktikum komputasi awan (Load balancing, provisioning, dll)
3. Good Luck :fist:
