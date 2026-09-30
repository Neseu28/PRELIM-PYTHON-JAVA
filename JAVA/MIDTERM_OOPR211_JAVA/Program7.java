import java.io.*;

public class Program7 {

    public static void main(String[] args) {

        try {

            BufferedReader br = new BufferedReader(
                    new FileReader("data.txt"));

            // Skip the header
            br.readLine();

            String line;

            System.out.println("eno\t\t ename\t\t\t mobile");
            System.out.println("--------------------------------------------");

            while ((line = br.readLine()) != null) {

                // Separate the data using TAB
                String[] data = line.split("\t");

                System.out.println(
                        data[0] + "\t\t" +
                        data[1] + "\t\t" +
                        data[2]
                );
            }

            br.close();

        } catch (Exception e) {

            System.out.println("Error: " + e.getMessage());
        }
    }
}