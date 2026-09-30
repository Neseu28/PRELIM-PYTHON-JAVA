import java.util.Scanner;

public class Program2 {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int[] numbers = new int[8];

        System.out.println("Enter 8 integers:");

        for (int i = 0; i < 8; i++) {
            numbers[i] = input.nextInt();
        }

        // Remv duplicates
        int[] unique = new int[8];
        int uniqueCount = 0;

        for (int i = 0; i < 8; i++) {

            boolean duplicate = false;

            for (int j = 0; j < uniqueCount; j++) {
                if (numbers[i] == unique[j]) {
                    duplicate = true;
                    break;
                }
            }

            if (!duplicate) {
                unique[uniqueCount] = numbers[i];
                uniqueCount++;
            }
        }

        System.out.print("Array without duplicates: ");

        for (int i = 0; i < uniqueCount; i++) {
            System.out.print(unique[i] + " ");
        }

        //second largest and second smallest
        if (uniqueCount >= 2) {

            int largest = unique[0];
            int secondLargest = unique[0];

            int smallest = unique[0];
            int secondSmallest = unique[0];

            for (int i = 1; i < uniqueCount; i++) {

                if (unique[i] > largest) {
                    secondLargest = largest;
                    largest = unique[i];
                } else if (unique[i] > secondLargest) {
                    secondLargest = unique[i];
                }

                if (unique[i] < smallest) {
                    secondSmallest = smallest;
                    smallest = unique[i];
                } else if (unique[i] < secondSmallest) {
                    secondSmallest = unique[i];
                }
            }

            System.out.println();
            System.out.println("Second largest: " + secondLargest);
            System.out.println("Second smallest: " + secondSmallest);

        } else {
            System.out.println("\nNot enough unique elements.");
        }
    }
}
