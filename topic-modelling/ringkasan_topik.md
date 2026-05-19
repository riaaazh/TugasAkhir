# Analisis dan Interpretasi Topik LDA

## Informasi Umum Model

| Komponen             | Hasil                                  |
| -------------------- | -------------------------------------- |
| Metode               | Latent Dirichlet Allocation (LDA)      |
| Data yang digunakan  | Tweet sentimen negatif terhadap DPR RI |
| Jumlah topik terbaik | 6 topik                                |
| Metode evaluasi      | Coherence Score (C_v)                  |
| Best Coherence Score | 0.3944                                 |

data negative dan topiknya:
[Data Tweet Negatif dan Topik](https://docs.google.com/spreadsheets/d/1WypPd2rzG8zVN7UGnV8t0hNSsckgWu2Z2L6XaMeum9g/edit?usp=sharing)
---
---
# Topik 1 - Pembahasan Kebijakan, Komisi, dan Sidang DPR

## Kata Dominan
`komisi, terkait, sidang, pembahasan, ruang, pks, jakarta, pimpinan, jabatan, pemerintah`

## Interpretasi Awal
Topik ini berkaitan dengan aktivitas internal DPR seperti:

* sidang
* pembahasan kebijakan
* rapat komisi
* pimpinan DPR
* dinamika ruang sidang

Topik ini menunjukkan percakapan publik mengenai proses kerja formal DPR dalam pembahasan isu tertentu.

## Validasi Manual Tweet

### Langkah Validasi
* Filter `dominant_topic = 1`
* Baca teks tweetnya
* Identifikasi pola pembahasan dominan

### Hasil Pengamatan
Mayoritas tweet membahas:

* sidang DPR
* pembahasan komisi
* rapat internal
* pimpinan DPR
* kebijakan pemerintah

### 10 Contoh Tweet
| No   | Teks Tweet  |
|------|-------------|
| 125  | banyak anggota dpr tak hadiri rapat paripurna kamis lalu cuma disuruh datang duduk dengar diam dan duit saja kok susah            |
| 416  | mungkin harus punya komisi khusus induk untuk para ulama agamawan jadi semua kebijakan harus ada persetujuan dari komisi ini cc   |
| 603  | dikata RDP di bareskrim apa ini anggota DPR ? lagi reses apa pegimana ?                                                           |
| 840  | membolos anggota di sidang paripurna pengesahan UU APBN takpatutdicontoh                                                          |
| 852  | detik paripurna pengesahan UU APBN anggota DPR tak hadir tetapi pantauan di dalam ruang newstoday                                 |
| 6289 | coba kasih solusi dong kebijakan apa yang harus diambil untuk mengurangi utang ? jangan bisanya cuma pada protes                  |
| 3844 | terkait RUU KEJAHATAN SEKSUAL HARUSNY harus secepatny meng golkanny anda semua kan juga punya anak DPR takut ?                    |
| 10006| ini aturan dan undang undang ada yang ditabrak nggak ? jika ada kok parlemen diam ? bung bang bagaimana ini ?                     |
| 12036| mantan ketua FPI di cipete jaksel melakukan pelecehan seksual anak PR di bawah umur ? mana suaranya ? sampai kapan menunda pengesahan RUU TPKS ? diam itu emas ? PKS GOLKAR terus menghambat pengesahan RUU TPKS ?                                                                                   |
| 12650 | ? ? sorry sangat sangat bitter dengan ini orang dan penyembahnya yang sahkan kalian juga sih dewan yang konon wakil rakyat entah rakyat yang mana maaf oot please banget sahkan RUU perampasan aset please please please dari jaman kapan memohon                                                     |

### Kesimpulan Topik
Interpretasi Topik 1 dinilai sesuai karena kata dominan konsisten dengan isi tweet yang membahas RUU, aktivitas sidang, dan komisi DPR.

<span style="color:brown">**Topik 1 lebih bersifat Prosedural-Struktural (Membahas alur jalannya sidang, rapat komisi, dan rancangan undang-undang).**</span>

**catatan**
- ada beberapa tweet yang sebenarnya lebih ke pelaporan atau informasi kegiatan/agenda
- kata terkait biasanya dihubungkan dengan pembahasan RUU
- kata ruang, lebih banyak dikaitkan dengan kehadiran anggota pada ruang persidangan
- kata jakarta, menginformasikan lokasi sidang
---

# Topik 2 - Kritik terhadap Kebijakan dan Representasi Wakil Rakyat

## Kata Dominan
`kebijakan, rakyat, negara, wakil_rakyat, masyarakat, undang_undang, ppn, pemerintah, orang, presiden`

## Interpretasi Awal
Topik ini menggambarkan opini publik terkait:

* kebijakan pemerintah
* dampak kebijakan terhadap rakyat
* peran DPR sebagai wakil rakyat
* isu undang-undang dan PPN

Topik ini cenderung menunjukkan kritik masyarakat terhadap kebijakan yang dianggap tidak berpihak kepada rakyat.

## Validasi Manual Tweet

### Langkah Validasi
* Filter `dominant_topic = 2`
* Baca teks tweetnya
* Cari pola pembahasan dominan

### Hasil Pengamatan
Mayoritas tweet membahas:

* kebijakan pemerintah
* rakyat dan kesejahteraan
* kritik terhadap DPR
* kebijakan pajak/PPN
* hubungan DPR dan pemerintah

### 10 Contoh Tweet
| No   | Teks Tweet |
|------|------------|
| 4496 | Coba DPR RI buat RUU korupsi yah biar negara ini aman dari antek korupsi yang buat negara ini bangkrut yang pada susah mah rakyat kecil aja semuanya yang diambil buat korupsi uang rakyat juga terus buat rakyat bisa nikmati apa                                                                            |
| 5114 | kebijakan pemerinta yang tak memikirkan rakyat senaknya sendiri dari garam sampai BBM listrik rokok sembako semuanya mahal tanpa subs      |
| 8776 | pak polisi tolong ada banyak orang hilang di anggota DPR ini cuma ada kursi doang orang orangnya tidak tahu pada ke mana                                                                                                                                                |
| 11967| Luar biasa aset koruptor mau di ambil lewat RUU malah di tolak Berarti lebih banyak wakil Koruptor di banding wakil rakyat Di pilih oleh rakyat dan di gaji oleh rakyat dan membela perampok uang rakyat                                                                                                        |
| 12389| sudah seperti kitab suci saja kau buat itu barang bisa dinaikkan bisa diturunkan hingga dan bisa ditunda itu amanat undang undang ! dasar wakil rakyat yang tidak mewakili rakyat kalian tidak berguna dan hanya menjadi beban masyarakat !                                                                     |
| 12542| siapapun yang terlibat dan menyetujui kenaikan pajak adalah orang orang jahanam dan keji kepada masyarakat harusnya sebagai wakil rakyat dalam memilih kebijakan yang baik tapi malah ingin menyengsarakan masyarakat kalian semua menjijikan?                                                             |
| 12635| omong kosong jika kader PDIP teriak soal kenaikan PPN hari ini bapak prabowo hanya meneruskan kebijakan yang diketok palu oleh DPR RI periode diparlemen itu banyak PDIP seharusnya teriak sebelum UU APBN diberlakukan                                                                                          |
| 12664| pak tolong kabarin teman separtainya yang di dpr lah jangan manutan sangat sama kebijakan tidak bijak wakil rakyat apa wakil kaum elit pajakmencekik tolakppnpersen sampaimenang tolakppnpersen                                                                                                          |
| 13000| pada kenyataanya undang undang atau peraturan pemerintah di negara ini dibuat hanya untuk mensejahterakan dan melindungi pejabat wakil rakyat bukan rakyat itu sendiri                                                                                                                                             |
| 13083| RUU PPRT diajukan dari tidak maju maju memang pemerintah wakil rakyat kita tidak peduli sama nasib masyarakat rentan                       |

### Kesimpulan Topik
Interpretasi Topik 2 dinilai sesuai karena isi tweet konsisten membahas kritik terhadap kebijakan dan representasi rakyat.

<span style="color:brown">**Topik 2 lebih bersifat Substantif-Sentimen (Membahas reaksi, dampak riil di masyarakat, serta konflik moral antara rakyat kecil dengan penguasa).**</span>

**catatan**
- ada beberapa tweet yang membahas kebijakan pemerintah (jadi tidak spesifik ke kebijakan yang disahkan sama DPR)
- ada beberapa tweet yang menyerang personal anggota DPR
---

# Topik 3 - Kritik terhadap Politik Partai dan Proses Legislasi DPR

## Kata Dominan
`undang_undang, partai, pengesahan, wakil_rakyat, presiden, menolak, pemerintah, setuju, ketua, perampasan_aset`

## Interpretasi Awal
Topik ini berkaitan dengan:

* proses pengesahan undang-undang
* dinamika politik partai
* dukungan dan penolakan kebijakan
* isu perampasan aset
* hubungan DPR dan presiden

## Validasi Manual Tweet

### Langkah Validasi
* Filter `dominant_topic = 3`
* Baca teks tweetnya
* Cari pola pembahasan dominan

### Hasil Pengamatan
Mayoritas tweet membahas:

* pengesahan RUU
* penolakan kebijakan
* partai politik
* keputusan DPR
* kontroversi regulasi

### 10 Contoh Tweet
| No   | Teks Tweet |
|------|------------|
|  831 | ketika metro tv menyiarkan sidang pleno DPR pengesahan RAPBN malu dan terkejut hampir kosong ruang sidang kapan wakil rakyat berubah ?|
| 4946 | pengesahan perpu ormas jadi UU menjadi bukti bahwa sebagian besar mereka bukanlah wakil rakyat tetapi wakil penguasa ! ! astaghfirullah|
| 6479 | DPR sebagai wakil rakyat harusnya memperjuangkan aspirasi rakyat bukan membawa suara partainya yang kadang bertentangan dengan suara rakyat banyak|
| 8586 | tidak semua wakil rakyat paham undang undang regulasi yang dia pahami persoalan undang undang pokok dia tidak paham materi undang undang yang dulu dan agreement saat itu yang diteken ginanjar KS dan undang undang minerba yang sekarang tidak bisa hentikan kontrak karya dengan konsesi tsbt|
| 12132| bagaimana ini wakil rakyat kok menolak RUU perampasan aset koruptor pengambian kembali uang rakyat yang diambil para koruptor ini bukti para wakil rakyat tidak mewakili rakyat tetapi mewakili para koleganya para koruptor duh gemas pengin tak ciweli tak pecuti karo peneba siji|
|12287 | RUU perampasan aset untuk miskinkan dan YANG DITAKUTI KORUPTOR mandeg di menunggu diperintah JURAGAN seperti kata bambang pacul siap ! ! jika diperintah JURAGAN katanya wakil rakyat eh malah TANPA SENGAJA jadi WAKIL JURAGAN emprof emprof emprof|
| 12611| oalah partai banteng juga banyak koruptornya ya ? ! makanya RUU perampasan asset tidak segera disahkan oleh DPR RI selama ketua DPR nya dari katanya RUU itu selamanya akan jadi RUU|
|12753 | tidak setuju selagi anggota DPR masih terafiliasi partai demokrasi tidak akan sehat karena masih banyak kongkalikong di balik kebijakan|
|12955 | JIKA PENGESAHAN UU PERAMPASAN ASET HARUS TANYA DULU KEPADA KETUA UMUM PARTAINYA MASING MASING TERUS APA FUNGSI NYA MONYET MOYET DI PARLEMEN ? ? ! ! CUMA JADI WAYANG SIH KETUA UMUM ? ? ! ! BUBARKAN SAJA PARLEMEN ! ! BUKAN WAKIL RAKYAT KOK ! !|
|13088 | selaku wakil rakyat jika niat membuka pintu untuk rakyat janganlah setengah hati supaya info aspirasi rakyat bisa sampai kepada kalian wakil rakyat shg kalian dengar dan cermati dengan baik tidak perlu menunggu rakyat bikin demo DPR hebat jika selalu dekat dengan rakyat|

### Kesimpulan Topik
Interpretasi Topik 3 sesuai karena tweet didominasi pembahasan politik legislasi dan pengesahan undang-undang.

<span style="color:brown">**Topik 3 (Institusional-Akuntabilitas Politik): Fokus pada kritik terhadap bobroknya performa legislasi, dominasi kepentingan partai politik di parlemen, dan desakan pengesahan UU Perampasan Aset.**</span>

**catatan**
- lumayan banyak membahas UU Perampasan Aset
- lebih banyak membahas tentang produk hukum/kebijakan
- terdapat tweet yang 1 teks di dominasi kata kasar
---

# Topik 4 - Reses dan Aktivitas Kelembagaan DPR

## Kata Dominan
`reses, komisi, gedung, indonesia, mkd, dibahas, wakil_ketua, kota, aneh, news`

## Interpretasi Awal
Topik ini berkaitan dengan:

* kegiatan reses DPR
* aktivitas kelembagaan
* MKD (Mahkamah Kehormatan Dewan)
* isu yang dibahas di lingkungan DPR

## Validasi Manual Tweet

### Langkah Validasi
* Filter `dominant_topic = 4`
* Baca teks tweetnya
* Cari pola pembahasan dominan

### Hasil Pengamatan
Mayoritas tweet membahas:

* kegiatan reses
* anggota DPR
* aktivitas gedung DPR
* pemberitaan politik
* pembahasan internal DPR

### 10 Contoh Tweet
| No   | Teks Tweet |
|------|------------|
|  89  | mengharukan wakil rakyat terlalu banyak waktunya untuk update disosmed hampir tidak ada waktu untuk update aspirasi rakyat yang diwakilinya|
| 1499 | kira berapa ya biaya anggaran komisi dpr ri bahas ruu pemilu yang tak bermutu untuk mengizinkan napi atau ekx penjahat jadi balon kdh nasib|
| 6181 | kita semua berkepentingan pertanyaannya apakah kepentingan kita sama molornya RUU pemilu ANTI TERORISME tidak menjadikan indonesia lebih baik|
| 6833 | lagi menunggu gedung DPR kena bom kali baru mau dikelarin tuh RUU|
| 8559 | makin marak saja kasus seperti begini dan komisi VII masih saja lamban menuntaskan RUU penghapusan kekerasan seksual ayo dong DPR kerja yang benar jangan cuma asik ngetwit saja|
| 8649 | parah mereka doyan jalan jalan habisi uang reses|
| 9055 | kenapa sih kinerja DPR RI dalam membuat UU rendah banget ? apa benar itu karena reses ? tetapi reses itu kan hal baik pertanyaannya mereka betulan melakukan reses nggak ? untuk lengkapnya masuk saja ke tautan ini PSI psibersihbersihdpr dedekuki|
| 10176|indonesia ini sudah teramat sangat tertinggal dari negara lain semestinya DPR cepat tanggap untuk bisa segera mengesyahkan RUU penyiaran entah sampai kapan RUU ini mangkrak di BALEG ? ? menyedihkan|
| 10650| itu bukan kebijakan itu perintah UU yang notabene produk DPR sebagai anggota DPR kok anda kontra dengan UU sendiri disini siapa yang aneh ! perihal buang sampah itukan bersifat umum tidak hanya bu tetapi semua rakyat harus jaga kebersihan|
| 12404| apakah institusi ini diisi para badut ? apakah mewakili aspirasi rakyat harus dipanggil seperti gini ? sudah se aneh itukah kita ?|

### Kesimpulan Topik
Interpretasi Topik 4 sesuai karena isi tweet dominan membahas aktivitas kelembagaan dan reses DPR.

<span style="color:brown">**Topik 4 Fokus pada aspek Akuntabilitas-Perilaku (Kritik terhadap moralitas kerja anggota dewan, isu bolos sidang, dan penyalahgunaan dana reses).**</span>

**catatan**
- beberapa tweet yang ada kata "wakil_ketua", lebih menjelaskan mengenai kebijakan atau kegiatan yang dilakukan oleh wakil ketua dpr
- lebih banyak membahas tentang pengawasan anggaran, terkhusus anggaran reses
---

# Topik 5 - Aspirasi Rakyat dan Fungsi Perwakilan DPR

## Kata Dominan
`wakil_rakyat, rakyat, aspirasi_rakyat, daerah, kebijakan, sih, parlemen, partai, reses, fungsi`

## Interpretasi Awal
Topik ini menggambarkan:

* fungsi DPR sebagai wakil rakyat
* penyampaian aspirasi masyarakat
* hubungan DPR dengan daerah
* kritik terhadap fungsi parlemen

## Validasi Manual Tweet

### Langkah Validasi
* Filter `dominant_topic = 5`
* Baca teks tweetnya
* Cari pola pembahasan dominan

### Hasil Pengamatan
Mayoritas tweet membahas:

* aspirasi rakyat
* fungsi DPR
* wakil rakyat
* kepentingan masyarakat
* kritik terhadap parlemen

### 10 Contoh Tweet
| No   | Teks Tweet |
|------|------------|
|  656 | kita semua berkepentingan pertanyaannya apakah kepentingan kita sama molornya RUU pemilu ANTI TERORISME tidak menjadikan indonesia lebih baik|
| 982  | kenapa para wakil rakyat diam saja ? mana tanggung jawab mereka yang tlh dipilh rakyat kamu mewakili menyuarakn aspirasi rakyat|
| 3626 | wakil rakyat harus nya mewakili aspirasi rakyat laah iya lah wong mereka wakil kok rakyat yang jadi ketua nya doong ? ? tanyakenapa|
| 5089 | halo kalian lagi reses ya enaknya jika gaji dari uang rakyat kerja tidak duit ambil semua banyak omong jika bela setnov|
| 5406 | indonesia lucu ya bathin rakyat diharuskan memaklumi KEBIJAKAN yang sudah dibuat sementara wakil rakyat nya pada asyik saling nyinyir|
| 10657| tugas wakil rakyat itu berjuang di parlemen pantesan di rapat pembahasan rapat paripurna banyak anggota DPR yang bolos karena mungkin merasa cukup dengan ngetwit yang tidak ada bedanya dengan buzzer|
| 12373| sesungguhnya angota DPR dipilih untuk menyuarakan suara rakyat tetapi kenyataan banyak anggota DPR yang tuli atau pura tuli terhadap keresahan rakyat akan suatu kebijakan tetapi jika anggota parlemen tlh menyuarankan rakyat kemudian dipermasalahkan artinya kezoliman tlh sdng terjadi|
| 12744| fungsi kontrol parlemen berjalan lah sini parlemen mbebek ke presiden sampai pengesahan UU bisa diatur bareng bareng yang katanya wakil rakyat malah nyusahkanbrakyat tetapi balik lagi mayoritas rakyatnya masih mau|
| 13023| karena yang katanya wakil rakyat hampir tidak pernah bisa menyampaikan aspirasi rakyat melainkan lebih sering kepentingan kelompoknya sendiri|
|13180 |yang katanya wakil rakyat rakyat sudah bersuara malah mereka abaikan jadi apa fungsi mereka ? dapat kucuran duit berapa dari sih begundal ? demi duit mereka bodo sangat sama aspirasi rakyat yang mereka wakili|

### Kesimpulan Topik
Interpretasi Topik 5 sesuai karena isi tweet dominan membahas representasi rakyat dan fungsi DPR.

<span style="color:brown">**Topik 5 (Komunikasi-Representasi): Bagaimana kegagalan DPR dalam menyerap dan menyalurkan aspirasi rakyat secara konstitusional.**</span>

**catatan**
- banyak tweet yang fokus pada gugatan publik terhadap fungsi esensial DPR sebagai penyambung lidah rakyat.
- intinya lebih membahas ke fungsi perwakilan dpr yang tidak mewakili
---

# Topik 6 - Korupsi dan Kritik terhadap Elite Politik

## Kata Dominan
`koruptor, rakyat, korupsi, bikin, kebijakan, undang_undang, perampasan_aset, presiden, negeri, jokowi`

## Interpretasi Awal
Topik ini berkaitan dengan:

* isu korupsi
* kritik terhadap elite politik
* perampasan aset koruptor
* kebijakan pemerintah
* kekecewaan publik terhadap pejabat negara

## Validasi Manual Tweet

### Langkah Validasi
* Filter `dominant_topic = 6`
* Baca teks tweetnya
* Cari pola pembahasan dominan

### Hasil Pengamatan
Mayoritas tweet membahas:

* korupsi
* koruptor
* kebijakan hukum
* hukuman bagi koruptor
* kritik terhadap pemerintah dan DPR

### 10 Contoh Tweet
| No   | Teks Tweet |
|------|------------|
| 8663 | TIDAK USAH BERDEBAT TIDAK PENTING YANG LEBIH PENTING anda DAN ANGGOTA SEGERA MEMBUAT RUU HUKUMAN MATI BAGI TERSANGKA KORUPTOR SIAPA PUN YANG TERBUKTI KORUPSI MAKA HARUS DI HUKUM MATI pasti tidak berani jokowisertifikasitanahmadura prabowo|
| 8746 | mestinya ada RUU untuk para oknum koruptor kenapa para wakil rakyat tidak bisa buat RUU untuk para koruptor buat RUU hukuman mati hukuman seumur hidup bisa juga aset harta uangnya sita buat negara|
| 9237 | JIKA MENGHARGAI JASA PARA PAHLAWAN ANGGOTA TOLONG DONG BUAT RUU HUKUMAN MATI BAGI TERSANGKA KORUPTOR BERAPA TRILIUN UANG RAKYAT YANG DI RAMPOK PARA KORUPTOR JANGAN HANYA JAGOAN BERDEBAT DEMI UNTUK PARTAINYA SAJA haripahlawan jangansuriahkanindonesia|
| 9286 | WAHAI WAKIL RAKYAT BERSERIUSLAH UNTUK MEMBERANTAS KORUPSI KITA RAKYAT INDONESIA JANGAN DI BODOHI TERUS BAGAIMANA indonesia HUTANGNYA BISA LUNAS jika PARA PEJABAT BANYAK YANG KORUPTOR BUATLAH RUU HUKUMAN MATI BAGI TERSANGKA KORUPTOR|
| 9881 | sudah tidak menjadi rahasia publik banyak anggota DPR sudah menyalahfungsikan tugasnya bukan MENIMBUN ASPIRASI rakyat malah MENIMBUN UANG rakyat stlah menimbun duit perlemah pula KPK lebih eksisnya lagi korupsinya berjemaah perlemah KPK sama dengan menyiram pupuk buat koruptor|
| 10152| dia juga seorang LEGISLATIF banyak RUU yang tidak selesai dan buanyak pula anggota DPR yang suka bolos kerja sebagai salah satu pimpinan DPR dia mengapai ? ?|
| 10212|semangkin tidak jelas kepribadian pola pikirnya katanya anggota DPR yang harus bisa menjaga marwah dan wibawa negara tetapi ada orang mau bikin ribut dia bela matian demi kelompokknya yang lain adalah musuh dan lucunya lagi hukum kebijakan akulah kendalinya|
| 11466| berani tidak ya yang namanya wakil rakyat membuat merevisi undang undang yang memberikan hukuman berat kepada koruptor ?|
| 12285| perjuangan mendesak wakil rakyat untuk segera mengesahkan RUU perampasan aset koruptor tidak akan pernah berhenti hukuman penjara jelas tidak bikin koruptor jera perlu hukuman lain yang bikin mereka ketakutan yaitu dimiskinkan tangkap koruptor ! sita aset asetnya ! itu baru|
| 12433| tau deh jadi anggota dpr juga tidak mampu menyuarakan dan memperjuangkan suara rakyat sampai mahasiswa harus selalu turun ke jalan gara kebijakan ngawur|

### Kesimpulan Topik
Interpretasi Topik 6 sesuai karena tweet secara dominan membahas isu korupsi dan kritik terhadap elite politik.

<span style="color:brown">**Topik 6 (Yudisial-Hukum): Kemarahan moral publik yang menuntut hukuman mati koruptor dan penolakan terhadap pelonggaran hukuman tipikor.**</span>

**catatan**
- di topik 6 ini banyak sekali didominasi oleh desakan radikal dari netizen yang sudah jenuh dengan korupsi massal (inti tweetnya kebanyakan tentang korupsi/hukuman koruptor)
- mayoritas tweet memang membahas tentang uu hukuman para koruptor