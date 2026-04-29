22 April 2026
**update**
updatenya adalah, awalnya di ground truth itu langsung ke label kategori (positive, neutral, negative), namun sekarang berubah menjadi angka numerik (mean dari penilaian annotator dengan setiap sentimen dinilai berdasarkan skala -4 sampai +4 dari 5 annotator) sesuai dengan format vader, yang awalnya hanya ada 1 annotator, sekarang ada 5 annotator.

- menyatukan semua penilaian dari masing-masing annotator menjadi 1 file (ada 2 file, untuk versi angkanya aja ada di "combined_annotations", untuk yang lengkap dengan teksnya dan juga konsensus, gt scaled, serta std ada di file "ground_truth_final")

23 April 2026
- memastikan format ground truthnya sudah benar
- Melakukan perbaikan untuk semua baris kode, dikarenakan ada perubahan format pada ground truth

