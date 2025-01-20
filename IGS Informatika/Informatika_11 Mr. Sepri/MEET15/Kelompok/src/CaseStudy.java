import java.util.*;

public class CaseStudy {
    private final Map<String, List<String>> jadwal = new HashMap<>();
    private final Map<String, List<String>> jamPelajaran = new HashMap<>();

    public CaseStudy() {
        jadwal.put("senin", Arrays.asList("Matematika", "Fisika", "Bahasa Inggris"));
        jadwal.put("selasa", Arrays.asList("Kimia", "Biologi", "Sejarah"));
        jadwal.put("rabu", Arrays.asList("Seni", "Olahraga", "Bahasa Indonesia"));
        jadwal.put("kamis", Arrays.asList("Ekonomi", "Geografi", "Sosiologi"));
        jadwal.put("jumat", Arrays.asList("Agama", "Pendidikan Kewarganegaraan"));

        jamPelajaran.put("senin", Arrays.asList("07:00 - 08:00", "08:15 - 09:15", "09:30 - 10:30"));
        jamPelajaran.put("selasa", Arrays.asList("07:00 - 08:00", "08:15 - 09:15", "09:30 - 10:30"));
        jamPelajaran.put("rabu", Arrays.asList("07:00 - 08:00", "08:15 - 09:15", "09:30 - 10:30"));
        jamPelajaran.put("kamis", Arrays.asList("07:00 - 08:00", "08:15 - 09:15", "09:30 - 10:30"));
        jamPelajaran.put("jumat", Arrays.asList("07:00 - 08:00", "08:15 - 09:15"));
    }

    public void tampilkanJadwal(String hari) {
        hari = hari.toLowerCase();
        List<String> pelajaran = jadwal.get(hari);
        List<String> jam = jamPelajaran.get(hari);

        if (pelajaran == null || jam == null) {
            System.out.println("Hari tidak ditemukan.");
            return;
        }

        System.out.println("\nJadwal pelajaran untuk " + hari + ":");
        System.out.println("+-------------------+--------------------------+");
        System.out.println("|       Jam         |        Pelajaran        |");
        System.out.println("+-------------------+--------------------------+");

        for (int i = 0; i < pelajaran.size(); i++) {
            String jamStr = i < jam.size() ? jam.get(i) : "-";
            System.out.printf("| %-17s | %-24s |%n", jamStr, pelajaran.get(i));
        }

        System.out.println("+-------------------+--------------------------+");
    }

    public void cariJadwal(String hari, int jamKe) {
        hari = hari.toLowerCase();
        List<String> pelajaran = jadwal.get(hari);
        List<String> jam = jamPelajaran.get(hari);

        if (pelajaran == null || jam == null || jamKe <= 0 || jamKe > pelajaran.size()) {
            System.out.println("Data tidak valid atau tidak ditemukan.");
            return;
        }

        String jamStr = jamKe <= jam.size() ? jam.get(jamKe - 1) : "-";
        System.out.printf("\nPelajaran pada hari %s jam %d (%s): %s%n", hari, jamKe, jamStr, pelajaran.get(jamKe - 1));
    }

    public void tambahPelajaran(String hari, String pelajaran, String jam) {
        hari = hari.toLowerCase();
        jadwal.computeIfAbsent(hari, k -> new ArrayList<>()).add(pelajaran);
        jamPelajaran.computeIfAbsent(hari, k -> new ArrayList<>()).add(jam);
        System.out.println("Pelajaran \"" + pelajaran + "\" dengan jam \"" + jam + "\" berhasil ditambahkan ke " + hari);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        CaseStudy js = new CaseStudy();

        System.out.println("+---------------------------------+");
        System.out.println("|          Mulai Program          |");
        System.out.println("+---------------------------------+");

        while (true) {
            System.out.println("\n+---------------------------------+");
            System.out.println("|   Menu Utama:                  |");
            System.out.println("|   1. Lihat Jadwal Harian       |");
            System.out.println("|   2. Cari Jadwal Berdasarkan   |");
            System.out.println("|      Jam Tertentu              |");
            System.out.println("|   3. Tambah Jadwal             |");
            System.out.println("|   4. Keluar                    |");
            System.out.println("+---------------------------------+");
            System.out.print("Pilihan Menu: ");
            int pilihan = scanner.nextInt();
            scanner.nextLine();

            if (pilihan == 4) {
                System.out.println("Terima kasih! Program selesai.");
                break;
            }

            System.out.print("Masukkan nama hari: ");
            String hari = scanner.nextLine();

            switch (pilihan) {
                case 1 -> js.tampilkanJadwal(hari);
                case 2 -> {
                    System.out.print("Masukkan nomor jam: ");
                    js.cariJadwal(hari, scanner.nextInt());
                }
                case 3 -> {
                    System.out.print("Masukkan nama pelajaran: ");
                    String pelajaran = scanner.nextLine();
                    System.out.print("Masukkan jam pelajaran (format HH:MM - HH:MM): ");
                    String jam = scanner.nextLine();
                    js.tambahPelajaran(hari, pelajaran, jam);
                }
                default -> System.out.println("Pilihan tidak valid.");
            }
        }

        scanner.close();
    }
}