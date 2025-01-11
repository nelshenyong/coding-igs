public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("______________________ ARRAY -1");
        String[] arrayString = new String[3];
        //diatas sering disebut Memory Stack
        arrayString[0] = "HENDY";
        arrayString[1] = "DAYAT";
        arrayString[2] = "JOHAN";
        System.out.println(arrayString);
        System.out.println("data - 0: " + arrayString[0]);
        System.out.println("data - 1: " + arrayString[1]);
        System.out.println("data - 2: " + arrayString[2]);
        
        System.out.println("______________________ARRAY -2");
        Byte[] arrayByte = new Byte[] {
            1,2,3,4
        };
        //DI ATAS SERING DISEBUT DENGAN MEMORY HEAP
        System.out.println("data - 0: " + arrayByte[0]);
        System.out.println("data - 1: " + arrayByte[1]);
        System.out.println("data - 2: " + arrayByte[2]);

        System.out.println("______________________ ARRAY -3");
        int [] arrayInt = {
            4,3,2,1
        };
        System.out.println("data - 0: " + arrayInt[0]);
        System.out.println("data - 1: " + arrayInt[1]);
        System.out.println("data - 2: " + arrayInt[2]);

        System.out.println("______________________ PANJANG ARRAY");
        System.out.println("Panjang arrayInt = " + arrayInt.length);

        System.out.println("______________________ FOR LOOP ARRAY");
        for ( int i = 0; i < arrayInt.length; i++) {
            System.out.println("data ke- " + (i+1) + " = " + arrayInt[i]);
        }

        System.out.println("______________________ FOR LOOP EACH ARRAY");
        for( int i : arrayInt ){
            System.out.println("data = " + i);
        }
    }
}