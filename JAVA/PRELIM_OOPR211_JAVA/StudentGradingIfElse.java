import java.util.Scanner;

public class StudentGradingIfElse {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String choice;

        do {
            System.out.print("Java Programming Score: ");
            double javaScore = input.nextDouble();

            System.out.print("C Programming Score: ");
            double cScore = input.nextDouble();

            System.out.print("Database Handling Score: ");
            double databaseScore = input.nextDouble();

            // Average
            double average = (javaScore + cScore + databaseScore) / 3;

            if (average >= 90 && average <= 100) {
                System.out.println("Grade: A");
            } 
            else if (average >= 80 && average <= 89) {
                System.out.println("Grade: B");
            } 
            else if (average >= 75 && average <= 79) {
                System.out.println("Grade: C");
            } 
            else if (average < 75) {
                System.out.println("Grade: F");
            } 
            else {
                System.out.println("Invalid score.");
            }

            System.out.printf("Average: %.3f%n", average);

            // Ask if user wants to continue
            System.out.print("Do you want to continue: YES / NO: ");
            choice = input.next();

        } while (choice.equalsIgnoreCase("YES"));

        System.out.println("Program terminated.");

        input.close();
    }
}