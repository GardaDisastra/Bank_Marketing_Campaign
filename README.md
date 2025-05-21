# Bank_Marketing_Campaign

## Business Problem Understanding
Sebuah bank komersial menghadapi tantangan dalam mengoptimalkan kampanye pemasaran produk deposito berjangka kepada nasabahnya. Kampanye tersebut dilakukan secara massal melalui telepon kepada seluruh nasabah. Pendekatan ini mengakibatkan tingginya biaya pemasaran dan waktu operasional yang besar, serta risiko gangguan terhadap nasabah yang kurang potensial.

### Problem Statement
Metode kampanye pemasaran konvensional yang bersifat mass marketing saat ini menimbulkan beberapa tantangan seperti Biaya operasional yang tinggi, Pemanfaatan sumber daya manusia yang kurang efisien, dan Kurangnya personalisasi dalam pendekatan yang dapat menurunkan kualitas interaksi dengan nasabah

### Goals
Proyek ini bertujuan untuk membangun sistem prediktif berbasis machine learning dengan sasaran utama: dapat mengidentifikasi nasabah dengan potensi tinggi untuk menerima penawaran produk deposito, Meningkatkan efisiensi kampanye pemasaran dengan menargetkan segmen nasabah yang lebih tepat, Meminimalkan risiko kehilangan potensi pendapatan, dan Menyeimbangkan antara efisiensi biaya dan potensi pendapatan.

### StakeHolder
1. Manajemen Eksekutif
2. Divisi Pemasaran

### Analytical Approach
Proyek ini dimulai dengan eksplorasi dan pembersihan data (data cleaning), dilanjutkan dengan eksplorasi fitur (EDA) untuk memahami karakteristik data dan distribusi dari target variabel deposit. Setelah itu, dilakukan pemrosesan fitur melalui teknik transformasi numerik dan encoding kategorikal agar data siap digunakan dalam model pembelajaran mesin. Metric yang digunakan adalah F2-score

Beberapa algoritma klasifikasi akan diuji, lalu dilakukan pendekatan tuning hyperparameter menggunakan RandomizedSearchCV. Untuk memastikan generalisasi model, proses pelatihan dan validasi dilakukan menggunakan Stratified K-Fold Cross Validation guna menjaga proporsi kelas yang seimbang pada setiap lipatan.

Model terbaik kemudian akan dievaluasi tidak hanya berdasarkan metrik, tetapi juga dari sisi interpretabilitas dan manfaat bisnis, guna memastikan hasil yang dapat diimplementasikan secara efektif oleh tim pemasaran dan mendukung pengambilan keputusan strategis.

### Model Terbaik
Model dengan performa terbaik diperoleh menggunakan AdaBoostClassifier setelah proses hyperparameter tuning dengan pemilihan threshold sebesar 0.4. Nilai F2 yang dihasilkan sebesar 76.8%.

Berdasarkan hasil evaluasi yang telah dilakukan, model machine learning terbukti memberikan efisiensi biaya dan waktu yang signifikan. Meskipun net profit yang dihasilkan sedikit lebih rendah dibandingkan pendekatan mass marketing, penghematan biaya kampanye sebesar kurang lebih Rp 75 juta (32,4%) serta pengurangan waktu kontak pelanggan sekitar 125 jam (32,4%) merupakan pencapaian penting dalam konteks efisiensi operasional dan produktivitas tenaga kerja.

Pendekatan mass marketing memang menghasilkan pendapatan yang lebih tinggi sebesar Rp. 73 juta (12.7%), namun hal tersebut dicapai dengan biaya dan alokasi waktu yang jauh lebih besar, yang dalam praktiknya dapat menjadi kurang efisien terutama bagi institusi dengan keterbatasan sumber daya.



