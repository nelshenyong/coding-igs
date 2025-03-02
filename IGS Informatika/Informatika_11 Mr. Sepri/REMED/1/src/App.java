class Person {
    public String name; // Access Modifier: Public
    private int age; // Access Modifier: Private

    // Constructor dengan parameter
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Getter
    public int getAge() {
        return this.age;
    }

    // Setter
    public void setAge(int age) {
        if (age > 0) {
            this.age = age;
        }
    }

    public void displayInfo() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
}

// Kelas turunan (Subclass) yang menggunakan inheritance
class Student extends Person {
    private String studentID;

    public Student(String name, int age, String studentID) {
        super(name, age); // Memanggil constructor superclass
        this.studentID = studentID;
    }

    // Getter 
    public String getStudentID() {
        return studentID;
    }

    // Setter
    public void setStudentID(String studentID) {
        this.studentID = studentID;
    }
}

public class App {
    public static void main(String[] args) {
        Student student = new Student("Alice", 20, "S12345");

        student.displayInfo();

        // Menggunakan setter
        student.setAge(22);
        student.setStudentID("S54321");

        System.out.println("\nSetelah perubahan:");
        student.displayInfo();
        System.out.println("Student ID: " + student.getStudentID());
    }
}
