public class Program5 {
    public static void main(String[] args) {

        for (int i = 1; i <= 4; i++) {

            System.out.print("*");

            for (int j = 1; j <= i - 1; j++) {
                System.out.print("A*");
            }

            System.out.println();
        }
    }
}