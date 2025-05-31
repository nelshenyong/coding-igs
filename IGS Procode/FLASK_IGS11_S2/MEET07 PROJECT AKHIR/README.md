![alt text](https://github.com/nelshenyong/coding-igs/blob/main/IGS%20Procode/FLASK_IGS11_S2/MEET07%20PROJECT%20AKHIR/preview.png?raw=true)

# Buddhist Wisdom Hub

Aplikasi web yang menyediakan koleksi kutipan Buddha dan paritta.

## Fitur

- Koleksi kutipan Buddha yang menginspirasi
- Perpustakaan paritta (mantra pelindung)
- Sistem autentikasi pengguna
- Panel admin untuk mengelola konten
- Desain responsif

## Teknologi yang Digunakan

- Python 3.x
- Flask
- SQLite
- Bootstrap 5
- Font Awesome

## Instalasi

1. Clone repositori ini:

```bash
git clone https://github.com/username/buddhist-wisdom-hub.git
cd buddhist-wisdom-hub
```

2. Buat dan aktifkan virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependensi:

```bash
pip install -r requirements.txt
```

4. Jalankan aplikasi:

```bash
python app.py
```

5. Buka browser dan akses `http://localhost:5000`

## Penggunaan

### Pengguna Biasa

- Melihat koleksi kutipan dan paritta
- Mendaftar dan login ke akun
- Mengedit profil

### Admin

- Menambah, mengedit, dan menghapus kutipan
- Menambah, mengedit, dan menghapus paritta
- Mengelola pengguna
- Mengatur hak akses

## Struktur Proyek

```
buddhist-wisdom-hub/
├── app.py              # File utama aplikasi
├── requirements.txt    # Daftar dependensi
├── static/            # File statis (CSS, gambar)
│   └── style.css
└── templates/         # Template HTML
    ├── base.html
    ├── home.html
    ├── login.html
    ├── register.html
    ├── quotes.html
    ├── parittas.html
    ├── add_quote.html
    ├── add_paritta.html
    ├── edit_quote.html
    ├── edit_paritta.html
    ├── edit_profile.html
    └── manage_users.html
```

## Kontak

Nelshen Yong - [@nelshen.yong](https://instagram.com/nelshen.yong)
