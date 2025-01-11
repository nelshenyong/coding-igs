public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("____ BITWISE : &");
        var a = 27;
        var b = 18;
        System.out.println("NILAI a = " + (a));
        System.out.println("BINARY a = " + Integer.toBinaryString(a));
        System.out.println("NILAI b = " + (b));
        System.out.println("BINARY B = " + Integer.toBinaryString(b));
        System.out.println("NILAI (a & b) = " + (a & b));
        System.out.println("BINARY NILAI (a & b) = " + (a & b));
        System.out.println(" ");
        System.out.println("____ BITWISE : |");
        System.out.println("NILAI a = " + (a));
        System.out.println("BINARY a = " + Integer.toBinaryString(a));
        System.out.println("NILAI b = " + (b));
        System.out.println("BINARY B = " + Integer.toBinaryString(b));
        System.out.println("NILAI (a | b) = " + (a | b));
        System.out.println("BINARY NILAI (a | b) = " + (a | b));
        System.out.println(" ");
        System.out.println("____ BITWISE : ^");
        System.out.println("NILAI a = " + (a));
        System.out.println("BINARY a = " + Integer.toBinaryString(a));
        System.out.println("NILAI b = " + (b));
        System.out.println("BINARY B = " + Integer.toBinaryString(b));
        System.out.println("NILAI (a ^ b) = " + (a ^ b));
        System.out.println("BINARYNILAI (a ^ b) = " + (a ^ b));
        System.out.println(" ");
        System.out.println("____ BITWISE : ~");
        System.out.println("NILAI a = " + (a));
        System.out.println("BINARY a = " + Integer.toBinaryString(a));
        System.out.println("NILAI (~a) = " + (~a));
        System.out.println("BINARY NILAI (~a) = " + (~a));
        System.out.println(" ");
        System.out.println("____ BITWISE : LEFT SHIFT (<<)");
        System.out.println("NILAI a = " + (a));
        System.out.println("BINARY a = " + Integer.toBinaryString(a));
        System.out.println("NILAI (a << 1) = " + (a << 1));
        System.out.println("BINARY NILAI (a << 1) = " + Integer.toBinaryString(a << 1));
        System.out.println(" ");
        System.out.println("____ BITWISE : RIGHT SHIFT (>>))");
        System.out.println("NILAI a = " + (a));
        System.out.println("BINARY a = " + Integer.toBinaryString(a));
        System.out.println("NILAI (a >> 2) = " + (a >> 2));
        System.out.println("BINARY NILAI (a >> 2) = " + Integer.toBinaryString(a >> 2));
    }
}