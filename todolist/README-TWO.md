# Tugas 6
## Danendra Herdiansyah - 2106707012 - PBP C
<hr>

### Back to Readme
>[README.md](README.md)

### Link Aplikasi Heroku
> [todolist](https://aplikasi-tugas-danen.herokuapp.com/todolist) : `https://aplikasi-tugas-danen.herokuapp.com/todolist`
<br>

### Perbedaan _asynchronous programming_ dengan _synchronous programming_
_Asynchronous programming_ terjadi apabila sebuah eksekusi bisa dilakukan bersamaan ketika terdapat beberapa operasi yang sedang berlangsung secara waktu nyata. Hal ini memungkinkan untuk mengerjakan beberapa operasi tanpa harus menunggu operasi lain untuk selesai atau dalam hal ini, operasi yang dilakukan terhadap halaman web bisa terjadi secara langsung dan nyata tanpa harus _refresh_ halaman web.

Sedangkan _synchronous programming_ terjadi apabila operasi yang dilakukan adalah satu kali dalam waktu tertentu dengan urutan yang sesuai. Sehingga ketika suatu operasi sedang dilakukan, maka operasi lainnya harus menunggu sampai pemicu (_triggers_) penyelesaian operasi sebelumnya telah selesai. Hal ini berhubungan dengan bahwa ketika ingin mendapatkan data terbaru setelah dilakukan suatu operasi, maka kita harus _refresh_ halaman web tersebut.
<br>
<br>

### Penerapan paradigma _Event-Driven Programming_ pada JavaScript dan Ajax
_Event-Driven Programming_ terjadi ketika seorang user berinteraksi dengan halaman web. Kemudian dari interaksi tersebut muncul sebuah _event_ dimana halaman web tersebut diperlukan untuk melakukan suatu perubahan berdasarkan interaksi yang diminta oleh user tersebut. Setelah itu kode-kode JavaScript atau Ajax yang berhubungan dengan _event_ tersebut akan menjalankan sesuai dengan perintahnya dan melakukan interaksi kembali dengan _response_. _Response_ tersebut kemudian melakukan pembaruan di halaman web tanpa melakukan _refresh_. Salah satu penerapan event ini di tugas kali ini adalah ketika ingin melakukan pengambilan data dari submit form. Penulisan menggunakan DOM atau asli dari JavaScript adalah dengan `windown.onload = function(){}`. Namun ketika penerapan tersebut menggunakan JQuery, maka penulisannya adalah `$(document).ready(function(){}`. Kedua penulisan tersebut memiliki tujuan yang sama yaitu untuk melakukan sebuah _event_ dimana _response_ nya adalah untuk melakukan pengambilan data secara asinkronus ke dalam halaman web.
<br>
<br>

### Penerapan _asynchronous programming_ pada Ajax
Penerapan asinkronus pada program menggunakan Ajax biasanya digunakan saat melakukan _request_ dan _response_ terhadap menangani data. Sehingga ketika seorang user melakukan sebuah _request_ terhadap halaman web tersebut, maka user tersebut akan mendapatkan _response_ dari Ajax tanpa harus _refresh_ halaman web tersebut. Salah satu penerapannya adalah dengan menggunakan JQuery dimana Ajax akan menggunakan library tersebut untuk mengambil data dari server dan melakukan pembaruan terhadap halaman web tersebut tanpa harus _reloading_.
<br>
<br>

### Pengimplementasian JavaScript dan AJAX pada Todolist (Tugas 6)
1. Pembuatan view baru untuk mengembalikan data task dalam bentuk JSON
Pembuatan view baru dilakukan dengan menambahkan satu function yang mengembalikan data Task dengan filter user yang sedang login. Kemudian data tersebut dikembalikan dengan data berbentuk Json dengan `HttpResponse(serializers.serialize('json', data_todolist_user), content_type="application/json")`
<br>

2. Pembuatan path `/todolist/json` yang mengarah ke view
Pembuatan path dilakukan dengan menambahkan path ke dalam `urls.py` yang ada di dalam folder todolist dengan pathnya yaitu `json/` yang akan terhubung dengan function `show_todolist_json` yang ada di dalam `views.py` yang ada di dalam folder todolist.
<br>

3. Pengambilan task menggunakan Ajax GET
Pengambilan task dilakukan dengan menambahkan script berbentuk text dari JavaScript yaitu dengan mengambil data dari dokumen terlebih dahulu (`$(document).ready(function(){}`) kemudian data yang telah dibuat dengan format Json akan diambil dengan menggunakan `$.getJson` yang akan terhubung dengan path `json/` dimana path tersebut terhubung dengan function `show_todolist_json`. Kemudian untuk mendapatkan semua data yang ada, maka dilakukan iterasi dengan `$.each(data, function(i,task)){}`. Kemudian data yang telah diambil akan ditambahkan ke dalam cards dengan `$("#...").append(...);`
<br>

4. Pembuatan tombol `Add Task` untuk membuka form penambahan task berbentuk modal
Pembuatan tombol dilakukan dengan melakukan penambahan terhadap interaksi (data-toggle) berupa "modal" yang kemudian akan mengarah ke Id modal tersebut (data-target)
<br>

5. Pembuatan view baru untuk menambahkan task baru ke dalam database
Pembuatan view dilakukan dengan menambakan satu function yang akan membuat objek baru terhadap task. Tentunya karena penambahan dilakukan dengan "POST", maka diperlukan penyesuaian request method dengan post. Ketika sesuai maka hal selanjutnya adalah membuat data baru yang ada di `models.py` berupa title,date, dan description. Penambahan data tersebut dilakukan dengan mengambil data dari yang telah di post terhadap nama yang sesuai. Kemudian setelah dibuat task dengan data yang baru tersebut, maka akan dilakukan simpan dengan `.save()`.
<br>

6. Pembuatan path `/todolist/add/` yang mengarah ke view
Pembuatan path dilakukan dengan menambahkan path ke dalam `urls.py` yang ada di dalam folder todolist dengan pathnya yaitu `add/` yang akan terhubung dengan function `add_task_ajax` yang ada di dalam `views.py` yang ada di dalam folder todolist.
<br>

7. Penghubungan modal ke path `/todolist/add` 
Setelah dibuatnya modal pada template html, maka penyambungan modal tersebut dengan function yang ada di path `add/` adalah dengan menggunakan event Ajax. Event yang dilakukan adalah ketika data yang diisi user di modal akan disubmit ke database. Dengan menggunakan Ajax (`$.ajax({})`), maka path url yang akan tersambung adalah `/todolist/add` dengan tipe dari aksi method tersebut adalah post. Kemudian data yang telah disubmit akan dimasukkan ke dalam database dengan mengambil value yang ada di form modal dan post data baru tersebut yang kemudian akan ditambahkan ke dalam cards yang berisi task.
