
---
### PENJELASAN RINCI CELL 1
---
Pada cell pertama, terdapat beberapa baris kode yang mendefinisikan untuk menginstall beberapa library. Pertanyannya adalah, bukannya kita hanya ingin menggunakan library selenium saja, mengapa terdapat beberapa library pada baris kode tersebut?

hal ini dikarenakan **satu library punya fungsi spesifik**. Sama seperti ketika kita membutuhkan pena, penghapus, dan penggaris untuk menggambar, satu alat saja tidak akan bisa mengerjakan semua.

Kemudian, beberapa library tersebut sebenarnya melengkapi fungsi dari selenium, sama anloginya seperti menulis. jika kita menulis itu kan biasanya menggunakan pulpen/pensil, dan itu sebagai alat utama kita untuk menulis, namun pensil/pulpen tidak mungkin berdiri sendiri pada penggunannya, terdapat tip-x dan penghapus sebagai pelengkapnya.
Berikut ini adalah penjelasan dari arti atau fungsi library tersebut:
1. **Selenium** digunakan untuk mengendalikan browser (Chrome, Firefox) lewat Python. Fungsinya untuk: membuka halaman web, login otomatis, gulir halaman (scroll), klik tombol, dan ambil sumber halaman (HTML).

2. **undetected-chromedriver** membantu selenium untuk mengelola driver Chrome (file .exe yang menghubungkan Python ke browser) secara otomatis. sehingga kita tidak perlu download dan setting path driver secara manual.

3. **webdriver-manager** membantu selenium untuk mengelola driver Chrome (file .exe yang menghubungkan Python ke browser) secara otomatis. jadinya kita tidak perlu download dan setting path driver secara manual.

4. Setelah selenium mengambil sumber halaman (HTML), **beautifulsoup4** membantu mengurai (parse) HTML itu dan mencari elemen spesifik (misalnya teks tweet, username) dengan mudah.

5. **pandas** ini digunakan untuk mengelola data dalam bentuk tabel (seperti Excel, tapi di Python). dan ini sangat penting, sehingga dapat digunakan untuk membaca file CSV, menggabungkan data dari berbagai tahun, menyimpan data ke file CSV.

6. lalu ada **Library Sastrawi** yang khusus untuk Bahasa Indonesia. penggunaanya untuk: 
    - Stopword Removal: Menghapus kata-kata umum seperti "yang", "dan", "adalah".
    - Stemming: Mengubah kata berimbuhan ke bentuk dasarnya (misalnya "kebijakan" jadi "bijak").


Kemudian kita bedah satu per satu dari makna kodenya ya, kode:

``` bash
!python -m pip install beautifulsoup4
!python -m pip install undetected-chromedriver
!python -m pip install selenium
!python -m pip install webdriver-manager
!python -m pip install pandas
!python -m pip install Sastrawi
```
   
- !: adalah perintah magic di Jupyter Notebook. Artinya, perintah yang mengikuti ! bukan perintah Python, tapi perintah yang dijalankan.
- python -m pip: untuk menjalankan modul pip menggunakan Python. pip adalah package installer untuk Python. Kenapa python -m pip dan bukan cuma pip? karena awalnya mengalami insiden serius, Windows tidak mengenali pip langsung. tapi karena pasti tahu di mana Python dan modul pip-nya berada, makanya menjalankankan dengan -m pip.
- install: Ini adalah perintah pip untuk mengunduh dan memasang sebuah library.
- nama_library: Ini adalah nama library yang ingin diinstall.


---
### PENJELASAN RINCI CELL 2
---
baris-baris kode di Cell 2 ini hanya memberi tahu Python bahwa kita ingin menggunakan library dan fungsi-fungsi tertentu dari library eksternal (selenium, bs4, undetected_chromedriver, dll) dan modul bawaan (time, json, csv, os).

tanpa import ini, Python tidak akan tahu apa itu webdriver, BeautifulSoup, Keys, uc, dsb. jadi, Cell 2 harus dijalankan terlebih dahulu sebelum cell-cell lain yang menggunakan fungsi-fungsi tersebut.

1. from bs4 import BeautifulSoup **digunakan untuk** mengambil kelas BeautifulSoup dari library bs4.**fungsinya dari** BeautifulSoup adalah untuk mengurai (parse) kode HTML yang diambil dari halaman web menjadi struktur data yang mudah dicari dan diambil elemennya oleh Python. Misalnya, mencari semua teks yang ada di dalam div dengan ID tertentu.

2. from selenium import webdriver **digunakan unruk** mengambil modul webdriver dari library selenium. **fungsi webdriver adalah** inti dari Selenium. Ini digunakan untuk membuat objek yang mewakili browser (seperti Chrome, Firefox) dan mengendalikannya (buka URL, klik tombol, isi form).

3. from selenium.webdriver.chrome.options import Options **artinya adalah** mengambil kelas Options dari modul selenium.webdriver.chrome.options. **fungsi dari options** yaitu untuk mengkonfigurasi bagaimana browser Chrome akan dibuka. Misalnya, apakah akan dibuka dalam mode headless (tanpa tampilan grafis), atau menonaktifkan ekstensi tertentu untuk menghindari deteksi bot.

4. from selenium.webdriver.common.keys import Keys
Maksud: Mengambil modul Keys dari selenium.webdriver.common.keys.
Fungsi: Keys berisi konstanta untuk tombol-tombol khusus pada keyboard, seperti Keys.RETURN (Enter), Keys.ESCAPE, Keys.ARROW_DOWN, dll. Ini digunakan untuk mengirimkan perintah menekan tombol ke elemen HTML (misalnya, menekan Enter setelah mengisi username).
from selenium.webdriver.common.by import By
Maksud: Mengambil modul By dari selenium.webdriver.common.by.
Fungsi: By berisi konstanta untuk menentukan metode pencarian elemen di halaman web. Misalnya, By.ID, By.CLASS_NAME, By.XPATH. Ini digunakan bersama fungsi find_element untuk mencari elemen spesifik (seperti field password).
from selenium.common.exceptions import NoSuchElementException, TimeoutException
Maksud: Mengambil dua jenis eksepsi (error) spesifik dari selenium.common.exceptions.
Fungsi:
NoSuchElementException: Akan dilempar oleh Selenium jika kamu mencoba mencari elemen (misalnya tombol login) tapi elemen itu tidak ditemukan di halaman.
TimeoutException: Akan dilempar jika WebDriverWait menunggu elemen muncul lebih lama dari batas waktu yang ditentukan.
Kita impor ini agar bisa menangani error ini secara spesifik dalam kode kita (misalnya, jika tombol login tidak muncul, lakukan hal lain).
from selenium.webdriver.support.ui import WebDriverWait
Maksud: Mengambil kelas WebDriverWait.
Fungsi: WebDriverWait digunakan untuk membuat skrip menunggu (wait) sampai suatu kondisi terpenuhi sebelum melanjutkan eksekusi. Ini sangat penting untuk scraping yang stabil, karena elemen bisa muncul dengan delay. Misalnya, menunggu field password benar-benar muncul sebelum diisi.
from selenium.webdriver.support import expected_conditions as EC
Maksud: Mengambil modul expected_conditions dan memberinya alias EC.
Fungsi: EC berisi daftar kondisi umum yang digunakan bersama WebDriverWait. Contoh: EC.presence_of_element_located (menunggu elemen muncul di DOM). EC ini adalah argumen untuk WebDriverWait.
from selenium.webdriver.chrome.service import Service as ChromeService
Maksud: Mengambil kelas Service dari modul selenium.webdriver.chrome.service dan memberinya alias ChromeService.
Fungsi: ChromeService digunakan untuk mengelola file driver Chrome secara manual. Biasanya digunakan bersama webdriver_manager (lihat baris berikutnya) untuk menginisiasi driver.
from webdriver_manager.chrome import ChromeDriverManager
Maksud: Mengambil kelas ChromeDriverManager.
Fungsi: ChromeDriverManager digunakan untuk mengunduh dan mengelola file driver Chrome yang diperlukan oleh Selenium. Ini menghindari kamu dari harus download dan setting path driver secara manual.
import undetected_chromedriver as uc
Maksud: Mengimpor seluruh library undetected_chromedriver dan memberinya alias uc.
Fungsi: Ini adalah versi khusus dari selenium.webdriver.Chrome yang dirancang untuk menghindari deteksi bot oleh situs web seperti X/Twitter. Kita akan menggunakannya untuk membuat objek driver yang lebih "manusiawi".
import time
Maksud: Mengimpor modul bawaan Python time.
Fungsi: Digunakan untuk memberi jeda (time.sleep()) dalam eksekusi skrip. Misalnya, memberi jeda 5 detik agar halaman termuat sebelum mencari elemen. Catatan: time.sleep() adalah cara "kasar" untuk menunggu, WebDriverWait lebih baik.
import json
Maksud: Mengimpor modul bawaan Python json.
Fungsi: Digunakan untuk membaca dan menulis file dalam format JSON. Di kode kamu, digunakan untuk membaca file login.json yang berisi email, username, dan password.
import csv
Maksud: Mengimpor modul bawaan Python csv.
Fungsi: Digunakan untuk membaca dan menulis file dalam format CSV (Comma-Separated Values), seperti spreadsheet sederhana. Di kode kamu, digunakan untuk menyimpan data tweet yang di-scrape ke file .csv.
import os
Maksud: Mengimpor modul bawaan Python os.
Fungsi: Digunakan untuk berinteraksi dengan sistem operasi, seperti mengakses file dan folder. Di kode kamu, digunakan untuk mengecek apakah file CSV sudah ada sebelum menyimpan data baru (untuk mencegah duplikat)