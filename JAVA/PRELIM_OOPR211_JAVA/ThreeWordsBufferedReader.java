import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class ThreeWordsBufferedReader {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(
            new InputStreamReader(System.in)
        );

        System.out.print("Enter first word: ");
        String word1 = input.readLine();

        System.out.print("Enter second word: ");
        String word2 = input.readLine();

        System.out.print("Enter third word: ");
        String word3 = input.readLine();

        System.out.println("\n" + word1 + " " + word2 + " " + word3);
    }
}