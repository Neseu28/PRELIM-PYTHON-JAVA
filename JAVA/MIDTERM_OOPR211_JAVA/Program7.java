import java.io.*;
import java.util.*;

class Employee {
    int eno;
    String ename;
    String mobile;

    Employee(int eno, String ename, String mobile) {
        this.eno = eno;
        this.ename = ename;
        this.mobile = mobile;
    }
}

public class Program7 {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        ArrayList<Employee> employees = new ArrayList<>();

        String choice;

        do {

            System.out.println("Choose the program you want to run");
            System.out.println();
            System.out.println("Number 1");
            System.out.println("Number 2");
            System.out.println("Number 3");
            System.out.println("Number 4");
            System.out.println("Number 5");
            System.out.println("Number 6");
            System.out.println("Number 7");

            System.out.print("\nEnter your choice: ");
            int number = input.nextInt();

            if (number == 7) {

                try {

                    BufferedReader br =
                            new BufferedReader(new FileReader("emp.txt"));

                    String line;

                    // Read each line from the text file
                    while ((line = br.readLine()) != null) {

                        // Split the data using TAB
                        String[] data = line.split("\\t");

                        // Skip header
                        if (data[0].equalsIgnoreCase("eno")) {
                            continue;
                        }

                        int eno = Integer.parseInt(data[0]);
                        String ename = data[1];
                        String mobile = data[2];

                        // Store in ArrayList
                        employees.add(
                            new Employee(eno, ename, mobile)
                        );
                    }

                    br.close();

                    // Display the data
                    System.out.println();
                    System.out.println("ENO\tENAME\t\tMOBILE");
                    System.out.println("----------------------------------------");

                    for (Employee emp : employees) {
                        System.out.println(
                            emp.eno + "\t" +
                            emp.ename + "\t\t" +
                            emp.mobile
                        );
                    }

                } catch (Exception e) {
                    System.out.println("Error: " + e.getMessage());
                }

            } else {
                System.out.println("You selected Number " + number);
            }

            System.out.print("\nDo you want to continue? Y/N: ");
            choice = input.next();

            System.out.println();

        } while (choice.equalsIgnoreCase("Y"));

        System.out.println("Program ended.");

        input.close();
    }
}