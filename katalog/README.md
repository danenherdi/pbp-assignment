# Tugas 1
## Danendra Herdiansyah - 2106707012 - PBP C

> [Link Aplikasi Heroku](https://aplikasi-tugas-danen.herokuapp.com/katalog/) : `https://aplikasi-tugas-danen.herokuapp.com/katalog/`

### Bagan _Request_ Klien ke Web Aplikasi Berbasis Django

Hubungan antara `urls.py` dengan `views.py` adalah petunjuk dari permintaan klien akan ditunjukkan ke data value yang sesuai. Kemudian `views.py` dan `models.py` akan menghubungkan permintaan data terhadap kumpulan data yang tersedia di database. Setelah itu berkas html digunakan untuk menampilkan data yang diminta klien dengan template yang sesuai.

### Python Virtual Environment
_Virtual environment_ digunakan oleh Python sebagai alat untuk menjaga ketergantungan satu proyek dengan proyek yang lainnya. Hal ini sangatlah berguna ketika memiliki proyek yang terpisah dengan versi yang berbeda-beda. Sehingga alat tersebut berfungsi untuk menjaga hubungan antara Python berbasis web dengan Django ataupun library lainnya yang berbeda versi antar satu sistem operasi.

Membuat aplikasi web berbasis Django sebenarnya bisa tanpa menggunakan _virtual environment_, tetapi disarankan untuk menggunakannya untuk mengatasi konsistensi dan kesesuaian versi Django yang berbeda ketika menambahkan suatu fitur di sistem operasi yang berbeda.

### Pengimplementasian Konsep Model-View-Template
Implementasi pertama yang dilakukan adalah menambahkan sebuah fungsi ke dalam `views.py` yang ada di folder `katalog` dengan parameter _request_ yang mengembalikan render sebagai _HttpResponse_ dengan model yang sesuai di `katalog.html`.

Kemudian untuk melakukan _routing_ maka dilakukanlah penambahan _urlpatterns_ terhadap fungsi `views.py` yang ada di folder `katalog` untuk ditampilkan output nya di halaman web dan menambahkan path tersebut ke dalam _urlpatterns_ yang ada di `project_django`.

Lalu untuk menghubungkan ketiga elemen tersebut (MVT) data - data katalog yang ada akan dipetakan ke HTMl dengan mengimpor data dari model katalog ke `views.py` yang ada di `katalog`. Kemudian masukkan semua object data katalog yang akan dikembalikan bersama dengan render agar selalu update. Ketika sudah dipetakan ke HTML, maka hal terakhir yang dilakukan adalah mengubah variabel-variabel yang ada di `katalog.html` dengan data-data yang sesuai.

Setelah membuat aplikasi Django, maka aplikasi tersebut akan dilakukan _deployment_ ke Heroku untuk aplikasi tersebut bisa diakses kapan saja dan siapa saja. Hal tersebut dilakukan dengan mengkonfigurasi proyek dengan file `yml` dan menambahkan root pada `settings.py` yang ada di `project_django`. Hal terakhir yang dilakukan adalah dengan menambahkan _secrets_ berupa API key dan nama aplikasi ke dalam GitHub untuk menghubungkan repositori dengan Heroku.
