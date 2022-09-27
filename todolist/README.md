# Tugas 4
## Danendra Herdiansyah - 2106707012 - PBP C
<hr>

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

### Pengimplementasian _checklist_ todolist
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