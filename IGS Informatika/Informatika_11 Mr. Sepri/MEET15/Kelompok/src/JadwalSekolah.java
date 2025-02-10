import java.io.*;
import java.util.*;

public class JadwalSekolah {
    private static final String FILE_NAME = "jadwal.txt";
    private static Map<String, List<String>> jadwalMap = new HashMap<>();

    public static void main(String[] args) {
        loadJadwal();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\n+---------------------------------+");
            System.out.println("|   Menu Utama:                  |");
            System.out.println("|   1. Lihat Semua Jadwal        |");
            System.out.println("|   2. Tambah Jadwal             |");
            System.out.println("|   3. Edit Jadwal               |");
            System.out.println("|   4. Hapus Jadwal              |");
            System.out.println("|   5. Cek Pelajaran di Hari     |");
            System.out.println("|   6. Simpan & Keluar           |");
            System.out.println("+---------------------------------+");
            System.out.print("Pilihan Menu: ");
            
            int pilihan = scanner.nextInt();
            scanner.nextLine();
            switch (pilihan) {
                case 1:
                    lihatJadwal();
                    break;
                case 2:
                    tambahJadwal(scanner);
                    break;
                case 3:
                    editJadwal(scanner);
                    break;
                case 4:
                    hapusJadwal(scanner);
                    break;
                case 5:
                    cekPelajaranHariIni(scanner);
                    break;
                case 6:
                    simpanJadwal();
                    System.out.println("Jadwal berhasil disimpan. Keluar...");
                    return;
                default:
                    System.out.println("Pilihan tidak valid.");
            }
        }
    }

    private static void lihatJadwal() {
        if (jadwalMap.isEmpty()) {
            System.out.println("Tidak ada jadwal tersimpan.");
        } else {
            for (String hari : jadwalMap.keySet()) {
                System.out.println("\n📅 Jadwal " + hari + ":");
                List<String> jadwalList = jadwalMap.get(hari);
                if (jadwalList.isEmpty()) {
                    System.out.println("Tidak ada jadwal untuk hari ini.");
                } else {
                    for (int i = 0; i < jadwalList.size(); i++) {
                        System.out.println((i + 1) + ". " + jadwalList.get(i));
                    }
                }
            }
        }
    }

    private static void tambahJadwal(Scanner scanner) {
        System.out.print("Masukkan hari (Senin, Selasa, Rabu, Kamis, Jumat, Sabtu, Minggu): ");
        String hari = scanner.nextLine();
        System.out.print("Masukkan jadwal baru (format HH:MM - HH:MM | Mata Pelajaran): ");
        String jadwal = scanner.nextLine();

        jadwalMap.computeIfAbsent(hari, k -> new ArrayList<>()).add(jadwal);
        System.out.println("✅ Jadwal berhasil ditambahkan!");
    }

    private static void editJadwal(Scanner scanner) {
        System.out.print("Masukkan hari (Senin, Selasa, Rabu, Kamis, Jumat, Sabtu, Minggu): ");
        String hari = scanner.nextLine();
        List<String> jadwalList = jadwalMap.get(hari);

        if (jadwalList == null || jadwalList.isEmpty()) {
            System.out.println("Tidak ada jadwal untuk hari ini.");
            return;
        }

        System.out.println("\n📅 Jadwal " + hari + ":");
        for (int i = 0; i < jadwalList.size(); i++) {
            System.out.println((i + 1) + ". " + jadwalList.get(i));
        }

        System.out.print("Masukkan nomor jadwal yang ingin diubah: ");
        int index = scanner.nextInt();
        scanner.nextLine(); // Konsumsi newline

        if (index > 0 && index <= jadwalList.size()) {
            System.out.print("Masukkan jadwal baru (format HH:MM - HH:MM | Mata Pelajaran): ");
            String jadwalBaru = scanner.nextLine();
            jadwalList.set(index - 1, jadwalBaru);
            System.out.println("✅ Jadwal berhasil diubah!");
        } else {
            System.out.println("❌ Nomor tidak valid.");
        }
    }

    private static void hapusJadwal(Scanner scanner) {
        System.out.print("Masukkan hari (Senin, Selasa, Rabu, Kamis, Jumat, Sabtu, Minggu): ");
        String hari = scanner.nextLine();
        List<String> jadwalList = jadwalMap.get(hari);

        if (jadwalList == null || jadwalList.isEmpty()) {
            System.out.println("Tidak ada jadwal untuk hari ini.");
            return;
        }

        System.out.println("\n📅 Jadwal " + hari + ":");
        for (int i = 0; i < jadwalList.size(); i++) {
            System.out.println((i + 1) + ". " + jadwalList.get(i));
        }

        System.out.print("Masukkan nomor jadwal yang ingin dihapus: ");
        int index = scanner.nextInt();
        scanner.nextLine();

        if (index > 0 && index <= jadwalList.size()) {
            System.out.println("🗑️ Jadwal '" + jadwalList.remove(index - 1) + "' berhasil dihapus!");
        } else {
            System.out.println("❌ Nomor tidak valid.");
        }
    }

    private static void cekPelajaranHariIni(Scanner scanner) {
        System.out.print("Masukkan hari (Senin, Selasa, Rabu, Kamis, Jumat, Sabtu, Minggu): ");
        String hari = scanner.nextLine();
        List<String> jadwalList = jadwalMap.get(hari);

        if (jadwalList == null || jadwalList.isEmpty()) {
            System.out.println("Tidak ada jadwal untuk hari " + hari + ".");
        } else {
            System.out.println("\n📅 Jadwal " + hari + ":");
            for (int i = 0; i < jadwalList.size(); i++) {
                System.out.println((i + 1) + ". " + jadwalList.get(i));
            }
        }
    }

    private static void simpanJadwal() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(FILE_NAME))) {
            for (Map.Entry<String, List<String>> entry : jadwalMap.entrySet()) {
                writer.write(entry.getKey() + ":");
                writer.newLine();
                for (String jadwal : entry.getValue()) {
                    writer.write(jadwal);
                    writer.newLine();
                }
            }
        } catch (IOException e) {
            System.out.println("⚠️ Gagal menyimpan jadwal: " + e.getMessage());
        }
    }

    private static void loadJadwal() {
        File file = new File(FILE_NAME);
        if (!file.exists()) return;
        
        try (BufferedReader reader = new BufferedReader(new FileReader(FILE_NAME))) {
            String line;
            String currentDay = null;
            while ((line = reader.readLine()) != null) {
                if (line.endsWith(":")) {
                    currentDay = line.substring(0, line.length() - 1);
                    jadwalMap.put(currentDay, new ArrayList<>());
                } else if (currentDay != null) {
                    jadwalMap.get(currentDay).add(line);
                }
            }
        } catch (IOException e) {
            System.out.println("⚠️ Gagal membaca file: " + e.getMessage());
        }
    }
}