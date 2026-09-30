import java.util.Scanner;

public class Program4 {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Enter Size of Array: ");
        int size = input.nextInt();

        int[] numbers = new int[size];

        System.out.println("Enter any " + size + " elements in Array:");

        for (int i = 0; i < size; i++) {
            numbers[i] = input.nextInt();
        }

        System.out.print("Even Elements: ");

        for (int i = 0; i < size; i++) {
            if (numbers[i] % 2 == 0) {
                System.out.print(numbers[i] + " ");
            }
        }

        System.out.print("\nOdd Elements: ");

        for (int i = 0; i < size; i++) {
            if (numbers[i] % 2 != 0) {
                System.out.print(numbers[i] + " ");
            }
        }
    }
}