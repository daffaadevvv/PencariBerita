# PencariBerita
Repository News Finder API untuk News Finder Twitter Bot

Disusun oleh :
* Muhammad Daffa Alfaridzi : 18217013

## Apa itu News Finder API?
News Finder API akan mengembalikan sebuah response berbentuk JSON yang berisikan *link* berita yang sesuai dengan *keyword* yang ingin dicari. Untuk menggunakan API ini, terdapat 2 endpoint :

    /internasional/keyword
    /dalamnegeri/keyword

Cara menggunakan API ini cukup simple : Ganti keyword dengan kata yang Anda ingin cari 

API ini akan dimanfaatkan oleh [Twitter API](https://github.com/luthfiihakiim/TST-018), API yang digunakan Twitter Bot yang dibuat oleh teman sekelompok saya Luthfi E.T. NIM 18217018.

API ini sudah di-*deploy* dan dapat dicoba di https://news-look.herokuapp.com/

## Penggunaan Docker Image
Pada direktori yang sudah tepat, jalankan command ini melalui CLI
```bash
$ docker load < twitter-news.tar.gz 
```
Setelah itu docker image akan tersimpan dan tinggal dijalankan

