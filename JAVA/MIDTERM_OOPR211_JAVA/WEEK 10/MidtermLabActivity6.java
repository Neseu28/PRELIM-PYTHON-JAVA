import java.util.ArrayList;
import java.util.Scanner;

/* WEEK 10
 * OOP MIDTERM - LAB ACTIVITY #6
 */
public class MidtermLabActivity6 {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int choice;
        do {
            System.out.println("\n========== OOP MIDTERM LAB ACTIVITY #6 ==========");
            System.out.println("1. Bank Account (withdraw and deposit)");
            System.out.println("2. Hospital Patient Database");
            System.out.println("3. Professor, Dean, and Executive");
            System.out.println("4. Exit");
            choice = readInt("Select an option: ");

            switch (choice) {
                case 1:
                    runBankProgram();
                    break;
                case 2:
                    runHospitalProgram();
                    break;
                case 3:
                    runProfessorProgram();
                    break;
                case 4:
                    System.out.println("Thank you for using the system!");
                    break;
                default:
                    System.out.println("Invalid option. Please select 1 to 4.");
            }
        } while (choice != 4);

        scanner.close();
    }

    // -------------------- PROGRAM 1: BANK ACCOUNT --------------------

    private static void runBankProgram() {
        System.out.println("\nWelcome!");
        double balance = readNonNegativeDouble("Enter your balance: ");

        int option;
        do {
            System.out.println("--------------------------------------------------");
            System.out.println("Select an option:");
            System.out.println("1. Withdraw Amount");
            System.out.println("2. Deposit Amount");
            System.out.println("3. Exit");
            option = readInt("Option: ");

            switch (option) {
                case 1: {
                    double amount = readPositiveDouble(
                        "How much amount do you want to withdraw from your account? Amount: ");
                    if (amount > balance) {
                        System.out.printf("Insufficient balance. Your balance is: %.2f%n", balance);
                    } else {
                        balance -= amount;
                        System.out.printf("Your new balance is: %.2f%n", balance);
                    }
                    break;
                }
                case 2: {
                    double amount = readPositiveDouble(
                        "How much amount do you want to deposit in your account? Amount: ");
                    balance += amount;
                    System.out.printf("Your new balance is: %.2f%n", balance);
                    break;
                }
                case 3:
                    System.out.println("Thank you for using the system!");
                    break;
                default:
                    System.out.println("Invalid option. Please select 1 to 3.");
            }
        } while (option != 3);
    }

    // -------------------- PROGRAM 2: HOSPITAL DATABASE --------------------

    // Date structure equivalent in Java.
    static class PatientDate {
        private final int year;
        private final int month;
        private final int day;

        PatientDate(int year, int month, int day) {
            this.year = year;
            this.month = month;
            this.day = day;
        }

        @Override
        public String toString() {
            return String.format("%04d-%02d-%02d", year, month, day);
        }
    }

    // Base class stores general patient information.
    static class Patient {
        private final String name;
        private final PatientDate admissionDate;
        private final String disease;
        private final PatientDate dischargeDate;

        Patient(String name, PatientDate admissionDate, String disease,
                PatientDate dischargeDate) {
            this.name = name;
            this.admissionDate = admissionDate;
            this.disease = disease;
            this.dischargeDate = dischargeDate;
        }

        public String getName() {
            return name;
        }

        public void displayInformation() {
            System.out.println("Name: " + name);
            System.out.println("Date of admission: " + admissionDate);
            System.out.println("Disease: " + disease);
            System.out.println("Date of discharge: " + dischargeDate);
        }
    }

    // Derived class stores age.
    static class PediatricPatient extends Patient {
        private final int age;

        PediatricPatient(String name, PatientDate admissionDate, String disease,
                         PatientDate dischargeDate, int age) {
            super(name, admissionDate, disease, dischargeDate);
            this.age = age;
        }

        public int getAge() {
            return age;
        }

        @Override
        public void displayInformation() {
            super.displayInformation();
            System.out.println("Age: " + age);
        }
    }

    private static void runHospitalProgram() {
        ArrayList<Patient> patients = new ArrayList<>();
        int option;

        do {
            System.out.println("\n========== HOSPITAL PATIENT DATABASE ==========");
            System.out.println("1. Insert New Patient");
            System.out.println("2. Display All Patients");
            System.out.println("3. Display Pediatric Patients (under 12)");
            System.out.println("4. Exit");
            option = readInt("Select an option: ");

            switch (option) {
                case 1:
                    Patient patient = readPatient();
                    patients.add(patient);
                    System.out.println("Patient added successfully.");
                    break;
                case 2:
                    displayAllPatients(patients);
                    break;
                case 3:
                    displayPediatricPatients(patients);
                    break;
                case 4:
                    System.out.println("Returning to main menu.");
                    break;
                default:
                    System.out.println("Invalid option. Please select 1 to 4.");
            }
        } while (option != 4);
    }

    private static Patient readPatient() {
        System.out.print("Name of patient: ");
        String name = scanner.nextLine().trim();
        while (name.isEmpty()) {
            System.out.print("Name cannot be empty. Enter name: ");
            name = scanner.nextLine().trim();
        }

        PatientDate admission = readDate("Date of admission");
        System.out.print("Disease: ");
        String disease = scanner.nextLine().trim();
        while (disease.isEmpty()) {
            System.out.print("Disease cannot be empty. Enter disease: ");
            disease = scanner.nextLine().trim();
        }
        PatientDate discharge = readDate("Date of discharge");
        int age = readInt("Age: ");
        while (age < 0 || age > 130) {
            System.out.println("Please enter a valid age from 0 to 130.");
            age = readInt("Age: ");
        }

        // The derived patient class stores age for all patient records.
        return new PediatricPatient(name, admission, disease, discharge, age);
    }

    private static PatientDate readDate(String label) {
        System.out.println(label + " (enter year, month, and day):");
        int year = readInt("Year: ");
        int month = readInt("Month (1-12): ");
        int day = readInt("Day (1-31): ");
        while (year < 1 || month < 1 || month > 12 || day < 1 || day > 31) {
            System.out.println("Invalid date values. Please enter the date again.");
            year = readInt("Year: ");
            month = readInt("Month (1-12): ");
            day = readInt("Day (1-31): ");
        }
        return new PatientDate(year, month, day);
    }

    private static void displayAllPatients(ArrayList<Patient> patients) {
        if (patients.isEmpty()) {
            System.out.println("No patient records found.");
            return;
        }

        System.out.println("\n========== ALL PATIENTS ==========");
        for (int i = 0; i < patients.size(); i++) {
            System.out.println("\nPatient #" + (i + 1));
            patients.get(i).displayInformation();
        }
    }

    private static void displayPediatricPatients(ArrayList<Patient> patients) {
        boolean found = false;
        System.out.println("\n========== PEDIATRIC PATIENTS (UNDER 12) ==========");
        for (Patient patient : patients) {
            if (patient instanceof PediatricPatient) {
                PediatricPatient pediatric = (PediatricPatient) patient;
                if (pediatric.getAge() < 12) {
                    pediatric.displayInformation();
                    System.out.println("-----------------------------------");
                    found = true;
                }
            }
        }
        if (!found) {
            System.out.println("No pediatric patients found.");
        }
    }

    // -------------------- PROGRAM 3: PROFESSOR, DEAN, EXECUTIVE --------------------

    static class Professor {
        protected final String name;
        protected final double salary;

        Professor(String name, double salary) {
            this.name = name;
            this.salary = salary;
        }

        @Override
        public String toString() {
            return "Name: " + name + "\nSalary: " + money(salary);
        }
    }

    // Dean inherits name and salary from Professor and adds department.
    static class Dean extends Professor {
        private final String department;

        Dean(String name, String department, double salary) {
            super(name, salary);
            this.department = department;
        }

        @Override
        public String toString() {
            return "Rank: Dean\nName: " + name
                + "\nDepartment: " + department
                + "\nSalary: " + money(salary);
        }
    }

    // Executive inherits the Dean class.
    static class Executive extends Dean {
        Executive(String name, String department, double salary) {
            super(name, department, salary);
        }

        @Override
        public String toString() {
            return "Rank: Executive\n" + super.toString().replaceFirst("Rank: Dean\\n", "");
        }
    }

    private static void runProfessorProgram() {
        System.out.println("\n========== PROFESSOR / DEAN / EXECUTIVE ==========");

        System.out.println("\nEnter Dean information");
        System.out.print("Name: ");
        String deanName = scanner.nextLine().trim();
        System.out.print("Department: ");
        String deanDepartment = scanner.nextLine().trim();
        double deanSalary = readNonNegativeDouble("Salary: ");
        Dean dean = new Dean(deanName, deanDepartment, deanSalary);

        System.out.println("\nEnter Executive information");
        System.out.print("Name: ");
        String executiveName = scanner.nextLine().trim();
        System.out.print("Department: ");
        String executiveDepartment = scanner.nextLine().trim();
        double executiveSalary = readNonNegativeDouble("Salary: ");
        Executive executive = new Executive(executiveName, executiveDepartment, executiveSalary);

        System.out.println("\nStatus");
        System.out.println(dean);
        System.out.println("\nStatus");
        System.out.println(executive);
    }

    // -------------------- INPUT HELPERS --------------------

    private static int readInt(String prompt) {
        while (true) {
            System.out.print(prompt);
            String input = scanner.nextLine().trim();
            try {
                return Integer.parseInt(input);
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a whole number.");
            }
        }
    }

    private static double readNonNegativeDouble(String prompt) {
        while (true) {
            double value = readDouble(prompt);
            if (value >= 0) {
                return value;
            }
            System.out.println("Value cannot be negative.");
        }
    }

    private static double readPositiveDouble(String prompt) {
        while (true) {
            double value = readDouble(prompt);
            if (value > 0) {
                return value;
            }
            System.out.println("Amount must be greater than zero.");
        }
    }

    private static double readDouble(String prompt) {
        while (true) {
            System.out.print(prompt);
            String input = scanner.nextLine().trim().replace(",", "");
            try {
                double value = Double.parseDouble(input);
                if (!Double.isNaN(value) && !Double.isInfinite(value)) {
                    return value;
                }
            } catch (NumberFormatException ignored) {
                // Display the message below.
            }
            System.out.println("Invalid amount. Enter a valid number.");
        }
    }

    private static String money(double value) {
        return String.format("₱%.2f", value);
    }
}
