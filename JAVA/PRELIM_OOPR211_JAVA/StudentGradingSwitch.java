import java.util.Scanner;

public class StudentGradingSwitch {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String choice;

        do {
            // Input scores
            System.out.print("Java Programming Score: ");
            double javaScore = input.nextDouble();

            System.out.print("C Programming Score: ");
            double cScore = input.nextDouble();

            System.out.print("Database Handling Score: ");
            double databaseScore = input.nextDouble();

            double average = (javaScore + cScore + databaseScore) / 3;

            int category;

            if (average >= 90 && average <= 100) {
                category = 1;
            } 
            else if (average >= 80) {
                category = 2;
            } 
            else if (average >= 75) {
                category = 3;
            } 
            else if (average < 75) {
                category = 4;
            } 
            else {
                category = 0;
            }

            // Switch-case for grade
            switch (category) {
                case 1:
                    System.out.println("Grade: A");
                    break;

                case 2:
                    System.out.println("Grade: B");
                    break;

                case 3:
                    System.out.println("Grade: C");
                    break;

                case 4:
                    System.out.println("Grade: F");
                    break;

                default:
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