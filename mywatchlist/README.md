# Tugas 3
## Danendra Herdiansyah - 2106707012 - PBP C
<hr>

### Link Aplikasi Heroku
> [HTML](https://aplikasi-tugas-danen.herokuapp.com/mywatchlist/html/) : `https://aplikasi-tugas-danen.herokuapp.com/mywatchlist/html/`<br>
> [XML](https://aplikasi-tugas-danen.herokuapp.com/mywatchlist/xml/) : `https://aplikasi-tugas-danen.herokuapp.com/mywatchlist/xml/`<br> 
>[JSON](https://aplikasi-tugas-danen.herokuapp.com/mywatchlist/json/) : `https://aplikasi-tugas-danen.herokuapp.com/mywatchlist/json/`<br>


### Perbedaan antara JSON, XML, dan HTML
Saat ini dimana digitalisasi dokumen berusaha untuk menampilkan data dengan format tertentu dan proses yang efisien. Isu - isu yang dihadapi terhadap proses ini diantaranya adalah tampilan konten, struktur data, dan format dokumen. Oleh karena itu terdapat beberapa cara untuk membawakan sebuah data agar bisa diakses di web yaitu HTML, XML, dan JSON. <br>

HTML dan XML sama-sama berasal dari _markup languange_ yang menggunakan tag, tetapi yang membedakan kedua format tersebut terdapat pada tipe data dan tampilan yang dibawanya. HTML dengan _hyper text_ yang digunakan untuk menampilkan data, sedangkan XML dengan _extensible_ yang digunakan hanya untuk menyimpan dan mengangkut data ke dan dari database. Kemudian dikarenakan HTML adalah _markup languange_ bersifat statis yang berbasis _predefined tags_, maka HTML memiliki jumlah tag yang terbatas. Sedangkan XML adalah _markup language_ bersifat dinamis yang berbasis _user defined tags_, maka XML memiliki tags yang dapat diperluas. <br>

JSON merupakan format interchange data yang ringan. Hal yang membedakan JSON dengan HTML dan XML terdapat pada penggunaan bahasa yang independen. JSON digunakan untuk merepresentasikan data berupa objek yang menampilkan data dalam format array. Hal - hal tersebut menyebabkan JSON dapat menyusun informasi data dengan cara yang lebih mudah dilihat dan lebih lancar dalam berinteraksi. <br>

### Mengapa kita memerlukan _data delivery_ dalam pengimplementasian sebuah platform ?
_Data delivery_ digunakan untuk mengoleksi, mengubah, menyatukan, dan mengirim data ke user yang telah melakukan _request_. _Data delivery_ di sini berguna untuk ketika mengembangkan suaatu platform dimana diperlukannya untuk pengiriman data dari satu platform ke platform lainnya. Sehingga hal ini diperlukan untuk konsistensi dalam pengiriman data di banyak platform dengan database yang terpisah. <br>

### Pengimplementasian mywatchlist
Untuk menambahkan sebuah aplikasi baru ke dalam projek django, maka perlu membuat ebuah `django-app` baru bernama `mywatchlist`. Setelah perintah tersebut dijalankan, maka akan terbentuk sebuah folder aplikasi baru. Kemudian setelah menambahkan nama aplikasi baru ke dalam `settings.py` yang ada di folder `project_django`, maka hal selanjutya adalah menambahkan kelas mywatchlist dengan objek - objeknya berupa film yang ingin atau sudah ditonton ke dalam `models.py` yang ada di folder `mywatchlist`. Setelah object terbuat, maka diperlukan  migrasi skema model ke dalam _database_ Django. Setelah dilakukan migrasi data, maka untuk menyimpan data-data yang ingin ditampilkan akan dibuat folder `fixtures` yang berisi file bernama `initial_mywatchlist_data.json` yang akan berisi informasi film. Lalu informasi data tersebut perlu dimasukkan ke dalam _database_ Django lokal.

Hal yang dilakukan setelah membuat aplikasi Django baru adalah mengimplementasi views. Hal ini dilakukan dengan cara menambahkan sebuah fungsi ke dalam `views.py` yang ada di folder `mywatchlist` dengan parameter _request_ yang mengembalikan render sebagai _HttpResponse_ dengan model yang sesuai di `mywatchlist.html`. Selain HTML, saya juga menambahkan format data berupa XML dan JSON untuk pengiriman data. Hal ini dilakukan dengan membuat fungsi baru dengan hasil return _HttpResponse_ berupa _serialize_ data dengan konten yang sesuai (XML/JSON). Kemudian menambahkan ketiga format tersebut untuk melakukan _Routing_ dengan penambahan _urlpatterns_ terhadap fungsi `views.py` yang ada di folder `mywatchlist` dengan path yang sesuai (HTML/XML/JSON) dan menambahkan path tersebut ke dalam _urlpatterns_ yang ada di `project_django`.

Lalu untuk menghubungkan models dengan views dan template, data - data tersebut dipetakan ke path nya masing-masing dengan mengimpor data dari model katalog ke `views.py` yang ada di `mywatchlist`. Kemudian object data film tersebut akan dikembalikan bersama dengan render agar selalu update. Untuk menguji apakah aplikasi (url) tersebut bsia memberikan respon, pada `tests.py` yang ada di dalam `mywatchlist` ditambahkan dengan _testcase_ terhadap _client_ berupa `HTTP response 200` yang akan memberikan sinyal "OK". terhadap ketiga format data. 

Setelah membuat aplikasi Django, maka aplikasi tersebut akan dilakukan _deployment_ ke Heroku agar bisa diakses kapan saja dan oleh siapa saja. Hal tersebut dilakukan dengan mengkonfigurasi proyek dengan file `yml` dan menambahkan root pada `settings.py` yang ada di `project_django`. Hal terakhir yang dilakukan adalah dengan menambahkan _secrets_ berupa `API Key` dan `nama aplikasi` ke dalam GitHub untuk menghubungkan repositori dengan Heroku.

### Screenshot akses URL menggunakan Postman

#### HTML
![Screenshot (382)](https://user-images.githubusercontent.com/87986916/191410691-207fdbb4-7c94-4cf3-bf12-6b1d5a07bb2b.png)

#### XML
![Screenshot (387)](https://user-images.githubusercontent.com/87986916/191411966-ba93023a-7b2f-4a88-bdf8-49bc64a98b6b.png)

#### JSON
![Screenshot (385)](https://user-images.githubusercontent.com/87986916/191410924-1aaeae1d-0cb1-41d3-abb2-b02bae66ce93.png)