import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

public class SortUniqueIntegers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // TreeSet: No duplicates + Sorted
        Set<Integer> numbers = new TreeSet<>();
        System.out.print("Enter how many numbers you want to enter (N): ");
        int n = sc.nextInt();
        System.out.println("Enter " + n + " integers:");
        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            numbers.add(num); // Duplicate values will be ignored automatically
        }
        System.out.println("Sorted unique numbers: " + numbers);
        sc.close();
    }
}