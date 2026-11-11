import java.util.Scanner;

public class WEEK14_F_ACTIVITY_1_Java_Array {
    static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        int choice;

        do {
            System.out.println("\n===== JAVA ARRAY ACTIVITIES =====");
            System.out.println("1. Exam Score Statistics");
            System.out.println("2. Store Stock Reorder Report");
            System.out.println("3. Branch Sales Matrix");
            System.out.println("4. Classroom Seat Booking");
            System.out.println("5. Temperature Monitoring");
            System.out.println("6. Shopping Cart and Checkout");
            System.out.println("7. Warehouse Stock Transfers");
            System.out.println("8. Student Performance Analyzer");
            System.out.println("9. Theater Reservations");
            System.out.println("10. Weekly Inventory and Lost Sales");
            System.out.println("0. Exit");
            System.out.print("Choose a program: ");
            choice = input.nextInt();

            switch (choice) {
                case 1: examScores(); break;
                case 2: storeStock(); break;
                case 3: branchSales(); break;
                case 4: seatBooking(); break;
                case 5: temperatures(); break;
                case 6: shoppingCart(); break;
                case 7: warehouse(); break;
                case 8: studentPerformance(); break;
                case 9: theater(); break;
                case 10: weeklyInventory(); break;
                case 0: System.out.println("Goodbye!"); break;
                default: System.out.println("Invalid choice.");
            }
        } while (choice != 0);
    }

    static int getNumber(String message, int min, int max) {
        int number;
        do {
            System.out.print(message);
            number = input.nextInt();
            if (number < min || number > max)
                System.out.println("Invalid input. Enter " + min + " to " + max + ".");
        } while (number < min || number > max);
        return number;
    }

    // PROGRAM 1
    static void examScores() {
        int n = getNumber("Number of students (1-50): ", 1, 50);
        int[] scores = new int[n];
        int total = 0, highest = -1, lowest = 101, pass = 0, fail = 0;

        for (int i = 0; i < n; i++) {
            scores[i] = getNumber("Score of student " + (i + 1) + " (0-100): ", 0, 100);
            total += scores[i];
            if (scores[i] > highest) highest = scores[i];
            if (scores[i] < lowest) lowest = scores[i];
            if (scores[i] >= 75) pass++;
            else fail++;
        }

        System.out.printf("Average: %.2f%n", (double) total / n);
        System.out.println("Highest: " + highest + "\nLowest: " + lowest);
        System.out.println("Passed: " + pass + "\nFailed: " + fail);
        System.out.print("Highest score achieved by student(s): ");
        for (int i = 0; i < n; i++)
            if (scores[i] == highest) System.out.print((i + 1) + " ");
        System.out.println();
    }

    // PROGRAM 2
    static void storeStock() {
        String[] names = {"Notebook", "Pen", "Folder", "USB"};
        int[] reorder = {5, 10, 5, 2};
        int[] target = {20, 30, 20, 10};
        int totalStock = 0, totalOrder = 0;

        for (int i = 0; i < names.length; i++) {
            int stock = getNumber(names[i] + " stock (0-10000): ", 0, 10000);
            totalStock += stock;
            if (stock <= reorder[i]) {
                int order = target[i] - stock;
                totalOrder += order;
                System.out.println(names[i] + " - Reorder " + order + " units.");
            } else {
                System.out.println(names[i] + " - Stock is sufficient.");
            }
        }
        System.out.println("Total stock: " + totalStock);
        System.out.println("Total suggested order: " + totalOrder);
    }

    // PROGRAM 3
    static void branchSales() {
        int[][] sales = new int[3][5];
        int[] branchTotal = new int[3];
        int grandTotal = 0, highest = 0;

        for (int r = 0; r < 3; r++) {
            for (int c = 0; c < 5; c++) {
                sales[r][c] = getNumber("Branch " + (r + 1) + ", Day " + (c + 1) + " sales: ", 0, 1000000);
                branchTotal[r] += sales[r][c];
                grandTotal += sales[r][c];
            }
            if (branchTotal[r] > highest) highest = branchTotal[r];
        }

        for (int r = 0; r < 3; r++)
            System.out.println("Branch " + (r + 1) + " total: " + branchTotal[r]);

        for (int c = 0; c < 5; c++) {
            int dayTotal = 0;
            for (int r = 0; r < 3; r++) dayTotal += sales[r][c];
            System.out.println("Day " + (c + 1) + " total: " + dayTotal);
        }

        System.out.println("Grand total: " + grandTotal);
        System.out.println("Highest branch total: " + highest);
        System.out.print("Branch(es) with highest total: ");
        for (int r = 0; r < 3; r++)
            if (branchTotal[r] == highest) System.out.print((r + 1) + " ");
        System.out.println();
    }

    // PROGRAM 4
    static void seatBooking() {
        int[][] seats = new int[4][5];
        int choice;

        do {
            showSeats(seats);
            System.out.println("1. Book seat  2. Cancel seat  3. Display seats  0. Exit");
            System.out.print("Choose: ");
            choice = input.nextInt();

            if (choice == 1 || choice == 2) {
                int row = getNumber("Row (1-4): ", 1, 4) - 1;
                int col = getNumber("Column (1-5): ", 1, 5) - 1;

                if (choice == 1) {
                    if (seats[row][col] == 0) {
                        seats[row][col] = 1;
                        System.out.println("Seat booked.");
                    } else System.out.println("Seat is already booked.");
                } else {
                    if (seats[row][col] == 1) {
                        seats[row][col] = 0;
                        System.out.println("Booking cancelled.");
                    } else System.out.println("Seat is already available.");
                }
            } else if (choice != 0 && choice != 3) {
                System.out.println("Invalid choice.");
            }

            if (choice != 0) {
                int available = 0;
                for (int r = 0; r < 4; r++)
                    for (int c = 0; c < 5; c++)
                        if (seats[r][c] == 0) available++;
                System.out.println("Available seats: " + available);
            }
        } while (choice != 0);
    }

    static void showSeats(int[][] seats) {
        System.out.println("\nSeats (0 = Available, 1 = Booked)");
        for (int r = 0; r < 4; r++) {
            for (int c = 0; c < 5; c++) System.out.print(seats[r][c] + " ");
            System.out.println();
        }
    }

    // PROGRAM 5
    static void temperatures() {
        int[][] temp = new int[3][4];
        int highest = -21;

        for (int r = 0; r < 3; r++) {
            for (int c = 0; c < 4; c++) {
                temp[r][c] = getNumber("Sensor " + (r + 1) + ", Period " + (c + 1) + " (-20 to 60): ", -20, 60);
                if (temp[r][c] > highest) highest = temp[r][c];
            }
        }

        for (int r = 0; r < 3; r++) {
            int total = 0;
            for (int c = 0; c < 4; c++) {
                total += temp[r][c];
                if (temp[r][c] > 35)
                    System.out.println("ALERT: Sensor " + (r + 1) + ", Period " + (c + 1) + " = " + temp[r][c]);
            }
            System.out.printf("Sensor %d average: %.2f%n", r + 1, total / 4.0);
        }

        System.out.println("Highest temperature: " + highest);
        System.out.print("Location(s): ");
        for (int r = 0; r < 3; r++)
            for (int c = 0; c < 4; c++)
                if (temp[r][c] == highest)
                    System.out.print("(Sensor " + (r + 1) + ", Period " + (c + 1) + ") ");
        System.out.println();
    }

    // PROGRAM 6
    static void shoppingCart() {
        String[] names = {"USB", "Notebook", "Pen", "Folder"};
        int[] price = {350, 200, 20, 15};
        int[] stock = {10, 10, 20, 20};
        int[] cart = new int[4];
        int choice;

        do {
            System.out.println("\n1. Add item  2. Remove quantity  3. View cart  4. Pay  5. Cancel");
            System.out.print("Choose: ");
            choice = input.nextInt();

            if (choice == 1 || choice == 2) {
                for (int i = 0; i < 4; i++)
                    System.out.println((i + 1) + ". " + names[i] + " - PHP " + price[i] + " (Stock: " + stock[i] + ")");
                int item = getNumber("Select product (1-4): ", 1, 4) - 1;
                int quantity = getNumber("Quantity: ", 1, 10000);

                if (choice == 1) {
                    if (cart[item] + quantity <= stock[item]) cart[item] += quantity;
                    else System.out.println("Not enough stock.");
                } else {
                    if (quantity <= cart[item]) cart[item] -= quantity;
                    else System.out.println("Quantity is greater than cart quantity.");
                }
            } else if (choice == 3) {
                showCart(names, price, cart);
            } else if (choice == 4) {
                int subtotal = 0;
                for (int i = 0; i < 4; i++) subtotal += cart[i] * price[i];

                if (subtotal == 0) {
                    System.out.println("Cart is empty.");
                } else {
                    int discount = subtotal >= 1000 ? (int) Math.floor(subtotal * 0.10 + 0.5) : 0;
                    int total = subtotal - discount;
                    System.out.println("Subtotal: PHP " + subtotal);
                    System.out.println("Discount: PHP " + discount);
                    System.out.println("Total: PHP " + total);
                    int cash = getNumber("Cash payment: PHP ", 0, 100000000);
                    if (cash >= total) {
                        for (int i = 0; i < 4; i++) stock[i] -= cart[i];
                        System.out.println("Payment successful. Change: PHP " + (cash - total));
                        for (int i = 0; i < 4; i++) cart[i] = 0;
                        choice = 5;
                    } else System.out.println("Insufficient payment. Cart unchanged.");
                }
            } else if (choice == 5) {
                System.out.println("Sale cancelled.");
            } else if (choice != 0) {
                System.out.println("Invalid choice.");
            }
        } while (choice != 0 && choice != 5);
    }

    static void showCart(String[] names, int[] price, int[] cart) {
        int subtotal = 0;
        for (int i = 0; i < 4; i++) {
            System.out.println(names[i] + ": " + cart[i] + " x PHP " + price[i]);
            subtotal += cart[i] * price[i];
        }
        System.out.println("Subtotal: PHP " + subtotal);
    }

    // PROGRAM 7
    static void warehouse() {
        int[][] stock = {
            {20, 30, 40, 50},
            {15, 25, 35, 45},
            {10, 20, 30, 40}
        };
        int[][] history = new int[50][4];
        int count = 0, choice;

        do {
            System.out.println("\n1. Transfer stock  2. Display stock  3. Show history  0. Exit");
            System.out.print("Choose: ");
            choice = input.nextInt();

            if (choice == 1) {
                int from = getNumber("Source warehouse (1-3): ", 1, 3) - 1;
                int to = getNumber("Destination warehouse (1-3): ", 1, 3) - 1;
                int product = getNumber("Product number (1-4): ", 1, 4) - 1;
                int quantity = getNumber("Quantity: ", 1, 1000);

                if (from == to) System.out.println("Warehouses must be different.");
                else if (stock[from][product] < quantity) System.out.println("Not enough stock.");
                else if (stock[to][product] + quantity > 1000) System.out.println("Destination capacity exceeded.");
                else if (count == 50) System.out.println("Transfer history is full.");
                else {
                    stock[from][product] -= quantity;
                    stock[to][product] += quantity;
                    history[count][0] = from + 1;
                    history[count][1] = to + 1;
                    history[count][2] = product + 1;
                    history[count][3] = quantity;
                    count++;
                    System.out.println("Transfer successful.");
                }
            } else if (choice == 2) {
                for (int r = 0; r < 3; r++) {
                    System.out.print("Warehouse " + (r + 1) + ": ");
                    for (int c = 0; c < 4; c++) System.out.print(stock[r][c] + " ");
                    System.out.println();
                }
                for (int c = 0; c < 4; c++) {
                    int total = 0;
                    for (int r = 0; r < 3; r++) total += stock[r][c];
                    System.out.println("Product " + (c + 1) + " total: " + total);
                }
            } else if (choice == 3) {
                for (int i = 0; i < count; i++)
                    System.out.println("From W" + history[i][0] + " to W" + history[i][1]
                            + ", Product " + history[i][2] + ", Quantity " + history[i][3]);
            } else if (choice != 0) System.out.println("Invalid choice.");
        } while (choice != 0);
    }

    // PROGRAM 8
    static void studentPerformance() {
        int n = getNumber("Number of students (2-10): ", 2, 10);
        int[][] marks = new int[n][4];
        double[] average = new double[n];
        int[] order = new int[n];
        double[] subjectAverage = new double[4];

        for (int r = 0; r < n; r++) {
            int total = 0;
            boolean qualified = true;
            for (int c = 0; c < 4; c++) {
                marks[r][c] = getNumber("Student " + (r + 1) + ", Subject " + (c + 1) + " score: ", 0, 100);
                total += marks[r][c];
                subjectAverage[c] += marks[r][c];
                if (marks[r][c] < 60) qualified = false;
            }
            average[r] = total / 4.0;
            if (average[r] < 75) qualified = false;
            System.out.printf("Student %d average: %.2f - %s%n", r + 1, average[r], qualified ? "Qualified" : "Not Qualified");
            order[r] = r;
        }

        double lowest = Double.MAX_VALUE;
        for (int c = 0; c < 4; c++) {
            subjectAverage[c] /= n;
            if (subjectAverage[c] < lowest) lowest = subjectAverage[c];
        }
        System.out.println("Lowest subject average: " + lowest);
        for (int c = 0; c < 4; c++)
            if (subjectAverage[c] == lowest) System.out.println("Subject " + (c + 1) + " has the lowest average.");

        // Simple manual selection sort of student indexes
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (average[order[j]] > average[order[i]]) {
                    int temp = order[i];
                    order[i] = order[j];
                    order[j] = temp;
                }
            }
        }

        System.out.println("Student rankings:");
        int rank = 1;
        for (int i = 0; i < n; i++) {
            if (i > 0 && average[order[i]] != average[order[i - 1]]) rank = i + 1;
            System.out.printf("Rank %d - Student %d (%.2f)%n", rank, order[i] + 1, average[order[i]]);
        }
    }

    // PROGRAM 9
    static void theater() {
        int[][] seats = new int[5][8];
        int nextId = 1, choice;

        do {
            System.out.println("\n1. Book group  2. Cancel booking  3. Display seats  0. Exit");
            System.out.print("Choose: ");
            choice = input.nextInt();

            if (choice == 1) {
                int group = getNumber("Group size (1-8): ", 1, 8);
                int foundRow = -1, foundCol = -1;

                for (int r = 0; r < 5 && foundRow == -1; r++) {
                    for (int c = 0; c <= 8 - group; c++) {
                        boolean free = true;
                        for (int k = 0; k < group; k++)
                            if (seats[r][c + k] != 0) free = false;
                        if (free) {
                            foundRow = r;
                            foundCol = c;
                            break;
                        }
                    }
                }

                if (foundRow == -1) System.out.println("No consecutive seats available.");
                else {
                    for (int k = 0; k < group; k++) seats[foundRow][foundCol + k] = nextId;
                    System.out.println("Booking successful. Booking ID: " + nextId);
                    nextId++;
                }
            } else if (choice == 2) {
                int id = getNumber("Booking ID: ", 1, 1000000);
                boolean found = false;
                for (int r = 0; r < 5; r++)
                    for (int c = 0; c < 8; c++)
                        if (seats[r][c] == id) {
                            seats[r][c] = 0;
                            found = true;
                        }
                System.out.println(found ? "Booking cancelled." : "Booking ID not found.");
            } else if (choice == 3) {
                for (int r = 0; r < 5; r++) {
                    for (int c = 0; c < 8; c++) System.out.print(seats[r][c] + "\t");
                    System.out.println();
                }
                int available = 0;
                for (int r = 0; r < 5; r++)
                    for (int c = 0; c < 8; c++)
                        if (seats[r][c] == 0) available++;
                System.out.println("Available seats: " + available);
            } else if (choice != 0) System.out.println("Invalid choice.");
        } while (choice != 0);
    }

    // PROGRAM 10
    static void weeklyInventory() {
        String[] names = {"Product 1", "Product 2", "Product 3"};
        int[] stock = {10, 15, 20};
        int[] reorder = {5, 5, 5};
        int[] price = {100, 50, 25};
        int[][] received = new int[3][7];
        int[][] demand = new int[3][7];
        int[][] sold = new int[3][7];
        int[][] closing = new int[3][7];
        int[] lost = new int[3];
        int[] unitsSold = new int[3];
        int[] revenue = new int[3];
        int[] dailyRevenue = new int[7];
        int openingTotal = 0, deliveryTotal = 0, salesTotal = 0;

        for (int p = 0; p < 3; p++) openingTotal += stock[p];

        for (int day = 0; day < 7; day++) {
            System.out.println("\nDAY " + (day + 1));
            for (int p = 0; p < 3; p++) {
                received[p][day] = getNumber(names[p] + " delivery (0-1000): ", 0, 1000);
                demand[p][day] = getNumber(names[p] + " demand (0-1000): ", 0, 1000);
                deliveryTotal += received[p][day];

                int available = stock[p] + received[p][day];
                sold[p][day] = Math.min(demand[p][day], available);
                lost[p] += demand[p][day] - sold[p][day];
                unitsSold[p] += sold[p][day];
                revenue[p] += sold[p][day] * price[p];
                dailyRevenue[day] += sold[p][day] * price[p];
                stock[p] = available - sold[p][day];
                closing[p][day] = stock[p];
                salesTotal += sold[p][day];
            }
        }

        for (int p = 0; p < 3; p++) {
            System.out.println("\n" + names[p]);
            System.out.println("Units sold: " + unitsSold[p]);
            System.out.println("Lost units: " + lost[p]);
            System.out.println("Revenue: PHP " + revenue[p]);
            System.out.println("Final stock: " + stock[p]);
            if (stock[p] <= reorder[p]) System.out.println("LOW STOCK ALERT");
        }

        int highestRevenue = dailyRevenue[0];
        for (int day = 1; day < 7; day++)
            if (dailyRevenue[day] > highestRevenue) highestRevenue = dailyRevenue[day];

        System.out.println("\nDaily revenue:");
        for (int day = 0; day < 7; day++)
            System.out.println("Day " + (day + 1) + ": PHP " + dailyRevenue[day]);

        System.out.println("Highest daily revenue: PHP " + highestRevenue);
        System.out.print("Day(s): ");
        for (int day = 0; day < 7; day++)
            if (dailyRevenue[day] == highestRevenue) System.out.print((day + 1) + " ");
        System.out.println();

        System.out.println("Stock check: Opening stock + deliveries - sales = closing stock");
        System.out.println(openingTotal + " + " + deliveryTotal + " - " + salesTotal
                + " = " + (stock[0] + stock[1] + stock[2]));
    }
}
