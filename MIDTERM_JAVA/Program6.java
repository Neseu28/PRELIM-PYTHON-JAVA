import java.util.Date;
import java.text.SimpleDateFormat;
import java.text.ParseException;

class Student {

    // Instance variables
    private String studentNo;
    private String studentName;
    private Date dateOfBirth;
    private int tariffPoints;

    // Class variable
    private static int noOfStudents = 0;


    // Setters
    public void setStudentNo(String studentNo) {
        this.studentNo = studentNo;
    }

    public void setStudentName(String studentName) {
        this.studentName = studentName;
    }

    public void setDateOfBirth(Date dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }

    public void setTariffPoints(int tariffPoints) {
        if (tariffPoints >= 20 && tariffPoints <= 280) {
            this.tariffPoints = tariffPoints;
        } else {
            this.tariffPoints = 20;
        }
    }


    public String getStudentNo() {
        return studentNo;
    }

    public String getStudentName() {
        return studentName;
    }

    public Date getDateOfBirth() {
        return dateOfBirth;
    }

    public int getTariffPoints() {
        return tariffPoints;
    }


    // Default constructor
    public Student() {

        studentNo = "not known";
        studentName = "not known";

        try {
            SimpleDateFormat format = new SimpleDateFormat("dd/MM/yyyy");
            dateOfBirth = format.parse("01/01/1995");
        } catch (ParseException e) {
            System.out.println("Invalid date.");
        }

        tariffPoints = 20;

        noOfStudents++;
    }


    public Student(String studentNo, String studentName,
                   Date dateOfBirth, int tariffPoints) {

        this.studentNo = studentNo;
        this.studentName = studentName;
        this.dateOfBirth = dateOfBirth;

        if (tariffPoints >= 20 && tariffPoints <= 280) {
            this.tariffPoints = tariffPoints;
        } else {
            this.tariffPoints = 20;
        }

        noOfStudents++;
    }


    // Get number of students
    public static int getNoOfStudents() {
        return noOfStudents;
    }
}


public class Program6 {

    public static void main(String[] args) {


        Student student1 = new Student();

        try {
            SimpleDateFormat format = new SimpleDateFormat("dd/MM/yyyy");

            Date date = format.parse("28/11/2002");

            Student student2 = new Student(
                "S002",
                "Juan Dela Cruz",
                date,
                250
            );

            // Display student 1
            System.out.println("Student 1:");
            System.out.println("Student No: " + student1.getStudentNo());
            System.out.println("Student Name: " + student1.getStudentName());
            System.out.println("Date of Birth: " +
                    format.format(student1.getDateOfBirth()));
            System.out.println("Tariff Points: " +
                    student1.getTariffPoints());

            System.out.println();

            // Display student 2
            System.out.println("Student 2:");
            System.out.println("Student No: " + student2.getStudentNo());
            System.out.println("Student Name: " + student2.getStudentName());
            System.out.println("Date of Birth: " +
                    format.format(student2.getDateOfBirth()));
            System.out.println("Tariff Points: " +
                    student2.getTariffPoints());

            System.out.println();
            System.out.println("Number of Students: " +
                    Student.getNoOfStudents());

        } catch (ParseException e) {
            System.out.println("Invalid date.");
        }
    }
}