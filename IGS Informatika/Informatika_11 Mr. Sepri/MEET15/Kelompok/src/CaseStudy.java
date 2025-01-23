import java.util.*;

public class CaseStudy {
    private final Map<String, List<String>> jadwal = new HashMap<>();
    private final Map<String, List<String>> jamPelajaran = new HashMap<>();

    public CaseStudy() {
        jadwal.put("senin", new ArrayList<>(List.of("Matematika", "Fisika", "Bahasa Inggris")));
        jadwal.put("selasa", new ArrayList<>(List.of("Kimia", "Biologi", "Sejarah")));
        jadwal.put("rabu", new ArrayList<>(List.of("Seni", "Olahraga", "Bahasa Indonesia")));
        jadwal.put("kamis", new ArrayList<>(List.of("Ekonomi", "Geografi", "Sosiologi")));
        jadwal.put("jumat", new ArrayList<>(List.of("Agama", "Pendidikan Kewarganegaraan")));

        jamPelajaran.put("senin", new ArrayList<>(List.of("07:00 - 08:00", "08:15 - 09:15", "09:30 - 10:30")));
        jamPelajaran.put("selasa", new ArrayList<>(List.of("07:00 - 08:00", "08:15 - 09:15", "09:30 - 10:30")));
        jamPelajaran.put("rabu", new ArrayList<>(List.of("07:00 - 08:00", "08:15 - 09:15", "09:30 - 10:30")));
        jamPelajaran.put("kamis", new ArrayList<>(List.of("07:00 - 08:00", "08:15 - 09:15", "09:30 - 10:30")));
        jamPelajaran.put("jumat", new ArrayList<>(List.of("07:00 - 08:00", "08:15 - 09:15")));
    }

    private boolean isValidTimeFormat(String time) {
        String timePattern = "^(?:[01]\\d|2[0-3]):[0-5]\\d - (?:[01]\\d|2[0-3]):[0-5]\\d$";
        if (!time.matches(timePattern)) {
            System.out.println("Format waktu tidak valid. Gunakan format HH:MM - HH:MM.");
            return false;
        }

        String[] times = time.split(" - ");
        if (times[0].compareTo(times[1]) >= 0) {
            System.out.println("Jam mulai harus lebih awal dari jam selesai.");
            return false;
        }

        return true;
    }

    public void tambahPelajaran(String hari, String pelajaran, String jam) {
        hari = hari.toLowerCase();
        if (!jadwal.containsKey(hari)) {
            System.out.println("Hari tidak ditemukan.");
            return;
        }

        if (!isValidTimeFormat(jam)) {
            return;
        }

        jadwal.get(hari).add(pelajaran);
        jamPelajaran.get(hari).add(jam);
        System.out.println("Pelajaran berhasil ditambahkan.");
    }

    public void lihatJadwal(String hari) {
        hari = hari.toLowerCase();
        if (!jadwal.containsKey(hari)) {
            System.out.println("Hari tidak ditemukan.");
            return;
        }

        System.out.println("Jadwal pelajaran untuk " + hari + ":");
        System.out.println("+-------------------+--------------------------+");
        System.out.println("|       Jam         |        Pelajaran        |");
        System.out.println("+-------------------+--------------------------+");
        
        List<String> pelajaranHari = jadwal.get(hari);
        List<String> jamHari = jamPelajaran.get(hari);

        for (int i = 0; i < pelajaranHari.size(); i++) {
            System.out.printf("| %-17s | %-24s |%n", jamHari.get(i), pelajaranHari.get(i));
        }

        System.out.println("+-------------------+--------------------------+");
    }

    public void menuUtama() {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("\n+---------------------------------+");
            System.out.println("|   Menu Utama:                  |");
            System.out.println("|   1. Lihat Jadwal Harian       |");
            System.out.println("|   2. Cari Jadwal Berdasarkan   |");
            System.out.println("|      Jam Tertentu              |");
            System.out.println("|   3. Tambah Jadwal             |");
            System.out.println("|   4. Edit Jadwal               |");
            System.out.println("|   5. Keluar                    |");
            System.out.println("+---------------------------------+");
            System.out.print("Pilihan Menu: ");

            int pilihan = scanner.nextInt();
            scanner.nextLine();

            switch (pilihan) {
                case 1 -> {
                    System.out.print("Masukkan nama hari: ");
                    String hari = scanner.nextLine();
                    lihatJadwal(hari);
                }
                case 3 -> {
                    System.out.print("Masukkan nama hari: ");
                    String hari = scanner.nextLine();
                    System.out.print("Masukkan nama pelajaran: ");
                    String pelajaran = scanner.nextLine();
                    System.out.print("Masukkan jam pelajaran (format HH:MM - HH:MM): ");
                    String jam = scanner.nextLine();
                    tambahPelajaran(hari, pelajaran, jam);
                }
                case 5 -> {
                    System.out.println("Keluar dari program.");
                    return;
                }
                default -> System.out.println("Pilihan tidak valid.");
            }
        }
    }

    public static void main(String[] args) {
        CaseStudy app = new CaseStudy();
        app.menuUtama();
    }
}
