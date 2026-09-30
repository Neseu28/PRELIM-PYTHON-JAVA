import java.util.Scanner;

public class Program3 {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int[] numbers = new int[5];

        System.out.print("Enter Data in Array: ");

        for (int i = 0; i < 5; i++) {
            numbers[i] = input.nextInt();
        }

        System.out.print("Stored Data in Array: ");

        for (int i = 0; i < 5; i++) {
            System.out.print(numbers[i] + " ");
        }

        System.out.print("\nEnter position of Element to Delete: ");
        int position = input.nextInt();

        // Convert position to array index
        int index = position - 1;

        if (position < 1 || position > 5) {

            System.out.println("Invalid position.");

        } else {

            // Shift elements to the left
            for (int i = index; i < 4; i++) {
                numbers[i] = numbers[i + 1];
            }

            System.out.print("New data in Array: ");

            for (int i = 0; i < 4; i++) {
                System.out.print(numbers[i] + " ");
            }
        }
    }
}