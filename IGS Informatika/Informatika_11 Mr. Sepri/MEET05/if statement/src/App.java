public class App {
    public static void main(String[] args) throws Exception {
        var nilai = 120;
        var present = 88;
        String nilai_inf;
        System.out.println("____ IF STATEMENT");

        // if (nilai >= 80 && present >= 85){
        //     if((nilai > 100) || (present > 100)) {
        //         nilai_inf = "E";
        //     } else {
        //         nilai_inf = "A";
        //     }
        // } else if (nilai >= 70 && present >= 75) {
        //     nilai_inf = "B";
        // } else if (nilai >= 60 && present >= 65) {
        //     nilai_inf = "C";
        // }
        // else if (nilai >= 50 && present >= 55) {
        //     nilai_inf = "D";
        // } else {
        //     nilai_inf = "E";
        // }

        if (nilai >= 80 && present >= 85){
            if((nilai > 100) || (present > 100)) {
                nilai_inf = "E";
            } else {
                nilai_inf = "A";
            }
        } else if (nilai >= 70 && present >= 75) {
            nilai_inf = "B";
        } else if (nilai >= 60 && present >= 65) {
            nilai_inf = "C";
        }
        else if (nilai >= 50 && present >= 55) {
            nilai_inf = "D";
        } else {
            nilai_inf = "E";
        }
        System.out.println("Nilai Informatika : " + nilai_inf);
        String status;
        System.out.println("____ SWITCH STATEMENT");
        switch (nilai_inf) {
            case "A":
                status = "Memilih jurusan yang SANGAT TEPAT";
                break;
            case "B":
                status = "Memilih jurusan yang SANGAT TEPAT";
                break;
            case "C":
            case "D":
                status = "Memilih jurusan yang SALAH";
                break;
            default:
            status = "Pindah jurusan aja dek...";
                break;
        }

        System.out.println("____ SWITCH STATEMENT : LAMBDA");
        switch (nilai_inf) {
            case "A" -> status = "Memilih jurusan yang SANGAT TEPAT";
            case "B" -> status = "Memilih jurusan yang SANGAT TEPAT";
            case "C", "D" -> status = "Memilih jurusan yang SALAH";
            default -> status = "Pindah jurusan aja dek...";
        }
        System.out.println("Status belajar: " + status);

        System.out.println("__________________ : SWITCH STATEMENT : YIELD ");
        status = switch (nilai_inf) {
            case "A" : yield "Memilih jurusan yang SANGAT TEPAT";
            case "B" : yield "Memilih jurusan yang  TEPAT";
            case "C", "D" : yield "Memilih jurusan yang SALAH";
            default :
            yield "PINDAH JURUSAN DEH...";
        };
        System.out.println("Status Belajar " + status);

    }
}
