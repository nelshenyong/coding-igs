# Kalkulator Fisika

Aplikasi kalkulator fisika berbasis JavaFX yang dapat menghitung berbagai rumus fisika dan memberikan informasi tentang konsep-konsep fisika.

## Fitur

- **Perhitungan Fisika**:

  - Gaya Gravitasi
  - Energi Kinetik
  - Energi Potensial
  - Hukum Ohm
  - Daya Listrik
  - Frekuensi

- **Informasi Konsep**:
  - Penjelasan detail setiap konsep fisika
  - Rumus yang digunakan
  - Satuan dan variabel yang terlibat

## Persyaratan Sistem

- Java Development Kit (JDK) 17 atau lebih baru
- JavaFX 17 atau lebih baru
- Sistem operasi: Windows/Linux/MacOS

## Cara Menjalankan Aplikasi

### Menggunakan Script (Direkomendasikan)

1. Buka terminal di folder proyek
2. Jalankan script:
   ```bash
   ./run.sh
   ```

### Cara Manual

1. Buka terminal di folder `src`
2. Compile program:
   ```bash
   javac --module-path /usr/share/openjfx/lib --add-modules javafx.controls,javafx.fxml App.java Controller.java
   ```
3. Jalankan aplikasi:
   ```bash
   java --module-path /usr/share/openjfx/lib --add-modules javafx.controls,javafx.fxml App
   ```

## Struktur Proyek

```
REMED/APP/
├── src/
│   ├── App.java              # Main class aplikasi
│   ├── Controller.java       # Controller untuk GUI
│   └── main.fxml            # File FXML untuk layout GUI
├── run.sh                   # Script untuk menjalankan aplikasi
└── README.md               # Dokumentasi proyek
```

## Cara Penggunaan

1. Pilih topik fisika dari dropdown menu
2. Masukkan nilai-nilai yang diperlukan
3. Klik tombol "Hitung"
4. Hasil perhitungan akan muncul di area hasil
5. Informasi tentang konsep fisika dapat dilihat di bagian bawah
