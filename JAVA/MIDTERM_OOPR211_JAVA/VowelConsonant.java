import java.util.Scanner;

public class VowelConsonant {


    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a letter: ");
        char letter = input.next().charAt(0);

        if (letter == 'A' || letter == 'E' || letter == 'I' ||
            letter == 'O' || letter == 'U' ||
            letter == 'a' || letter == 'e' || letter == 'i' ||
            letter == 'o' || letter == 'u') {

            System.out.println("It's a vowel!");
        } else {
            System.out.println("It's a consonant!");
            
        }
    }
}