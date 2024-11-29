import pygame  # Untuk menggambar ular di layar menggunakan fungsi pygame
from conf import SNAKE_SIZE, SNAKE_COLOR, GRID_SIZE  # Import konfigurasi ukuran ular, warna ular, dan ukuran grid

class Snake:
    def __init__(self, x, y, initial_length=3):
        """
        Inisialisasi ular.
        :param x: Posisi awal kepala ular (koordinat x)
        :param y: Posisi awal kepala ular (koordinat y)
        :param initial_length: Panjang awal ular
        """
        self.body = [(x - GRID_SIZE * i, y) for i in range(initial_length)]  # Membuat tubuh ular
        self.direction = (1, 0)  # Arah gerakan awal (ke kanan)
        self.growing = False  # Menandakan apakah ular sedang bertumbuh
        self.color = SNAKE_COLOR  # Warna ular

    def move(self, width, height):
        """
        Menggerakkan ular satu langkah sesuai arah.
        :param width: Lebar layar untuk wrapping
        :param height: Tinggi layar untuk wrapping
        """
        # Hitung posisi kepala baru berdasarkan arah
        new_head = (self.body[0][0] + self.direction[0] * GRID_SIZE, 
                    self.body[0][1] + self.direction[1] * GRID_SIZE)

        # Wrap posisi kepala jika keluar layar
        new_head = (new_head[0] % width, new_head[1] % height)

        # Tambahkan kepala baru ke tubuh ular
        self.body = [new_head] + self.body

        # Jika ular tidak bertumbuh, buang ekor terakhir
        if not self.growing:
            self.body.pop()
        
        # Reset status pertumbuhan
        self.growing = False

    def draw(self, win):
        """
        Menggambar ular di layar.
        :param win: Objek layar (surface) pygame
        """
        for segment in self.body:
            pygame.draw.rect(win, self.color, (*segment, SNAKE_SIZE, SNAKE_SIZE))

    def change_direction(self, direction):
        """
        Mengubah arah ular jika arah baru tidak berlawanan.
        :param direction: Arah baru dalam bentuk tuple (x, y)
        """
        if (self.direction[0] * -1, self.direction[1] * -1) != direction:
            self.direction = direction

    def grow(self):
        "Memicu pertumbuhan ular."
        self.growing = True

    def check_collision(self):
        """
        Mengecek apakah kepala ular bertabrakan dengan tubuhnya sendiri.
        :return: True jika terjadi tabrakan, False jika tidak
        """
        return self.body[0] in self.body[1:]
