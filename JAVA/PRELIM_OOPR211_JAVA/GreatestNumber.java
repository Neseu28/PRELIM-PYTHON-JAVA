import java.util.Scanner;

public class GreatestNumber {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter first number: ");
        double num1 = input.nextDouble();

        System.out.print("Enter second number: ");
        double num2 = input.nextDouble();

        System.out.print("Enter third number: ");
        double num3 = input.nextDouble();

        double highest;

        if (num1 >= num2 && num1 >= num3) {
            highest = num1;
        } 
        else if (num2 >= num1 && num2 >= num3) {
            highest = num2;
        } 
        else {
            highest = num3;
        }

        System.out.println("\nThe highest number is " + highest);

        input.close();
    }
}