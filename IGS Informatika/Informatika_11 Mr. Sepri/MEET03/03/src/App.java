public class App {
    public static void main(String[] args) throws Exception {
        char ischr = 'a';
        String isStr = "IPAA1";
        System.out.println("Char : "+ ischr +         " String : " + isStr);

        
        System.out.println("____________Boolean");
        boolean t = true;
        boolean f = false;
        System.out.println("T : " + t + "F : " + f);

        System.out.println("____________ va & Final");
        byte isByte = 120;
        var isvar = 121;
        var isvarf = 12.1;
        var isvarStr = "javac";
        
        isvar = 212;
        final var isFinal = 15;
        // isFinal = 515; 

        System.out.println("____________ Assigment Operator");
        /* 
         * +=
         * -=
         * *=
         * /=
         * %=
         */
        var G = 4;
        System.out.println("1G : "+G);
        G += 2 ;
        System.out.println("2G : "+G);
        
        System.out.println("UNARY Operator");
        //+ -
        byte abc = 12;
        System.out.println("abc -12 : "  + - abc);
        System.out.println("abc -12 : "  + + abc);
        //Decrement : post & Pre
        byte isDec = 10;
        System.out.printf("pre-Decrement : %d ",++isDec);
        //pre - Decrement
        byte isPost = 20;
        System.out.printf("\n1pre-Decrement : %d ",isPost++);
        System.out.printf("\n2pre-Decrement : %d ",isPost);
        //Increment (-) : Post & pre
        System.out.printf("\npre-increment : %d ",--isDec);
        System.out.printf("\n1pre-increment : %d ",isPost--);
        System.out.printf("\n2pre-increment : %d ",isPost);
        System.out.println("____________ Comparison Operator");
        /* 
         * >
         * <
         * >=
         * <=
         * ==
         * !=
        */

        System.out.println("____________ Operator Logika");
        /* 
            * && (and)
            * || (or)
            * ! (not)
            * ^ (xor)
        */

        System.out.println("T and T " + (true && true)); 
        System.out.println("T or T " + (true | true)); 
        System.out.println("T xor T " + (true ^ true)); 
        System.out.println("Not T " + (!true)); 
    }
}
