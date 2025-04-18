import java.util.*;

class DuplicateNumberException extends Exception {
    public DuplicateNumberException(String message) {
        super(message);
    }
}

public class DuplicateCheck {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Set<Integer> numberSet = new HashSet<>();
        System.out.print("Enter how many numbers: ");
        int n = sc.nextInt();
        System.out.println("Enter " + n + " integers:");
        try {
            for (int i = 0; i < n; i++) {
                int num = sc.nextInt();
                if (!numberSet.add(num)) {
                    // If add() returns false, it means the number already exists
                    throw new DuplicateNumberException("Duplicate number found: " + num);
                }
            }
            System.out.println("All numbers are unique: " + numberSet);
        } catch (DuplicateNumberException e) {
            System.out.println("Exception: " + e.getMessage());
        }
        sc.close();
    }
}