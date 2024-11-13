import java.lang.classfile.constantpool.IntegerEntry;

public class App {

    // Statement print di java:
    // - println
    // - print
    // - printf

    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        System.out.println("Hello, World!");
        System.out.print("Hello, World! \n");
        System.out.print("Hello, World! \n");
        System.out.println("Nilai pi: " + 3.14);
        System.out.printf("Nilai a %d + %f",10, 11.1);

        // Tipe data Integer & Floating:
        System.out.println("- TIPE DATA INTEGER & FLOATING");

        byte isByte = 10;
        short isShort = 10;
        int isInt = 10;
        long isLong = 10L;
        float isFloat = 10.0f;
        double isDouble = 10.0;


        System.out.println("-________isByte");
        System.out.println("MAX: " + Byte.MAX_VALUE);
        System.out.println("MIN: " + Byte.MIN_VALUE);
        System.out.println("Byte: " + Byte.BYTES);
        System.out.println("SIZE: " + Byte.SIZE);

        System.out.println("-________isShort");
        System.out.println("MAX: " + Short.MAX_VALUE);
        System.out.println("MIN: " + Short.MIN_VALUE);
        System.out.println("Byte: " + Short.BYTES);
        System.out.println("SIZE: " + Short.SIZE);

        System.out.println("-________isInt");
        System.out.println("MAX: " + Integer.MAX_VALUE);
        System.out.println("MIN: " + Integer.MIN_VALUE);
        System.out.println("Byte: " + Integer.BYTES);
        System.out.println("SIZE: " + Integer.SIZE);

        System.out.println("-________isLong");
        System.out.println("MAX: " + Long.MAX_VALUE);
        System.out.println("MIN: " + Long.MIN_VALUE);
        System.out.println("Byte: " + Long.BYTES);
        System.out.println("SIZE: " + Long.SIZE);

        System.out.println("-________isFloat");
        System.out.println("MAX: " + Float.MAX_VALUE);
        System.out.println("MIN: " + Float.MIN_VALUE);
        System.out.println("Byte: " + Float.BYTES);
        System.out.println("SIZE: " + Float.SIZE);

        System.out.println("-________isDouble");
        System.out.println("MAX: " + Double.MAX_VALUE);
        System.out.println("MIN: " + Double.MIN_VALUE);
        System.out.println("Byte: " + Double.BYTES);
        System.out.println("SIZE: " + Double.SIZE);

        System.out.println("________Literal Code :");
        int HexNum = 0xAB;
        int BinNum = 0b10101;
        int OctNum = 071;
        System.out.println("Nilai Hex (AB) : " + HexNum);
        System.out.println("Nilai BinNum (10101) : " + BinNum);
        System.out.println("Nilai Oct (71) : " + OctNum);
    }
}