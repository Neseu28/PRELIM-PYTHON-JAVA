import java.util.Scanner;

/* WEEK 10
 * OOPR - MIDTERM LAB ACTIVITY 5
 * Console Banking System
 */

// Abstract parent class
abstract class Account {
    private final String accountNumber;
    private double balance;

    public Account(String accountNumber, double openingBalance) {
        this.accountNumber = accountNumber;
        this.balance = openingBalance;
    }

    public String getAccountNumber() {
        return accountNumber;
    }

    public double getBalance() {
        return balance;
    }

    public boolean deposit(double amount) {
        if (amount <= 0) {
            System.out.println("Invalid deposit. Amount must be greater than zero.");
            return false;
        }

        balance += amount;
        return true;
    }

    public boolean withdraw(double amount) {
        if (amount <= 0) {
            System.out.println("Invalid withdrawal. Amount must be greater than zero.");
            return false;
        }

        // Polymorphism: the fee depends on the actual account object.
        double fee = calculateWithdrawalFee();

        if (balance < amount + fee) {
            System.out.printf(
                "Insufficient funds. Your balance is ₱%.2f; withdrawal plus fee is ₱%.2f.%n",
                balance, amount + fee
            );
            return false;
        }

        balance -= amount + fee;
        System.out.printf("Withdrawal fee: ₱%.2f | ", fee);
        System.out.printf("New %s balance: ₱%.2f%n", getAccountType(), balance);
        return true;
    }

    public abstract double calculateWithdrawalFee();

    public abstract String getAccountType();
}

// Savings account has no withdrawal fee.
class SavingsAccount extends Account {
    public SavingsAccount(String accountNumber, double openingBalance) {
        super(accountNumber, openingBalance);
    }

    @Override
    public double calculateWithdrawalFee() {
        return 0.0;
    }

    @Override
    public String getAccountType() {
        return "Savings";
    }
}

// Checking account charges a flat ₱10 withdrawal fee.
class CheckingAccount extends Account {
    public CheckingAccount(String accountNumber, double openingBalance) {
        super(accountNumber, openingBalance);
    }

    @Override
    public double calculateWithdrawalFee() {
        return 10.0;
    }

    @Override
    public String getAccountType() {
        return "Checking";
    }
}

// Main application
public class BankingApp {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("Welcome to the OOP Banking System");

        double openingBalance = readNonNegativeBalance();

        // Both accounts start with the same opening balance but keep separate balances.
        SavingsAccount savingsAccount =
            new SavingsAccount("SAV-1001", openingBalance);
        CheckingAccount checkingAccount =
            new CheckingAccount("CHK-1001", openingBalance);

        // The selected account can refer to either subclass.
        Account selectedAccount = savingsAccount;

        printAccountSummary(selectedAccount);

        boolean running = true;
        while (running) {
            showMenu();
            int choice = readInt("Choice: ");

            switch (choice) {
                case 1: {
                    double amount = readPositiveAmount("Amount to withdraw: ");
                    selectedAccount.withdraw(amount);
                    break;
                }
                case 2: {
                    double amount = readPositiveAmount("Amount to deposit: ");
                    if (selectedAccount.deposit(amount)) {
                        System.out.printf("New %s balance: ₱%.2f%n",
                            selectedAccount.getAccountType(),
                            selectedAccount.getBalance());
                    }
                    break;
                }
                case 3:
                    printAccountSummary(selectedAccount);
                    break;
                case 4:
                    if (selectedAccount == savingsAccount) {
                        selectedAccount = checkingAccount;
                    } else {
                        selectedAccount = savingsAccount;
                    }
                    System.out.println("Account switched successfully.");
                    printAccountSummary(selectedAccount);
                    break;
                case 5:
                    running = false;
                    System.out.println("Thank you for using the system!");
                    break;
                default:
                    System.out.println("Invalid menu choice. Please choose 1 to 5.");
            }
            if (running) {
                System.out.println();
            }
        }

        scanner.close();
    }

    public static void showMenu() {
        System.out.println("1 Withdraw");
        System.out.println("2 Deposit");
        System.out.println("3 Show balance");
        System.out.println("4 Switch account");
        System.out.println("5 Exit");
    }

    public static double readNonNegativeBalance() {
        while (true) {
            double amount = readDouble("Opening balance: ");
            if (amount >= 0) {
                return amount;
            }
            System.out.println("Invalid opening balance. Enter zero or a positive amount.");
        }
    }

    public static double readPositiveAmount(String prompt) {
        while (true) {
            double amount = readDouble(prompt);
            if (amount > 0) {
                return amount;
            }
            System.out.println("Invalid amount. Enter an amount greater than zero.");
        }
    }

    public static void printAccountSummary(Account account) {
        System.out.printf("Current account: %s | Balance: ₱%.2f%n",
            account.getAccountType(), account.getBalance());
        System.out.println("Account number: " + account.getAccountNumber());
    }

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

    private static double readDouble(String prompt) {
        while (true) {
            System.out.print(prompt);
            String input = scanner.nextLine().trim().replace(",", "");
            try {
                double amount = Double.parseDouble(input);
                if (Double.isNaN(amount) || Double.isInfinite(amount)) {
                    System.out.println("Please enter a valid finite amount.");
                } else {
                    return amount;
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid amount. Please enter a number, such as 1234.50.");
            }
        }
    }
}
