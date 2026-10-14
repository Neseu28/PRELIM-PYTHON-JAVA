import java.util.Scanner;
import java.time.LocalDate;
import java.time.format.DateTimeParseException;
import java.time.temporal.ChronoUnit;

public class OOPMidddtermLabActivity2{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int totalPages = 0, pagesRead = 0;
        double percentage;
        long remainingDays;
        int pagesLeft, pagesPerDay;

        System.out.println("=== Welcome Nestor Guerrero ===");

        while (true) {
            System.out.print("Enter total pages of the book: ");
            if (input.hasNextInt()) {
                totalPages = input.nextInt();
                if (totalPages <= 0) {
                    System.out.println("Warning: Total pages must be greater than 0. Try again.\n");
                } else {
                    break; 
                }
            } else {
                System.out.println("Warning: Invalid input. Please enter a valid number.\n");
                input.next(); 
            }
        }


        while (true) {
            System.out.print("Enter pages you have read: ");
            if (input.hasNextInt()) {
                pagesRead = input.nextInt();
                if (pagesRead < 0 || pagesRead > totalPages) {
                    System.out.println("Warning: Pages read cannot be negative or more than total pages (" + totalPages + "). Try again.\n");
                } else {
                    break; 
                }
            } else {
                System.out.println("Warning: Invalid input. Please enter a valid number.\n");
                input.next(); 
            }
        }

        input.nextLine(); 

        LocalDate issueDate = null;
        LocalDate dueDate = null;

        while (true) {
            try {
                System.out.print("Enter issue date (YYYY-MM-DD): ");
                issueDate = LocalDate.parse(input.nextLine());
                break; 
            } catch (DateTimeParseException e) {
                System.out.println("Warning: Invalid date format. Please use YYYY-MM-DD.\n");
            }
        }

        while (true) {
            try {
                System.out.print("Enter due date (YYYY-MM-DD): ");
                dueDate = LocalDate.parse(input.nextLine());
                
                if (dueDate.isBefore(issueDate)) {
                    System.out.println("Warning: Due date cannot be before issue date. Try again.\n");
                } else {
                    break; 
                }
            } catch (DateTimeParseException e) {
                System.out.println("Warning: Invalid date format. Please use YYYY-MM-DD.\n");
            }
        }

    
        LocalDate today = LocalDate.now();
        percentage = (double) pagesRead / totalPages * 100;
        pagesLeft = totalPages - pagesRead;
        remainingDays = ChronoUnit.DAYS.between(today, dueDate);

        System.out.println("\n=== SUMMARY ===");
        System.out.printf("You have read %.0f%% of the book.%n", percentage);

        if (remainingDays < 0) {
            System.out.println("Your book is overdue.");
        } else if (remainingDays == 0) {
            System.out.println("Your book is due today.");
        } else {
            System.out.println("You have " + remainingDays + " days remaining to return the book.");
        }

        System.out.println("You have " + pagesLeft + " pages left to read.");

        if (pagesLeft == 0) {
            System.out.println("You have finished the book!");
        } else if (remainingDays > 0) {
            pagesPerDay = (int) Math.ceil((double) pagesLeft / remainingDays);
            System.out.println("You should read " + pagesPerDay + " pages per day.");
        } else {
            System.out.println("The book must be returned now.");
        }

        input.close();
    }
}
