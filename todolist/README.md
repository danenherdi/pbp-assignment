# Tugas 4
## Danendra Herdiansyah - 2106707012 - PBP C
<hr>

### Readme Tugas 6
>[README-TWO.md](todolist\README-TWO.md)

### Link Aplikasi Heroku
> [todolist](https://aplikasi-tugas-danen.herokuapp.com/todolist) : `https://aplikasi-tugas-danen.herokuapp.com/todolist`
<br>


### Kegunaan `{% csrf_token %}` pada elemen `<form>` serta perihal yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`
CSRF dikenal sebagai _Cross-Site Request Forgery_ yang berbentuk token digunakan sebagai alat keamanan terhadap serangan berbasis web yang biasanya berasal dari _malicious site_ atau _malicious user_ yang menggunakan website tersebut. Kasus penggunaan CSRF token ini biasanya ditemui terhadap situs web yang memerlukan pengguna untuk mengisi data tertentu atas nama pengguna yang berhubungan dengan metode `POST`. Kemudian data tersebut pastinya bersifat rentan terhadap serangan sehingga diperlukan sebuah sistem keamanan yang unik untuk mencegah serangan CSRF tersebut. Token dari CSRF ini bersifat unik seperti kode alfanumerik atau memiliki nilai rahasia acak yang khas untuk situs tersebut dan kode tersebut berbeda untuk situs lainnya setiap _session_ dari seorang pengguna. Sehingga ketika token CSRF tidak diaplikasikan ke dalam elemen `<form>`, maka hal yang mungkin terjadi adalah ketika terjadi metode `GET`, pesan _Invalid_ atau _missing CSRF token_ akan muncul karena browser tersebut tidak bisa membuat cookie yang aman atau dalam kata lain tidak dapat mengakses cookie tersebut untuk mengotorisasi _login_ akun data pengguna yang bersangkutan. 
<br>
<br>

### Pembuatan elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`) 
Membuat elemen form tanpa menggunakan generator adalah hal yang bisa dilakukan. Contoh dari pengaplikasian manual ini terdapat pada template `login.html` dimana pada saat ingin mengambil data dari pengguna, maka digunakan _input_. Metode _input_ tersebut akan mengambil tipe, nama, placeholder, dan class dari data yang ingin diambil. Sehingga ketika data tersebut dimasukkan, fungsi yang berkaitan di `views.py` akan mendapatkan respon dari _request_ web menggunakan metode `request.POST.get('item')`. Hal ini bertujuan untuk mendapatkan data yang sudah di `POST` yang kemudian akan disimpan ke dalam database form.
<br>
<br>

### Penjelasan Proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML
Alur data bermula dari pengguna yang mengisi data submisi berbentuk input yang kemudian di-submit menggunakan tombol yang tersedia. Data tersebut kemudian akan membuat objek baru dengan metode `POST` dari "`request.POST`" untuk mengirim data ke database form. Kemudian ketika form tersebut sudah valid dengan menggunakan `form.is_valid()`, maka hal selanjutnya ialah menyimpan data form tersebut dengan `form.save()` untuk kemudian akan ditampilkan. Untuk menampilkan data ke template HTML, fungsi `show_todolist` yang ada di `views.py` akan memetakan data terhadap model yang telah dibuat di `models.py`. Dikarenakan aplikasi ini berbasis akses akun pengguna, maka objek `todolist` yang ingin ditunjukkan menggunakan filter terhadap akun yang sedang login dengan `.objects.filter(user=user_logged_in)`. Ketika sudah dipetakan, maka fungsi tersebut akan mengembalikan data dengan render sesuai request terhadap template html. Munculnya data di template html dilakukan dengan iterasi sterhadap list dari todolist yang sudah dibuat terhadap akun pengguna tersebut.
<br>
<br>

### Pengimplementasian _Checklist_ todolist (Tugas 4)
1. Pembuatan aplikasi bernama `todolist` dilakukan dengan menggunakan perintah `python manage.py startapp todolist` dan menambahkan aplikasi `todolist` ke dalam variabel `INSTALLED_APPS` yang terdapat di `project_django`.
<br>

2. Penambahan _path_ `todolist` dilakukan dengan membuat berkas `urls.py` di dalam folder `todolist` dan menambahkan `urlpatterns` yang sesuai dengan fungsi yang bersangkutan di `views.py` (`path('', show_todolist, name='show_todolist')`). Pendaftaran _path_ juga dilakukan pada `urls.py` yang ada pada folder `project_django` dengan menambahkan `path('todolist/', include('todolist.urls'))`.
<br>

3. Pembuatan model `Task` yang memiliki atribut `user`, `date`, `title`, dan `description` dilakukan dengan menambahkan sebuah class pada `models.py` yang ada di dalam folder `todolist`. Atribut `user` menggunakan tipe model `models.ForeignKey` untuk token unik yang sesuai dengan akun masing-masing dengan parameter `User, on_delete=models.CASCADE` untuk menghapus objek ketika user tersebut dihapus. Atribut `date` menggunakan tipe model `models.DateTimeField`, sedangkan `title` menggunakan tipe model `models.CharField` dan `description` menggunakan tipe model `models.TextField`.
<br>

4. Pengimplementasian form registrasi, login, dan logout dilakukan dengan membuat fungsi masing-masing pada `views.py` yang ada di dalam folder `todolist` yang kemudian ditampilkan pada template HTML. form registrasi dibuat dengan fungsi `register_todolist` yang menggunakan `UserCreationForm` dari django yang kemudian disimpan ketika metode yang digunakan adalah `POST` untuk mengirim data ke database form. Login dan logout akun diimplementasikan dengan mengambil data akun yang telah di `POST` dengan `request.POST.get` dan mengautentikasi akun yang sesuai untuk login, sedangkan untuk logout maka dilakukan _request_ untuk logout dan menghapus sesi cookie saat itu.
<br>

5. Pembuatan halaman utama `todolist` dilakukan dengan menambahkan beberapa tag pada `todolist.html`. Tag untuk menampilkan `Task` user adalah dengan iterasi setiap objek yang ada di list. Tombol `Tambah Task Baru` dan `logout` diimplementasikan dengan menggunakan tag `<button><a href="...">...</a></button>` dimana di dalam href adalah url yang sesuai dengan fungsi tombol tersebut.
<br>

6. Pembuatan halaman form untuk membuat task baru adalah dengan membuat berkas `forms.py` yang berisikan class `Meta` terhadap model berupa `Task` dan _fields_ berupa `title` dan `description`. Pemetaan data ke dalam model form dilakukan dengan membuat fungsi baru di `views.py` yang berguna untuk mengambil data form dengan `POST` dan simpan form baru tersebut dengan `....save()`. Setelah itu untuk ditampilan ke dalam template HTML, diperlukan berkas baru bernama `create_task.html` yang berisikan elemen form dengan _generator_ `{{form.as_table}}` untuk menampilkan form berbasis table. Kemudian terdapat juga tombol untuk submit data form yang telah diisi.
<br>

7. Pembuatan _routing_ dilakukan untuk mengakses aplikasi yang telah dibuat melalui URL dengan menambahkan path ke dalam variabel `urlpatterns` yang terdapat di `urls.py` pada folder `todolist`. Masing - masing fungsi dilakukan penambahan path dengan format awalan nama perintah tersebut seperti `login/`, `register/`, `create-task/`, dan `logout/`.
<br>

8. _deployment_ ke Heroku dilakukan dengan _push_ file-file todolist ke dalam repositori GitHub yang kemudian akan dihubungkan dengan _secrets_ yang telah disesuaikan.
<br>

9. Pembuatan dua akun pengguna dan tiga _dummy_ data dilakukan dengan melakukan registrasi akun yang kemudian digunakan untuk mengisi Task pada todolist.

<br>
<hr>

### Perbedaan dari Inline, Internal, dan External CSS
1. #### Inline CSS
    Tipe ini menggunakan atribut `style` yang dimasukkan ke dalam bagian body dari sebuah tag elemen di HTML sehingga satu tag HTML memiliki satu `style` yang unik. Kelebihan dari tipe ini adalah metode ini memiliki cara penempatan kode CSS yang lebih mudah dan cepat ke dalam HTML sehingga sangat berguna ketika ingin menguji ataupun melihat perbedaan style yang telah dibuat. Selain itu tipe ini juga tidak butuh file eksternal. Sedangkan kekurangan dari tipe ini adalah struktur yang dibuat di HTML akan menjadi lebih rumit untuk dibaca. Selain itu dikarenakan satu tag memiliki satu style, maka ketika memiliki style yang banyak akan berpengaruh terhadap ukuran halaman web (file HTML) dan waktu download.
<br>

2. #### Internal CSS
    Tipe ini mempunyai tag berupa `<style>` yang berada di dalam bagian `<head>` pada berkas template HTML. Gaya ini biasanya digunakan untuk memodifikasi satu berkas HTML dengan gaya masing-masing yang unik. Sehingga penempatan CSS dilakukan dengan _embedded_ di dalam file HTML. Kelebihan dari gaya ini adalah karena terdapat di dalam file HTML, maka tidak perlu menambahkan file lainnya untuk _styling_. Sedangkan kekurangannya adalah karena CSS terdapat di dalam file HTML, maka ukuran dan waktu pemuatan dari halaman web tersebut terjadi lebih lama dikarenakan ukurannya yang semakin besar.
<br>

3. #### External CSS
    Tipe ini membutuhkan file CSS eksternal yang terpisah dengan membuat file `.css` yang kemudian dihubungkan dengan file template HTML dengan tag link. Kelebihan dari tipe ini adalah bisa dihubungkan dengan satu file `.css` untuk _styling_ halaman web yang berbeda-beda. Selain itu dikarenakan kode CSS terdapat di file yang berbeda dengan HTML, maka file HTML memiliki ukuran yang lebih kecil. Sedangkan kekurangan dari tipe ini adalah dikarenakan file HTML dihubungkan dengan file eksternal CSS, maka bisa saja halaman web tidak dapat _rendered_ karena file CSS yang harus di-_load_ terlebih dahulu. Selain itu ketika terjadi penghubungan file CSS yang berbeda-beda, maka halaman web tersebut akan memiliki waktu download yang meningkat.

<br>
<br>

### Tag HTML5
HTML5 memiliki beberapa tag yang tidak ada di HTML biasa, contohnya adalah `<header>`, `<footer>`, `<article>`, `<section>`, `<audio>`, `<video>`, `canvas`, dll. Tag `<header>` ini digunakan untuk menyatakan awalan atau _header_ dari sebuah dokumen atau _section_ yang biasanya terdapat judul. Tag `<footer>` digunakan untuk menandakan akhir dari dokumen atau _section_ yang biasanya berisi informasi dari dokumen tersebut. Tag `<article>` digunakan untuk memberikan konten dokumen dari _section_. Tag `<section>` digunakan untuk mendefinisikan _header_, _footer_, dan _article_ yang telah dibuat di dokumen tersebut. Tag `<audio>` digunakan untuk memasukkan audio ke dalam halaman web (dokumen HTML). Tag `<video>` digunakan untuk memasukkan video ke dalam berkas HTML. Tag `<canvas>` ini digunakan untuk membuat sebuah area kosong yang kemudian digunakan untuk menggambar grafik tertentu dengan _scripting_ yang biasanya menggunakan JavaScript. 
<br>
<br>

### Tipe-Tipe CSS selector
1. #### Simple Selectors (elemen/tipe, class, id)
    Pengelompokkan ini dilakukan dengan mencakup penargetan tag elemen, class, maupun ID dari HTML.<br>
Contoh dari tag/elemen selector:
```
h1{
    color : ... ;
    text-align : ... ;
}
```
Contoh dari class selector:
```
.login{
    background-color : ... ;
    padding : ... ;
}
```
Contoh dari ID selector:
```
#header{
    color : ... ;
    padding : ... ;
}
```

2. #### Combinator Selectors
    Tipe Selector yang menggabungkan selector lain untuk sebuah elemen dalam dokumen HTML. Terdapat beberapa combinator seperti, _descendant selector_ yang menggunakan `(space)` untuk penurunan sebuah elemen. _Child selector_ yang menggunakan `>` untuk menyatakan anak dari sebuah elemen dalam dokumen HTML. _Adjacent sibling selector_ yang menggunakan `+` untuk menyatakan elemen saudara yang berdekatan dan memiliki elemen dengan induk yang sama. Kemudian yang terakhir adalah _general sibling selector_ yang menggunakan `~` untuk menyatakan elemen saudara kandung umum terhadap pemilihan elemen saudara kandung berikutnya.
<br>

3. #### Pseudo-class Selectors
    Pseudo-class digunakan untuk mendefinisikan sebuah tag elemen dengan style yang unik dan berbeda-beda.
Syntax dari selector ini adalah sebagai berikut:
```
selector : pseudo-class{
    property : value;
}
```
Contohnya adalah
```
a : hover{
    color : blue;
}
```

4. #### Pseudo-elements Selectors
    Pseudo-element digunakan untuk memberi style terhadap tag elemen yang lebih spesifik dengan style yang unik.
Syntax dari selector ini adalah
```
selector :: pseudo-element {
    property : value;
}
```
Contohnya adalah
```
p::first-line {
    font-weight : bold;
}
```

5. #### Attribute Selectors
Atribut yang dimaksud dihubungkan untuk menata tag elemen HTML terhadap nilai dari atribut tersebut untuk menggunakan style tertentu.
Contoh dari selector ini adalah
```
a[target]{
    background-color : red;
}
a[target = _blank]{
    backround-color : yellow;
}
# [attribute ~= "value"]
[title ~= "Login"]{
    background-color : blue;
}
```
<br>

### Pengimplementasian _Checklist_ todolist (Tugas 5)
1. Kustomisasi templat untuk halaman login, register, todolist, dan create_task dilakukan menggunakan penulisan CSS dengan cara _external style sheet_ dimana menggunakan file eksternal CSS yang bernama `login.css` yang kemudian dihubungkan ke template login dengan `{% load static %}` dan `<link rel="stylesheet" href="{% static '... .css' %}">` pada tag _head_. Lalu penambahan style ke template dilakukan dengan memasukkan style-style yang ingin dimasukkan dengan class selector. Selain itu, kustomisasi dilakukan juga dengan cara _inline_style_sheet_ untuk styling yang berhubungan dengan elemen dari bootstrap. Contoh bootstrap yang dipakai adalah _form-floating_ untuk mengisi form login dan navbar untuk header dari halaman todolist serta button.
<br>

2. Implementasi cards untuk menampilkan task di halaman utama todolist dilakukan dengan pertama - tama mengatur bootstrap container menjadi `container-fluid` untuk berubah setiap _breakpoint_. Kemudian menggunakan `row g-3` untuk mengatur horizontal dari baris cards. Lalu untuk membuat satu cards untuk satu task, di dalam iterasi for loop `todolist_task` dilakukan pendefinisian class card dengan panjang tertentu. Mendefinisikan satu card dilakukan dengan membuat class `card-body` dimana di dalamnya terdapat `card-title` untuk judul task, `card-subtitle` untuk tanggal pembuatan task tersebut, dan `card-text` untuk deskripsi dari task yang bersangkutan.
<br>

3. _Responsive web_ dilakukan dengan mengatur automatis dasar dari bootstrap yang dimasukkan ke dalam `base.html` berupa pengambilan link bootstrap dan script untuk pembuatan bootstrap serta masukkan kode berupa `<meta name="viewport" content="width=device-width, initial-scale=1.0">` untuk mengatur layar sesuai perangkat yang digunakan dengan `scaling`. Kemudian untuk mengatur responsive terhadap cards yang ada di halaman utama todolist dilakukan dengan membuat div class baru yang berisi `col-12 col-md-6 col-lg-4`. `col-12` disini digunakan untuk _scaling_ utama dari banyaknya cards. Kemudian untuk mengatur jika layar web sedang dikecilkan, maka dilakukan pengaturan untuk ukuran medium dengan `col-md-6` dimana jika ukuran web sedang medium maka cards yang muncul per-baris adalah 2 (sisa bagi dari scaling utama) serta untuk ukuran large dengan `col-lg-4` dimana jika web sedang ukuran besar maka cards yang muncul per-baris nya adalah 3 cards.
<br>

4. Pengimplementasian bonus dilakukan dengan menambahkan elemen properti `hover` pada class card di CSS yang kemudian diisi dengan mengganti warna dasar dan warna tulisan menjadi _dark mdoe_ serta memperbesar ukuran cards tersebut dengan transisi untuk _focus mode_.
<br>