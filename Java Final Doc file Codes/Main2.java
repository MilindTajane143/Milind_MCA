import java.util.Scanner;

interface CardOperations {
    void useCard(double amount);

    void payCredit(double amount);

    void increaseLimit(double amount);
}

class InvalidUserException extends Exception {
    public InvalidUserException(String message) {
        super(message);
    }
}

class User {
    int age;
    double income;
    String city;
    String vehicle;

    public void validateUser() throws InvalidUserException {
        if (age < 18 || age > 55)
            throw new InvalidUserException("Age must be between 18 and 55.");
        if (income < 50000 || income > 100000)
            throw new InvalidUserException("Income must be between Rs. 50,000 and Rs. 1,00,000.");
        if (!(city.equalsIgnoreCase("Pune") || city.equalsIgnoreCase("Mumbai") || city.equalsIgnoreCase("Nashik") ||
                city.equalsIgnoreCase("Bangalore") || city.equalsIgnoreCase("Chennai")))
            throw new InvalidUserException("City must be Nashik, Pune, Mumbai, Bangalore, or Chennai.");
        if (!(vehicle.equalsIgnoreCase("4-wheeler")))
            throw new InvalidUserException("User must have a 4-wheeler.");
    }
}

class GoldCardCustomer extends User implements CardOperations {
    double creditAmount = 0;
    double creditLimit = 20000;
    int limitIncreaseCount = 0;

    public void useCard(double amount) {
        if ((creditAmount + amount) <= creditLimit) {
            creditAmount += amount;
            System.out.println("Card used. Current credit amount: Rs. " + creditAmount);
        } else {
            System.out.println("Cannot use card. Limit exceeded.");
        }
    }

    public void payCredit(double amount) {
        creditAmount -= amount;
        if (creditAmount < 0)
            creditAmount = 0;
        System.out.println("Payment done. Remaining credit amount: Rs. " + creditAmount);
    }

    public void increaseLimit(double amount) {
        if (limitIncreaseCount < 3 && amount <= 5000) {
            creditLimit += amount;
            limitIncreaseCount++;
            System.out.println("Credit limit increased. New limit: Rs. " + creditLimit);
        } else {
            System.out.println("Limit cannot be increased further.");
        }
    }
}

public class Main2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        GoldCardCustomer customer = new GoldCardCustomer();
        try {
            // Get user input
            System.out.print("Enter Age: ");
            customer.age = sc.nextInt();
            System.out.print("Enter Monthly Income: ");
            customer.income = sc.nextDouble();
            sc.nextLine(); // consume newline
            System.out.print("Enter City: ");
            customer.city = sc.nextLine();
            System.out.print("Enter Vehicle Type: ");
            customer.vehicle = sc.nextLine();
            customer.validateUser();
            System.out.println("User validated successfully!");
            customer.useCard(5000);
            customer.useCard(18000);
            customer.payCredit(2000);
            customer.increaseLimit(4000);
            customer.increaseLimit(3000);
            customer.increaseLimit(5000);
            customer.increaseLimit(1000);
        } catch (InvalidUserException e) {
            System.out.println("Validation Error: " + e.getMessage());
        }
        sc.close();
    }
}
