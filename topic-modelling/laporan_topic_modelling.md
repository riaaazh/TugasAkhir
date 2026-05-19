Total distribusi negatif adalah 4.854, kemudian karena ada preprocessing ulang dan melihat kembali data yang bisa dilanjutkan ke pemodelan topik, sehinggan **total data yang bisa digunakan pada pemodelan topik adalah sebesar: 4378**

kemudian dilakukan penentuan sendiri untuk pencarian rentang kandidat jumlah topik (candidate topic range), yaitu k = 2, 3, 4, 5, 6, 7. lalu didapatkan **jumlah topik optimal (optimal number of topics) yaitu k = 6**, karena menghasilkan **coherence score tertinggi (0.3944)**. Maka **model LDA final dilatih ulang khusus dengan 6 topik**, bukan 7, bukan 2.

----
input: 4378 dokumen atau data

analisis kata dominan per topik dari "lda_topics_keywords.csv"
-> melihat 10 kata dengan probabilitas tertinggi di masing-masing topic
Pemilihan 10 kata teratas didasarkan pada konvensi yang sudah mapan dalam literatur topic modeling, mengikuti standar yang ditetapkan sejak paper seminal LDA oleh Blei et al. (2003).


**PENDETAILAN ANALISIS PER TOPIK**
**Topik 1, 795 tweet, 18.2%**
- Kritik kebijakan teknis dan komisi sektoral -
Sentimen negatif terhadap kebijakan spesifik (bebaas visa, terorisme, batas laut) yang dibahas di level komisi DPR

kata katanya: komisi, sidang, pembahasan, terkait, ruang, pks, jakarta, jabatan, pimpinan, pemerintah

<kesimpulan>
Kritik Kebijakan Sektoral DPR
atau Proses Legislasi dan Kerja Komisi


**Topik 2, 1.020 tweet, proporsi dokumen: 23.3%** (terbesar)
- Kegagalan DPR merespons kebijakan yang menyengsarakan rakyat -
Topik terbesar fokus pada kebijakan umum (pajak, UU, PPN) yang dinilai merugikan masyarakat, DPR dianggap diam atau berpihak ke pemerintah

kata katanya: kebijakan, rakyat, negara, ppn, wakil_rakyat, masyakat, undang_undang, presiden, orang, pemerintah

<kesimpulan>
Kegagalan Responsivitas Kebijakan
atau Kebijakan Publik dan Dampak Sosial

**Topik 3, 613 tweet, proporsi dokumen: 14.0%**
- Penolakan publik terhadap pengesahan undang-undang kontroversial -
Pengesahan UU yang dinilai terburu-buru, tanpa persetujuan rakyat, termasuk sinyal terkait RUU perampasan aset

kata-katanya: undang_undang, pengesahan, menolak, perampasan_aset, partai, presiden, wakil_rakyat, pemerintah, setuju, ketua

<kesimpulan>
Penolakan Pengesahan Undang-Undang
atau Politik Pengesahan UU

**Topik 4, 767 tweet, proporsi dokumen: 17.5%**
- Aktivitas reses yang dipertanyakan dan integritas kelembagaan - 
Kritik terhadap reses yang dianggap seremonial, kinerja MKD, serta kehadiran anggota di gedung DPR yang disorot

kata-katanya: reses, mkd, gedung, aceh, komisi, indonesia, dibahas, wakil_ketua, kota, news

"note: kata 'news' muncul di sini, kemungkinan noise dari judul berita yang ikut terindeks"

<kesimpulan>
Persoalan Kinerja dan Integritas Kelembagaan
atau Aktivitas Reses dan Sorotan Media

**Topik 5, 745 tweet, proporsi dokumen: 17.0%**
- Krisis fungsi representasi dan aspirasi rakyat yang diabaikan - 
DPR dinilai gagal menyerap aspirasi rakyat di daerah, reses tidak bermakna, dan fungsi parlemen sebagi wakil rakyat diragukan

kata-katanya: wakil_rakyat, aspirasi_rakyat, fungsi, parlemen, rakyat, daerah, kebijakan, reses, partai, dewan_perwakilan_rakyat

<kesimpulan>
Krisis Fungsi Representasi Rakyat 
atau Fungsi Representasi dan Aspirasi


**Topik 6, 438 tweet, proporsi dokumen: 10.0%**
- Korupsi legislatif dan tuntutan pemidanaan koruptor - 
Topik paling spesifik dan keras, tuntutan hukum seumur hidup untuk koruptor, dikaitkan langsung dengan DPR dan jokowi

kata-katanya: koruptor, korupsi, perampasan_aset, seumur_hidup, rakyat, bikin, undang_undang, presiden, negeri, jokowi

"note: nama 'jokowi' muncul, ini bisa jadi penting untuk interpretasi konteks temporal data (masa pemerintahan mana)

<kesimpulan>
Tuntutan Pemberantasan Korupsi Legislatif
atau Korupsi dan Akuntabilitas


--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
Topik 2 adalah yang paling dominan (23,3%). Publik paling banyak membahas kegagalan DPR dalam merespons kebijakan ekonomi yang dianggap menyengsarakan rakyat, khususnya soal PPN dan regulasi berbasis undang-undang.
---

Topik 3 dan 6 saling melengkapi, keduanya sama-sama menyentuh isu legislasi, tapi dari sudut berbeda. Topik 3 soal proses pengesahan UU yang ditolak publik, sedangkan Topik 6 lebih ke tuntutan hukum terhadap koruptor di lingkaran DPR. Ini bisa dijadikan satu klaster temuan: "kegagalan integritas legislatif."
---

Topik 4, ada kata "news" yang kemungkinan adalah noise dari judul berita yang ikut masuk ke corpus. Ini bukan kesalahan besar, tapi harus dimasukkan skripsi sebagai keterbatasan preprocessing.
---

Soal nama "jokowi" di Topik 6, ini sinyal konteks temporal yang penting. Pada dataku mencakup era pemerintahan Jokowi, maka wajar sih. Tapi perlu disebut bahwa ini saat interpretasi agar reviewer tahu kalau aku sadar data ini terikat periode tertentu.



**ANALISIS MENDALAM TOPIK 2, KARENA YANG DOMINAN ATAU BESAR (23.3%)**
Kebijakan yang paling sering di kritik
