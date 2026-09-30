import java.util.Scanner;

public class Program1 {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        double[] numbers = new double[10];

        // Input 10 real numbers
        System.out.println("Enter 10 real numbers:");

        for (int i = 0; i < 10; i++) {
            numbers[i] = input.nextDouble();
        }

        // Find sum and average of positive numbers
        double sum = 0;
        int positiveCount = 0;

        for (int i = 0; i < 10; i++) {
            if (numbers[i] > 0) {
                sum = sum + numbers[i];
                positiveCount++;
            }
        }

        if (positiveCount > 0) {
            double average = sum / positiveCount;

            System.out.println("Sum of positive numbers: " + sum);
            System.out.println("Average of positive numbers: " + average);
        } else {
            System.out.println("There are no positive numbers.");
        }

        // Count negative numbers
        int negativeCount = 0;

        for (int i = 0; i < 10; i++) {
            if (numbers[i] < 0) {
                negativeCount++;
            }
        }

        System.out.println("Number of negative numbers: " + negativeCount);

        // Find minimum value
        double minimum = numbers[0];

        for (int i = 1; i < 10; i++) {
            if (numbers[i] < minimum) {
                minimum = numbers[i];
            }
        }

        System.out.println("Minimum value: " + minimum);
    }
}