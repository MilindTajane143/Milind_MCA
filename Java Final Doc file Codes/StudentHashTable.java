import java.util.Hashtable;
import java.util.Scanner;

public class StudentHashTable {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Hashtable<String, Double> studentTable = new Hashtable<>();
        System.out.print("Enter number of students: ");
        int n = sc.nextInt();
        sc.nextLine(); // consume newline
        // Input: Student Name and Percentage
        for (int i = 0; i < n; i++) {
            System.out.print("Enter student name: ");
            String name = sc.nextLine();
            System.out.print("Enter percentage: ");
            double percentage = sc.nextDouble();
            sc.nextLine(); // consume newline
            studentTable.put(name, percentage);
        }
        // Display all entries
        System.out.println("\n--- Student Records ---");
        for (String key : studentTable.keySet()) {
            System.out.println("Name: " + key + ", Percentage: " + studentTable.get(key));
        }
        // Search for a student
        System.out.print("\nEnter name of student to search: ");
        String searchName = sc.nextLine();
        if (studentTable.containsKey(searchName)) {
            System.out.println("Percentage of " + searchName + ": " + studentTable.get(searchName));
        } else {
            System.out.println("Student " + searchName + " not found.");
        }
        sc.close();
    }
}