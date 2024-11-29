import pygame  # Modul utama untuk membuat game
import random  # Untuk menentukan posisi acak makanan
from sprite.snake import Snake  # Mengimpor kelas Snake dari file snake.py
from conf import *  # Mengimpor semua pengaturan dari conf.py

# Inisialisasi pygame
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))  # Membuat jendela game dengan ukuran dari konfigurasi
pygame.display.set_caption(GAME_TITLE)  # Memberi judul jendela game

# Load musik latar
pygame.mixer.music.load(MUSIC_PATH)  # Memuat file musik dari jalur yang ditentukan
pygame.mixer.music.set_volume(MUSIC_VOLUME)  # Menyesuaikan volume musik
pygame.mixer.music.play(-1)  # Memutar musik tanpa henti (loop)
is_muted = False  # Status awal musik (tidak dimute)

# Inisialisasi font
font = pygame.font.Font(FONT_PATH, SCORE_FONT_SIZE) if FONT_PATH else pygame.font.Font(None, SCORE_FONT_SIZE)  # Font untuk skor
menu_font = pygame.font.Font(FONT_PATH, MENU_FONT_SIZE) if FONT_PATH else pygame.font.Font(None, MENU_FONT_SIZE)  # Font menu
title_font = pygame.font.Font(FONT_PATH, TITLE_FONT_SIZE) if FONT_PATH else pygame.font.Font(None, TITLE_FONT_SIZE)  # Font judul
credit_font = pygame.font.Font(FONT_PATH, CREDIT_FONT_SIZE) if FONT_PATH else pygame.font.Font(None, CREDIT_FONT_SIZE)  # Font kredit
mute_font = pygame.font.Font(FONT_PATH, MUTE_BUTTON_FONT_SIZE) if FONT_PATH else pygame.font.Font(None, MUTE_BUTTON_FONT_SIZE)  # Font tombol mute
button_font = pygame.font.Font(FONT_PATH, BUTTON_FONT_SIZE) if FONT_PATH else pygame.font.Font(None, BUTTON_FONT_SIZE)  # Font tombol

def draw_button(text, y_position, color=BUTTON_COLOR, hover_color=BUTTON_HOVER_COLOR):
    """
    Menggambar tombol dengan teks.
    :variabel iab text: Teks pada tombol
    :variabel y_position: Posisi vertikal tombol
    :variabel color: Warna tombol default
    :variabel hover_color: Warna tombol saat dihover
    """
    mouse = pygame.mouse.get_pos()  # Mendapatkan posisi mouse
    click = pygame.mouse.get_pressed()  # Mengecek apakah tombol mouse ditekan

    text_surface = button_font.render(text, True, WHITE)  # Membuat permukaan teks
    text_rect = text_surface.get_rect(center=(WIDTH // 2, y_position))  # Pusatkan teks di tombol
    button_rect = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2,
                              y_position - BUTTON_HEIGHT // 2,
                              BUTTON_WIDTH, BUTTON_HEIGHT)  # Membuat kotak tombol
    
    # Cek apakah mouse berada di atas tombol
    if button_rect.collidepoint(mouse):
        pygame.draw.rect(win, hover_color, button_rect, border_radius=BUTTON_RADIUS)  # Warna hover
        if click[0]:  # Jika tombol mouse kiri ditekan
            return True
    else:
        pygame.draw.rect(win, color, button_rect, border_radius=BUTTON_RADIUS)  # Warna default

    win.blit(text_surface, text_rect)  # Gambar teks di tengah tombol
    return False

def draw_grid():
    """Menggambar grid untuk latar belakang."""
    for x in range(0, WIDTH, GRID_SIZE):  # Garis vertikal
        for y in range(0, HEIGHT, GRID_SIZE):  # Garis horizontal
            pygame.draw.rect(win, GRID_COLOR, (x, y, GRID_SIZE, GRID_SIZE), 1)

def toggle_music():
    """Menghidupkan atau mematikan musik latar."""
    global is_muted
    if is_muted:
        pygame.mixer.music.unpause()  # Hidupkan musik
    else:
        pygame.mixer.music.pause()  # Matikan musik
    is_muted = not is_muted  # Ganti status mute

def draw_score(win, score):
    """
    Menggambar skor di layar.
    :param win: Objek layar pygame
    :param score: Nilai skor
    """
    score_text = font.render(f"Score: {score}", True, SCORE_COLOR)
    score_rect = score_text.get_rect(center=(WIDTH // 2, SCORE_POSITION))
    win.blit(score_text, score_rect)

def draw_mute_button(win, is_muted):
    """
    Menggambar tombol mute/unmute.
    :param win: Objek layar pygame
    :param is_muted: Status mute (True/False)
    """
    mute_text = mute_font.render("Mute" if not is_muted else "Unmute", True, MUTE_BUTTON_TEXT_COLOR)
    mute_rect = mute_text.get_rect(center=(WIDTH - 100, 30))
    win.blit(mute_text, mute_rect)

def main_menu():
    """Menampilkan menu utama."""
    while True:
        win.fill(BACKGROUND_COLOR)  # Bersihkan layar dengan warna latar belakang
        title_text = title_font.render(GAME_TITLE, True, TITLE_COLOR)  # Teks judul
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        win.blit(title_text, title_rect)

        # Subjudul (opsional)
        if GAME_SUBTITLE:
            subtitle_text = title_font.render(GAME_SUBTITLE, True, SUBTITLE_COLOR)
            subtitle_rect = subtitle_text.get_rect(center=(WIDTH // 2, HEIGHT // 3 + 50))
            win.blit(subtitle_text, subtitle_rect)

        # Tombol Play dan Quit
        play_clicked = draw_button("Play", HEIGHT // 2)
        quit_clicked = draw_button("Quit", HEIGHT // 2 + BUTTON_HEIGHT + 20)

        # Kredit di bagian bawah layar
        creator_text = credit_font.render(f"Created by {CREATOR_NAME} - {YEAR}", True, CREDIT_COLOR)
        creator_rect = creator_text.get_rect(center=(WIDTH // 2, HEIGHT - 30))
        win.blit(creator_text, creator_rect)

        pygame.display.update()  # Perbarui layar

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

        if play_clicked:
            return "play"
        if quit_clicked:
            return "quit"

def game_loop():
    """
    Loop utama game. Mengatur jalannya permainan.
    """
    clock = pygame.time.Clock()
    snake = Snake(WIDTH // 2, HEIGHT // 2, INITIAL_LENGTH)  # Buat ular di tengah layar
    dot_position = (random.randint(0, (WIDTH - FOOD_SIZE) // GRID_SIZE) * GRID_SIZE, 
                    random.randint(0, (HEIGHT - FOOD_SIZE) // GRID_SIZE) * GRID_SIZE)  # Posisi makanan
    score = 0
    running = True

    while running:
        clock.tick(FPS)  # Atur kecepatan game
        win.fill(BACKGROUND_COLOR)  # Bersihkan layar
        draw_grid()  # Gambar grid

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # Kontrol gerakan
                if event.key == pygame.K_w and snake.direction != (0, 1):
                    snake.change_direction((0, -1))
                elif event.key == pygame.K_s and snake.direction != (0, -1):
                    snake.change_direction((0, 1))
                elif event.key == pygame.K_a and snake.direction != (1, 0):
                    snake.change_direction((-1, 0))
                elif event.key == pygame.K_d and snake.direction != (-1, 0):
                    snake.change_direction((1, 0))
                elif event.key == pygame.K_m:
                    toggle_music()  # Tombol untuk mute/unmute musik

        snake.move(WIDTH, HEIGHT)  # Gerakkan ular
        snake.draw(win)  # Gambar ular

        # Gambar makanan
        pygame.draw.rect(win, FOOD_COLOR, (*dot_position, FOOD_SIZE, FOOD_SIZE))

        # Deteksi makan makanan
        if snake.body[0] == dot_position:
            snake.grow()
            score += SCORE_INCREMENT
            dot_position = (random.randint(0, (WIDTH - FOOD_SIZE) // GRID_SIZE) * GRID_SIZE,
                            random.randint(0, (HEIGHT - FOOD_SIZE) // GRID_SIZE) * GRID_SIZE)

        draw_score(win, score)  # Gambar skor
        draw_mute_button(win, is_muted)  # Gambar tombol mute/unmute

        # Deteksi tabrakan
        if snake.check_collision():
            return score

        pygame.display.update()

def main():
    """
    Fungsi utama untuk menjalankan game.
    """
    running = True
    while running:
        result = main_menu()
        if result == "quit":
            running = False
        elif result == "play":
            score = game_loop()
            print(f"Game over! Final Score: {score}")

if __name__ == "__main__":
    main()
