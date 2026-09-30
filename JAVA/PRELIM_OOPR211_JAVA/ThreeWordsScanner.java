import java.util.Scanner;

public class ThreeWordsScanner {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter first word: ");
        String word1 = input.nextLine();

        System.out.print("Enter second word: ");
        String word2 = input.nextLine();

        System.out.print("Enter third word: ");
        String word3 = input.nextLine();

        System.out.println("\n" + word1 + " " + word2 + " " + word3);

        input.close();
    }
}