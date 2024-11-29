# Pengaturan layar
WIDTH = 1000  # Lebar layar
HEIGHT = 1000  # Tinggi layar
GRID_SIZE = 20  # Ukuran kotak grid (untuk pergerakan ular)
FPS = 20 # Frame per detik (kecepatan game)

# Informasi game
GAME_TITLE = "SNAKE GAME"  # Judul game
GAME_SUBTITLE = "Classic Arcade Game"  # Subjudul
CREATOR_NAME = "Nelshen Yong"  # Nama pembuat
YEAR = "2024"  # Tahun pembuatan

# Warna (dalam format RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRID_COLOR = (50, 50, 50)
BACKGROUND_COLOR = BLACK
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
SCORE_COLOR = WHITE
MENU_TEXT_COLOR = WHITE
GAME_OVER_TEXT_COLOR = (255, 0, 0)
TITLE_COLOR = (0, 255, 0)
SUBTITLE_COLOR = (0, 200, 0)
CREDIT_COLOR = (200, 200, 200)

# Pengaturan font
TITLE_FONT_SIZE = 72  # Ukuran font untuk judul
CREDIT_FONT_SIZE = 24  # Ukuran font untuk kredit
SCORE_FONT_SIZE = 36  # Ukuran font untuk skor
MENU_FONT_SIZE = 36  # Ukuran font untuk menu
MUTE_BUTTON_FONT_SIZE = 24  # Ukuran font untuk tombol mute

# Pengaturan ular
INITIAL_LENGTH = 2  # Panjang awal ular
SNAKE_SPEED = 1  # Kecepatan gerak ular
SNAKE_SIZE = GRID_SIZE  # Ukuran setiap segmen ular
FOOD_SIZE = GRID_SIZE  # Ukuran makanan ular

# Pengaturan skor
SCORE_INCREMENT = 10  # Penambahan skor per makanan

# Jalur asset
FONT_PATH = None  # Jalur font, jika ada
MUSIC_PATH = "assets/backsound.wav"  # Jalur musik latar

# Pengaturan audio
MUSIC_VOLUME = 0.5  # Volume musik (0.0 - 1.0)
MUTE_BUTTON_TEXT_COLOR = WHITE  # Warna teks tombol mute

# Pengaturan tombol
BUTTON_WIDTH = 200  # Lebar tombol
BUTTON_HEIGHT = 50  # Tinggi tombol
BUTTON_RADIUS = 10  # Radius sudut tombol (rounded corner)
BUTTON_COLOR = (50, 150, 50)  # Warna tombol
BUTTON_HOVER_COLOR = (70, 200, 70)  # Warna tombol saat dihover
BUTTON_FONT_SIZE = 32  # Ukuran font tombol

# Pengaturan posisi skor
SCORE_POSITION = 50  # Posisi vertikal untuk skor
