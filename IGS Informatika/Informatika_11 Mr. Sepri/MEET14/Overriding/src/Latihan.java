import java.util.Random;

class Game {
    String playerName; // Default
    public int level; // Public
    private int points; // Private

    Game(String playerName) {
        this.playerName = playerName;
        this.level = 1;
        this.points = 0;
    }

    void displayStatus() {
        System.out.println("Player: " + playerName);
        System.out.println("Level: " + level);
        System.out.println("Points: " + points);
    }

    public void addPoints(int additionalPoints) {
        points += additionalPoints;
        if (points >= level * 20 && level < 4) { // Maksimal level 4
            level++;
            System.out.println("Naik ke level " + level + "!");
        }
    }
}

public class App {
    public static void main(String[] args) {
        Random random = new Random();
        Game game = new Game("Pemain1");

        while (game.level <= 4) {
            game.displayStatus();

            // Membuat soal berdasarkan level
            int a = random.nextInt(10 * game.level) + 1; // Bilangan pertama
            int b = random.nextInt(10 * game.level) + 1; // Bilangan kedua
            int jawabBenar = a + b; // Operasi: Penjumlahan
            System.out.println("Soal Level " + game.level + ": " + a + " + " + b);

            // Simulasi jawaban pemain (benar atau salah secara acak)
            int jawabanSimulasi = random.nextBoolean() ? jawabBenar : random.nextInt(10 * game.level) + 1;

            if (jawabanSimulasi == jawabBenar) {
                System.out.println("Jawaban benar! +20 poin");
                game.addPoints(20);
            } else {
                System.out.println("Jawaban salah!");
            }

            System.out.println("--------------------");

            // Jika level sudah mencapai 4 dan soal terakhir selesai, keluar
            if (game.level == 4 && game.points >= 20 * game.level) {
                break;
            }
        }

        System.out.println("Permainan selesai. Terima kasih telah bermain!");
    }
}
